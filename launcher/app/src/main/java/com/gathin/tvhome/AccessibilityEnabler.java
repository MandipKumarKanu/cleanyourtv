package com.gathin.tvhome;

import android.content.Context;
import android.provider.Settings;
import android.util.Log;

/**
 * Ensures that HomeKeyService and InputKeyService are always enabled in Android's
 * secure settings. When granted WRITE_SECURE_SETTINGS, this persists across reboots
 * and prevents the system or OEM power savers from leaving the services disabled.
 */
public final class AccessibilityEnabler {
    private static final String TAG = "AccessibilityEnabler";

    private AccessibilityEnabler() {}

    public static void ensureEnabled(Context context) {
        if (context == null) return;
        try {
            String pkg = context.getPackageName();
            String homeSvc = pkg + "/.HomeKeyService";
            String inputSvc = pkg + "/.InputKeyService";

            String enabled = Settings.Secure.getString(context.getContentResolver(), Settings.Secure.ENABLED_ACCESSIBILITY_SERVICES);
            String current = enabled != null ? enabled : "";

            boolean hasHome = current.contains(homeSvc) || current.contains(pkg + "/com.gathin.tvhome.HomeKeyService");
            boolean hasInput = current.contains(inputSvc) || current.contains(pkg + "/com.gathin.tvhome.InputKeyService");

            if (!hasHome || !hasInput) {
                StringBuilder sb = new StringBuilder(current);
                if (!hasHome) {
                    if (sb.length() > 0) sb.append(':');
                    sb.append(homeSvc);
                }
                if (!hasInput) {
                    if (sb.length() > 0) sb.append(':');
                    sb.append(inputSvc);
                }
                Settings.Secure.putString(context.getContentResolver(), Settings.Secure.ENABLED_ACCESSIBILITY_SERVICES, sb.toString());
                Log.i(TAG, "Restored enabled_accessibility_services: " + sb);
            }

            int a11y = Settings.Secure.getInt(context.getContentResolver(), Settings.Secure.ACCESSIBILITY_ENABLED, 0);
            if (a11y != 1) {
                Settings.Secure.putInt(context.getContentResolver(), Settings.Secure.ACCESSIBILITY_ENABLED, 1);
                Log.i(TAG, "Restored accessibility_enabled: 1");
            }
        } catch (Exception e) {
            // Ignored if WRITE_SECURE_SETTINGS permission is not yet granted
            Log.d(TAG, "Could not set accessibility settings: " + e.getMessage());
        }
    }
}
