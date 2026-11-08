#!/usr/bin/env python3
import os
import sys
import shutil
import subprocess
import random
import string
import zipfile
import math
from PIL import Image, ImageDraw

HOME = '/data/data/com.termux/files/home'
BUILD_DIR = os.path.join(HOME, 'diwali-app-builder')
TOOLS_DIR = os.path.join(HOME, '.gemini/antigravity-cli/brain/c32bb36b-51bd-4d52-8d4c-0892b566b606/scratch/aab-build')
WEB_DIR = os.path.join(HOME, 'diwali_website')

AAPT2 = '/data/data/com.termux/files/usr/bin/aapt2'
ANDROID_JAR = os.path.join(TOOLS_DIR, 'android.jar')
BUNDLETOOL = os.path.join(TOOLS_DIR, 'bundletool.jar')
R8_JAR = os.path.join(TOOLS_DIR, 'r8.jar')

PACKAGE = 'com.prajwal.diwalicrackers'
APP_NAME = 'Diwali Cracker Studio'
KEYSTORE = os.path.join(BUILD_DIR, 'diwali_release.jks')
KEY_PASS = 'diwali123'
KEY_ALIAS = 'diwalicrackers'

print("=== STARTING DIWALI CRACKER STUDIO ENTERPRISE AAB & APK BUILD PIPELINE ===")
os.makedirs(BUILD_DIR, exist_ok=True)

# 1. Clean previous build files if any
for d in ['src', 'compiled', 'module_base', 'assets', 'r8_out']:
    p = os.path.join(BUILD_DIR, d)
    if os.path.exists(p):
        shutil.rmtree(p)
for f in ['base.zip', 'linked.zip', 'DiwaliCrackerStudio_unsigned.aab', 'DiwaliCrackerStudio.aab', 'diwali.apks', 'DiwaliCrackerStudio.apk', 'classes.dex', 'proguard-rules.pro', 'mapping.txt']:
    p = os.path.join(BUILD_DIR, f)
    if os.path.exists(p):
        os.remove(p)

res_dir = os.path.join(BUILD_DIR, 'src/res')
java_dir = os.path.join(BUILD_DIR, 'src/java/com/prajwal/diwalicrackers')
os.makedirs(res_dir, exist_ok=True)
os.makedirs(java_dir, exist_ok=True)
os.makedirs(os.path.join(BUILD_DIR, 'compiled'), exist_ok=True)
os.makedirs(os.path.join(BUILD_DIR, 'src/classes'), exist_ok=True)

# 2. Generate values (strings, colors, styles, network security)
values_dir = os.path.join(res_dir, 'values')
xml_dir = os.path.join(res_dir, 'xml')
os.makedirs(values_dir, exist_ok=True)
os.makedirs(xml_dir, exist_ok=True)

with open(os.path.join(values_dir, 'strings.xml'), 'w') as f:
    f.write(f'''<?xml version="1.0" encoding="utf-8"?>
<resources>
    <string name="app_name">{APP_NAME}</string>
</resources>
''')

with open(os.path.join(values_dir, 'colors.xml'), 'w') as f:
    f.write('''<?xml version="1.0" encoding="utf-8"?>
<resources>
    <color name="colorPrimary">#070709</color>
    <color name="colorPrimaryDark">#070709</color>
    <color name="colorAccent">#d4af37</color>
</resources>
''')

with open(os.path.join(values_dir, 'styles.xml'), 'w') as f:
    f.write('''<?xml version="1.0" encoding="utf-8"?>
<resources>
    <style name="AppTheme" parent="@android:style/Theme.DeviceDefault.NoActionBar">
        <item name="android:windowBackground">#070709</item>
        <item name="android:statusBarColor">#070709</item>
        <item name="android:navigationBarColor">#070709</item>
    </style>
</resources>
''')

with open(os.path.join(xml_dir, 'network_security_config.xml'), 'w') as f:
    f.write('''<?xml version="1.0" encoding="utf-8"?>
<network-security-config>
    <base-config cleartextTrafficPermitted="false">
        <trust-anchors>
            <certificates src="system" />
        </trust-anchors>
    </base-config>
    <domain-config>
        <domain includeSubdomains="true">diwali-cracker-studio.pages.dev</domain>
        <domain includeSubdomains="true">pages.dev</domain>
        <trust-anchors>
            <certificates src="system" />
        </trust-anchors>
    </domain-config>
</network-security-config>
''')

# 3. Generate high-res adaptive launcher icons
def create_app_icon(size):
    img = Image.new('RGBA', (size, size), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)
    center = size / 2
    r = size * 0.46

    bbox = [center - r, center - r, center + r, center + r]
    corner = int(size * 0.22)
    draw.rounded_rectangle(bbox, radius=corner, fill=(10, 10, 15, 255), outline=(212, 175, 55, 255), width=max(2, int(size * 0.035)))

    r_in = r - int(size * 0.04)
    bbox_in = [center - r_in, center - r_in, center + r_in, center + r_in]
    draw.rounded_rectangle(bbox_in, radius=corner - int(size*0.03), outline=(247, 208, 112, 120), width=max(1, int(size * 0.015)))

    num_rays = 12
    for i in range(num_rays):
        angle = i * (2 * math.pi / num_rays)
        ray_r1 = size * 0.18
        ray_r2 = size * 0.32 if i % 2 == 0 else size * 0.25
        x1 = center + ray_r1 * math.cos(angle)
        y1 = center + ray_r1 * math.sin(angle)
        x2 = center + ray_r2 * math.cos(angle)
        y2 = center + ray_r2 * math.sin(angle)
        draw.line([x1, y1, x2, y2], fill=(255, 215, 0, 220), width=max(1, int(size * 0.02)))

    bowl_w = size * 0.42
    bowl_h = size * 0.18
    bowl_y = center + size * 0.05
    bowl_box = [center - bowl_w/2, bowl_y, center + bowl_w/2, bowl_y + bowl_h]
    draw.chord(bowl_box, start=0, end=180, fill=(212, 175, 55, 255), outline=(255, 235, 150, 255), width=max(1, int(size * 0.02)))

    flame_top_y = center - size * 0.22
    flame_bottom_y = bowl_y + size * 0.03
    flame_w = size * 0.16
    draw.polygon([
        (center, flame_top_y),
        (center + flame_w/2, (flame_top_y + flame_bottom_y)/2),
        (center, flame_bottom_y),
        (center - flame_w/2, (flame_top_y + flame_bottom_y)/2)
    ], fill=(255, 140, 0, 255))
    core_w = flame_w * 0.5
    draw.polygon([
        (center, flame_top_y + size * 0.04),
        (center + core_w/2, (flame_top_y + flame_bottom_y)/2 + size * 0.02),
        (center, flame_bottom_y - size * 0.01),
        (center - core_w/2, (flame_top_y + flame_bottom_y)/2 + size * 0.02)
    ], fill=(255, 245, 180, 255))
    return img

densities = {
    'mipmap-mdpi': 48,
    'mipmap-hdpi': 72,
    'mipmap-xhdpi': 96,
    'mipmap-xxhdpi': 144,
    'mipmap-xxxhdpi': 192
}
for d_name, d_size in densities.items():
    d_path = os.path.join(res_dir, d_name)
    os.makedirs(d_path, exist_ok=True)
    icon_img = create_app_icon(d_size)
    icon_img.save(os.path.join(d_path, 'ic_launcher.png'), 'PNG')

play_icon = create_app_icon(512)
play_icon.save(os.path.join(BUILD_DIR, 'DiwaliCrackerStudio_512.png'), 'PNG')
print("Generated adaptive launcher mipmaps and 512x512 Play Store icon.")

# 4. Generate AndroidManifest.xml
manifest_path = os.path.join(BUILD_DIR, 'src/AndroidManifest.xml')
with open(manifest_path, 'w') as f:
    f.write(f'''<?xml version="1.0" encoding="utf-8"?>
<manifest xmlns:android="http://schemas.android.com/apk/res/android"
    package="{PACKAGE}"
    android:versionCode="1"
    android:versionName="1.0.0">

    <uses-sdk
        android:minSdkVersion="24"
        android:targetSdkVersion="35" />

    <uses-permission android:name="android.permission.INTERNET" />
    <uses-permission android:name="android.permission.ACCESS_NETWORK_STATE" />
    <uses-permission android:name="android.permission.VIBRATE" />

    <application
        android:allowBackup="true"
        android:hardwareAccelerated="true"
        android:icon="@mipmap/ic_launcher"
        android:roundIcon="@mipmap/ic_launcher"
        android:label="@string/app_name"
        android:supportsRtl="true"
        android:theme="@style/AppTheme"
        android:usesCleartextTraffic="false"
        android:networkSecurityConfig="@xml/network_security_config">
        <activity
            android:name="{PACKAGE}.MainActivity"
            android:exported="true"
            android:screenOrientation="portrait"
            android:configChanges="keyboard|keyboardHidden|orientation|screenLayout|screenSize|smallestScreenSize|uiMode"
            android:windowSoftInputMode="adjustResize">
            <intent-filter>
                <action android:name="android.intent.action.MAIN" />
                <category android:name="android.intent.category.LAUNCHER" />
            </intent-filter>
            <intent-filter>
                <action android:name="android.intent.action.VIEW" />
                <category android:name="android.intent.category.DEFAULT" />
                <category android:name="android.intent.category.BROWSABLE" />
                <data android:scheme="diwalicrackers" />
            </intent-filter>
        </activity>
    </application>
</manifest>
''')

# 5. Build Encrypted Assets and Honeypot Decoys
assets_dir = os.path.join(BUILD_DIR, 'assets')
os.makedirs(assets_dir, exist_ok=True)

# Read index.html
with open(os.path.join(WEB_DIR, 'index.html'), 'rb') as f:
    raw_html = f.read()

# Encrypt with XOR 0x4A and decoy metadata header
decoy_header = b'<!-- DIWALI_CORE_V1_METADATA_HEADER: 0x98f4e2 -->\n'
encrypted_payload = bytearray()
for b in raw_html:
    encrypted_payload.append(b ^ 0x4A)
final_asset_bytes = decoy_header + bytes(encrypted_payload)

os.makedirs(os.path.join(assets_dir, 'core'), exist_ok=True)
with open(os.path.join(assets_dir, 'core/diwali_engine.dat'), 'wb') as f:
    f.write(final_asset_bytes)

# Add decoy architectural packages (similar to Enterprise security structure)
decoy_folders = [
    'packages/sound_fx',
    'packages/physics_core',
    'runtime/v8_sandbox',
    'runtime/webgl_rasterizer',
    'cluster/particle_pool',
    'telemetry/fps_monitor',
    'storage/asset_vault'
]
for df in decoy_folders:
    dp = os.path.join(assets_dir, df)
    os.makedirs(dp, exist_ok=True)
    with open(os.path.join(dp, 'config.json'), 'w') as f:
        f.write('{"status":"active","shards":4,"verified":true,"build":"2026.11"}')

print(f"Generated encrypted asset ({len(final_asset_bytes)} bytes) and enterprise security decoy structure.")

# 6. Generate MainActivity.java
with open(os.path.join(java_dir, 'MainActivity.java'), 'w') as f:
    f.write('''package com.prajwal.diwalicrackers;

import android.app.Activity;
import android.app.AlertDialog;
import android.content.ActivityNotFoundException;
import android.content.Context;
import android.content.DialogInterface;
import android.content.Intent;
import android.graphics.Color;
import android.net.Uri;
import android.os.Build;
import android.os.Bundle;
import android.view.View;
import android.view.ViewGroup;
import android.view.Window;
import android.view.WindowManager;
import android.webkit.CookieManager;
import android.webkit.PermissionRequest;
import android.webkit.WebChromeClient;
import android.webkit.WebResourceRequest;
import android.webkit.WebResourceResponse;
import android.webkit.WebSettings;
import android.webkit.WebView;
import android.webkit.WebViewClient;
import android.webkit.WebResourceError;
import android.webkit.SslErrorHandler;
import android.net.http.SslError;
import java.io.InputStream;
import java.io.ByteArrayOutputStream;
import android.view.WindowInsets;
import android.widget.FrameLayout;

public class MainActivity extends Activity {
    private static final String APP_HOST = "diwali-cracker-studio.pages.dev";
    private WebView mWebView;

    private String loadDecryptedLauncher() {
        try {
            InputStream is = getAssets().open("core/diwali_engine.dat");
            ByteArrayOutputStream buffer = new ByteArrayOutputStream();
            int nRead;
            byte[] data = new byte[4096];
            while ((nRead = is.read(data, 0, data.length)) != -1) {
                buffer.write(data, 0, nRead);
            }
            buffer.flush();
            is.close();
            byte[] rawBytes = buffer.toByteArray();

            int payloadStart = 0;
            for (int i = 0; i <= rawBytes.length - 3; i++) {
                if (rawBytes[i] == '-' && rawBytes[i+1] == '-' && rawBytes[i+2] == '>') {
                    payloadStart = i + 3;
                    while (payloadStart < rawBytes.length && (rawBytes[payloadStart] == '\\r' || rawBytes[payloadStart] == '\\n')) {
                        payloadStart++;
                    }
                    break;
                }
            }

            int payloadLen = rawBytes.length - payloadStart;
            byte[] decrypted = new byte[payloadLen];
            for (int i = 0; i < payloadLen; i++) {
                decrypted[i] = (byte) (rawBytes[payloadStart + i] ^ 0x4A);
            }
            return new String(decrypted, "UTF-8");
        } catch (Exception e) {
            return "<!DOCTYPE html><html><body style='background:#070709;color:#d4af37;display:flex;align-items:center;justify-content:center;height:100vh;margin:0;font-family:sans-serif;'><h2>Loading Diwali Cracker Studio...</h2></body></html>";
        }
    }

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);

        try {
            WebView.setWebContentsDebuggingEnabled(false);
        } catch (Exception ignored) {}

        Window window = getWindow();
        int darkBg = Color.parseColor("#070709");
        if (Build.VERSION.SDK_INT >= Build.VERSION_CODES.LOLLIPOP) {
            window.clearFlags(WindowManager.LayoutParams.FLAG_TRANSLUCENT_STATUS | WindowManager.LayoutParams.FLAG_TRANSLUCENT_NAVIGATION);
            window.addFlags(WindowManager.LayoutParams.FLAG_DRAWS_SYSTEM_BAR_BACKGROUNDS);
            window.setStatusBarColor(darkBg);
            window.setNavigationBarColor(darkBg);
        }

        if (Build.VERSION.SDK_INT >= Build.VERSION_CODES.P) {
            WindowManager.LayoutParams lp = window.getAttributes();
            lp.layoutInDisplayCutoutMode = WindowManager.LayoutParams.LAYOUT_IN_DISPLAY_CUTOUT_MODE_SHORT_EDGES;
            window.setAttributes(lp);
        }

        FrameLayout rootLayout = new FrameLayout(this);
        rootLayout.setBackgroundColor(darkBg);
        rootLayout.setFitsSystemWindows(true);

        mWebView = new WebView(this);
        mWebView.setBackgroundColor(darkBg);
        mWebView.setLayerType(View.LAYER_TYPE_HARDWARE, null);
        rootLayout.addView(mWebView, new FrameLayout.LayoutParams(
            ViewGroup.LayoutParams.MATCH_PARENT,
            ViewGroup.LayoutParams.MATCH_PARENT
        ));

        if (Build.VERSION.SDK_INT >= Build.VERSION_CODES.KITKAT_WATCH) {
            rootLayout.setOnApplyWindowInsetsListener(new View.OnApplyWindowInsetsListener() {
                @Override
                public WindowInsets onApplyWindowInsets(View v, WindowInsets insets) {
                    v.setPadding(
                        insets.getSystemWindowInsetLeft(),
                        insets.getSystemWindowInsetTop(),
                        insets.getSystemWindowInsetRight(),
                        insets.getSystemWindowInsetBottom()
                    );
                    return insets;
                }
            });
        }

        setContentView(rootLayout);

        CookieManager cookieManager = CookieManager.getInstance();
        cookieManager.setAcceptCookie(true);
        if (Build.VERSION.SDK_INT >= Build.VERSION_CODES.LOLLIPOP) {
            cookieManager.setAcceptThirdPartyCookies(mWebView, true);
        }

        WebSettings settings = mWebView.getSettings();
        settings.setJavaScriptEnabled(true);
        settings.setDomStorageEnabled(true);
        settings.setDatabaseEnabled(true);
        settings.setAllowFileAccess(false);
        settings.setAllowContentAccess(false);
        settings.setAllowFileAccessFromFileURLs(false);
        settings.setAllowUniversalAccessFromFileURLs(false);
        settings.setSaveFormData(false);
        settings.setSavePassword(false);
        settings.setCacheMode(WebSettings.LOAD_DEFAULT);
        settings.setMediaPlaybackRequiresUserGesture(false);

        String defaultUa = settings.getUserAgentString();
        if (defaultUa != null) {
            String cleanUa = defaultUa.replace("; wv", "").replace("Version/4.0 ", "");
            settings.setUserAgentString(cleanUa + " DiwaliCrackerStudioApp/1.0");
        }

        if (Build.VERSION.SDK_INT >= Build.VERSION_CODES.LOLLIPOP) {
            settings.setMixedContentMode(WebSettings.MIXED_CONTENT_ALWAYS_ALLOW);
        }

        mWebView.setWebViewClient(new WebViewClient() {
            @Override
            public boolean shouldOverrideUrlLoading(WebView view, WebResourceRequest request) {
                if (request != null && request.getUrl() != null) {
                    String url = request.getUrl().toString();
                    if (url.contains(APP_HOST) || url.startsWith("file://") || url.contains("pages.dev")) {
                        return false;
                    }
                    try {
                        Intent intent = new Intent(Intent.ACTION_VIEW, Uri.parse(url));
                        startActivity(intent);
                        return true;
                    } catch (Exception ignored) {}
                }
                return false;
            }

            @Override
            public void onReceivedSslError(WebView view, SslErrorHandler handler, SslError error) {
                handler.cancel();
            }
        });

        mWebView.setWebChromeClient(new WebChromeClient() {
            @Override
            public void onPermissionRequest(final PermissionRequest request) {
                request.grant(request.getResources());
            }
        });

        String decryptedHtml = loadDecryptedLauncher();
        mWebView.loadDataWithBaseURL("https://" + APP_HOST, decryptedHtml, "text/html", "UTF-8", null);
    }

    @Override
    protected void onResume() {
        super.onResume();
        if (mWebView != null) {
            mWebView.onResume();
            mWebView.resumeTimers();
        }
    }

    @Override
    protected void onPause() {
        super.onPause();
        if (mWebView != null) {
            mWebView.onPause();
            mWebView.pauseTimers();
        }
    }

    @Override
    protected void onDestroy() {
        if (mWebView != null) {
            mWebView.destroy();
            mWebView = null;
        }
        super.onDestroy();
    }

    @Override
    public void onBackPressed() {
        if (mWebView != null && mWebView.canGoBack()) {
            mWebView.goBack();
        } else {
            super.onBackPressed();
        }
    }
}
''')

# 7. Generate proguard-rules.pro
proguard_path = os.path.join(BUILD_DIR, 'proguard-rules.pro')
with open(proguard_path, 'w') as f:
    f.write('''-dontwarn **
-keep class com.prajwal.diwalicrackers.** { *; }
-keepclassmembers class * {
    @android.webkit.JavascriptInterface <methods>;
}
-repackageclasses 'com.prajwal.diwalicrackers.core'
-allowaccessmodification
-optimizations !code/simplification/arithmetic,!field/*,!class/merging/*
-optimizationpasses 5
''')

# 8. Compile Java source code
print("Compiling Java source code with javac...")
cmd_javac = [
    'javac',
    '-source', '8',
    '-target', '8',
    '-cp', ANDROID_JAR,
    '-d', os.path.join(BUILD_DIR, 'src/classes'),
    os.path.join(java_dir, 'MainActivity.java')
]
subprocess.run(cmd_javac, check=True)

# 9. R8 Obfuscation & Dexing
print("Running R8 Optimizer & Proguard obfuscator...")
class_files = []
classes_root = os.path.join(BUILD_DIR, 'src/classes')
for root, _, files in os.walk(classes_root):
    for fl in files:
        if fl.endswith('.class'):
            class_files.append(os.path.join(root, fl))

mapping_txt = os.path.join(BUILD_DIR, 'mapping.txt')
cmd_r8 = [
    'java', '-cp', R8_JAR, 'com.android.tools.r8.R8',
    '--release',
    '--min-api', '24',
    '--lib', ANDROID_JAR,
    '--pg-conf', proguard_path,
    '--pg-map-output', mapping_txt,
    '--output', BUILD_DIR
] + class_files
subprocess.run(cmd_r8, check=True)
print("R8 successfully generated classes.dex and mapping.txt.")

# 10. AAPT2 Compile Resources
print("Compiling resources with aapt2...")
cmd_aapt2_compile = [
    AAPT2, 'compile',
    '--dir', res_dir,
    '-o', os.path.join(BUILD_DIR, 'compiled/res.zip')
]
subprocess.run(cmd_aapt2_compile, check=True)

# 11. AAPT2 Link Resources in Proto-Format for AAB
print("Linking resources in proto-format...")
cmd_aapt2_link = [
    AAPT2, 'link',
    '--proto-format',
    '-I', ANDROID_JAR,
    '--manifest', manifest_path,
    '-o', os.path.join(BUILD_DIR, 'linked.zip'),
    os.path.join(BUILD_DIR, 'compiled/res.zip'),
    '--auto-add-overlay'
]
subprocess.run(cmd_aapt2_link, check=True)

# 12. Assemble Base Module
print("Assembling Base Module for Bundletool...")
module_base = os.path.join(BUILD_DIR, 'module_base')
os.makedirs(module_base, exist_ok=True)

with zipfile.ZipFile(os.path.join(BUILD_DIR, 'linked.zip'), 'r') as z:
    z.extractall(module_base)

os.makedirs(os.path.join(module_base, 'manifest'), exist_ok=True)
os.makedirs(os.path.join(module_base, 'dex'), exist_ok=True)
os.makedirs(os.path.join(module_base, 'assets'), exist_ok=True)

shutil.move(os.path.join(module_base, 'AndroidManifest.xml'), os.path.join(module_base, 'manifest/AndroidManifest.xml'))
shutil.copy(os.path.join(BUILD_DIR, 'classes.dex'), os.path.join(module_base, 'dex/classes.dex'))

for item in os.listdir(assets_dir):
    s = os.path.join(assets_dir, item)
    d = os.path.join(module_base, 'assets', item)
    if os.path.isdir(s):
        shutil.copytree(s, d)
    else:
        shutil.copy(s, d)

# Zip module_base into base.zip
base_zip = os.path.join(BUILD_DIR, 'base.zip')
with zipfile.ZipFile(base_zip, 'w', zipfile.ZIP_DEFLATED) as z_out:
    for root, _, files in os.walk(module_base):
        for fl in files:
            full_p = os.path.join(root, fl)
            rel_p = os.path.relpath(full_p, module_base)
            z_out.write(full_p, rel_p)

# 13. Generate 25-Year Production Release Keystore (if not existing)
if not os.path.exists(KEYSTORE):
    print("Generating official 25+ year production Keystore...")
    cmd_keytool = [
        'keytool', '-genkeypair', '-v',
        '-keystore', KEYSTORE,
        '-alias', KEY_ALIAS,
        '-keyalg', 'RSA',
        '-keysize', '2048',
        '-validity', '10000',
        '-storepass', KEY_PASS,
        '-keypass', KEY_PASS,
        '-dname', 'CN=Prajwal, OU=Production, O=DiwaliStudio, L=Mumbai, ST=Maharashtra, C=IN'
    ]
    subprocess.run(cmd_keytool, check=True)

# 14. Build Android App Bundle (.aab) with Bundletool
print("Building Android App Bundle (.aab) with bundletool...")
aab_unsigned = os.path.join(BUILD_DIR, 'DiwaliCrackerStudio_unsigned.aab')
aab_signed = os.path.join(BUILD_DIR, 'DiwaliCrackerStudio.aab')

cmd_bundle = [
    'java', '-jar', BUNDLETOOL,
    'build-bundle',
    f'--modules={base_zip}',
    f'--output={aab_unsigned}'
]
subprocess.run(cmd_bundle, check=True)

# Sign AAB with jarsigner
print("Signing AAB with jarsigner...")
shutil.copy(aab_unsigned, aab_signed)
cmd_sign_aab = [
    'jarsigner',
    '-sigalg', 'SHA256withRSA',
    '-digestalg', 'SHA-256',
    '-keystore', KEYSTORE,
    '-storepass', KEY_PASS,
    '-keypass', KEY_PASS,
    aab_signed,
    KEY_ALIAS
]
subprocess.run(cmd_sign_aab, check=True)

# 15. Generate Universal Signed APK from AAB via Bundletool
print("Generating Universal Signed APK from AAB via bundletool...")
apks_path = os.path.join(BUILD_DIR, 'diwali.apks')
cmd_build_apks = [
    'java', '-jar', BUNDLETOOL,
    'build-apks',
    f'--bundle={aab_signed}',
    f'--output={apks_path}',
    '--mode=universal',
    f'--aapt2={AAPT2}',
    f'--ks={KEYSTORE}',
    f'--ks-pass=pass:{KEY_PASS}',
    f'--ks-key-alias={KEY_ALIAS}',
    f'--key-pass=pass:{KEY_PASS}',
    '--overwrite'
]
subprocess.run(cmd_build_apks, check=True)

# Extract universal.apk
apk_signed = os.path.join(BUILD_DIR, 'DiwaliCrackerStudio.apk')
with zipfile.ZipFile(apks_path, 'r') as z_apks:
    with open(apk_signed, 'wb') as f_out:
        f_out.write(z_apks.read('universal.apk'))

aab_size = os.path.getsize(aab_signed) / 1024
apk_size = os.path.getsize(apk_signed) / 1024
print(f"\\n🎉 BUILD SUCCESSFUL!")
print(f"📦 Generated Signed AAB: {aab_signed} ({aab_size:.1f} KB)")
print(f"📱 Generated Signed APK: {apk_signed} ({apk_size:.1f} KB)")
print(f"🗺️ Generated Proguard Mapping: {mapping_txt}")
print(f"🔑 Production Keystore: {KEYSTORE}")

# 16. Copy to /storage/emulated/0/Download
downloads_dir = '/storage/emulated/0/Download'
if os.path.exists(downloads_dir):
    dst_aab = os.path.join(downloads_dir, 'DiwaliCrackerStudio.aab')
    dst_apk = os.path.join(downloads_dir, 'DiwaliCrackerStudio.apk')
    dst_map = os.path.join(downloads_dir, 'DiwaliCrackerStudio_mapping.txt')
    dst_icon = os.path.join(downloads_dir, 'DiwaliCrackerStudio_512.png')
    dst_ks = os.path.join(downloads_dir, 'diwali_release.jks')
    shutil.copy(aab_signed, dst_aab)
    shutil.copy(apk_signed, dst_apk)
    shutil.copy(mapping_txt, dst_map)
    shutil.copy(os.path.join(BUILD_DIR, 'DiwaliCrackerStudio_512.png'), dst_icon)
    shutil.copy(KEYSTORE, dst_ks)
    print(f"✅ Delivered all Play Store release artifacts directly to: {downloads_dir}")
    scan_bin = shutil.which('termux-media-scan')
    if scan_bin:
        subprocess.run([scan_bin, dst_apk], capture_output=True)
        subprocess.run([scan_bin, dst_aab], capture_output=True)

print("=== PIPELINE FINISHED WITH ZERO ERRORS ===")
