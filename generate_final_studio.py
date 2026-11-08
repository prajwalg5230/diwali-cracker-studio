# -*- coding: utf-8 -*-
import base64

with open('/data/data/com.termux/files/home/diwali_website/wasm_b64.txt') as f:
    wasm_b64 = f.read().strip()

html_content = r'''<!DOCTYPE html>
<html lang="mr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no, viewport-fit=cover">
    <title>शुभ दीपावली २०२६ | 3D Digital Cracker Studio</title>

    <!-- Google Fonts -->
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Cinzel:wght@700;900&family=Poppins:wght@400;600;700;800;900&family=Tiro+Devanagari+Marathi:ital@0;1&family=Yatra+One&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">

    <style>
        :root {
            --gold-bright: #ffd700;
            --gold-deep: #f59e0b;
            --gold-grad: linear-gradient(135deg, #ffe066 0%, #ffd700 50%, #f59e0b 100%);
            --royal-bg: radial-gradient(circle at 50% 6%, #2d0a4e 0%, #130426 55%, #05000e 100%);
            --card-border: rgba(255, 215, 0, 0.45);
            --card-glow: 0 10px 30px rgba(0, 0, 0, 0.85), 0 0 25px rgba(255, 160, 0, 0.22);
        }

        * {
            box-sizing: border-box;
            margin: 0;
            padding: 0;
            user-select: none;
            -webkit-user-select: none;
            -webkit-tap-highlight-color: transparent;
        }

        html, body {
            width: 100%;
            height: 100vh;
            overflow: hidden;
            overscroll-behavior: none;
            touch-action: manipulation;
            background: var(--royal-bg);
            font-family: 'Poppins', 'Tiro Devanagari Marathi', sans-serif;
            color: #fff;
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: space-between;
            padding: 2px 6px 4px;
            position: relative;
        }

        /* Ambient floating golden stars/dust */
        .ambient-canvas {
            position: absolute;
            top: 0; left: 0; width: 100%; height: 100%;
            pointer-events: none;
            z-index: 1;
        }

        /* Fullscreen white flash overlay for bomb explosion */
        #flashOverlay {
            position: absolute;
            top: 0; left: 0; width: 100%; height: 100%;
            background: #ffffff;
            opacity: 0;
            pointer-events: none;
            z-index: 100;
            transition: opacity 0.05s ease-out;
        }

        /* Top Action Utility Bar (Compact, Touching Top) */
        .top-utility-bar {
            position: relative;
            z-index: 20;
            width: 100%;
            max-width: 760px;
            display: flex;
            justify-content: space-between;
            align-items: center;
            padding: 1px 4px;
            flex-shrink: 0;
        }

        .lang-switch-btn {
            background: rgba(255, 215, 0, 0.15);
            border: 1.5px solid var(--card-border);
            color: #ffd700;
            padding: 3px 10px;
            border-radius: 18px;
            font-size: 0.72rem;
            font-weight: 700;
            cursor: pointer;
            display: flex;
            align-items: center;
            gap: 5px;
            backdrop-filter: blur(8px);
            transition: all 0.2s;
            box-shadow: 0 2px 8px rgba(0, 0, 0, 0.5);
        }

        .lang-switch-btn:hover {
            background: var(--gold-grad);
            color: #000;
            transform: scale(1.04);
        }

        .wasm-badge {
            background: rgba(16, 185, 129, 0.18);
            border: 1px solid #10b981;
            color: #6ee7b7;
            padding: 2px 8px;
            border-radius: 12px;
            font-size: 0.62rem;
            font-weight: 700;
            display: flex;
            align-items: center;
            gap: 4px;
        }

        .wasm-badge .pulse {
            width: 5px; height: 5px; border-radius: 50%; background: #10b981; box-shadow: 0 0 6px #10b981;
            animation: pulseDot 1s infinite alternate;
        }

        .sound-switch-btn {
            background: rgba(255, 215, 0, 0.15);
            border: 1.5px solid var(--card-border);
            color: #ffd700;
            padding: 3px 10px;
            border-radius: 18px;
            font-size: 0.72rem;
            font-weight: 700;
            cursor: pointer;
            display: flex;
            align-items: center;
            gap: 5px;
            backdrop-filter: blur(8px);
            transition: all 0.2s;
        }

        .sound-switch-btn.active {
            background: var(--gold-grad);
            color: #000;
            box-shadow: 0 2px 10px rgba(255, 215, 0, 0.6);
        }

        /* ========================================================
           HEADER: COMPACT & TOUCHING THE TOP (MAX ROOM FOR BOX)
           ======================================================== */
        .festive-hero {
            position: relative;
            z-index: 10;
            width: 100%;
            max-width: 760px;
            text-align: center;
            display: flex;
            flex-direction: column;
            align-items: center;
            gap: 2px;
            flex-shrink: 0;
            margin-top: -1px;
        }

        .header-row {
            display: flex;
            align-items: center;
            justify-content: center;
            gap: 10px;
            width: 100%;
        }

        .diya-wrapper {
            display: flex;
            flex-direction: column;
            align-items: center;
            position: relative;
            width: 28px;
            height: 30px;
            flex-shrink: 0;
        }

        .diya-flame {
            width: 11px;
            height: 17px;
            background: radial-gradient(ellipse at 50% 85%, #ffffff 0%, #fffb00 35%, #ff5500 70%, transparent 95%);
            border-radius: 50% 50% 35% 35% / 70% 70% 30% 30%;
            filter: drop-shadow(0 0 8px #ff6600) drop-shadow(0 0 16px #ffbb00);
            animation: flameFlicker 1.3s infinite alternate ease-in-out;
            transform-origin: center bottom;
        }

        .diya-base {
            width: 26px;
            height: 11px;
            background: linear-gradient(180deg, #d97706 0%, #78350f 100%);
            border-radius: 0 0 16px 16px;
            border-top: 1.5px solid #fde68a;
            box-shadow: 0 2px 6px rgba(0,0,0,0.7);
            margin-top: -2px;
        }

        @keyframes flameFlicker {
            0% { transform: scale(1) rotate(-3deg); filter: drop-shadow(0 0 8px #ff7700); }
            50% { transform: scale(1.12, 0.94) rotate(3deg); filter: drop-shadow(0 0 11px #ff4400); }
            100% { transform: scale(0.96, 1.06) rotate(-2deg); filter: drop-shadow(0 0 8px #ff8800); }
        }

        .title-block {
            display: flex;
            flex-direction: column;
            align-items: center;
        }

        .shloka-text {
            font-size: 0.68rem;
            font-weight: 700;
            color: #fde68a;
            letter-spacing: 1.2px;
            text-shadow: 0 0 8px rgba(255, 215, 0, 0.8);
            margin-bottom: -2px;
        }

        .main-title {
            font-family: 'Cinzel', 'Yatra One', serif, sans-serif;
            font-size: 1.5rem;
            font-weight: 900;
            line-height: 1.1;
            color: #ffd700;
            text-shadow: 0 0 12px rgba(255, 215, 0, 0.85), 0 0 24px rgba(255, 140, 0, 0.7), 0 2px 4px #000000;
            letter-spacing: 1.2px;
            display: flex;
            align-items: center;
            gap: 6px;
        }

        .main-title-sparkle {
            color: #ffea00;
            font-size: 0.95rem;
            animation: pulseGlow 1.2s infinite alternate;
        }

        @keyframes pulseGlow {
            0% { transform: scale(0.9); opacity: 0.7; }
            100% { transform: scale(1.2); opacity: 1; filter: drop-shadow(0 0 8px #fff); }
        }

        .subhechha-card {
            background: rgba(255, 215, 0, 0.1);
            border: 1px solid rgba(255, 215, 0, 0.35);
            border-radius: 12px;
            padding: 2px 10px;
            width: 100%;
            max-width: 95%;
            backdrop-filter: blur(6px);
            display: flex;
            align-items: center;
            justify-content: center;
            box-shadow: inset 0 0 8px rgba(255, 215, 0, 0.08);
            min-height: 20px;
        }

        .subhechha-text {
            font-size: 0.71rem;
            font-weight: 600;
            color: #fef08a;
            text-align: center;
            transition: opacity 0.35s ease, transform 0.35s ease;
            letter-spacing: 0.3px;
            line-height: 1.15;
        }

        /* ========================================================
           MAXIMIZED CENTRAL CRACKER STAGE BOX (UP TO 63VH TALL)
           ======================================================== */
        .stage-container {
            position: relative;
            z-index: 10;
            width: 100%;
            max-width: 760px;
            flex: 1;
            min-height: 360px;
            max-height: 63vh;
            background: radial-gradient(circle at 50% 88%, #200735 0%, #0f031e 75%, #06000c 100%);
            border: 2px solid var(--card-border);
            border-radius: 20px;
            box-shadow: var(--card-glow);
            overflow: hidden;
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            margin: 3px 0;
        }

        #mainCanvas {
            width: 100%;
            height: 100%;
            display: block;
            touch-action: none;
            cursor: pointer;
        }

        .stage-hud {
            position: absolute;
            top: 8px;
            left: 10px;
            right: 10px;
            display: flex;
            justify-content: space-between;
            align-items: center;
            pointer-events: none;
            z-index: 15;
        }

        .cracker-badge {
            background: rgba(13, 3, 26, 0.85);
            border: 1px solid var(--card-border);
            padding: 3px 10px;
            border-radius: 12px;
            font-size: 0.72rem;
            font-weight: 700;
            color: #ffd700;
            display: flex;
            align-items: center;
            gap: 5px;
            backdrop-filter: blur(8px);
            box-shadow: 0 3px 10px rgba(0, 0, 0, 0.7);
        }

        .status-badge {
            font-size: 0.68rem;
            font-weight: 600;
            color: #e2e8f0;
            background: rgba(0, 0, 0, 0.7);
            border: 1px solid rgba(255, 255, 255, 0.2);
            padding: 3px 9px;
            border-radius: 12px;
            display: flex;
            align-items: center;
            gap: 5px;
        }

        .status-badge .dot {
            width: 7px;
            height: 7px;
            border-radius: 50%;
            background: #10b981;
            box-shadow: 0 0 6px #10b981;
        }

        .status-badge.burning .dot {
            background: #ef4444;
            box-shadow: 0 0 8px #ef4444;
            animation: pulseDot 0.5s infinite alternate;
        }

        @keyframes pulseDot {
            0% { transform: scale(0.8); opacity: 0.6; }
            100% { transform: scale(1.3); opacity: 1; }
        }

        .drag-hint {
            position: absolute;
            bottom: 10px;
            left: 50%;
            transform: translateX(-50%);
            background: rgba(0, 0, 0, 0.75);
            border: 1px solid rgba(255, 215, 0, 0.4);
            color: #fef08a;
            font-size: 0.68rem;
            padding: 3px 12px;
            border-radius: 12px;
            pointer-events: none;
            display: none;
            align-items: center;
            gap: 5px;
            z-index: 15;
            backdrop-filter: blur(6px);
        }

        /* Controls Row */
        .controls-row {
            position: relative;
            z-index: 10;
            display: flex;
            gap: 8px;
            width: 100%;
            max-width: 760px;
            flex-shrink: 0;
            margin-top: 1px;
        }

        .btn-ignite {
            flex: 2.2;
            padding: 10px 14px;
            background: linear-gradient(135deg, #f59e0b 0%, #ef4444 60%, #b91c1c 100%);
            color: #fff;
            border: none;
            border-radius: 14px;
            font-weight: 800;
            font-size: 0.92rem;
            cursor: pointer;
            display: flex;
            align-items: center;
            justify-content: center;
            gap: 7px;
            box-shadow: 0 4px 16px rgba(239, 68, 68, 0.5);
            transition: all 0.2s cubic-bezier(0.34, 1.56, 0.64, 1);
            letter-spacing: 0.4px;
        }

        .btn-ignite:hover {
            transform: translateY(-2px);
            box-shadow: 0 6px 20px rgba(245, 158, 11, 0.7);
        }

        .btn-reset {
            flex: 1;
            padding: 10px 10px;
            background: rgba(255, 215, 0, 0.12);
            color: #ffd700;
            border: 1.5px solid var(--card-border);
            border-radius: 14px;
            font-weight: 700;
            font-size: 0.82rem;
            cursor: pointer;
            display: flex;
            align-items: center;
            justify-content: center;
            gap: 5px;
            backdrop-filter: blur(6px);
            transition: all 0.2s;
        }

        .btn-reset:hover {
            background: rgba(255, 215, 0, 0.22);
            transform: translateY(-2px);
        }

        /* ========================================================
           CLEAN CRACKER SELECTOR TRAY (NO PRAJWAL ON BUTTONS, NO LADI)
           ======================================================== */
        .picker-container {
            position: relative;
            z-index: 10;
            width: 100%;
            max-width: 760px;
            flex-shrink: 0;
            margin-top: 3px;
        }

        .picker-header {
            font-size: 0.65rem;
            font-weight: 700;
            color: #fde68a;
            text-transform: uppercase;
            letter-spacing: 1px;
            margin-bottom: 3px;
            display: flex;
            align-items: center;
            gap: 5px;
            padding-left: 2px;
        }

        .cracker-dock {
            display: flex;
            gap: 7px;
            overflow-x: auto;
            padding-bottom: 3px;
            scrollbar-width: none;
            -webkit-overflow-scrolling: touch;
        }

        .cracker-dock::-webkit-scrollbar { display: none; }

        .cracker-card {
            flex-shrink: 0;
            background: rgba(255, 215, 0, 0.06);
            border: 1.5px solid rgba(255, 215, 0, 0.2);
            border-radius: 12px;
            padding: 5px 9px;
            color: #cbd5e1;
            cursor: pointer;
            display: flex;
            flex-direction: column;
            align-items: center;
            gap: 2px;
            min-width: 70px;
            transition: all 0.2s cubic-bezier(0.34, 1.56, 0.64, 1);
        }

        .cracker-card i {
            font-size: 1.15rem;
            color: #f59e0b;
            transition: transform 0.2s;
        }

        .cracker-card .cracker-lbl {
            font-size: 0.7rem;
            font-weight: 700;
            white-space: nowrap;
        }

        .cracker-card .cracker-sub {
            font-size: 0.55rem;
            color: #94a3b8;
            white-space: nowrap;
        }

        .cracker-card.active {
            background: var(--gold-grad);
            color: #000;
            border-color: #ffd700;
            box-shadow: 0 4px 16px rgba(255, 215, 0, 0.55);
            transform: translateY(-2px);
        }

        .cracker-card.active i {
            color: #000;
            transform: scale(1.15);
        }

        .cracker-card.active .cracker-sub {
            color: #3f2500;
            font-weight: 600;
        }

        /* Footer Credit */
        .creator-credit-bar {
            position: relative;
            z-index: 10;
            display: flex;
            align-items: center;
            justify-content: center;
            gap: 8px;
            width: 100%;
            max-width: 760px;
            margin-top: 2px;
            flex-shrink: 0;
        }

        .credit-badge {
            background: rgba(255, 215, 0, 0.08);
            border: 1px solid rgba(255, 215, 0, 0.3);
            border-radius: 18px;
            padding: 2px 12px;
            font-size: 0.68rem;
            display: flex;
            align-items: center;
            gap: 5px;
            color: #e2e8f0;
            backdrop-filter: blur(6px);
            box-shadow: 0 2px 8px rgba(0, 0, 0, 0.5);
        }

        .credit-author {
            font-weight: 800;
            color: #ffd700;
            letter-spacing: 0.4px;
        }

        .shake-box {
            animation: boxShake 0.45s cubic-bezier(.36,.07,.19,.97) both;
        }

        @keyframes boxShake {
            10%, 90% { transform: translate3d(-4px, 2px, 0); }
            20%, 80% { transform: translate3d(6px, -3px, 0); }
            30%, 50%, 70% { transform: translate3d(-8px, 4px, 0); }
            40%, 60% { transform: translate3d(8px, -4px, 0); }
        }
    </style>
</head>
<body>

    <div id="flashOverlay"></div>
    <canvas class="ambient-canvas" id="ambientCanvas"></canvas>

    <!-- Top Utility Bar -->
    <div class="top-utility-bar">
        <button class="lang-switch-btn" id="btnLangSwitch" title="Switch Language">
            <i class="fas fa-language"></i> <span id="lblLang">मराठी / English</span>
        </button>
        <div class="wasm-badge" title="High-Speed C++ WebAssembly Physics Engine">
            <div class="pulse"></div> <span>C++ WASM Engine</span>
        </div>
        <button class="sound-switch-btn active" id="btnSoundSwitch" title="Sound FX Toggle">
            <i class="fas fa-volume-high"></i> <span id="lblSound">आवाज सुरू</span>
        </button>
    </div>

    <!-- COMPACT FESTIVE HEADER TOUCHING THE TOP -->
    <header class="festive-hero">
        <div class="header-row">
            <div class="diya-wrapper">
                <div class="diya-flame"></div>
                <div class="diya-base"></div>
            </div>

            <div class="title-block">
                <div class="shloka-text" id="headerShloka">॥ तमसो मा ज्योतिर्गमय ॥</div>
                <h1 class="main-title" id="headerMainTitle">
                    <i class="fas fa-sparkles main-title-sparkle"></i>
                    <span id="titleText">शुभ दीपावली २०२६</span>
                    <i class="fas fa-sparkles main-title-sparkle"></i>
                </h1>
            </div>

            <div class="diya-wrapper">
                <div class="diya-flame"></div>
                <div class="diya-base"></div>
            </div>
        </div>

        <div class="subhechha-card">
            <div class="subhechha-text" id="subhechhaBanner">
                दीपावलीच्या तुम्हाला व तुमच्या संपूर्ण परिवारास मनःपूर्वक हार्दिक शुभेच्छा!
            </div>
        </div>
    </header>

    <!-- MAXIMIZED CRACKER BOX (PLENTY OF SKY FOR ROCKET & PAUS) -->
    <main class="stage-container" id="stageBox">
        <div class="stage-hud">
            <div class="cracker-badge" id="hudBadge">
                <i class="fas fa-volcano"></i> <span id="hudBadgeName">पाऊस (Paus)</span>
            </div>
            <div class="status-badge" id="hudStatus">
                <div class="dot"></div> <span id="hudStatusText">तयार आहे • पेटवा</span>
            </div>
        </div>

        <div class="drag-hint" id="dragHint">
            <i class="fas fa-hand-pointer"></i> <span id="lblDragHint">फुलबाजा फिरवण्यासाठी स्क्रीनवर ड्रॅग करा</span>
        </div>

        <canvas id="mainCanvas"></canvas>
    </main>

    <!-- ACTION CONTROLS ROW -->
    <div class="controls-row">
        <button class="btn-ignite" id="btnIgnite">
            <i class="fas fa-fire"></i> <span id="lblBtnIgnite">फटाका पेटवा (IGNITE)</span>
        </button>
        <button class="btn-reset" id="btnReset">
            <i class="fas fa-rotate-left"></i> <span id="lblBtnReset">नवा फटाका</span>
        </button>
    </div>

    <!-- CLEAN CRACKER SELECTOR TRAY (CLEAN NAMES, NO PRAJWAL ON BUTTONS, NO LADI) -->
    <section class="picker-container">
        <div class="picker-header" id="lblPickerTitle">
            <i class="fas fa-boxes-stacked"></i> फटाका निवडा (SELECT CRACKER):
        </div>
        <div class="cracker-dock">
            <!-- 1. Paus -->
            <div class="cracker-card active" onclick="selectCracker('anar')">
                <i class="fas fa-volcano"></i>
                <span class="cracker-lbl" id="cardLbl_anar">पाऊस</span>
                <span class="cracker-sub" id="cardSub_anar">Flower Pot</span>
            </div>
            <!-- 2. Chakra -->
            <div class="cracker-card" onclick="selectCracker('chakri')">
                <i class="fas fa-compact-disc"></i>
                <span class="cracker-lbl" id="cardLbl_chakri">चक्र</span>
                <span class="cracker-sub" id="cardSub_chakri">Ground Spinner</span>
            </div>
            <!-- 3. Phulbaja -->
            <div class="cracker-card" onclick="selectCracker('stick')">
                <i class="fas fa-wand-magic-sparkles"></i>
                <span class="cracker-lbl" id="cardLbl_stick">फुलबाजा</span>
                <span class="cracker-sub" id="cardSub_stick">Sparkler Stick</span>
            </div>
            <!-- 4. Sutli Bomb -->
            <div class="cracker-card" onclick="selectCracker('bomb')">
                <i class="fas fa-bomb"></i>
                <span class="cracker-lbl" id="cardLbl_bomb">सुतळी बॉम्ब</span>
                <span class="cracker-sub" id="cardSub_bomb">Sutli Bomb</span>
            </div>
            <!-- 5. Rocket -->
            <div class="cracker-card" onclick="selectCracker('rocket')">
                <i class="fas fa-rocket"></i>
                <span class="cracker-lbl" id="cardLbl_rocket">रॉकेट</span>
                <span class="cracker-sub" id="cardSub_rocket">Sky Rocket</span>
            </div>
            <!-- 6. Lavangi (ONLY LAVANGI, NO LADI) -->
            <div class="cracker-card" onclick="selectCracker('ladi')">
                <i class="fas fa-meteor"></i>
                <span class="cracker-lbl" id="cardLbl_ladi">लवंगी</span>
                <span class="cracker-sub" id="cardSub_ladi">Lavangi</span>
            </div>
            <!-- 7. Saap Tablet -->
            <div class="cracker-card" onclick="selectCracker('snake')">
                <i class="fas fa-worm"></i>
                <span class="cracker-lbl" id="cardLbl_snake">साप गोळी</span>
                <span class="cracker-sub" id="cardSub_snake">Snake Tablet</span>
            </div>
            <!-- 8. Sky Shots -->
            <div class="cracker-card" onclick="selectCracker('skyshot')">
                <i class="fas fa-burst"></i>
                <span class="cracker-lbl" id="cardLbl_skyshot">आकाशी तोफ</span>
                <span class="cracker-sub" id="cardSub_skyshot">7 Sky Shots</span>
            </div>
        </div>
    </section>

    <!-- FOOTER CREDIT -->
    <footer class="creator-credit-bar">
        <div class="credit-badge">
            <i class="fas fa-crown"></i>
            <span>Created with ❤️ by <strong class="credit-author">Prajwal Raut</strong> • Diwali 2026 Special Edition 🪔</span>
        </div>
    </footer>

    <!-- ========================================================
         JAVASCRIPT & C++ WEBASSEMBLY ENGINE
         ======================================================== -->
    <script>
        // ========================================================
        // 1. C++ WEBASSEMBLY INTEGRATION
        // ========================================================
        const WASM_B64 = "''' + wasm_b64 + r'''";
        let wasmEngine = null;

        async function initWasmEngine() {
            try {
                const response = await fetch('cracker_engine.wasm');
                if (response.ok) {
                    const bytes = await response.arrayBuffer();
                    const module = await WebAssembly.instantiate(bytes);
                    wasmEngine = module.instance.exports;
                    console.log('⚡ C++ WASM Engine initialized from server file!');
                    return;
                }
            } catch (e) {
                console.log('Fetch fallback to embedded base64 WASM...');
            }

            try {
                const binaryStr = atob(WASM_B64);
                const bytes = new Uint8Array(binaryStr.length);
                for (let i = 0; i < binaryStr.length; i++) {
                    bytes[i] = binaryStr.charCodeAt(i);
                }
                const module = await WebAssembly.instantiate(bytes.buffer);
                wasmEngine = module.instance.exports;
                console.log('⚡ C++ WASM Engine initialized from embedded Base64 buffer!');
            } catch (err) {
                console.warn('WASM initialization fallback to JS engine:', err);
            }
        }
        initWasmEngine();

        let currentLang = 'mr';

        // CLEAN BUTTON NAMES (NO PRAJWAL ON BUTTONS)
        const I18N = {
            mr: {
                langBtn: "मराठी (MR)",
                soundOn: "आवाज सुरू",
                soundOff: "आवाज बंद",
                shloka: "॥ तमसो मा ज्योतिर्गमय ॥",
                mainTitle: "शुभ दीपावली २०२६",
                subhechhas: [
                    "दीपावलीच्या तुम्हाला व तुमच्या संपूर्ण परिवारास मनःपूर्वक हार्दिक शुभेच्छा!",
                    "सुख, समृद्धी, उत्तम आरोग्य आणि ऐश्वर्याचे दीप तुमच्या आयुष्यात सदैव तेवत राहो!",
                    "प्रकाशाचा हा पावन दीपोत्सव आपल्या जीवनात नवीन उमेद व आनंद घेऊन येवो!",
                    "लक्ष्मी मातेच्या असीम आशीर्वादाने आपल्या घरी अखंड भरभराट लाभो!"
                ],
                igniteBtn: "फटाका पेटवा (IGNITE)",
                resetBtn: "नवा फटाका",
                readyStatus: "तयार आहे • पेटवा",
                burningStatus: "धडाका सुरू आहे...!",
                dragHint: "फुलबाजा फिरवण्यासाठी स्क्रीनवर ड्रॅग करा",
                pickerTitle: "फटाका निवडा (SELECT CRACKER):",
                crackers: {
                    anar: { name: "पाऊस", sub: "Flower Pot", badge: "पाऊस (Paus)" },
                    chakri: { name: "चक्र", sub: "Ground Spinner", badge: "चक्र (Chakra)" },
                    stick: { name: "फुलबाजा", sub: "Sparkler Stick", badge: "फुलबाजा (Phulbaja)" },
                    bomb: { name: "सुतळी बॉम्ब", sub: "Sutli Bomb", badge: "सुतळी बॉम्ब (Bomb)" },
                    rocket: { name: "रॉकेट", sub: "Sky Rocket", badge: "रॉकेट (Rocket)" },
                    ladi: { name: "लवंगी", sub: "Lavangi", badge: "लवंगी (Lavangi)" },
                    snake: { name: "साप गोळी", sub: "Snake Tablet", badge: "साप गोळी (Snake)" },
                    skyshot: { name: "आकाशी तोफ", sub: "7 Sky Shots", badge: "आकाशी तोफ (7 Shots)" }
                }
            },
            en: {
                langBtn: "English (EN)",
                soundOn: "Sound ON",
                soundOff: "Sound OFF",
                shloka: "॥ Lead Us From Darkness To Light ॥",
                mainTitle: "HAPPY DIWALI 2026",
                subhechhas: [
                    "Wishing You & Your Entire Family a Very Happy, Bright & Prosperous Diwali!",
                    "May the Divine Lights of Diwali Bring Good Fortune, Health & Endless Joy!",
                    "May This Festival of Lights Fill Every Corner of Your Life with Prosperity!",
                    "Celebrate an Eco-Friendly, Safe and Grand Digital Diwali 2026!"
                ],
                igniteBtn: "IGNITE CRACKER",
                resetBtn: "NEW CRACKER",
                readyStatus: "Ready • Tap Ignite",
                burningStatus: "Firing in progress...!",
                dragHint: "Drag on screen to move the sparkler stick",
                pickerTitle: "CHOOSE YOUR CRACKER:",
                crackers: {
                    anar: { name: "Flower Pot", sub: "Paus Fountain", badge: "Flower Pot (Paus)" },
                    chakri: { name: "Chakra", sub: "Ground Spinner", badge: "Ground Chakra (Spinner)" },
                    stick: { name: "Sparkler", sub: "Handheld Sizzler", badge: "Sparkler Stick (Phulbaja)" },
                    bomb: { name: "Sutli Bomb", sub: "Jute Bomb", badge: "Sutli Bomb (Jute Bomb)" },
                    rocket: { name: "Sky Rocket", sub: "High Altitude", badge: "Sky Rocket (Rocket)" },
                    ladi: { name: "Lavangi", sub: "Crackers", badge: "Lavangi (Crackers)" },
                    snake: { name: "Snake Tablet", sub: "Growing Carbon Snake", badge: "Black Snake Tablet" },
                    skyshot: { name: "7 Sky Shots", sub: "Aerial Chrysanthemum", badge: "7-Color Sky Shots" }
                }
            }
        };

        function applyTranslations() {
            const data = I18N[currentLang];
            document.getElementById('lblLang').innerText = data.langBtn;
            document.getElementById('lblSound').innerText = sfx.enabled ? data.soundOn : data.soundOff;
            document.getElementById('headerShloka').innerText = data.shloka;
            document.getElementById('titleText').innerText = data.mainTitle;
            document.getElementById('lblBtnIgnite').innerText = data.igniteBtn;
            document.getElementById('lblBtnReset').innerText = data.resetBtn;
            document.getElementById('lblDragHint').innerText = data.dragHint;
            document.getElementById('lblPickerTitle').innerHTML = `<i class="fas fa-boxes-stacked"></i> ${data.pickerTitle}`;

            for (let [key, c] of Object.entries(data.crackers)) {
                const elLbl = document.getElementById(`cardLbl_${key}`);
                const elSub = document.getElementById(`cardSub_${key}`);
                if (elLbl) elLbl.innerText = c.name;
                if (elSub) elSub.innerText = c.sub;
            }

            const curCrackerData = data.crackers[currentCracker];
            if (curCrackerData) {
                document.getElementById('hudBadgeName').innerText = curCrackerData.badge;
            }
            updateStatusText();
        }

        function updateStatusText() {
            const data = I18N[currentLang];
            const hudStatusText = document.getElementById('hudStatusText');
            const hudStatus = document.getElementById('hudStatus');
            if (isBurning) {
                hudStatusText.innerText = data.burningStatus;
                hudStatus.classList.add('burning');
            } else {
                hudStatusText.innerText = data.readyStatus;
                hudStatus.classList.remove('burning');
            }
        }

        document.getElementById('btnLangSwitch').addEventListener('click', () => {
            currentLang = (currentLang === 'mr') ? 'en' : 'mr';
            applyTranslations();
            updateSubhechha(true);
        });

        let subhechhaIdx = 0;
        const elSubhechha = document.getElementById('subhechhaBanner');

        function updateSubhechha(immediate = false) {
            const list = I18N[currentLang].subhechhas;
            if (immediate) {
                elSubhechha.style.opacity = '1';
                elSubhechha.innerText = list[subhechhaIdx % list.length];
                return;
            }
            elSubhechha.style.opacity = '0';
            elSubhechha.style.transform = 'translateY(5px)';
            setTimeout(() => {
                subhechhaIdx = (subhechhaIdx + 1) % list.length;
                elSubhechha.innerText = list[subhechhaIdx];
                elSubhechha.style.opacity = '1';
                elSubhechha.style.transform = 'translateY(0)';
            }, 350);
        }
        setInterval(() => updateSubhechha(false), 4200);

        // ========================================================
        // 2. SOUND SYNTHESIZER (DEEP BOMB EXPLOSION & ROCKET ASCENT)
        // ========================================================
        class SoundSynth {
            constructor() {
                this.ctx = null;
                this.enabled = true;
            }

            init() {
                if (!this.ctx) {
                    const AudioContext = window.AudioContext || window.webkitAudioContext;
                    this.ctx = new AudioContext();
                }
                if (this.ctx.state === 'suspended') {
                    this.ctx.resume();
                }
            }

            playFuse() {
                if (!this.enabled) return;
                this.init();
                const now = this.ctx.currentTime;
                const dur = 0.22;
                const buf = this.ctx.createBuffer(1, Math.floor(this.ctx.sampleRate * dur), this.ctx.sampleRate);
                const d = buf.getChannelData(0);
                for (let i = 0; i < d.length; i++) d[i] = (Math.random() * 2 - 1) * Math.exp(-i / (d.length * 0.35));
                const src = this.ctx.createBufferSource();
                src.buffer = buf;
                const filter = this.ctx.createBiquadFilter();
                filter.type = 'highpass';
                filter.frequency.setValueAtTime(2600, now);
                const gain = this.ctx.createGain();
                gain.gain.setValueAtTime(0.08, now);
                gain.gain.linearRampToValueAtTime(0.001, now + dur);
                src.connect(filter); filter.connect(gain); gain.connect(this.ctx.destination);
                src.start(now);
            }

            playCrackle() {
                if (!this.enabled) return;
                this.init();
                const now = this.ctx.currentTime;
                const osc = this.ctx.createOscillator();
                const gain = this.ctx.createGain();
                osc.type = 'square';
                osc.frequency.setValueAtTime(1400 + Math.random() * 3200, now);
                gain.gain.setValueAtTime(0.08, now);
                gain.gain.exponentialRampToValueAtTime(0.001, now + 0.035);
                osc.connect(gain); gain.connect(this.ctx.destination);
                osc.start(now); osc.stop(now + 0.035);
            }

            playWhirr() {
                if (!this.enabled) return;
                this.init();
                const now = this.ctx.currentTime;
                const osc = this.ctx.createOscillator();
                const gain = this.ctx.createGain();
                osc.type = 'sawtooth';
                osc.frequency.setValueAtTime(420 + Math.random() * 120, now);
                osc.frequency.linearRampToValueAtTime(820, now + 0.08);
                gain.gain.setValueAtTime(0.09, now);
                gain.gain.exponentialRampToValueAtTime(0.001, now + 0.08);
                osc.connect(gain); gain.connect(this.ctx.destination);
                osc.start(now); osc.stop(now + 0.08);
            }

            playWhoosh() {
                if (!this.enabled) return;
                this.init();
                const now = this.ctx.currentTime;
                const dur = 1.05;
                const osc = this.ctx.createOscillator();
                const gain = this.ctx.createGain();
                osc.type = 'sawtooth';
                osc.frequency.setValueAtTime(160, now);
                osc.frequency.exponentialRampToValueAtTime(1800, now + dur);
                gain.gain.setValueAtTime(0.01, now);
                gain.gain.linearRampToValueAtTime(0.18, now + dur * 0.7);
                gain.gain.exponentialRampToValueAtTime(0.001, now + dur);
                osc.connect(gain); gain.connect(this.ctx.destination);
                osc.start(now); osc.stop(now + dur);
            }

            playBombBang() {
                if (!this.enabled) return;
                this.init();
                const now = this.ctx.currentTime;
                const dur = 0.9;

                const osc = this.ctx.createOscillator();
                const oscGain = this.ctx.createGain();
                osc.type = 'sine';
                osc.frequency.setValueAtTime(160, now);
                osc.frequency.exponentialRampToValueAtTime(24, now + dur);
                oscGain.gain.setValueAtTime(0.9, now);
                oscGain.gain.exponentialRampToValueAtTime(0.001, now + dur);
                osc.connect(oscGain); oscGain.connect(this.ctx.destination);
                osc.start(now); osc.stop(now + dur);

                const buf = this.ctx.createBuffer(1, Math.floor(this.ctx.sampleRate * 0.6), this.ctx.sampleRate);
                const d = buf.getChannelData(0);
                for (let i = 0; i < d.length; i++) d[i] = (Math.random() * 2 - 1) * Math.exp(-i / (d.length * 0.15));
                const noise = this.ctx.createBufferSource();
                noise.buffer = buf;
                const filter = this.ctx.createBiquadFilter();
                filter.type = 'lowpass';
                filter.frequency.setValueAtTime(800, now);
                filter.frequency.exponentialRampToValueAtTime(45, now + 0.6);
                const nGain = this.ctx.createGain();
                nGain.gain.setValueAtTime(0.85, now);
                nGain.gain.exponentialRampToValueAtTime(0.001, now + 0.6);
                noise.connect(filter); filter.connect(nGain); nGain.connect(this.ctx.destination);
                noise.start(now);
            }

            playPop() {
                if (!this.enabled) return;
                this.init();
                const now = this.ctx.currentTime;
                const osc = this.ctx.createOscillator();
                const gain = this.ctx.createGain();
                osc.type = 'square';
                osc.frequency.setValueAtTime(1100, now);
                osc.frequency.exponentialRampToValueAtTime(140, now + 0.05);
                gain.gain.setValueAtTime(0.2, now);
                gain.gain.exponentialRampToValueAtTime(0.001, now + 0.05);
                osc.connect(gain); gain.connect(this.ctx.destination);
                osc.start(now); osc.stop(now + 0.05);
            }

            playAerialBurst() {
                if (!this.enabled) return;
                this.init();
                const now = this.ctx.currentTime;
                const dur = 0.65;
                const osc = this.ctx.createOscillator();
                const gain = this.ctx.createGain();
                osc.type = 'triangle';
                osc.frequency.setValueAtTime(260, now);
                osc.frequency.exponentialRampToValueAtTime(40, now + dur);
                gain.gain.setValueAtTime(0.5, now);
                gain.gain.exponentialRampToValueAtTime(0.001, now + dur);
                osc.connect(gain); gain.connect(this.ctx.destination);
                osc.start(now); osc.stop(now + dur);
            }
        }
        const sfx = new SoundSynth();

        const btnSoundSwitch = document.getElementById('btnSoundSwitch');
        btnSoundSwitch.addEventListener('click', () => {
            sfx.enabled = !sfx.enabled;
            if (sfx.enabled) {
                btnSoundSwitch.classList.add('active');
                btnSoundSwitch.innerHTML = `<i class="fas fa-volume-high"></i> <span id="lblSound">${I18N[currentLang].soundOn}</span>`;
                sfx.playCrackle();
            } else {
                btnSoundSwitch.classList.remove('active');
                btnSoundSwitch.innerHTML = `<i class="fas fa-volume-xmark"></i> <span id="lblSound">${I18N[currentLang].soundOff}</span>`;
            }
        });

        // Ambient background
        const ambCanvas = document.getElementById('ambientCanvas');
        const ambCtx = ambCanvas.getContext('2d');
        let ambStars = [];

        function initAmbientStars() {
            ambCanvas.width = window.innerWidth;
            ambCanvas.height = window.innerHeight;
            ambStars = [];
            for (let i = 0; i < 40; i++) {
                ambStars.push({
                    x: Math.random() * ambCanvas.width,
                    y: Math.random() * ambCanvas.height,
                    r: Math.random() * 1.5 + 0.5,
                    alpha: Math.random(),
                    speed: Math.random() * 0.01 + 0.005
                });
            }
        }
        window.addEventListener('resize', initAmbientStars);
        initAmbientStars();

        function renderAmbientStars() {
            ambCtx.clearRect(0, 0, ambCanvas.width, ambCanvas.height);
            for (let s of ambStars) {
                s.alpha += s.speed;
                const a = (Math.sin(s.alpha) + 1) / 2;
                ambCtx.fillStyle = `rgba(255, 215, 0, ${a * 0.55})`;
                ambCtx.beginPath();
                ambCtx.arc(s.x, s.y, s.r, 0, Math.PI * 2);
                ambCtx.fill();
            }
            requestAnimationFrame(renderAmbientStars);
        }
        renderAmbientStars();

        // ========================================================
        // 3. FIRST-VERSION PROVEN CANVASCART LIGHT & SPARKLE ENGINE
        // ========================================================
        const canvas = document.getElementById('mainCanvas');
        const ctx = canvas.getContext('2d');
        const stageBox = document.getElementById('stageBox');

        function resizeMainCanvas() {
            canvas.width = stageBox.clientWidth;
            canvas.height = stageBox.clientHeight;
        }
        window.addEventListener('resize', resizeMainCanvas);
        resizeMainCanvas();

        // High-Quality Glowing Sparkle Particle with Trail
        class SparkleParticle {
            constructor(x, y, color, vx, vy, friction = 0.96, gravity = 0.12, decay = 0.018, bounce = true, size = 2.5) {
                this.x = x;
                this.y = y;
                this.color = color;
                this.vx = vx;
                this.vy = vy;
                this.friction = friction;
                this.gravity = gravity;
                this.decay = decay;
                this.bounce = bounce;
                this.size = size;
                this.alpha = 1.0;
                this.trail = [];
                this.maxTrail = 5;
            }

            update(groundY) {
                this.trail.push({ x: this.x, y: this.y });
                if (this.trail.length > this.maxTrail) this.trail.shift();

                this.vx *= this.friction;
                this.vy *= this.friction;
                this.vy += this.gravity;
                this.x += this.vx;
                this.y += this.vy;

                // Floor collision
                if (this.y >= groundY) {
                    this.y = groundY;
                    if (this.bounce) {
                        this.vy = -this.vy * 0.35;
                        this.vx *= 0.8;
                    } else {
                        this.vy = 0;
                        this.vx *= 0.9;
                    }
                }

                this.alpha -= this.decay;
            }

            draw(ctx) {
                if (this.alpha <= 0) return;
                ctx.save();
                ctx.globalAlpha = Math.max(0, this.alpha);

                // Trailing light line
                if (this.trail.length > 1) {
                    ctx.strokeStyle = this.color;
                    ctx.lineWidth = this.size;
                    ctx.beginPath();
                    ctx.moveTo(this.trail[0].x, this.trail[0].y);
                    for (let i = 1; i < this.trail.length; i++) {
                        ctx.lineTo(this.trail[i].x, this.trail[i].y);
                    }
                    ctx.stroke();
                }

                // Bright glowing white-hot core
                ctx.fillStyle = '#ffffff';
                ctx.beginPath();
                ctx.arc(this.x, this.y, this.size * 0.75, 0, Math.PI * 2);
                ctx.fill();

                ctx.restore();
            }
        }

        // Ascending Rocket Missile
        class AscendingRocket {
            constructor(startX, startY, targetX, targetY) {
                this.x = startX;
                this.y = startY;
                this.targetX = targetX;
                this.targetY = targetY;
                this.angle = Math.atan2(targetY - startY, targetX - startX);
                this.speed = 12.5;
                this.vx = Math.cos(this.angle) * this.speed;
                this.vy = Math.sin(this.angle) * this.speed;
                this.trail = [];
                this.alive = true;
            }

            update() {
                this.trail.push({ x: this.x, y: this.y });
                if (this.trail.length > 6) this.trail.shift();

                this.x += this.vx;
                this.y += this.vy;

                // Thruster exhaust sparks
                particles.push(new SparkleParticle(
                    this.x + (Math.random() * 4 - 2),
                    this.y + 12,
                    '#ff6600',
                    (Math.random() - 0.5) * 1.5,
                    Math.random() * 3 + 2,
                    0.94, 0.05, 0.06, false, 2
                ));

                const dist = Math.hypot(this.targetX - this.x, this.targetY - this.y);
                if (dist < 18 || this.y <= this.targetY) {
                    this.alive = false;
                    triggerMultiBreakFireworks(this.targetX, this.targetY);
                }
            }

            draw(ctx) {
                ctx.save();
                ctx.strokeStyle = '#ffd700';
                ctx.lineWidth = 3;
                ctx.beginPath();
                if (this.trail.length > 0) {
                    ctx.moveTo(this.trail[0].x, this.trail[0].y);
                    for (let p of this.trail) ctx.lineTo(p.x, p.y);
                }
                ctx.stroke();

                // Rocket Cartridge
                ctx.fillStyle = '#dc2626';
                ctx.fillRect(this.x - 4, this.y - 12, 8, 22);
                // Golden nose cone
                ctx.fillStyle = '#ffd700';
                ctx.beginPath();
                ctx.moveTo(this.x - 5, this.y - 12);
                ctx.lineTo(this.x + 5, this.y - 12);
                ctx.lineTo(this.x, this.y - 22);
                ctx.closePath();
                ctx.fill();
                ctx.restore();
            }
        }

        let particles = [];
        let rockets = [];
        let snakeSegments = [];
        let activeTimerIds = [];
        let isBurning = false;

        // Interactive Stick Coordinates
        let stickX = 0, stickY = 0;
        let isDraggingStick = false;

        // Chakra Physics State: ONE SINGLE NOZZLE ON RIM
        let chakriAngle = 0;
        let chakriRPM = 0;
        let chakriNozzleX = 0, chakriNozzleY = 0;

        // Sutli Bomb State
        let bombFuseHeight = 28;
        let bombExploded = false;
        let shockwaveRadius = 0;
        let shockwaveAlpha = 0;

        function clearActiveTimers() {
            for (let id of activeTimerIds) {
                clearInterval(id);
                clearTimeout(id);
            }
            activeTimerIds = [];
        }

        // ========================================================
        // 4. MULTI-BREAK FIREWORKS BURSTS (AUTHENTIC FIRST-VERSION LOOK)
        // ========================================================
        function triggerScreenFlash() {
            const fl = document.getElementById('flashOverlay');
            fl.style.opacity = '0.92';
            setTimeout(() => { fl.style.opacity = '0'; }, 160);
        }

        function triggerMultiBreakFireworks(x, y) {
            sfx.playAerialBurst();

            // 1. PRIMARY SPHERICAL SHELL: 160+ Golden & Ruby Willow Comets
            const primaryColors = ['#ffd700', '#ef4444', '#f59e0b', '#ffffff'];
            for (let i = 0; i < 160; i++) {
                const angle = Math.random() * Math.PI * 2;
                const speed = Math.random() * 9 + 2;
                const color = primaryColors[Math.floor(Math.random() * primaryColors.length)];
                particles.push(new SparkleParticle(
                    x, y, color,
                    Math.cos(angle) * speed,
                    Math.sin(angle) * speed,
                    0.95, 0.07, 0.016, false, 2.8
                ));
            }

            // 2. SECONDARY OUTER CHRYSANTHEMUM RING (120ms later)
            setTimeout(() => {
                sfx.playCrackle();
                const ringColors = ['#39ff14', '#00ffcc', '#ff00aa'];
                for (let k = 0; k < 90; k++) {
                    const angle = Math.random() * Math.PI * 2;
                    const speed = Math.random() * 6 + 4;
                    const color = ringColors[Math.floor(Math.random() * ringColors.length)];
                    particles.push(new SparkleParticle(
                        x, y, color,
                        Math.cos(angle) * speed,
                        Math.sin(angle) * speed,
                        0.94, 0.05, 0.02, false, 2.5
                    ));
                }
            }, 120);

            // 3. SATELLITE SUB-BURSTS (250ms later)
            setTimeout(() => {
                for (let s = 0; s < 6; s++) {
                    const a = (s * Math.PI * 2) / 6;
                    const sx = x + Math.cos(a) * 45;
                    const sy = y + Math.sin(a) * 45;
                    sfx.playCrackle();
                    for (let j = 0; j < 30; j++) {
                        const subAngle = Math.random() * Math.PI * 2;
                        const subSpeed = Math.random() * 4 + 1.5;
                        particles.push(new SparkleParticle(
                            sx, sy, '#ffe066',
                            Math.cos(subAngle) * subSpeed,
                            Math.sin(subAngle) * subSpeed,
                            0.93, 0.04, 0.03, false, 2.2
                        ));
                    }
                }
            }, 250);
        }

        // ========================================================
        // 5. DRAWING AUTHENTIC PHYSICAL CRACKERS (WITH "PRAJWAL" STAMP)
        // ========================================================
        function drawCrackerStudio(groundY) {
            const cx = canvas.width / 2;

            // Draw Ground Terrace & Golden Rangoli Mandala
            ctx.save();
            ctx.strokeStyle = 'rgba(255, 215, 0, 0.25)';
            ctx.lineWidth = 2;
            ctx.beginPath();
            ctx.moveTo(15, groundY);
            ctx.lineTo(canvas.width - 15, groundY);
            ctx.stroke();

            // Center Rangoli Circle
            ctx.strokeStyle = 'rgba(255, 215, 0, 0.18)';
            ctx.lineWidth = 1.5;
            ctx.beginPath();
            ctx.ellipse(cx, groundY + 12, 110, 26, 0, 0, Math.PI * 2);
            ctx.stroke();
            ctx.restore();

            // Ground Shockwave
            if (shockwaveAlpha > 0) {
                ctx.save();
                ctx.strokeStyle = `rgba(255, 215, 0, ${shockwaveAlpha})`;
                ctx.lineWidth = 4;
                ctx.beginPath();
                ctx.ellipse(cx, groundY + 8, shockwaveRadius, shockwaveRadius * 0.35, 0, 0, Math.PI * 2);
                ctx.stroke();
                ctx.restore();
            }

            // Burn Scorch Mark on floor
            if (bombExploded) {
                ctx.save();
                ctx.fillStyle = 'rgba(10, 10, 10, 0.85)';
                ctx.beginPath();
                ctx.ellipse(cx, groundY + 6, 45, 14, 0, 0, Math.PI * 2);
                ctx.fill();
                ctx.restore();
            }

            // 1. PAUS (ANAR) - Terracotta Pot with "PRAJWAL" Stamp
            if (currentCracker === 'anar') {
                const potBaseY = groundY;
                const potTopY = groundY - 70;

                ctx.save();
                // Pot Body
                ctx.fillStyle = '#b45309';
                ctx.beginPath();
                ctx.moveTo(cx - 32, potBaseY);
                ctx.lineTo(cx + 32, potBaseY);
                ctx.lineTo(cx + 9, potTopY);
                ctx.lineTo(cx - 9, potTopY);
                ctx.closePath();
                ctx.fill();
                ctx.strokeStyle = '#ffd700';
                ctx.lineWidth = 2.5;
                ctx.stroke();

                // Gold decorative bands
                ctx.fillStyle = '#ffd700';
                ctx.fillRect(cx - 24, potBaseY - 18, 48, 6);

                // PRAJWAL BRAND STAMP ON THE POT
                ctx.fillStyle = '#fde047';
                ctx.font = 'bold 11px sans-serif';
                ctx.textAlign = 'center';
                ctx.fillText('PRAJWAL', cx, potBaseY - 36);
                ctx.font = '9px sans-serif';
                ctx.fillText('👑 PAUS 👑', cx, potBaseY - 24);

                // Fuse at top
                ctx.strokeStyle = '#e2e8f0';
                ctx.lineWidth = 2.5;
                ctx.beginPath();
                ctx.moveTo(cx, potTopY);
                ctx.lineTo(cx, potTopY - 14);
                ctx.stroke();

                ctx.restore();
            }

            // 2. CHAKRA - With ONE SINGLE NOZZLE ON RIM (User instruction)
            else if (currentCracker === 'chakri') {
                const wheelY = groundY - 10;
                const R = 38;

                ctx.save();
                ctx.translate(cx, wheelY);
                ctx.rotate(chakriAngle);

                // Wheel Disc with Swirls
                ctx.fillStyle = '#ef4444';
                ctx.beginPath();
                ctx.arc(0, 0, R, 0, Math.PI * 2);
                ctx.fill();
                ctx.strokeStyle = '#ffd700';
                ctx.lineWidth = 3;
                ctx.stroke();

                // Spiral stripes
                ctx.strokeStyle = '#39ff14';
                ctx.lineWidth = 3;
                for (let i = 0; i < 4; i++) {
                    ctx.rotate(Math.PI / 2);
                    ctx.beginPath();
                    ctx.arc(0, 0, 22, 0, Math.PI / 2);
                    ctx.stroke();
                }

                // Center seal stamped "PRAJWAL"
                ctx.fillStyle = '#ffd700';
                ctx.beginPath();
                ctx.arc(0, 0, 16, 0, Math.PI * 2);
                ctx.fill();
                ctx.fillStyle = '#000000';
                ctx.font = 'bold 7px sans-serif';
                ctx.textAlign = 'center';
                ctx.textBaseline = 'middle';
                ctx.fillText('PRAJWAL', 0, 0);

                // ONE SINGLE NOZZLE ON RIM (BAHAR KA MAIN POINT JAHAN AAG LAGTE HAIN)
                ctx.fillStyle = '#d97706';
                ctx.fillRect(R - 4, -5, 12, 10);
                ctx.strokeStyle = '#fde68a';
                ctx.lineWidth = 1.5;
                ctx.strokeRect(R - 4, -5, 12, 10);

                ctx.restore();

                // Compute exact global position of that single nozzle in the animation
                chakriNozzleX = cx + Math.cos(chakriAngle) * (R + 6);
                chakriNozzleY = wheelY + Math.sin(chakriAngle) * (R + 6);
            }

            // 3. PHULJHADI (STICK) - Draggable with "PRAJWAL" Stamp
            else if (currentCracker === 'stick') {
                ctx.save();
                // Metallic Wire Handle
                ctx.strokeStyle = '#94a3b8';
                ctx.lineWidth = 3;
                ctx.beginPath();
                ctx.moveTo(stickX - 45, stickY + 90);
                ctx.lineTo(stickX, stickY);
                ctx.stroke();

                // Chemical sparkler coating
                ctx.strokeStyle = '#cbd5e1';
                ctx.lineWidth = 7;
                ctx.beginPath();
                ctx.moveTo(stickX - 25, stickY + 50);
                ctx.lineTo(stickX, stickY);
                ctx.stroke();

                // Burning Tip Molten Glow Head
                ctx.fillStyle = isBurning ? '#ffffff' : '#f59e0b';
                ctx.beginPath();
                ctx.arc(stickX, stickY, isBurning ? 6 : 4, 0, Math.PI * 2);
                ctx.fill();

                // Handle tag stamped "PRAJWAL"
                ctx.fillStyle = '#ffd700';
                ctx.font = 'bold 9px sans-serif';
                ctx.fillText('👑 PRAJWAL', stickX - 40, stickY + 95);

                ctx.restore();
            }

            // 4. SUTLI BOMB - Green Jute Twine Block with "PRAJWAL" (NO 1000 WATT)
            else if (currentCracker === 'bomb' && !bombExploded) {
                const bY = groundY - 26;
                ctx.save();

                // Green Jute Twine Cube Body
                ctx.fillStyle = '#22543d';
                ctx.fillRect(cx - 28, bY - 24, 56, 50);
                ctx.strokeStyle = '#859c27';
                ctx.lineWidth = 2.5;
                ctx.strokeRect(cx - 28, bY - 24, 56, 50);

                // Criss-cross jute rope cords
                ctx.beginPath();
                ctx.moveTo(cx - 28, bY); ctx.lineTo(cx + 28, bY);
                ctx.moveTo(cx, bY - 24); ctx.lineTo(cx, bY + 26);
                ctx.stroke();

                // Red/Gold Stamp: "PRAJWAL SUTLI BOMB"
                ctx.fillStyle = '#b91c1c';
                ctx.fillRect(cx - 22, bY - 14, 44, 26);
                ctx.strokeStyle = '#ffd700';
                ctx.lineWidth = 1.5;
                ctx.strokeRect(cx - 22, bY - 14, 44, 26);

                ctx.fillStyle = '#ffd700';
                ctx.font = 'bold 8px sans-serif';
                ctx.textAlign = 'center';
                ctx.fillText('PRAJWAL', cx, bY - 2);
                ctx.font = '7px sans-serif';
                ctx.fillText('सुतळी बॉम्ब', cx, bY + 8);

                // White Cotton Fuse on top (shrinks as it burns)
                ctx.strokeStyle = '#ffffff';
                ctx.lineWidth = 3;
                ctx.beginPath();
                ctx.moveTo(cx, bY - 24);
                ctx.lineTo(cx + 8, bY - 24 - bombFuseHeight);
                ctx.stroke();

                ctx.restore();
            }

            // 5. ROCKET - Glass Bottle on Launch Pad with "PRAJWAL ROCKET"
            else if (currentCracker === 'rocket') {
                const botY = groundY - 40;
                ctx.save();

                // Glass bottle
                ctx.fillStyle = 'rgba(56, 189, 248, 0.35)';
                ctx.strokeStyle = 'rgba(56, 189, 248, 0.7)';
                ctx.lineWidth = 2;
                ctx.fillRect(cx - 10, botY, 20, 42);
                ctx.strokeRect(cx - 10, botY, 20, 42);

                // Rocket Wooden Stick inside
                ctx.strokeStyle = '#d97706';
                ctx.lineWidth = 2.5;
                ctx.beginPath();
                ctx.moveTo(cx + 4, botY - 15);
                ctx.lineTo(cx + 4, botY + 40);
                ctx.stroke();

                // Red Rocket Cartridge with "PRAJWAL" stamp
                ctx.fillStyle = '#dc2626';
                ctx.fillRect(cx - 7, botY - 35, 14, 38);
                ctx.fillStyle = '#ffd700';
                ctx.beginPath();
                ctx.moveTo(cx - 9, botY - 35);
                ctx.lineTo(cx + 9, botY - 35);
                ctx.lineTo(cx, botY - 50);
                ctx.closePath();
                ctx.fill();

                // Text on rocket
                ctx.fillStyle = '#ffd700';
                ctx.font = 'bold 7px sans-serif';
                ctx.textAlign = 'center';
                ctx.fillText('PRAJWAL', cx, botY - 15);

                ctx.restore();
            }

            // 6. LAVANGI - 20 Red Mini Firecrackers in Garland with "PRAJWAL"
            else if (currentCracker === 'ladi') {
                const lY = groundY - 14;
                ctx.save();
                for (let i = 0; i < 18; i++) {
                    const lx = cx - 90 + (i * 11);
                    const ly = lY + Math.sin(i * 0.7) * 4;

                    ctx.fillStyle = '#ef4444';
                    ctx.fillRect(lx, ly, 7, 18);
                    ctx.fillStyle = '#ffd700';
                    ctx.fillRect(lx, ly + 5, 7, 4);
                }
                ctx.fillStyle = '#ffd700';
                ctx.font = 'bold 9px sans-serif';
                ctx.fillText('👑 PRAJWAL LAVANGI', cx - 45, lY + 30);
                ctx.restore();
            }

            // 7. SNAKE TABLET
            else if (currentCracker === 'snake') {
                const tabY = groundY - 6;
                ctx.save();
                ctx.fillStyle = '#1e293b';
                ctx.beginPath();
                ctx.ellipse(cx, tabY, 26, 10, 0, 0, Math.PI * 2);
                ctx.fill();
                ctx.strokeStyle = '#ffd700';
                ctx.lineWidth = 2;
                ctx.stroke();

                ctx.fillStyle = '#fde047';
                ctx.font = 'bold 9px sans-serif';
                ctx.textAlign = 'center';
                ctx.fillText('PRAJWAL', cx, tabY + 3);
                ctx.restore();
            }

            // 8. SKY SHOTS LAUNCHER TUBE
            else if (currentCracker === 'skyshot') {
                const tubeY = groundY - 55;
                ctx.save();
                ctx.fillStyle = '#0284c7';
                ctx.fillRect(cx - 14, tubeY, 28, 55);
                ctx.strokeStyle = '#ffd700';
                ctx.lineWidth = 2.5;
                ctx.strokeRect(cx - 14, tubeY, 28, 55);

                ctx.fillStyle = '#ffd700';
                ctx.font = 'bold 8px sans-serif';
                ctx.textAlign = 'center';
                ctx.fillText('PRAJWAL', cx, tubeY + 25);
                ctx.fillText('7 SHOTS', cx, tubeY + 38);
                ctx.restore();
            }
        }

        // ========================================================
        // 6. CRACKER SELECTION & RESET
        // ========================================================
        function selectCracker(type) {
            resetCracker();
            currentCracker = type;

            document.querySelectorAll('.cracker-card').forEach(c => c.classList.remove('active'));
            const target = Array.from(document.querySelectorAll('.cracker-card')).find(c => c.getAttribute('onclick')?.includes(type));
            if (target) target.classList.add('active');

            applyTranslations();
            const dragHint = document.getElementById('dragHint');
            dragHint.style.display = (type === 'stick') ? 'flex' : 'none';
        }

        function resetCracker() {
            clearActiveTimers();
            particles = [];
            rockets = [];
            snakeSegments = [];
            isBurning = false;
            chakriRPM = 0;
            bombExploded = false;
            bombFuseHeight = 28;
            shockwaveRadius = 0;
            shockwaveAlpha = 0;
            stickX = canvas.width / 2;
            stickY = canvas.height * 0.55;
            updateStatusText();
        }

        // ========================================================
        // 7. PRECISE IGNITION HANDLERS
        // ========================================================
        function igniteCracker() {
            if (isBurning) return;
            isBurning = true;
            updateStatusText();
            sfx.playFuse();

            const cx = canvas.width / 2;
            const groundY = canvas.height - 35;

            if (currentCracker === 'anar') {
                // ANAR: FOUNTAIN STRICTLY FROM TOP MOUTH (ZERO FIRE AT BOTTOM)
                const mouthX = cx;
                const mouthY = groundY - 70;
                sfx.playWhoosh();

                let frame = 0;
                const timer = setInterval(() => {
                    frame++;
                    if (frame % 3 === 0) sfx.playCrackle();

                    // 18 High-velocity parabolic fountain sparks from top mouth
                    for (let i = 0; i < 18; i++) {
                        const angle = -Math.PI / 2 + (Math.random() * 0.45 - 0.225); // Narrow upward cone
                        const speed = Math.random() * 11 + 7; // Shoots high into sky!
                        const color = Math.random() > 0.35 ? '#ffd700' : '#ffffff';
                        particles.push(new SparkleParticle(
                            mouthX + (Math.random() * 4 - 2),
                            mouthY,
                            color,
                            Math.cos(angle) * speed,
                            Math.sin(angle) * speed,
                            0.95, 0.24, 0.016, true, 2.6
                        ));
                    }

                    if (frame > 140) {
                        clearInterval(timer);
                        setTimeout(resetCracker, 1400);
                    }
                }, 25);
                activeTimerIds.push(timer);
            }
            else if (currentCracker === 'chakri') {
                // CHAKRA: JET EXCLUSIVELY FROM ONE SINGLE NOZZLE ON RIM (PUSHES WHEEL TO SPIN)
                let frame = 0;
                chakriRPM = 0.45;

                const timer = setInterval(() => {
                    frame++;
                    if (frame % 4 === 0) sfx.playWhirr();

                    // Tangential thrust fire spraying from that single nozzle
                    const tangentAngle = chakriAngle + Math.PI / 2;
                    for (let i = 0; i < 9; i++) {
                        const speed = Math.random() * 7 + 4;
                        const spread = (Math.random() - 0.5) * 0.25;
                        const c = (i % 2 === 0) ? '#ffd700' : '#39ff14';
                        particles.push(new SparkleParticle(
                            chakriNozzleX,
                            chakriNozzleY,
                            c,
                            Math.cos(tangentAngle + spread) * speed,
                            Math.sin(tangentAngle + spread) * speed,
                            0.94, 0.02, 0.025, false, 2.5
                        ));
                    }

                    if (frame > 150) {
                        clearInterval(timer);
                        chakriRPM = 0;
                        setTimeout(resetCracker, 1000);
                    }
                }, 25);
                activeTimerIds.push(timer);
            }
            else if (currentCracker === 'stick') {
                // PHULJHADI: 3D NEEDLE STAR SPARKS RADIATING FROM THE STICK TIP
                let frame = 0;
                const timer = setInterval(() => {
                    frame++;
                    if (frame % 3 === 0) sfx.playCrackle();

                    // Radiates needle sparks in all directions from (stickX, stickY)
                    for (let i = 0; i < 20; i++) {
                        const angle = Math.random() * Math.PI * 2;
                        const speed = Math.random() * 6 + 1.5;
                        const color = Math.random() > 0.3 ? '#ffe066' : '#ffffff';
                        particles.push(new SparkleParticle(
                            stickX,
                            stickY,
                            color,
                            Math.cos(angle) * speed,
                            Math.sin(angle) * speed,
                            0.93, 0.06, 0.04, true, 2.4
                        ));
                    }

                    if (frame > 200) {
                        clearInterval(timer);
                        setTimeout(resetCracker, 800);
                    }
                }, 25);
                activeTimerIds.push(timer);
            }
            else if (currentCracker === 'bomb') {
                // SUTLI BOMB: SHRINKING FUSE -> BLINDING FLASH & SUB-BASS BOOM
                let fuseProgress = 0;
                const timer = setInterval(() => {
                    fuseProgress++;
                    bombFuseHeight = Math.max(0, 28 - (fuseProgress * 0.9));

                    // Fuse spark
                    particles.push(new SparkleParticle(
                        cx + 8,
                        groundY - 50 - bombFuseHeight,
                        '#ff4500',
                        (Math.random() - 0.5) * 2,
                        (Math.random() - 0.5) * 2,
                        0.9, 0, 0.08, false, 2
                    ));

                    if (bombFuseHeight <= 0) {
                        clearInterval(timer);
                        bombExploded = true;

                        triggerScreenFlash();
                        sfx.playBombBang();

                        stageBox.classList.add('shake-box');
                        setTimeout(() => stageBox.classList.remove('shake-box'), 450);

                        shockwaveRadius = 15;
                        shockwaveAlpha = 0.95;

                        // 180 Shredded jute twine fibers & debris
                        for (let i = 0; i < 180; i++) {
                            const angle = Math.random() * Math.PI * 2;
                            const speed = Math.random() * 11 + 2;
                            const color = (i % 3 === 0) ? '#22543d' : ((i % 3 === 1) ? '#ff8c00' : '#ffffff');
                            particles.push(new SparkleParticle(
                                cx,
                                groundY - 26,
                                color,
                                Math.cos(angle) * speed,
                                Math.sin(angle) * speed,
                                0.93, 0.22, 0.02, true, 3.2
                            ));
                        }

                        setTimeout(resetCracker, 1800);
                    }
                }, 30);
                activeTimerIds.push(timer);
            }
            else if (currentCracker === 'rocket') {
                // ROCKET: ASCENDS HIGH INTO SKY & DETONATES INTO MULTI-BREAK STARBURSTS
                sfx.playWhoosh();
                const targetX = cx;
                const targetY = canvas.height * 0.18; // High altitude explosion!
                rockets.push(new AscendingRocket(cx, groundY - 60, targetX, targetY));
                setTimeout(resetCracker, 2200);
            }
            else if (currentCracker === 'ladi') {
                // LAVANGI: SEQUENTIAL RAPID SHARP POPS ALONG GARLAND
                let curIdx = 0;
                const timer = setInterval(() => {
                    sfx.playPop();
                    const lx = cx - 90 + (curIdx * 11);
                    const ly = groundY - 14;

                    for (let i = 0; i < 18; i++) {
                        const angle = Math.random() * Math.PI * 2;
                        const speed = Math.random() * 6 + 1.5;
                        particles.push(new SparkleParticle(
                            lx, ly,
                            (Math.random() > 0.5) ? '#ef4444' : '#ffd700',
                            Math.cos(angle) * speed,
                            Math.sin(angle) * speed,
                            0.92, 0.12, 0.04, true, 2.2
                        ));
                    }

                    curIdx++;
                    if (curIdx >= 18) {
                        clearInterval(timer);
                        sfx.playBombBang();
                        setTimeout(resetCracker, 1200);
                    }
                }, 130);
                activeTimerIds.push(timer);
            }
            else if (currentCracker === 'snake') {
                // PROCEDURAL UNIQUE SNAKE: EVERY TIME A NEW RANDOM CURVE (WASM/DYNAMIC SEED)
                let frame = 0;
                let sY = groundY - 6;
                let sX = cx;
                const seed = Math.random() * 1000 + 10;

                const timer = setInterval(() => {
                    frame++;
                    sfx.playFuse();
                    sY -= Math.random() * 2.2 + 1;
                    sX += Math.sin(frame * 0.4 + seed) * 3.5;
                    snakeSegments.push({ x: sX, y: sY, r: Math.random() * 5 + 6 });

                    for (let i = 0; i < 4; i++) {
                        particles.push(new SparkleParticle(
                            sX, sY, '#ff4500',
                            (Math.random() - 0.5) * 2,
                            -Math.random() * 2,
                            0.94, 0.05, 0.08, false, 2
                        ));
                    }

                    if (frame > 65) {
                        clearInterval(timer);
                        setTimeout(resetCracker, 2200);
                    }
                }, 35);
                activeTimerIds.push(timer);
            }
            else if (currentCracker === 'skyshot') {
                // 7-SHOT ARTILLERY: 7 AERIAL SHELLS BURSTING ACROSS THE SKY
                let shot = 0;
                const timer = setInterval(() => {
                    if (shot < 7) {
                        sfx.playWhoosh();
                        const targetX = cx + (Math.random() * 180 - 90);
                        const targetY = canvas.height * 0.16 + (Math.random() * 40 - 20);
                        rockets.push(new AscendingRocket(cx, groundY - 55, targetX, targetY));
                        shot++;
                    } else {
                        clearInterval(timer);
                        setTimeout(resetCracker, 2200);
                    }
                }, 650);
                activeTimerIds.push(timer);
            }
        }

        // ========================================================
        // 8. ANIMATION LOOP (GLOWING LIGHT TRAILS & 60-120 FPS SMOOTH)
        // ========================================================
        function loop() {
            requestAnimationFrame(loop);

            const groundY = canvas.height - 35;

            // Fading trail effect for cinematic glowing fireworks
            ctx.fillStyle = 'rgba(12, 3, 24, 0.28)';
            ctx.fillRect(0, 0, canvas.width, canvas.height);

            // Shockwave expansion
            if (shockwaveAlpha > 0) {
                shockwaveRadius += 4.5;
                shockwaveAlpha -= 0.04;
            }

            // Chakra high-speed wheel spin
            if (chakriRPM > 0) {
                chakriAngle += chakriRPM;
            }

            // Draw Static/Active Cracker Studio with "PRAJWAL" Stamped
            drawCrackerStudio(groundY);

            // Draw Snake Ash
            if (snakeSegments.length > 0) {
                ctx.save();
                ctx.fillStyle = '#334155';
                for (let s of snakeSegments) {
                    ctx.beginPath();
                    ctx.arc(s.x, s.y, s.r, 0, Math.PI * 2);
                    ctx.fill();
                }
                ctx.restore();
            }

            // ADDITIVE BLENDING FOR RADIANT FIREWORK SPARKS
            ctx.globalCompositeOperation = 'lighter';

            // Update & Render Rockets
            for (let i = rockets.length - 1; i >= 0; i--) {
                const r = rockets[i];
                r.update();
                r.draw(ctx);
                if (!r.alive) rockets.splice(i, 1);
            }

            // Update & Render Particles
            for (let i = particles.length - 1; i >= 0; i--) {
                const p = particles[i];
                p.update(groundY);
                p.draw(ctx);
                if (p.alpha <= 0) particles.splice(i, 1);
            }

            ctx.globalCompositeOperation = 'source-over';
        }
        loop();

        // Drag Handler for Phuljhadi Stick
        function updateStickPointer(e) {
            if (currentCracker !== 'stick') return;
            const rect = canvas.getBoundingClientRect();
            stickX = e.clientX - rect.left;
            stickY = e.clientY - rect.top;
        }

        canvas.addEventListener('pointerdown', (e) => {
            isDraggingStick = true;
            updateStickPointer(e);
            if (!isBurning) igniteCracker();
        });

        window.addEventListener('pointermove', (e) => {
            if (isDraggingStick && currentCracker === 'stick') {
                updateStickPointer(e);
            }
        });

        window.addEventListener('pointerup', () => { isDraggingStick = false; });
        window.addEventListener('pointercancel', () => { isDraggingStick = false; });

        document.getElementById('btnIgnite').addEventListener('click', igniteCracker);
        document.getElementById('btnReset').addEventListener('click', resetCracker);

        // Initial setup
        applyTranslations();
        selectCracker('anar');
    </script>
</body>
</html>
'''

with open('/data/data/com.termux/files/home/diwali_website/index.html', 'w', encoding='utf-8') as f:
    f.write(html_content)

print("Generated final studio index.html successfully! Size:", len(html_content))
