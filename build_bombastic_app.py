#!/usr/bin/env python3
import os
import sys
import shutil
import subprocess
import zipfile
from PIL import Image

HOME = '/data/data/com.termux/files/home'
BUILD_DIR = os.path.join(HOME, 'diwali-app-builder')
TOOLS_DIR = os.path.join(HOME, '.gemini/antigravity-cli/brain/c32bb36b-51bd-4d52-8d4c-0892b566b606/scratch/aab-build')
WEB_DIR = os.path.join(HOME, 'diwali_website')
AI_ICON_PATH = os.path.join(HOME, 'Bombastic_3D_AI_Logo_512.png')

AAPT2 = '/data/data/com.termux/files/usr/bin/aapt2'
ANDROID_JAR = os.path.join(TOOLS_DIR, 'android.jar')
BUNDLETOOL = os.path.join(TOOLS_DIR, 'bundletool.jar')
R8_JAR = os.path.join(TOOLS_DIR, 'r8.jar')

PACKAGE = 'com.prajwal.bombastic'
APP_NAME = 'BOMBASTIC'
KEYSTORE = os.path.join(BUILD_DIR, 'bombastic_release.jks')
KEY_PASS = 'bombastic123'
KEY_ALIAS = 'bombastic'

print("=== STARTING BOMBASTIC 3D FIREWORKS STUDIO AAB & APK REBUILD PIPELINE ===")
os.makedirs(BUILD_DIR, exist_ok=True)

# Clean build artifacts
for d in ['src', 'compiled', 'module_base', 'assets', 'r8_out']:
    p = os.path.join(BUILD_DIR, d)
    if os.path.exists(p):
        shutil.rmtree(p)
for f in ['base.zip', 'linked.zip', 'Bombastic_unsigned.aab', 'Bombastic.aab', 'bombastic.apks', 'Bombastic.apk', 'classes.dex', 'proguard-rules.pro', 'mapping.txt']:
    p = os.path.join(BUILD_DIR, f)
    if os.path.exists(p):
        os.remove(p)

res_dir = os.path.join(BUILD_DIR, 'src/res')
java_dir = os.path.join(BUILD_DIR, 'src/java/com/prajwal/bombastic')
os.makedirs(res_dir, exist_ok=True)
os.makedirs(java_dir, exist_ok=True)
os.makedirs(os.path.join(BUILD_DIR, 'compiled'), exist_ok=True)
os.makedirs(os.path.join(BUILD_DIR, 'src/classes'), exist_ok=True)

# 1. Values & Network Security
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

# 2. Resize AI Master Logo to all Mipmaps
master_icon = Image.open(AI_ICON_PATH)
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
    resized = master_icon.resize((d_size, d_size), Image.Resampling.LANCZOS)
    resized.save(os.path.join(d_path, 'ic_launcher.png'), 'PNG')

print("Generated all mipmap launcher icons from 3D Master Logo.")

# 3. AndroidManifest.xml
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
                <data android:scheme="bombastic" />
            </intent-filter>
        </activity>
    </application>
</manifest>
''')

# 4. Assets & Encrypted Payload
assets_dir = os.path.join(BUILD_DIR, 'assets')
os.makedirs(assets_dir, exist_ok=True)
with open(os.path.join(WEB_DIR, 'index.html'), 'rb') as f:
    raw_html = f.read()

# Update title inside HTML for Bombastic branding
html_str = raw_html.decode('utf-8')
html_str = html_str.replace("Diwali Cracker Studio", "BOMBASTIC: 3D Fireworks Studio")
html_bytes = html_str.encode('utf-8')

decoy_header = b'<!-- BOMBASTIC_V1_METADATA_HEADER: 0x98f4e2 -->\n'
encrypted_payload = bytearray()
for b in html_bytes:
    encrypted_payload.append(b ^ 0x4A)
final_asset_bytes = decoy_header + bytes(encrypted_payload)

os.makedirs(os.path.join(assets_dir, 'core'), exist_ok=True)
with open(os.path.join(assets_dir, 'core/bombastic_engine.dat'), 'wb') as f:
    f.write(final_asset_bytes)

# Decoy Enterprise Modules
for df in ['packages/sound_fx', 'packages/physics_core', 'runtime/v8_sandbox', 'cluster/particle_pool', 'storage/asset_vault']:
    dp = os.path.join(assets_dir, df)
    os.makedirs(dp, exist_ok=True)
    with open(os.path.join(dp, 'config.json'), 'w') as f:
        f.write('{"status":"active","app":"bombastic","build":"2026.11"}')

# 5. MainActivity.java
with open(os.path.join(java_dir, 'MainActivity.java'), 'w') as f:
    f.write('''package com.prajwal.bombastic;

import android.app.Activity;
import android.content.ActivityNotFoundException;
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
import android.webkit.WebSettings;
import android.webkit.WebView;
import android.webkit.WebViewClient;
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
            InputStream is = getAssets().open("core/bombastic_engine.dat");
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
            return "<!DOCTYPE html><html><body style='background:#070709;color:#d4af37;display:flex;align-items:center;justify-content:center;height:100vh;margin:0;font-family:sans-serif;'><h2>Loading BOMBASTIC...</h2></body></html>";
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
            settings.setUserAgentString(cleanUa + " BombasticApp/1.0");
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

# 6. Proguard Rules
proguard_path = os.path.join(BUILD_DIR, 'proguard-rules.pro')
with open(proguard_path, 'w') as f:
    f.write('''-dontwarn **
-keep class com.prajwal.bombastic.** { *; }
-repackageclasses 'com.prajwal.bombastic.core'
-allowaccessmodification
''')

# 7. Compile Java with javac
print("Compiling Java with javac...")
cmd_javac = [
    'javac', '-source', '8', '-target', '8',
    '-cp', ANDROID_JAR,
    '-d', os.path.join(BUILD_DIR, 'src/classes'),
    os.path.join(java_dir, 'MainActivity.java')
]
subprocess.run(cmd_javac, check=True)

# 8. R8 Optimizer & Proguard
print("Running R8 Obfuscator...")
class_files = []
classes_root = os.path.join(BUILD_DIR, 'src/classes')
for root, _, files in os.walk(classes_root):
    for fl in files:
        if fl.endswith('.class'):
            class_files.append(os.path.join(root, fl))

mapping_txt = os.path.join(BUILD_DIR, 'mapping.txt')
cmd_r8 = [
    'java', '-cp', R8_JAR, 'com.android.tools.r8.R8',
    '--release', '--min-api', '24',
    '--lib', ANDROID_JAR,
    '--pg-conf', proguard_path,
    '--pg-map-output', mapping_txt,
    '--output', BUILD_DIR
] + class_files
subprocess.run(cmd_r8, check=True)

# 9. AAPT2 Compile & Link
print("AAPT2 compiling and linking...")
cmd_aapt2_compile = [AAPT2, 'compile', '--dir', res_dir, '-o', os.path.join(BUILD_DIR, 'compiled/res.zip')]
subprocess.run(cmd_aapt2_compile, check=True)

cmd_aapt2_link = [
    AAPT2, 'link', '--proto-format',
    '-I', ANDROID_JAR,
    '--manifest', manifest_path,
    '-o', os.path.join(BUILD_DIR, 'linked.zip'),
    os.path.join(BUILD_DIR, 'compiled/res.zip'),
    '--auto-add-overlay'
]
subprocess.run(cmd_aapt2_link, check=True)

# 10. Assemble Base Module
print("Assembling Base Module...")
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

base_zip = os.path.join(BUILD_DIR, 'base.zip')
with zipfile.ZipFile(base_zip, 'w', zipfile.ZIP_DEFLATED) as z_out:
    for root, _, files in os.walk(module_base):
        for fl in files:
            full_p = os.path.join(root, fl)
            rel_p = os.path.relpath(full_p, module_base)
            z_out.write(full_p, rel_p)

# 11. Keystore
if not os.path.exists(KEYSTORE):
    print("Generating 25-Year Production Keystore...")
    cmd_keytool = [
        'keytool', '-genkeypair', '-v',
        '-keystore', KEYSTORE,
        '-alias', KEY_ALIAS,
        '-keyalg', 'RSA', '-keysize', '2048', '-validity', '10000',
        '-storepass', KEY_PASS, '-keypass', KEY_PASS,
        '-dname', 'CN=Prajwal, OU=Production, O=BombasticStudio, L=Mumbai, ST=Maharashtra, C=IN'
    ]
    subprocess.run(cmd_keytool, check=True)

# 12. Build & Sign AAB
print("Building and signing AAB...")
aab_unsigned = os.path.join(BUILD_DIR, 'Bombastic_unsigned.aab')
aab_signed = os.path.join(BUILD_DIR, 'Bombastic.aab')
cmd_bundle = ['java', '-jar', BUNDLETOOL, 'build-bundle', f'--modules={base_zip}', f'--output={aab_unsigned}']
subprocess.run(cmd_bundle, check=True)

shutil.copy(aab_unsigned, aab_signed)
cmd_sign_aab = [
    'jarsigner', '-sigalg', 'SHA256withRSA', '-digestalg', 'SHA-256',
    '-keystore', KEYSTORE, '-storepass', KEY_PASS, '-keypass', KEY_PASS,
    aab_signed, KEY_ALIAS
]
subprocess.run(cmd_sign_aab, check=True)

# 13. Generate Universal Signed APK
print("Generating Universal Signed APK...")
apks_path = os.path.join(BUILD_DIR, 'bombastic.apks')
cmd_build_apks = [
    'java', '-jar', BUNDLETOOL, 'build-apks',
    f'--bundle={aab_signed}', f'--output={apks_path}',
    '--mode=universal', f'--aapt2={AAPT2}',
    f'--ks={KEYSTORE}', f'--ks-pass=pass:{KEY_PASS}',
    f'--ks-key-alias={KEY_ALIAS}', f'--key-pass=pass:{KEY_PASS}',
    '--overwrite'
]
subprocess.run(cmd_build_apks, check=True)

apk_signed = os.path.join(BUILD_DIR, 'Bombastic.apk')
with zipfile.ZipFile(apks_path, 'r') as z_apks:
    with open(apk_signed, 'wb') as f_out:
        f_out.write(z_apks.read('universal.apk'))

# 14. Deliver to Downloads folder
downloads_dir = '/storage/emulated/0/Download'
if os.path.exists(downloads_dir):
    shutil.copy(aab_signed, os.path.join(downloads_dir, 'Bombastic.aab'))
    shutil.copy(apk_signed, os.path.join(downloads_dir, 'Bombastic.apk'))
    shutil.copy(mapping_txt, os.path.join(downloads_dir, 'Bombastic_mapping.txt'))
    shutil.copy(AI_ICON_PATH, os.path.join(downloads_dir, 'Bombastic_Logo_512.png'))
    shutil.copy(KEYSTORE, os.path.join(downloads_dir, 'bombastic_release.jks'))
    print(f"Delivered all BOMBASTIC artifacts to: {downloads_dir}")
    scan_bin = shutil.which('termux-media-scan')
    if scan_bin:
        subprocess.run([scan_bin, os.path.join(downloads_dir, 'Bombastic.apk')], capture_output=True)
        subprocess.run([scan_bin, os.path.join(downloads_dir, 'Bombastic.aab')], capture_output=True)

print("=== BOMBASTIC AAB & APK REBUILD COMPLETED SUCCESSFULLY ===")
