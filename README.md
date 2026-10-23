<p align="center">
  <img src="docs/banner.png" alt="CleanYourTV. Your TV, minus the ads." width="800">
</p>

<h1 align="center">CleanYourTV</h1>

<h3 align="center">Minimalist Apple TV-Style Launcher · 1,100+ Live DTH Channels · Zero-Bloat Android & Google TV Makeover</h3>

<p align="center">
  <a href="https://github.com/MandipKumarKanu/cleanyourtv/blob/main/LICENSE"><img src="https://img.shields.io/badge/license-MIT-blue.svg?style=flat-square" alt="License: MIT"></a>
  <a href="https://github.com/MandipKumarKanu/cleanyourtv"><img src="https://img.shields.io/badge/platform-Android%20TV%20%7C%20Google%20TV-3DDC84.svg?style=flat-square&logo=android" alt="Platform: Android TV"></a>
  <a href="launcher/"><img src="https://img.shields.io/badge/launcher-Native%20Java%20%C2%B7%20390%20KB-007ACC.svg?style=flat-square" alt="Launcher: 390 KB"></a>
  <a href="apps/live-tv/"><img src="https://img.shields.io/badge/live--tv-Flutter%20%2B%20Media3%20ExoPlayer-02569B.svg?style=flat-square&logo=flutter" alt="Live TV: Flutter"></a>
  <a href="examples/"><img src="https://img.shields.io/badge/tested%20devices-120%2B%20models-orange.svg?style=flat-square" alt="Tested Devices"></a>
  <a href="https://github.com/MandipKumarKanu/cleanyourtv"><img src="https://img.shields.io/badge/maintained%20by-Mandip%20Kumar%20Kanu-purple.svg?style=flat-square" alt="Maintainer"></a>
</p>

---

Transform any **Android TV** or **Google TV** over Wi-Fi. Strip out the telemetry, intrusive sponsored recommendations, and OEM bloatware, and upgrade your smart television with:

1. **Apple TV-Style Minimalist Launcher** (`launcher/`): An ultra-lightweight (390 KB) native Java launcher with dynamic grid sizing, smooth glass highlights, ambient top shelf glow, HDMI-CEC input switching, and quick settings.
2. **Built-in Live TV & DTH Player** (`apps/live-tv`): A blazingly fast TV player streaming 1,100+ live channels with a classic Tata Play / Airtel DTH-style 4-hour timeline program guide (EPG), multi-audio language switching, and full D-pad remote navigation.
3. **Non-Destructive Debloat Engine** (`tools/`): Safe, reversible ADB management. No rooting required, no voided warranties, no files permanently removed, and a one-command instant rollback if needed.

<p align="center">
  <img src="docs/stock-vs-new-side.jpg" alt="Before: stock Google TV home with a sponsored ad. After: the Clean Your TV launcher" width="800">
</p>

---

## Table of Contents

- [Core Components](#core-components)
  - [1. Apple TV-Style Native Launcher](#1-apple-tv-style-native-launcher)
  - [2. Built-in Live TV & DTH Player](#2-built-in-live-tv--dth-player)
  - [3. Non-Destructive Debloat Engine](#3-non-destructive-debloat-engine)
- [Visual Showcase](#visual-showcase)
- [Supported TV Models](#supported-tv-models)
- [Quick Start Guide](#quick-start-guide)
  - [Prerequisites: Enable USB & Network Debugging](#prerequisites-enable-usb--network-debugging)
  - [Option A: 🤖 Automated Setup with AI (Antigravity, Codex, Claude Code, OpenCode)](#option-a--automated-setup-with-ai-antigravity-codex-claude-code-opencode)
  - [Option B: 🛠️ Manual Step-by-Step Installation](#option-b-%EF%B8%8F-manual-step-by-step-installation)
- [Project Structure](#project-structure)
- [Tools & Utilities Reference](#tools--utilities-reference)
- [Frequently Asked Questions](#frequently-asked-questions)
- [Contributing](#contributing)
- [Author & Maintainer](#author--maintainer)
- [License](#license)

---

## Core Components

### 1. Apple TV-Style Native Launcher

Located in [`launcher/`](launcher/), this is a hyper-optimized Android TV application written in pure Java (about 390 KB installed size).

- **Apple TV-Inspired Dock**: Four customizable favorite apps pinned on a frosted dock with quick launch.
- **Top Shelf Ambient Glow**: Dynamic ambient halo extracting primary colors from the focused application's banner art.
- **Slide-up Grid with Dynamic Columns**: Smoothly browse all installed applications in a grid configured to your screen width (4, 5, or 6 columns).
- **Spring Glass Highlight**: Single floating glass selector tile that springs seamlessly between focus nodes.
- **Frosted Quick Access Buttons**:
  - **Inputs Menu**: Directly switches between active HDMI ports (showing custom HDMI-CEC device labels like *PlayStation 5*, *Apple TV*, *Soundbar*), AV, and Live TV.
  - **Network Status**: One-glance Wi-Fi network SSID or Ethernet link status.
  - **Quick Settings Panel**: Fast flyout toggling Wi-Fi, Bluetooth, Screensaver, and Sound without digging into manufacturer menus.
- **Customizable Screensaver**: Minimalist floating drifting clock (`Outfit` typeface) prevents OLED/LED panel burn-in.

### 2. Built-in Live TV & DTH Player

Located in [`apps/live-tv/`](apps/live-tv/), this is a production-grade TV player built with Flutter and ExoPlayer Media3.

| | |
|---|---|
| ![Live TV Channel Browser](docs/live-tv-home.png) | ![DTH-Style 4-Hour Timeline Program Guide (EPG)](docs/live-tv-epg.png) |
| *1,100+ Live Channels categorized with Voice Search & Language Filter* | *Classic 4-Hour Timeline EPG with Program Synopsis & PIP Video* |
| <img src="docs/live-tv-player.png" alt="Full-screen HD live broadcast playback" width="400"> | <img src="docs/live-tv-epg.png" alt="DTH Timeline Guide with program synopsis" width="400"> |
| *Full HD Live Playback with Multi-Audio & Fit Controls* | *DTH Program Guide with instant D-pad Genre Switching* |

- **1,100+ Live Channels**: Curated Indian & International feeds (*News, Entertainment, Movies, Sports, Music, Kids, Infotainment, Business, Devotional*) with automatic fallback streams.
- **DTH-Style 4-Hour Timeline EPG**: Modeled after standard Indian STBs (Tata Play / Airtel Digital TV). Displays program descriptions, progress bars, and upcoming shows with live background PIP playback.
- **100% D-Pad Remote Navigable**:
  - Press **Up (⬆️)** in the guide to focus the category pill.
  - Cycle genres with **Left / Right (⬅️/➡️)** or press **OK** to open a clean **Category Picker Modal Dialog**.
  - Fast-scroll large channel lists with **Channel Up / Channel Down (Page Up / Page Down)**.
- **Multi-Audio Track & Dual-Language Switching**:
  - Hardware-accelerated ExoPlayer Media3 audio pipeline.
  - Direct audio language switching (*English, Hindi, Spanish, Tamil, German, Japanese, etc.*) for channels with multi-audio feeds.
- **Live Jitter Buffer Window**: Maintains an 18-second jitter-buffer safety window behind the live edge to eliminate buffering stutters on wireless networks.
- **TV Remote Shortcuts**: Voice search with TV remote microphone support, one-click screen aspect ratio fit (*Fit, Fill, Zoom, 16:9*), favorite channels bookmarking, and instant Last Channel recall.
- **60 FPS Performance on 1 GB RAM**: Pre-rendered offstage caching and zero per-tile animation overhead.

### 3. Non-Destructive Debloat Engine

Android TVs share the same Android Debug Bridge (ADB) architecture as phones. Using `pm disable-user --user 0`, CleanYourTV puts vendor telemetry, lockscreen ads, and junk services into deep hibernation:

- **Zero Rooting**: Operates completely within Android's stock user management permissions.
- **No Lost System Updates**: OEM system updates remain functional.
- **Instant Rollback**: Every disabled package is logged in `debloat.txt` and can be restored in seconds with `tools/recovery.py`.

---

## Visual Showcase

| | |
|---|---|
| ![The top shelf names the focused app over an ambient glow in its colour](docs/focus-2-up-netflix.png) | ![The Inputs popup: HDMI ports with what is connected, AV and Live TV](docs/inputs-menu.jpg) |
| *Top shelf and ambient glow* | *Inputs: HDMI with connection state, AV, Live TV* |
| ![The grid with the glass highlight on a tile and its name beneath](docs/focus-1-fancode.png) | ![The Clock screensaver: a thin clock drifting over the glow](docs/clock-screensaver.png) |
| *The grid, one glass highlight, the tile's name* | *Clock screensaver, drifts so nothing burns in* |
| ![The aurora theme: a wallpaper and tinted pills, pushed without a rebuild](docs/theme-aurora.jpg) | ![Six columns and a six-app dock from a theme's config.json](docs/theme-six-columns.jpg) |
| *Aurora theme, pushed with `tools/theme.sh`* | *Six columns and a six-app dock, same launcher* |

---

## Supported TV Models

Tested profiles with specific debloat lists and configuration options are located in [`examples/`](examples/):

**TCL** (26 models) · **Sony** (18 models) · **Xiaomi** (16 models) · **Philips** (8 models) · **Hisense** (6 models) · **Amazon Fire TV** (3 models) · **Panasonic** (3 models) · **BenQ** · **CHiQ** · **Haier** · **Hitachi** · **NVIDIA Shield** · **Skyworth** · **Vu** · **Chromecast with Google TV** · **OnePlus** · **onn** · **Motorola** · **Redmi** · **Toshiba** · **Freebox** · **BYINTEK, JMGO, Portronics, Wanbo & XGIMI projectors**

<details>
<summary><strong>Click to expand the full list of 120+ verified TV models</strong></summary>

| TV Model & Hardware Platform | Default OS |
|---|---|
| AiPro2K (Expressluck, dongnae; Changhong AI PONT family) | Android TV 14 |
| AIWA AI PONT SA (Changhong, osaka, ISDB86AW) | Google TV 14 |
| Amazon Fire TV 50" 4K smart TV (AFTTIFF43, brandenburg) | Fire OS 7.7 / Android 9 |
| Amazon Fire TV Stick 4K, 1st gen 2018 (AFTMM, mantis) | Fire OS 6.7 / Android 7.1 |
| Amazon Fire TV Stick Lite, 1st gen 2020 (AFTSS, sheldon) | Fire OS 7.7 / Android 9 |
| BenQ E55-735 (Changhong AI PONT, DVB96BQ) | Google TV 14 |
| BenQ E55-750 (Changhong AI PONT, DVB96BQ) | Google TV (Android 11) |
| BYINTEK Love U4 projector, 1080P (Skyworth RG_HS352, HiSilicon, 1 GB) | Android 9 |
| BYINTEK T5 Max projector (SkyworthDigital YYT, Amlogic) | Google TV 14 |
| Cecotec VQU10065S 65" QLED (Vestel, shandao, MediaTek) | Android TV 14 |
| CHiQ AI PONT (Changhong GTVU65, dangni, MediaTek mt5867) | Google TV 14 |
| Chromecast with Google TV 4K (sabrina) | Google TV 14 |
| Compac ATV R2 (SCBC R2, Realtek RTD285O) | Android TV 9 |
| EKO 2K Google TV (MTC-built, tennoji, MediaTek mt5867) | Google TV 14 |
| FFalcon 鹤6 PRO 65S585C Pro (MediaTek MT9653) | Android TV 11 |
| Freebox Player POP (Free, fbx8am, Amlogic) | Android TV 10 |
| Haier Android TV DVB2K (broadway, HaierATVT56DVB) | Android TV 11 |
| Haier H32S80EFX (MatrixTV CE, HRT56EU, deto, MediaTek) | Google TV 14 |
| Hisense E5Q Pro (VIDAA_TV, MediaTek MT9653) | Android TV 11 |
| Hisense HiSmartTV A4 (xiaoyushan, MStar m7322) | Android TV 11 |
| Hisense SmartTV 4K FFM (huangshan, MediaTek) | Android TV 10 |
| Hisense U75 (hengshan, MediaTek) | Google TV 12 |
| Hitachi 65QLEDSM20 (MTC, bangbae, MediaTek m7322) | Android TV 11 |
| Insignia 55" F30 4K Fire TV (NS-55F301NA25, AFTDCT31) | Fire OS 7 / Android 9 |
| JMGO N1S projector (K80A, holan, MediaTek m7332) | Google TV 14 |
| Kalley R10G (device R10G, product ACER_FFM, Realtek RTD2875P) | Google TV 14 |
| Motorola SWTV-24AE-FHD (Skyworth OEM beomil) | Google TV 14 |
| NVIDIA SHIELD TV Pro 2019 (P2897, mdarcy) | Android TV 11 |
| OnePlus TV (D00) | Google TV 14 |
| onn 4K Streaming Box (2023, Walmart; YOC, Amlogic) | Google TV 14 |
| Panasonic 4KTV-0SU (Skyworth-built SW4H, MediaTek m7332) | Android TV 10 |
| Panasonic TH-40HS550K (Skyworth-built, GS655 shibuya) | Android TV 11 |
| Philips 50PUS8517/12 (TP Vision, PH1M_EA_9970A, MediaTek MT5895) | Android TV 11 |
| Philips 55OLED707/12 (TP Vision, PH1M_EA_9970A, MediaTek MT5895) | Android TV 11 |
| Philips 75PUS8505/12 (TP Vision TPM191E, MediaTek MT5887) | Android TV 12 |
| Polytron 2K (WLTV POLYTRON2K, hayward, MediaTek mt5867) | Android TV 11 |
| Portronics Beem 470 Smart LED Projector (Allwinner H713, 1 GB) | Android 11 |
| PRISM+ Q65 Ultra 2026 QLED 4K AI Google TV (Realtek RTD2875 SoC) | Google TV 14 |
| Redmi TV (MiTV-ANTL0, starwars) | Android 5.1.1 |
| Skyworth SWTV-24NA-4K NF (eleonas, MediaTek mt5896) | Google TV 14 |
| Sony BRAVIA 4K AE2 (BRAVIA_AE2, MediaTek MT5897) | Google TV 14 |
| Sony BRAVIA 4K VH2 (KD-55X80J, BRAVIA_VH2, MediaTek) | Google TV 12 |
| Sony BRAVIA 9 II (K-65XR90M2, BRAVIA_AE3, MediaTek MT5838) | Google TV 14 |
| Sony BRAVIA KD-49X8307C (2015, SVP-DTV15, MediaTek) | Android TV 7.0 |
| Sony BRAVIA KD-55XE8596 (2017, BRAVIA_ATV2_EU, MediaTek MT5891) | Android TV 9 |
| TCL 32S5400A / 32S5K (C06, MediaTek MT9221, 1 GB) | Android TV 11 |
| TCL 43C645 (Smart TV Pro, Realtek RTD2851 / R51MT05) | Google TV 11 |
| TCL 55" 4K Google TV (G10, Realtek RTD2851) | Google TV 12 |
| TCL 65C735 (Smart TV Pro, G05, MediaTek) | Google TV 11 |
| TCL 85RM7L (G08, MediaTek tcl9618) | Google TV 14 |
| Xiaomi Mi TV 4A / 4S / 5 Pro (PatchWall) | Android TV 9 |

</details>

---

## Quick Start Guide

### Prerequisites: Enable USB & Network Debugging

1. **On your TV**:
   - Go to **Settings** → **Device Preferences** (or **System**) → **About**.
   - Scroll down to **Build** and click the **OK** button **7 times** until you see *"You are now a developer!"*.
   - Return to the previous menu, enter **Developer options**, and turn **USB debugging** (and **Network debugging** if present) **ON**.
   - Note the TV's IP address in **Settings** → **Network & Internet**.
2. **On your computer** (connected to the same Wi-Fi network):
   ```bash
   adb connect <TV-IP-ADDRESS>:5555
   ```
   *Accept the "Allow USB debugging?" prompt on your TV screen.*

### Option A: 🤖 Automated Setup with AI (Antigravity, Codex, Claude Code, OpenCode)

If you have a coding assistant with terminal / shell access:
1. Turn on **USB debugging** on the TV.
2. Open [`PROMPT.md`](PROMPT.md).
3. Copy the prompt into **Google Antigravity**, **OpenAI Codex**, **Claude Code**, or **OpenCode**.
4. Fill in your TV model name: the AI will automatically connect, back up system settings, debloat vendor telemetry, install the clean launcher, and verify every step with on-screen screenshots!

---

### Option B: 🛠️ Manual Step-by-Step Installation

#### Step 1: Debloat Your Television

Run the automated Python helper to inspect packages and back up your current state:

```bash
# Verify ADB connection
python tools/tv.py 'getprop ro.product.model'

# Back up installed packages before making any changes
tools/tv.py 'pm list packages -f' > my_tv_backup.txt

# Disable bloatware from an existing model profile (e.g., TCL or Xiaomi)
bash tools/disable.sh examples/tcl-32s5k/debloat.txt
```

> [!NOTE]
> If you need to restore any package at any time:
> ```bash
> python tools/recovery.py my_tv_backup.txt
> ```

---

#### Step 2: Build & Install Clean Launcher

The launcher builds directly with Gradle:

```bash
cd launcher
./gradlew assembleRelease

# Install onto your connected TV
adb install -r app/build/outputs/apk/release/app-release.apk

# Set CleanYourTV as default launcher
tools/tv.py 'cmd package set-home-activity com.gathin.tvhome/.MainActivity'
```

---

#### Step 3: Build & Install Live TV & DTH Player

Build the Flutter application with hardware acceleration:

```bash
cd apps/live-tv

# Build APK for ARM architectures
flutter build apk --release --target-platform android-arm,android-arm64

# Install on your TV
adb install -r build/app/outputs/flutter-apk/app-release.apk
```

---

## Project Structure

```
cleanyourtv/
├── apps/
│   └── live-tv/               # Flutter + ExoPlayer Live TV & DTH Player app
│       ├── lib/               # Dart source (Providers, EPG timeline, Widgets)
│       ├── android/           # Android wrapper with Media3 ProGuard rules
│       └── pubspec.yaml       # Dependencies
├── launcher/                  # Native Java Android TV Launcher (com.gathin.tvhome)
│   ├── app/src/main/
│   │   ├── java/com/gathin/tvhome/
│   │   │   ├── MainActivity.java            # Home grid, focus engine, glass highlight
│   │   │   ├── QuickSettingsActivity.java   # Wi-Fi, Bluetooth, screensaver, sound panel
│   │   │   ├── HomeKeyService.java          # Accessibility remote key interception
│   │   │   └── WallpaperPlayer.java         # Ambient glow and dynamic video wallpapers
│   │   └── res/                             # Layouts, vector drawables, localized strings
│   └── build.gradle
├── examples/                  # Tested debloat lists for 120+ TV models
├── tools/                     # Helper CLI utilities
│   ├── tv.py                  # ADB shell command runner
│   ├── disable.sh             # Batch debloater with safety checks
│   ├── recovery.py            # Rollback and package enabler
│   ├── analyze_streams.py     # Channel stream diagnostics and health checker
│   ├── theme.sh               # Push theme configurations over Wi-Fi
│   └── adb-closed.py          # Port scanner to ensure ADB port is closed after setup
├── themes/                    # Modular themes (Aurora, Minimalist, Cinematic)
└── docs/                      # Screenshots, documentation, and architecture diagrams
```

---

## Tools & Utilities Reference

- **`tools/tv.py`**: Clean, lightweight wrapper to run adb commands directly:
  ```bash
  python tools/tv.py 'pm list packages -d'   # View disabled packages
  python tools/tv.py 'input keyevent 3'      # Simulate Home button
  ```
- **`tools/disable.sh`**: Disables packages from a text file, skipping essential TV display drivers and Wi-Fi services.
- **`tools/theme.sh`**: Uploads custom wallpaper backgrounds, layout density, and accent colors without rebuilding the APK.
- **`tools/analyze_streams.py`**: Validates live channel streams, HTTP status codes, and latency for IPTV / M3U sources.
- **`tools/adb-closed.py`**: Verifies that ADB port 5555 is closed and secured after installation.

---

## Frequently Asked Questions

<details>
<summary><strong>Is this safe? Can it brick my TV?</strong></summary>
Nothing is flashed to the bootloader, rooted, or deleted from <code>/system</code>. All operations execute strictly via <code>pm disable-user</code> in user space. If an essential service is accidentally disabled, it can be re-enabled instantly with <code>pm enable</code> or through the TV's native Settings → Apps page.
</details>

<details>
<summary><strong>Will streaming apps (Netflix, Prime Video, YouTube) still work?</strong></summary>
Yes. All DRM pipelines (Widevine L1/L3), video decoders, and Google Play Store services remain intact. Apps continue to update normally.
</details>

<details>
<summary><strong>Can I change the number of app columns on the home screen?</strong></summary>
Yes. Open Launcher Settings on your TV (or push a config) to toggle between 4, 5, or 6 columns per row.
</details>

<details>
<summary><strong>How do I close the ADB port when done?</strong></summary>
Once you are finished configuring your TV:
1. Go to <strong>Settings</strong> → <strong>Developer options</strong>.
2. Turn <strong>USB debugging</strong> and <strong>Network debugging</strong> OFF.
3. Revoke all debugging authorizations.
4. Run <code>python tools/adb-closed.py &lt;TV-IP&gt;</code> to verify port 5555 is inaccessible.
</details>

---

## Contributing

Contributions are warmly welcomed! You can contribute by:
- Adding a debloat profile for your specific TV model in [`examples/`](examples/).
- Improving Launcher features or translations.
- Enhancing Live TV channel guides and EPG parsers.

Please refer to [`CONTRIBUTING.md`](CONTRIBUTING.md) for testing guidelines.

---

## Author & Maintainer

Maintained and developed by **Mandip Kumar Kanu**:
- **GitHub**: [@MandipKumarKanu](https://github.com/MandipKumarKanu)
- **Repository**: [MandipKumarKanu/cleanyourtv](https://github.com/MandipKumarKanu/cleanyourtv)
- **Email**: [mandipshah3@gmail.com](mailto:mandipshah3@gmail.com)

---

## License

This project is licensed under the **MIT License** — see the [`LICENSE`](LICENSE) file for details.  
The Outfit typeface is distributed under the SIL Open Font License 1.1.
