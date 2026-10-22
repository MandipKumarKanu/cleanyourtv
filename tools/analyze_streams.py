#!/usr/bin/env python3
"""
Stream Analyzer & Backup Link Tester for Live TV.
Analyzes all channels and their backup streams to identify:
  - Channels where main link is healthy
  - Channels where main link is DEAD but BACKUP link is WORKING (Recoverable)
  - Channels where all links are dead

Can export `stream_memory.json` to pre-seed the Android TV app with working backup links!
"""

import argparse
import concurrent.futures
import json
import os
import re
import sys
import time
import urllib.error
import urllib.request

STREAMS_CATALOG_URL = (
    "https://raw.githubusercontent.com/kananinirav/Indian-IPTV-App/refs/heads/master/data/streams.csv"
)
LOGO_INDEX_URL = "https://iptv-org.github.io/iptv/countries/in.m3u"

USER_AGENT = (
    "Mozilla/5.0 (Linux; Android 10; TV) AppleWebKit/537.36 "
    "(KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
)

TVG_ID_RE = re.compile(r'tvg-id="([^"]*)"')
TVG_LOGO_RE = re.compile(r'tvg-logo="([^"]*)"')
GROUP_RE = re.compile(r'group-title="([^"]*)"')


def clean_name_key(name: str) -> str:
    cleaned = re.sub(r"\(.*?\)|\(.*?\)|\[.*?\]", "", name)
    cleaned = re.sub(r"\bhd\b", "", cleaned, flags=re.IGNORECASE)
    return re.sub(r"[^a-z0-9]", "", cleaned.lower())


def res_rank(name: str) -> int:
    if "2160p" in name or "4K" in name:
        return 4
    if "1080p" in name:
        return 3
    if "720p" in name:
        return 2
    if "576p" in name:
        return 1
    return 0


def res_label(name: str) -> str:
    if "2160p" in name or "4K" in name:
        return "4K"
    if "1080p" in name:
        return "1080p"
    if "720p" in name:
        return "720p"
    if "576p" in name:
        return "576p"
    if "480p" in name:
        return "480p"
    return "HD"


def fetch_url(url: str, timeout: int = 15) -> str:
    req = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
    with urllib.request.urlopen(req, timeout=timeout) as resp:
        return resp.read().decode("utf-8", errors="ignore")


def check_stream(url: str, timeout: int = 4) -> bool:
    """Checks whether an HLS or video stream URL responds with 200/206/302."""
    if not url.startswith("http"):
        return False
    try:
        # Request only first 1KB to test connectivity without downloading video stream
        req = urllib.request.Request(
            url,
            headers={
                "User-Agent": USER_AGENT,
                "Range": "bytes=0-1024",
            },
        )
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            code = resp.getcode()
            if code in (200, 206):
                return True
    except urllib.error.HTTPError as e:
        # Some servers return 403 on range or HEAD, try a quick 1-byte read
        if e.code in (302, 301, 307, 308):
            return True
    except Exception:
        pass
    return False


def parse_m3u_entries(body: str):
    entries = []
    info = None
    for raw in body.splitlines():
        line = raw.strip()
        if line.startswith("#EXTINF:"):
            info = line
        elif line and not line.startswith("#") and info:
            entries.append((info, line))
            info = None
    return entries


def load_channels():
    print("⏳ Downloading streams catalog & playlists...")
    catalog_csv = fetch_url(STREAMS_CATALOG_URL)
    sources = []
    for line in catalog_csv.splitlines():
        t = line.strip()
        if not t or t.lower().startswith("name,"):
            continue
        comma = t.find(",")
        if comma <= 0:
            continue
        sources.append((t[:comma].strip(), t[comma + 1 :].strip()))

    print(f"📥 Found {len(sources)} playlist sources. Loading in parallel...")
    with concurrent.futures.ThreadPoolExecutor(max_workers=10) as executor:
        future_to_src = {executor.submit(fetch_url, s[1], 15): s for s in sources}
        playlists = []
        for f in concurrent.futures.as_completed(future_to_src):
            src = future_to_src[f]
            try:
                body = f.result()
                playlists.append((src[0], body))
            except Exception as e:
                print(f"   ⚠️ Warning: failed to fetch {src[0]}: {e}")

    # Merge into channels
    by_key = {}
    for name, body in playlists:
        for info, url in parse_m3u_entries(body):
            name_part = info[info.rfind(",") + 1 :].strip()
            key = clean_name_key(name_part)
            if not key:
                continue

            id_m = TVG_ID_RE.search(info)
            tvg_id = id_m.group(1) if id_m else ""
            logo_m = TVG_LOGO_RE.search(info)
            logo = logo_m.group(1) if logo_m else ""
            group_m = GROUP_RE.search(info)
            group = group_m.group(1) if group_m else "General"

            stream_obj = {
                "url": url,
                "rank": res_rank(name_part),
                "label": res_label(name_part),
            }

            if key in by_key:
                exist = by_key[key]
                if not any(s["url"] == url for s in exist["streams"]):
                    exist["streams"].append(stream_obj)
            else:
                by_key[key] = {
                    "name": re.sub(r"\s*\(\d+[pi]\)", "", name_part).strip(),
                    "id": tvg_id,
                    "logo": logo,
                    "category": group,
                    "key": key,
                    "streams": [stream_obj],
                }

    # Sort streams in each channel by rank
    channels = list(by_key.values())
    for c in channels:
        c["streams"].sort(key=lambda s: s["rank"], reverse=True)

    print(f"✅ Loaded {len(channels)} unique channels with multiple streams merged.")
    return channels


def analyze_channel(channel: dict, max_probe_timeout: int = 4):
    streams = channel["streams"]
    results = []
    working_stream_url = None
    working_index = -1

    for idx, s in enumerate(streams):
        is_up = check_stream(s["url"], timeout=max_probe_timeout)
        results.append({"url": s["url"], "label": s["label"], "works": is_up})
        if is_up and working_stream_url is None:
            working_stream_url = s["url"]
            working_index = idx

    primary_works = len(results) > 0 and results[0]["works"]
    backup_works = any(r["works"] for r in results[1:]) if len(results) > 1 else False

    status = "UNKNOWN"
    if primary_works:
        status = "PRIMARY_OK"
    elif backup_works:
        status = "RECOVERED_BY_BACKUP"
    else:
        status = "ALL_DEAD"

    channel_key = channel["id"].lower() if channel["id"] else f"{channel['category']}|{channel['name'].lower()}"

    return {
        "name": channel["name"],
        "category": channel["category"],
        "channel_key": channel_key,
        "total_streams": len(streams),
        "primary_works": primary_works,
        "working_index": working_index,
        "working_stream_url": working_stream_url,
        "status": status,
        "streams": results,
    }


def main():
    parser = argparse.ArgumentParser(description="Analyze channel streams & backups for Live TV")
    parser.add_argument("--workers", type=int, default=20, help="Concurrent probe threads (default 20)")
    parser.add_argument("--timeout", type=int, default=4, help="Stream probe timeout in seconds (default 4)")
    parser.add_argument("--limit", type=int, default=0, help="Limit number of channels to test (0 = all)")
    parser.add_argument("--export-memory", type=str, default="", help="Path to export stream_memory.json")
    parser.add_argument("--output", type=str, default="stream_analysis_report.json", help="Output report JSON file")
    args = parser.parse_args()

    channels = load_channels()
    if args.limit > 0:
        channels = channels[: args.limit]
        print(f"🔬 Testing limited batch of {len(channels)} channels...")

    print(f"🚀 Starting stream health check with {args.workers} concurrent workers (timeout {args.timeout}s)...")
    start_time = time.time()

    analyzed = []
    completed = 0
    total = len(channels)

    with concurrent.futures.ThreadPoolExecutor(max_workers=args.workers) as executor:
        future_to_chan = {executor.submit(analyze_channel, ch, args.timeout): ch for ch in channels}
        for f in concurrent.futures.as_completed(future_to_chan):
            res = f.result()
            analyzed.append(res)
            completed += 1
            if completed % 10 == 0 or completed == total:
                print(f"   Progress: {completed}/{total} channels probed ({completed/total*100:.1f}%)", end="\r")

    print("\n🏁 Probing finished in {:.1f}s!".format(time.time() - start_time))

    # Statistics
    primary_ok = [c for c in analyzed if c["status"] == "PRIMARY_OK"]
    recovered = [c for c in analyzed if c["status"] == "RECOVERED_BY_BACKUP"]
    all_dead = [c for c in analyzed if c["status"] == "ALL_DEAD"]

    print("\n" + "=" * 60)
    print("📊 STREAM HEALTH ANALYSIS REPORT")
    print("=" * 60)
    print(f"Total Channels Tested:     {len(analyzed)}")
    print(f"🟢 Primary Stream Live:    {len(primary_ok)} ({len(primary_ok)/len(analyzed)*100:.1f}%)")
    print(f"🔄 Recovered by Backup:    {len(recovered)} ({len(recovered)/len(analyzed)*100:.1f}%)")
    print(f"🔴 All Streams Dead:       {len(all_dead)} ({len(all_dead)/len(analyzed)*100:.1f}%)")
    print("=" * 60)

    if recovered:
        print("\n✨ Channels rescued by Backup Streams:")
        for r in recovered[:15]:
            streams_info = f"backup #{r['working_index'] + 1} working ({r['streams'][r['working_index']]['label']})"
            print(f"  • {r['name']:<28} ➔ {streams_info}")
        if len(recovered) > 15:
            print(f"  ...and {len(recovered) - 15} more channels!")

    # Write full JSON report
    with open(args.output, "w", encoding="utf-8") as f:
        json.dump(analyzed, f, indent=2)
    print(f"\n📄 Saved detailed report to: {args.output}")

    # Export stream memory if requested
    if args.export_memory:
        memory_map = {}
        for c in analyzed:
            if c["working_stream_url"]:
                memory_map[c["channel_key"]] = c["working_stream_url"]
        with open(args.export_memory, "w", encoding="utf-8") as f:
            json.dump(memory_map, f, indent=2)
        print(f"💾 Exported working stream memory to: {args.export_memory} ({len(memory_map)} working channels)")


if __name__ == "__main__":
    main()
