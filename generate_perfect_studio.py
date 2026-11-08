# -*- coding: utf-8 -*-
"""
Ultimate Diwali Cracker Studio Generator - Professional Black & Premium Gold Edition
Updates:
1. Professional Black & Premium Gold Theme:
   - Deep obsidian jet black background with warm 24K molten gold gradients and glassmorphism.
   - Luxury gold brushed borders, glowing gold typography with Cinzel font, premium gold buttons.
2. Removed C++ WASM Badge:
   - Clean top utility bar with only Language Switch (left) and Sound FX toggle (right).
   - High-performance C++ WASM physics engine continues to run silently in the background.
3. Lavangi Maal Dynamic Shortening & Exploding:
   - As each cracker pops, it explodes into sparks/confetti and disappears leaving charred ash,
     visibly shortening the garland until all 18 explode!
   - Smoothly restarts fresh with a full garland for the next round.
4. Paus Fountain Fixed:
   - Wick disappears when burning.
   - Sparks erupt exclusively from the top nozzle mouth with strictly skyward velocity (speed 18-28.5),
     eliminating any sparks or flame below the wick mouth.
5. All other cracker physics & features preserved exactly without changes!
"""

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
    <link href="https://fonts.googleapis.com/css2?family=Cinzel:wght@700;800;900&family=Poppins:wght@400;500;600;700;800;900&family=Tiro+Devanagari+Marathi:ital@0;1&family=Yatra+One&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">

    <style>
        :root {
            /* Professional Black & Premium Gold Palette */
            --gold-bright: #fff2a3;
            --gold-primary: #ffd700;
            --gold-rich: #d4af37;
            --gold-dark: #996515;
            --gold-grad: linear-gradient(135deg, #fff3a8 0%, #ffd700 35%, #d4af37 70%, #996515 100%);
            --gold-border: rgba(212, 175, 55, 0.45);
            --gold-glow: 0 0 25px rgba(212, 175, 55, 0.25);

            --obsidian-bg: radial-gradient(circle at 50% 12%, #181206 0%, #090703 55%, #000000 100%);
            --card-bg: rgba(18, 14, 5, 0.82);
            --card-border: 1.5px solid rgba(212, 175, 55, 0.35);
            --card-shadow: 0 10px 35px rgba(0, 0, 0, 0.95), 0 0 20px rgba(212, 175, 55, 0.12);
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
            background: var(--obsidian-bg);
            font-family: 'Poppins', 'Tiro Devanagari Marathi', sans-serif;
            color: #fff;
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: space-between;
            padding: 2px 6px 4px;
            position: relative;
        }

        .ambient-canvas {
            position: absolute;
            top: 0; left: 0; width: 100%; height: 100%;
            pointer-events: none;
            z-index: 1;
        }

        #flashOverlay {
            position: absolute;
            top: 0; left: 0; width: 100%; height: 100%;
            background: #ffffff;
            opacity: 0;
            pointer-events: none;
            z-index: 100;
            transition: opacity 0.05s ease-out;
        }

        /* Top Action Utility Bar (Clean Layout without C++ Badge) */
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
            background: rgba(18, 14, 5, 0.85);
            border: 1.5px solid var(--gold-border);
            color: var(--gold-primary);
            padding: 3px 12px;
            border-radius: 18px;
            font-size: 0.72rem;
            font-weight: 700;
            cursor: pointer;
            display: flex;
            align-items: center;
            gap: 6px;
            backdrop-filter: blur(10px);
            transition: all 0.2s;
            box-shadow: 0 2px 10px rgba(0, 0, 0, 0.7);
        }

        .lang-switch-btn:hover {
            background: var(--gold-grad);
            color: #000;
            transform: scale(1.04);
            box-shadow: 0 0 14px rgba(255, 215, 0, 0.4);
        }

        .sound-switch-btn {
            background: rgba(18, 14, 5, 0.85);
            border: 1.5px solid var(--gold-border);
            color: var(--gold-primary);
            padding: 3px 12px;
            border-radius: 18px;
            font-size: 0.72rem;
            font-weight: 700;
            cursor: pointer;
            display: flex;
            align-items: center;
            gap: 6px;
            backdrop-filter: blur(10px);
            transition: all 0.2s;
            box-shadow: 0 2px 10px rgba(0, 0, 0, 0.7);
        }

        .sound-switch-btn.active {
            background: var(--gold-grad);
            color: #000;
            box-shadow: 0 0 16px rgba(255, 215, 0, 0.5);
        }

        /* ========================================================
           HEADER: PROFESSIONAL BLACK & GOLD ELEGANCE
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
            margin-top: 0px;
        }

        .header-row {
            display: flex;
            align-items: center;
            justify-content: center;
            gap: 14px;
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
            filter: drop-shadow(0 0 8px #ff7700) drop-shadow(0 0 16px #ffbb00);
            animation: flameFlicker 1.3s infinite alternate ease-in-out;
            transform-origin: center bottom;
        }

        .diya-base {
            width: 26px;
            height: 11px;
            background: linear-gradient(180deg, #d4af37 0%, #78350f 100%);
            border-radius: 0 0 16px 16px;
            border-top: 1.5px solid #fff2a3;
            box-shadow: 0 2px 8px rgba(0,0,0,0.85);
            margin-top: -2px;
        }

        @keyframes flameFlicker {
            0% { transform: scale(1) rotate(-3deg); filter: drop-shadow(0 0 8px #ff7700); }
            50% { transform: scale(1.12, 0.94) rotate(3deg); filter: drop-shadow(0 0 12px #ff4400); }
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
            letter-spacing: 1.4px;
            text-shadow: 0 0 8px rgba(255, 215, 0, 0.85);
            margin-bottom: -2px;
        }

        .main-title {
            font-family: 'Cinzel', 'Yatra One', serif, sans-serif;
            font-size: 1.45rem;
            font-weight: 900;
            line-height: 1.1;
            color: #ffd700;
            text-shadow: 0 0 14px rgba(255, 215, 0, 0.9), 0 0 28px rgba(212, 175, 55, 0.75), 0 2px 5px #000000;
            letter-spacing: 1.3px;
            display: flex;
            align-items: center;
            gap: 7px;
        }

        .main-title-sparkle {
            color: #ffea00;
            font-size: 0.95rem;
            animation: pulseGlow 1.2s infinite alternate;
        }

        @keyframes pulseGlow {
            0% { transform: scale(0.9); opacity: 0.7; }
            100% { transform: scale(1.2); opacity: 1; filter: drop-shadow(0 0 10px #fff); }
        }

        .subhechha-card {
            background: rgba(18, 14, 5, 0.85);
            border: 1px solid rgba(212, 175, 55, 0.4);
            border-radius: 12px;
            padding: 2px 12px;
            width: 100%;
            max-width: 95%;
            backdrop-filter: blur(8px);
            display: flex;
            align-items: center;
            justify-content: center;
            box-shadow: inset 0 0 10px rgba(212, 175, 55, 0.08), 0 2px 8px rgba(0,0,0,0.7);
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
           STAGE BOX: LUXURY OBSIDIAN & BRUSHED GOLD
           ======================================================== */
        .stage-container {
            position: relative;
            z-index: 10;
            width: 100%;
            max-width: 760px;
            flex: 1;
            min-height: 330px;
            max-height: 63vh;
            background: radial-gradient(circle at 50% 88%, #140e04 0%, #080602 65%, #000000 100%);
            border: 2px solid var(--gold-border);
            border-radius: 20px;
            box-shadow: var(--card-shadow);
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
            background: rgba(14, 11, 4, 0.88);
            border: 1.5px solid var(--gold-border);
            padding: 3px 12px;
            border-radius: 14px;
            font-size: 0.72rem;
            font-weight: 700;
            color: #ffd700;
            display: flex;
            align-items: center;
            gap: 6px;
            backdrop-filter: blur(10px);
            box-shadow: 0 4px 12px rgba(0, 0, 0, 0.8);
        }

        .status-badge {
            font-size: 0.68rem;
            font-weight: 600;
            color: #e2e8f0;
            background: rgba(14, 11, 4, 0.88);
            border: 1px solid rgba(212, 175, 55, 0.3);
            padding: 3px 10px;
            border-radius: 14px;
            display: flex;
            align-items: center;
            gap: 6px;
            box-shadow: 0 4px 12px rgba(0, 0, 0, 0.8);
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
            box-shadow: 0 0 10px #ef4444;
            animation: pulseDot 0.5s infinite alternate;
        }

        .drag-hint {
            position: absolute;
            bottom: 10px;
            left: 50%;
            transform: translateX(-50%);
            background: rgba(14, 11, 4, 0.88);
            border: 1px solid var(--gold-border);
            color: #fef08a;
            font-size: 0.68rem;
            padding: 3px 14px;
            border-radius: 14px;
            pointer-events: none;
            display: none;
            align-items: center;
            gap: 6px;
            z-index: 15;
            backdrop-filter: blur(8px);
            box-shadow: 0 4px 12px rgba(0, 0, 0, 0.8);
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
            background: linear-gradient(135deg, #fff3a8 0%, #ffd700 40%, #d4af37 75%, #996515 100%);
            color: #000;
            border: none;
            border-radius: 14px;
            font-weight: 900;
            font-size: 0.92rem;
            cursor: pointer;
            display: flex;
            align-items: center;
            justify-content: center;
            gap: 8px;
            box-shadow: 0 4px 20px rgba(255, 215, 0, 0.45);
            transition: all 0.2s cubic-bezier(0.34, 1.56, 0.64, 1);
            letter-spacing: 0.5px;
        }

        .btn-ignite:hover {
            transform: translateY(-2px);
            box-shadow: 0 6px 25px rgba(255, 215, 0, 0.7);
        }

        .btn-ignite:active {
            transform: translateY(1px);
        }

        .btn-reset {
            flex: 1;
            padding: 10px 10px;
            background: rgba(18, 14, 5, 0.85);
            color: var(--gold-primary);
            border: 1.5px solid var(--gold-border);
            border-radius: 14px;
            font-weight: 700;
            font-size: 0.82rem;
            cursor: pointer;
            display: flex;
            align-items: center;
            justify-content: center;
            gap: 6px;
            backdrop-filter: blur(8px);
            transition: all 0.2s;
            box-shadow: 0 3px 12px rgba(0, 0, 0, 0.7);
        }

        .btn-reset:hover {
            background: rgba(255, 215, 0, 0.18);
            transform: translateY(-2px);
        }

        /* ========================================================
           CRACKER TRAY: SLEEK OBSIDIAN & GOLD GLASS
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
            letter-spacing: 1.2px;
            margin-bottom: 3px;
            display: flex;
            align-items: center;
            gap: 6px;
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
            background: rgba(18, 14, 5, 0.85);
            border: 1.5px solid rgba(212, 175, 55, 0.25);
            border-radius: 12px;
            padding: 5px 9px;
            color: #cbd5e1;
            cursor: pointer;
            display: flex;
            flex-direction: column;
            align-items: center;
            gap: 2px;
            min-width: 72px;
            transition: all 0.2s cubic-bezier(0.34, 1.56, 0.64, 1);
            box-shadow: 0 2px 8px rgba(0, 0, 0, 0.6);
        }

        .cracker-card i {
            font-size: 1.15rem;
            color: var(--gold-primary);
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
            box-shadow: 0 4px 18px rgba(255, 215, 0, 0.65);
            transform: translateY(-2px);
        }

        .cracker-card.active i {
            color: #000;
            transform: scale(1.15);
        }

        .cracker-card.active .cracker-sub {
            color: #2b1d03;
            font-weight: 700;
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
            background: rgba(18, 14, 5, 0.85);
            border: 1px solid var(--gold-border);
            border-radius: 18px;
            padding: 2px 14px;
            font-size: 0.68rem;
            display: flex;
            align-items: center;
            gap: 6px;
            color: #e2e8f0;
            backdrop-filter: blur(8px);
            box-shadow: 0 3px 10px rgba(0, 0, 0, 0.7);
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

    <!-- Top Utility Bar (Clean Layout: Lang Switch on Left, Sound Switch on Right) -->
    <div class="top-utility-bar">
        <button class="lang-switch-btn" id="btnLangSwitch" title="Switch Language">
            <i class="fas fa-language"></i> <span id="lblLang">मराठी / English</span>
        </button>
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

    <!-- MAXIMIZED CRACKER BOX -->
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

    <!-- CLEAN CRACKER SELECTOR TRAY -->
    <section class="picker-container">
        <div class="picker-header" id="lblPickerTitle">
            <i class="fas fa-boxes-stacked"></i> फटाका निवडा (SELECT CRACKER):
        </div>
        <div class="cracker-dock">
            <div class="cracker-card active" onclick="selectCracker('anar')">
                <i class="fas fa-volcano"></i>
                <span class="cracker-lbl" id="cardLbl_anar">पाऊस</span>
                <span class="cracker-sub" id="cardSub_anar">Flower Pot</span>
            </div>
            <div class="cracker-card" onclick="selectCracker('chakri')">
                <i class="fas fa-compact-disc"></i>
                <span class="cracker-lbl" id="cardLbl_chakri">चक्र</span>
                <span class="cracker-sub" id="cardSub_chakri">Ground Spinner</span>
            </div>
            <div class="cracker-card" onclick="selectCracker('stick')">
                <i class="fas fa-wand-magic-sparkles"></i>
                <span class="cracker-lbl" id="cardLbl_stick">फुलबाजा</span>
                <span class="cracker-sub" id="cardSub_stick">Sparkler Stick</span>
            </div>
            <div class="cracker-card" onclick="selectCracker('bomb')">
                <i class="fas fa-bomb"></i>
                <span class="cracker-lbl" id="cardLbl_bomb">सुतळी बॉम्ब</span>
                <span class="cracker-sub" id="cardSub_bomb">Sutli Bomb</span>
            </div>
            <div class="cracker-card" onclick="selectCracker('rocket')">
                <i class="fas fa-rocket"></i>
                <span class="cracker-lbl" id="cardLbl_rocket">रॉकेट</span>
                <span class="cracker-sub" id="cardSub_rocket">Sky Rocket</span>
            </div>
            <div class="cracker-card" onclick="selectCracker('ladi')">
                <i class="fas fa-fire-flame-curved"></i>
                <span class="cracker-lbl" id="cardLbl_ladi">लवंगी माळ</span>
                <span class="cracker-sub" id="cardSub_ladi">Lavangi Maal</span>
            </div>
            <div class="cracker-card" onclick="selectCracker('snake')">
                <i class="fas fa-worm"></i>
                <span class="cracker-lbl" id="cardLbl_snake">साप गोळी</span>
                <span class="cracker-sub" id="cardSub_snake">Snake Tablet</span>
            </div>
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
        // Core State Variables
        let currentCracker = 'anar';
        let currentLang = 'mr';
        let isBurning = false;
        let rocketInBottle = true;

        // Dynamic Interactive States
        let snakeTabletScale = 1.0;
        let stickBurnProgress = 0.0;
        let activeSkyshotBarrel = -1;
        let ladiBurstIdx = 0; // Tracks which crackers have exploded in Lavangi Maal

        // C++ WebAssembly Physics Engine (Running Silently in Background)
        const WASM_B64 = "''' + wasm_b64 + r'''";
        let wasmEngine = null;

        async function initWasmEngine() {
            try {
                const response = await fetch('cracker_engine.wasm');
                if (response.ok) {
                    const bytes = await response.arrayBuffer();
                    const module = await WebAssembly.instantiate(bytes);
                    wasmEngine = module.instance.exports;
                    return;
                }
            } catch (e) {}

            try {
                const binaryStr = atob(WASM_B64);
                const bytes = new Uint8Array(binaryStr.length);
                for (let i = 0; i < binaryStr.length; i++) {
                    bytes[i] = binaryStr.charCodeAt(i);
                }
                const module = await WebAssembly.instantiate(bytes.buffer);
                wasmEngine = module.instance.exports;
            } catch (err) {}
        }
        initWasmEngine();

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
                    anar: { name: "पाऊस", sub: "Flower Pot", badge: "पाऊस (Paus Fountain)" },
                    chakri: { name: "चक्र", sub: "Ground Spinner", badge: "चक्र (Ground Chakra)" },
                    stick: { name: "फुलबाजा", sub: "Sparkler Stick", badge: "फुलबाजा (Sparkler Stick)" },
                    bomb: { name: "सुतळी बॉम्ब", sub: "Sutli Bomb", badge: "सुतळी बॉम्ब (Jute Bomb)" },
                    rocket: { name: "रॉकेट", sub: "Sky Rocket", badge: "रॉकेट (Sky Rocket)" },
                    ladi: { name: "लवंगी माळ", sub: "Lavangi Maal", badge: "लवंगी माळ (Lavangi Maal)" },
                    snake: { name: "साप गोळी", sub: "Snake Tablet", badge: "साप गोळी (Snake Tablet)" },
                    skyshot: { name: "आकाशी तोफ", sub: "7 Sky Shots", badge: "आकाशी तोफ (7 Sky Shots)" }
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
                    anar: { name: "Flower Pot", sub: "Paus Fountain", badge: "Flower Pot (Paus Fountain)" },
                    chakri: { name: "Chakra", sub: "Ground Spinner", badge: "Ground Chakra (Spinner)" },
                    stick: { name: "Sparkler", sub: "Handheld Sizzler", badge: "Sparkler Stick (Phulbaja)" },
                    bomb: { name: "Sutli Bomb", sub: "Jute Bomb", badge: "Sutli Bomb (Jute Bomb)" },
                    rocket: { name: "Sky Rocket", sub: "High Altitude", badge: "Sky Rocket (Rocket)" },
                    ladi: { name: "Firecracker Garland", sub: "Lavangi Maal", badge: "Firecracker Garland (Lavangi Maal)" },
                    snake: { name: "Snake Tablet", sub: "Carbon Snake", badge: "Black Snake Tablet" },
                    skyshot: { name: "7 Sky Shots", sub: "Aerial Chrysanthemum", badge: "7-Color Sky Shots" }
                }
            }
        };

        function applyTranslations() {
            const data = I18N[currentLang];
            const elLang = document.getElementById('lblLang');
            if (elLang) elLang.innerText = data.langBtn;

            const elSound = document.getElementById('lblSound');
            if (elSound) elSound.innerText = sfx.enabled ? data.soundOn : data.soundOff;

            const elShloka = document.getElementById('headerShloka');
            if (elShloka) elShloka.innerText = data.shloka;

            const elTitle = document.getElementById('titleText');
            if (elTitle) elTitle.innerText = data.mainTitle;

            const elBtnIgnite = document.getElementById('lblBtnIgnite');
            if (elBtnIgnite) elBtnIgnite.innerText = data.igniteBtn;

            const elBtnReset = document.getElementById('lblBtnReset');
            if (elBtnReset) elBtnReset.innerText = data.resetBtn;

            const elDrag = document.getElementById('lblDragHint');
            if (elDrag) elDrag.innerText = data.dragHint;

            const elPicker = document.getElementById('lblPickerTitle');
            if (elPicker) elPicker.innerHTML = `<i class="fas fa-boxes-stacked"></i> ${data.pickerTitle}`;

            for (let [key, c] of Object.entries(data.crackers)) {
                const elLbl = document.getElementById(`cardLbl_${key}`);
                const elSub = document.getElementById(`cardSub_${key}`);
                if (elLbl) elLbl.innerText = c.name;
                if (elSub) elSub.innerText = c.sub;
            }

            const curCrackerData = data.crackers[currentCracker];
            const elBadge = document.getElementById('hudBadgeName');
            if (curCrackerData && elBadge) {
                elBadge.innerText = curCrackerData.badge;
            }
            updateStatusText();
        }

        function updateStatusText() {
            const data = I18N[currentLang];
            const hudStatusText = document.getElementById('hudStatusText');
            const hudStatus = document.getElementById('hudStatus');
            if (!hudStatusText || !hudStatus) return;
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
            if (!elSubhechha) return;
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

        // Sound Synthesizer (100% Fail-Safe)
        class SoundSynth {
            constructor() {
                this.ctx = null;
                this.enabled = true;
            }

            init() {
                try {
                    if (!this.ctx) {
                        const AudioContext = window.AudioContext || window.webkitAudioContext;
                        if (AudioContext) {
                            this.ctx = new AudioContext();
                        }
                    }
                    if (this.ctx && this.ctx.state === 'suspended') {
                        this.ctx.resume().catch(() => {});
                    }
                } catch (e) {}
            }

            playFuse() {
                if (!this.enabled) return;
                try {
                    this.init();
                    if (!this.ctx) return;
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
                } catch (e) {}
            }

            playCrackle() {
                if (!this.enabled) return;
                try {
                    this.init();
                    if (!this.ctx) return;
                    const now = this.ctx.currentTime;
                    const osc = this.ctx.createOscillator();
                    const gain = this.ctx.createGain();
                    osc.type = 'square';
                    osc.frequency.setValueAtTime(1400 + Math.random() * 3200, now);
                    gain.gain.setValueAtTime(0.08, now);
                    gain.gain.exponentialRampToValueAtTime(0.001, now + 0.035);
                    osc.connect(gain); gain.connect(this.ctx.destination);
                    osc.start(now); osc.stop(now + 0.035);
                } catch (e) {}
            }

            playWhirr() {
                if (!this.enabled) return;
                try {
                    this.init();
                    if (!this.ctx) return;
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
                } catch (e) {}
            }

            playWhoosh() {
                if (!this.enabled) return;
                try {
                    this.init();
                    if (!this.ctx) return;
                    const now = this.ctx.currentTime;
                    const dur = 0.95;
                    const osc = this.ctx.createOscillator();
                    const gain = this.ctx.createGain();
                    osc.type = 'sawtooth';
                    osc.frequency.setValueAtTime(160, now);
                    osc.frequency.exponentialRampToValueAtTime(2000, now + dur);
                    gain.gain.setValueAtTime(0.01, now);
                    gain.gain.linearRampToValueAtTime(0.2, now + dur * 0.7);
                    gain.gain.exponentialRampToValueAtTime(0.001, now + dur);
                    osc.connect(gain); gain.connect(this.ctx.destination);
                    osc.start(now); osc.stop(now + dur);
                } catch (e) {}
            }

            playBombBang() {
                if (!this.enabled) return;
                try {
                    this.init();
                    if (!this.ctx) return;
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
                } catch (e) {}
            }

            playPop() {
                if (!this.enabled) return;
                try {
                    this.init();
                    if (!this.ctx) return;
                    const now = this.ctx.currentTime;
                    const osc = this.ctx.createOscillator();
                    const gain = this.ctx.createGain();
                    osc.type = 'square';
                    osc.frequency.setValueAtTime(1200 + Math.random() * 400, now);
                    osc.frequency.exponentialRampToValueAtTime(120, now + 0.06);
                    gain.gain.setValueAtTime(0.24, now);
                    gain.gain.exponentialRampToValueAtTime(0.001, now + 0.06);
                    osc.connect(gain); gain.connect(this.ctx.destination);
                    osc.start(now); osc.stop(now + 0.06);
                } catch (e) {}
            }

            playAerialBurst() {
                if (!this.enabled) return;
                try {
                    this.init();
                    if (!this.ctx) return;
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
                } catch (e) {}
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

        // Ambient Background Stars (Golden Stardust)
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
                ambCtx.fillStyle = `rgba(255, 215, 0, ${a * 0.45})`;
                ambCtx.beginPath();
                ambCtx.arc(s.x, s.y, s.r, 0, Math.PI * 2);
                ambCtx.fill();
            }
            requestAnimationFrame(renderAmbientStars);
        }
        renderAmbientStars();

        // ========================================================
        // HIGH-PERFORMANCE ZERO-ALLOCATION PARTICLE POOL (1200 SLOTS)
        // ========================================================
        const canvas = document.getElementById('mainCanvas');
        const ctx = canvas.getContext('2d');
        const stageBox = document.getElementById('stageBox');

        function resizeMainCanvas() {
            const rect = stageBox.getBoundingClientRect();
            const w = Math.floor(rect.width || stageBox.clientWidth || stageBox.offsetWidth || window.innerWidth || 440);
            const h = Math.floor(rect.height || stageBox.clientHeight || stageBox.offsetHeight || (window.innerHeight * 0.55) || 360);
            if (w > 50 && h > 50 && (canvas.width !== w || canvas.height !== h)) {
                canvas.width = w;
                canvas.height = h;
            }
        }
        window.addEventListener('resize', resizeMainCanvas);
        window.addEventListener('load', resizeMainCanvas);
        resizeMainCanvas();

        class ParticlePool {
            constructor(size = 1200) {
                this.pool = new Array(size);
                for (let i = 0; i < size; i++) {
                    this.pool[i] = {
                        active: false,
                        x: 0, y: 0,
                        vx: 0, vy: 0,
                        trailX: 0, trailY: 0,
                        color: '#ffd700',
                        size: 2.8,
                        friction: 0.96,
                        gravity: 0.12,
                        decay: 0.018,
                        bounce: true,
                        alpha: 1.0
                    };
                }
                this.nextIdx = 0;
            }

            spawn(x, y, color, vx, vy, friction = 0.96, gravity = 0.12, decay = 0.018, bounce = true, size = 2.8) {
                for (let i = 0; i < this.pool.length; i++) {
                    const idx = (this.nextIdx + i) % this.pool.length;
                    const p = this.pool[idx];
                    if (!p.active) {
                        p.active = true;
                        p.x = x; p.y = y;
                        p.trailX = x; p.trailY = y;
                        p.color = color;
                        p.vx = vx; p.vy = vy;
                        p.friction = friction;
                        p.gravity = gravity;
                        p.decay = decay;
                        p.bounce = bounce;
                        p.size = size;
                        p.alpha = 1.0;
                        this.nextIdx = (idx + 1) % this.pool.length;
                        return p;
                    }
                }
                return null;
            }

            clear() {
                for (let i = 0; i < this.pool.length; i++) {
                    this.pool[i].active = false;
                }
            }
        }
        const particlePool = new ParticlePool(1200);

        class AscendingRocket {
            constructor(startX, startY, targetX, targetY, isMortarShell = false, colorTheme = 0) {
                this.x = startX;
                this.y = startY;
                this.targetX = targetX;
                this.targetY = targetY;
                this.speed = isMortarShell ? 10.5 : 4.5;
                this.accel = isMortarShell ? 0.45 : 0.6;
                this.trail = [];
                this.alive = true;
                this.isMortar = isMortarShell;
                this.colorTheme = colorTheme;
            }

            update() {
                this.trail.push({ x: this.x, y: this.y });
                if (this.trail.length > 7) this.trail.shift();

                this.speed += this.accel;
                this.y -= this.speed;

                for (let i = 0; i < 2; i++) {
                    particlePool.spawn(
                        this.x + (Math.random() * 4 - 2),
                        this.y + (this.isMortar ? 10 : 22),
                        Math.random() > 0.3 ? '#ff6600' : '#ffd700',
                        (Math.random() - 0.5) * 2,
                        Math.random() * 3 + 2,
                        0.94, 0.05, 0.06, false, 2.5
                    );
                }

                if (this.y <= this.targetY) {
                    this.alive = false;
                    if (this.isMortar) {
                        triggerColoredPeonyBurst(this.x, this.y, this.colorTheme);
                    } else {
                        triggerMultiBreakFireworks(this.x, this.y);
                    }
                }
            }

            draw(ctx) {
                ctx.save();
                if (this.trail.length > 1) {
                    ctx.strokeStyle = '#ffd700';
                    ctx.lineWidth = 3.5;
                    ctx.beginPath();
                    ctx.moveTo(this.trail[0].x, this.trail[0].y);
                    for (let p of this.trail) ctx.lineTo(p.x, p.y);
                    ctx.stroke();
                }

                if (this.isMortar) {
                    ctx.fillStyle = '#ffffff';
                    ctx.beginPath();
                    ctx.arc(this.x, this.y, 5, 0, Math.PI * 2);
                    ctx.fill();
                    ctx.strokeStyle = '#f59e0b';
                    ctx.lineWidth = 2;
                    ctx.stroke();
                } else {
                    ctx.strokeStyle = '#b45309';
                    ctx.lineWidth = 2.5;
                    ctx.beginPath();
                    ctx.moveTo(this.x + 5, this.y - 10);
                    ctx.lineTo(this.x + 5, this.y + 70);
                    ctx.stroke();

                    const grad = ctx.createLinearGradient(this.x - 9, this.y, this.x + 9, this.y);
                    grad.addColorStop(0, '#991b1b');
                    grad.addColorStop(0.5, '#ef4444');
                    grad.addColorStop(1, '#7f1d1d');
                    ctx.fillStyle = grad;
                    ctx.fillRect(this.x - 9, this.y - 20, 18, 44);

                    ctx.fillStyle = '#ffd700';
                    ctx.fillRect(this.x - 9, this.y - 4, 18, 5);

                    ctx.fillStyle = '#fbbf24';
                    ctx.beginPath();
                    ctx.moveTo(this.x - 11, this.y - 20);
                    ctx.lineTo(this.x + 11, this.y - 20);
                    ctx.lineTo(this.x, this.y - 42);
                    ctx.closePath();
                    ctx.fill();

                    ctx.fillStyle = '#ffffff';
                    ctx.font = 'bold 7px sans-serif';
                    ctx.textAlign = 'center';
                    ctx.fillText('PRAJWAL', this.x, this.y + 12);
                }
                ctx.restore();
            }
        }

        let rockets = [];
        let snakeSegments = [];
        let activeTimerIds = [];

        let stickX = 220, stickY = 180;
        let isDraggingStick = false;

        let chakriAngle = 0;
        let chakriRPM = 0;
        let chakriNokX = 0, chakriNokY = 0;

        let bombFuseHeight = 36;
        let bombExploded = false;
        let shockwaveRadius = 0;
        let shockwaveAlpha = 0;

        // Phuljhadi Co-axial Geometry
        const STICK_DX = -0.573576; // -cos(55 deg)
        const STICK_DY = 0.819152;  // sin(55 deg)
        const STICK_TOTAL_LEN = 190;
        const STICK_COAT_LEN = 125;

        function getStickPoint(s) {
            return {
                x: stickX + s * STICK_DX,
                y: stickY + s * STICK_DY
            };
        }

        function clearActiveTimers() {
            for (let id of activeTimerIds) {
                clearInterval(id);
                clearTimeout(id);
            }
            activeTimerIds = [];
        }

        function triggerScreenFlash() {
            const fl = document.getElementById('flashOverlay');
            if (fl) {
                fl.style.opacity = '0.94';
                setTimeout(() => { fl.style.opacity = '0'; }, 160);
            }
        }

        const THEME_PALETTES = [
            ['#ffd700', '#f59e0b', '#ffffff'],
            ['#22c55e', '#4ade80', '#ffffff'],
            ['#ef4444', '#f87171', '#fde047'],
            ['#06b6d4', '#38bdf8', '#ffffff'],
            ['#d946ef', '#f43f5e', '#fef08a'],
            ['#eab308', '#ffffff', '#a855f7'],
            ['#ef4444', '#22c55e', '#3b82f6', '#ffd700', '#ffffff']
        ];

        function triggerColoredPeonyBurst(x, y, themeIdx) {
            sfx.playAerialBurst();
            const palette = THEME_PALETTES[themeIdx % THEME_PALETTES.length];
            for (let i = 0; i < 150; i++) {
                const angle = Math.random() * Math.PI * 2;
                const speed = Math.random() * 9 + 2.5;
                const col = palette[Math.floor(Math.random() * palette.length)];
                particlePool.spawn(
                    x, y, col,
                    Math.cos(angle) * speed,
                    Math.sin(angle) * speed,
                    0.95, 0.08, 0.018, false, 2.9
                );
            }
            setTimeout(() => {
                sfx.playCrackle();
                for (let k = 0; k < 60; k++) {
                    const angle = Math.random() * Math.PI * 2;
                    const speed = Math.random() * 5 + 3;
                    particlePool.spawn(
                        x, y, '#ffd700',
                        Math.cos(angle) * speed,
                        Math.sin(angle) * speed,
                        0.94, 0.06, 0.024, false, 2.4
                    );
                }
            }, 130);
        }

        function triggerMultiBreakFireworks(x, y) {
            sfx.playAerialBurst();
            const primaryColors = ['#ffd700', '#ef4444', '#f59e0b', '#ffffff'];
            for (let i = 0; i < 180; i++) {
                const angle = Math.random() * Math.PI * 2;
                const speed = Math.random() * 10 + 2.5;
                const color = primaryColors[Math.floor(Math.random() * primaryColors.length)];
                particlePool.spawn(
                    x, y, color,
                    Math.cos(angle) * speed,
                    Math.sin(angle) * speed,
                    0.95, 0.07, 0.016, false, 3.0
                );
            }

            setTimeout(() => {
                sfx.playCrackle();
                const ringColors = ['#39ff14', '#00ffcc', '#ff00aa', '#facc15'];
                for (let k = 0; k < 90; k++) {
                    const angle = Math.random() * Math.PI * 2;
                    const speed = Math.random() * 7 + 4.5;
                    const color = ringColors[Math.floor(Math.random() * ringColors.length)];
                    particlePool.spawn(
                        x, y, color,
                        Math.cos(angle) * speed,
                        Math.sin(angle) * speed,
                        0.94, 0.05, 0.02, false, 2.6
                    );
                }
            }, 140);

            setTimeout(() => {
                for (let s = 0; s < 8; s++) {
                    const a = (s * Math.PI * 2) / 8;
                    const sx = x + Math.cos(a) * 55;
                    const sy = y + Math.sin(a) * 55;
                    sfx.playCrackle();
                    for (let j = 0; j < 28; j++) {
                        const subAngle = Math.random() * Math.PI * 2;
                        const subSpeed = Math.random() * 4.5 + 1.8;
                        particlePool.spawn(
                            sx, sy, '#ffe066',
                            Math.cos(subAngle) * subSpeed,
                            Math.sin(subAngle) * subSpeed,
                            0.93, 0.04, 0.03, false, 2.3
                        );
                    }
                }
            }, 280);
        }

        // ========================================================
        // 3D HIGH-DEFINITION CRACKER RENDERING ENGINE
        // ========================================================
        function drawCrackerStudio(groundY) {
            const cx = canvas.width / 2;

            ctx.save();
            ctx.strokeStyle = 'rgba(212, 175, 55, 0.3)';
            ctx.lineWidth = 2;
            ctx.beginPath();
            ctx.moveTo(15, groundY);
            ctx.lineTo(canvas.width - 15, groundY);
            ctx.stroke();

            // Ground Rangoli
            ctx.strokeStyle = 'rgba(212, 175, 55, 0.22)';
            ctx.lineWidth = 2;
            ctx.beginPath();
            ctx.ellipse(cx, groundY + 14, 130, 32, 0, 0, Math.PI * 2);
            ctx.stroke();

            ctx.strokeStyle = 'rgba(239, 68, 68, 0.2)';
            ctx.lineWidth = 1.5;
            ctx.beginPath();
            ctx.ellipse(cx, groundY + 14, 85, 20, 0, 0, Math.PI * 2);
            ctx.stroke();
            ctx.restore();

            if (shockwaveAlpha > 0) {
                ctx.save();
                ctx.strokeStyle = `rgba(255, 215, 0, ${shockwaveAlpha})`;
                ctx.lineWidth = 4;
                ctx.beginPath();
                ctx.ellipse(cx, groundY + 8, shockwaveRadius, shockwaveRadius * 0.35, 0, 0, Math.PI * 2);
                ctx.stroke();
                ctx.restore();
            }

            if (bombExploded) {
                ctx.save();
                ctx.fillStyle = 'rgba(5, 5, 5, 0.95)';
                ctx.beginPath();
                ctx.ellipse(cx, groundY + 6, 65, 18, 0, 0, Math.PI * 2);
                ctx.fill();
                ctx.restore();
            }

            // 1. PAUS (ANAR) - 110px TALL CONE, ZERO LOWER WICK BLEED
            if (currentCracker === 'anar') {
                const potBaseY = groundY;
                const potTopY = groundY - 110;
                const baseW = 42;
                const topW = 12;

                ctx.save();
                ctx.fillStyle = 'rgba(0, 0, 0, 0.65)';
                ctx.beginPath();
                ctx.ellipse(cx, potBaseY + 4, baseW + 6, 12, 0, 0, Math.PI * 2);
                ctx.fill();

                const bodyGrad = ctx.createLinearGradient(cx - baseW, 0, cx + baseW, 0);
                bodyGrad.addColorStop(0, '#591e08');
                bodyGrad.addColorStop(0.35, '#c2410c');
                bodyGrad.addColorStop(0.7, '#ea580c');
                bodyGrad.addColorStop(1, '#431407');

                ctx.fillStyle = bodyGrad;
                ctx.beginPath();
                ctx.moveTo(cx - baseW, potBaseY);
                ctx.lineTo(cx + baseW, potBaseY);
                ctx.lineTo(cx + topW, potTopY);
                ctx.lineTo(cx - topW, potTopY);
                ctx.closePath();
                ctx.fill();

                ctx.strokeStyle = '#ffd700';
                ctx.lineWidth = 3;
                ctx.stroke();

                ctx.fillStyle = '#ffd700';
                ctx.fillRect(cx - (baseW - 4), potBaseY - 14, (baseW - 4) * 2, 8);
                ctx.fillRect(cx - (topW + 2), potTopY + 4, (topW + 2) * 2, 6);

                ctx.fillStyle = '#831843';
                ctx.fillRect(cx - 30, potBaseY - 65, 60, 42);
                ctx.strokeStyle = '#fde047';
                ctx.lineWidth = 1.5;
                ctx.strokeRect(cx - 30, potBaseY - 65, 60, 42);

                ctx.fillStyle = '#fde047';
                ctx.font = 'bold 11px sans-serif';
                ctx.textAlign = 'center';
                ctx.fillText('👑 PRAJWAL', cx, potBaseY - 48);
                ctx.font = 'bold 8.5px sans-serif';
                ctx.fillText('SPECIAL ANAR', cx, potBaseY - 36);
                ctx.font = '7.5px sans-serif';
                ctx.fillText('★ 30-FOOT SKY-HIGH ★', cx, potBaseY - 26);

                // ONLY DRAW WICK WHEN NOT BURNING (Prevents lower wick visual conflict!)
                if (!isBurning) {
                    ctx.strokeStyle = '#f1f5f9';
                    ctx.lineWidth = 3;
                    ctx.beginPath();
                    ctx.moveTo(cx, potTopY);
                    ctx.quadraticCurveTo(cx + 8, potTopY - 12, cx + 2, potTopY - 20);
                    ctx.stroke();
                } else {
                    // White-hot incandescent glowing nozzle mouth
                    ctx.fillStyle = '#ffffff';
                    ctx.beginPath();
                    ctx.ellipse(cx, potTopY, topW + 1, 3.5, 0, 0, Math.PI * 2);
                    ctx.fill();
                    ctx.strokeStyle = '#ffd700';
                    ctx.lineWidth = 2;
                    ctx.stroke();
                }

                ctx.restore();
            }

            // 2. CHAKRA - 3D PERSPECTIVE FLAT WHEEL WITH EXACT NOZZLE TIP (NOK)
            else if (currentCracker === 'chakri') {
                const wheelY = groundY - 12;
                const Rx = 55;
                const Ry = 22;
                const H = 14;

                ctx.save();
                ctx.fillStyle = 'rgba(0,0,0,0.65)';
                ctx.beginPath();
                ctx.ellipse(cx, wheelY + H + 4, Rx + 8, Ry + 4, 0, 0, Math.PI * 2);
                ctx.fill();

                for (let i = H; i >= 0; i--) {
                    ctx.fillStyle = (i % 3 === 0) ? '#991b1b' : ((i % 3 === 1) ? '#b45309' : '#15803d');
                    ctx.beginPath();
                    ctx.ellipse(cx, wheelY + i, Rx, Ry, 0, 0, Math.PI * 2);
                    ctx.fill();
                }

                ctx.save();
                ctx.translate(cx, wheelY);
                ctx.fillStyle = '#ef4444';
                ctx.beginPath();
                ctx.ellipse(0, 0, Rx, Ry, 0, 0, Math.PI * 2);
                ctx.fill();
                ctx.strokeStyle = '#ffd700';
                ctx.lineWidth = 3;
                ctx.stroke();

                ctx.strokeStyle = '#22c55e';
                ctx.lineWidth = 3;
                for (let a = 0; a < 4; a++) {
                    const ang = chakriAngle + (a * Math.PI / 2);
                    ctx.beginPath();
                    ctx.ellipse(0, 0, Rx * 0.65, Ry * 0.65, ang, 0, Math.PI / 2);
                    ctx.stroke();
                }

                ctx.fillStyle = '#f59e0b';
                ctx.beginPath();
                ctx.ellipse(0, 0, 22, 9, 0, 0, Math.PI * 2);
                ctx.fill();
                ctx.strokeStyle = '#fef08a';
                ctx.lineWidth = 1.5;
                ctx.stroke();

                ctx.fillStyle = '#000000';
                ctx.font = 'bold 7px sans-serif';
                ctx.textAlign = 'center';
                ctx.textBaseline = 'middle';
                ctx.fillText('👑 PRAJWAL', 0, 0);
                ctx.restore();

                const nozzleBaseX = cx + Math.cos(chakriAngle) * Rx;
                const nozzleBaseY = wheelY + Math.sin(chakriAngle) * Ry;
                chakriNokX = cx + Math.cos(chakriAngle) * (Rx + 12);
                chakriNokY = wheelY + Math.sin(chakriAngle) * (Ry + 5);

                ctx.save();
                ctx.strokeStyle = '#78350f';
                ctx.lineWidth = 7;
                ctx.beginPath();
                ctx.moveTo(nozzleBaseX, nozzleBaseY);
                ctx.lineTo(chakriNokX, chakriNokY);
                ctx.stroke();

                ctx.strokeStyle = '#fde047';
                ctx.lineWidth = 2;
                ctx.beginPath();
                ctx.arc(chakriNokX, chakriNokY, 3, 0, Math.PI * 2);
                ctx.stroke();

                if (isBurning) {
                    ctx.fillStyle = '#ffffff';
                    ctx.beginPath();
                    ctx.arc(chakriNokX, chakriNokY, 4, 0, Math.PI * 2);
                    ctx.fill();
                }
                ctx.restore();

                ctx.restore();
            }

            // 3. PHULJHADI (SPARKLER) - 100% MATHEMATICALLY CO-AXIAL ALIGNED WIRE & COATING
            else if (currentCracker === 'stick') {
                ctx.save();

                const pTip = getStickPoint(0);
                const pHandle = getStickPoint(STICK_TOTAL_LEN);

                // Step 1: Metallic Steel Wire (काठी)
                ctx.strokeStyle = '#94a3b8';
                ctx.lineWidth = 3.5;
                ctx.lineCap = 'round';
                ctx.beginPath();
                ctx.moveTo(pTip.x, pTip.y);
                ctx.lineTo(pHandle.x, pHandle.y);
                ctx.stroke();

                // Step 2: Co-axial Chemical Coating Layer
                const currentBurnS = stickBurnProgress * STICK_COAT_LEN;
                const pBurn = getStickPoint(currentBurnS);
                const pCoatEnd = getStickPoint(STICK_COAT_LEN);

                if (stickBurnProgress < 1.0) {
                    const coatGrad = ctx.createLinearGradient(pCoatEnd.x, pCoatEnd.y, pBurn.x, pBurn.y);
                    coatGrad.addColorStop(0, '#1e293b');
                    coatGrad.addColorStop(0.35, '#475569');
                    coatGrad.addColorStop(0.7, '#64748b');
                    coatGrad.addColorStop(1, '#94a3b8');

                    ctx.strokeStyle = coatGrad;
                    ctx.lineWidth = 9.5;
                    ctx.lineCap = 'round';
                    ctx.beginPath();
                    ctx.moveTo(pCoatEnd.x, pCoatEnd.y);
                    ctx.lineTo(pBurn.x, pBurn.y);
                    ctx.stroke();

                    ctx.strokeStyle = 'rgba(255, 255, 255, 0.22)';
                    ctx.lineWidth = 1.8;
                    ctx.beginPath();
                    ctx.moveTo(pCoatEnd.x - 1, pCoatEnd.y - 1);
                    ctx.lineTo(pBurn.x - 1, pBurn.y - 1);
                    ctx.stroke();
                }

                // Step 3: White-Hot Burning Spark Front Point
                ctx.fillStyle = isBurning ? '#ffffff' : '#f59e0b';
                ctx.beginPath();
                ctx.arc(pBurn.x, pBurn.y, isBurning ? 6.5 : 4.5, 0, Math.PI * 2);
                ctx.fill();

                if (isBurning) {
                    ctx.strokeStyle = '#fde047';
                    ctx.lineWidth = 2;
                    ctx.beginPath();
                    ctx.arc(pBurn.x, pBurn.y, 8.5, 0, Math.PI * 2);
                    ctx.stroke();
                }

                // Handle Grip Stamped PRAJWAL
                const pLabel = getStickPoint(145);
                ctx.fillStyle = '#ffd700';
                ctx.font = 'bold 9px sans-serif';
                ctx.fillText('👑 PRAJWAL SPARKLER', pLabel.x - 45, pLabel.y + 12);

                ctx.restore();
            }

            // 4. SUTLI BOMB - 84x76px CHUNKY JUTE TWINE CUBE (NO 1000 WATT)
            else if (currentCracker === 'bomb' && !bombExploded) {
                const bY = groundY - 38;
                const bW = 42;
                const bH = 38;

                ctx.save();
                ctx.fillStyle = 'rgba(0, 0, 0, 0.65)';
                ctx.beginPath();
                ctx.ellipse(cx, groundY + 5, bW + 8, 14, 0, 0, Math.PI * 2);
                ctx.fill();

                ctx.fillStyle = '#1c422c';
                ctx.fillRect(cx - bW, bY - bH, bW * 2, bH * 2);

                ctx.strokeStyle = '#70882b';
                ctx.lineWidth = 3;
                ctx.strokeRect(cx - bW, bY - bH, bW * 2, bH * 2);

                ctx.beginPath();
                ctx.moveTo(cx - bW, bY); ctx.lineTo(cx + bW, bY);
                ctx.moveTo(cx, bY - bH); ctx.lineTo(cx + bH, bY + bH);
                ctx.moveTo(cx - bW, bY - 18); ctx.lineTo(cx + bW, bY - 18);
                ctx.moveTo(cx - bW, bY + 18); ctx.lineTo(cx + bW, bY + 18);
                ctx.moveTo(cx - 20, bY - bH); ctx.lineTo(cx - 20, bY + bH);
                ctx.moveTo(cx + 20, bY - bH); ctx.lineTo(cx + 20, bY + bH);
                ctx.stroke();

                ctx.fillStyle = '#859c27';
                ctx.beginPath();
                ctx.arc(cx, bY, 7, 0, Math.PI * 2);
                ctx.fill();

                ctx.fillStyle = '#991b1b';
                ctx.fillRect(cx - 28, bY - 16, 56, 32);
                ctx.strokeStyle = '#ffd700';
                ctx.lineWidth = 2;
                ctx.strokeRect(cx - 28, bY - 16, 56, 32);

                ctx.fillStyle = '#fde047';
                ctx.font = 'bold 9.5px sans-serif';
                ctx.textAlign = 'center';
                ctx.fillText('👑 PRAJWAL', cx, bY - 2);
                ctx.font = 'bold 8px sans-serif';
                ctx.fillText('सुतळी बॉम्ब', cx, bY + 10);

                ctx.strokeStyle = '#f8fafc';
                ctx.lineWidth = 4;
                ctx.beginPath();
                ctx.moveTo(cx, bY - bH);
                ctx.quadraticCurveTo(cx + 12, bY - bH - (bombFuseHeight * 0.5), cx + 6, bY - bH - bombFuseHeight);
                ctx.stroke();
                ctx.restore();
            }

            // 5. ROCKET - REALISTIC GLASS BOTTLE & ROCKET
            else if (currentCracker === 'rocket') {
                const botY = groundY - 50;
                ctx.save();
                ctx.fillStyle = 'rgba(0,0,0,0.5)';
                ctx.beginPath();
                ctx.ellipse(cx, groundY + 4, 20, 8, 0, 0, Math.PI * 2);
                ctx.fill();

                const glassGrad = ctx.createLinearGradient(cx - 14, 0, cx + 14, 0);
                glassGrad.addColorStop(0, 'rgba(56, 189, 248, 0.45)');
                glassGrad.addColorStop(0.5, 'rgba(255, 255, 255, 0.75)');
                glassGrad.addColorStop(1, 'rgba(14, 116, 144, 0.55)');

                ctx.fillStyle = glassGrad;
                ctx.fillRect(cx - 14, botY, 28, 50);
                ctx.strokeStyle = 'rgba(56, 189, 248, 0.85)';
                ctx.lineWidth = 2;
                ctx.strokeRect(cx - 14, botY, 28, 50);

                ctx.fillRect(cx - 7, botY - 14, 14, 14);
                ctx.strokeRect(cx - 7, botY - 14, 14, 14);

                if (rocketInBottle) {
                    ctx.strokeStyle = '#b45309';
                    ctx.lineWidth = 2.5;
                    ctx.beginPath();
                    ctx.moveTo(cx + 5, botY - 25);
                    ctx.lineTo(cx + 5, botY + 45);
                    ctx.stroke();

                    const rGrad = ctx.createLinearGradient(cx - 9, 0, cx + 9, 0);
                    rGrad.addColorStop(0, '#991b1b');
                    rGrad.addColorStop(0.5, '#ef4444');
                    rGrad.addColorStop(1, '#7f1d1d');

                    ctx.fillStyle = rGrad;
                    ctx.fillRect(cx - 9, botY - 45, 18, 44);

                    ctx.fillStyle = '#ffd700';
                    ctx.fillRect(cx - 9, botY - 30, 18, 5);

                    ctx.fillStyle = '#fbbf24';
                    ctx.beginPath();
                    ctx.moveTo(cx - 11, botY - 45);
                    ctx.lineTo(cx + 11, botY - 45);
                    ctx.lineTo(cx, botY - 67);
                    ctx.closePath();
                    ctx.fill();

                    ctx.fillStyle = '#ffffff';
                    ctx.font = 'bold 7px sans-serif';
                    ctx.textAlign = 'center';
                    ctx.fillText('PRAJWAL', cx, botY - 12);
                }
                ctx.restore();
            }

            // 6. LAVANGI MAAL ("लवंगी माळ") - VISIBLY BURNS & SHORTENS CRACKER BY CRACKER!
            else if (currentCracker === 'ladi') {
                const lY = groundY - 16;
                ctx.save();
                ctx.fillStyle = 'rgba(0,0,0,0.5)';
                ctx.beginPath();
                ctx.ellipse(cx, groundY + 4, 105, 10, 0, 0, Math.PI * 2);
                ctx.fill();

                // Connecting Fuse Cord
                ctx.strokeStyle = '#22c55e';
                ctx.lineWidth = 2.5;
                ctx.beginPath();
                ctx.moveTo(cx - 100, lY + 8);
                ctx.lineTo(cx + 100, lY + 8);
                ctx.stroke();

                for (let i = 0; i < 18; i++) {
                    const lx = cx - 95 + (i * 11);
                    const ly = lY + Math.sin(i * 0.75) * 5;

                    // If this cracker already exploded, draw charred ash mark!
                    if (i < ladiBurstIdx) {
                        ctx.fillStyle = 'rgba(20, 20, 20, 0.75)';
                        ctx.fillRect(lx - 1, ly + 8, 10, 6);
                        ctx.strokeStyle = 'rgba(70, 70, 70, 0.5)';
                        ctx.strokeRect(lx - 1, ly + 8, 10, 6);
                    } else {
                        // Unexploded active red firecracker
                        ctx.fillStyle = '#dc2626';
                        ctx.fillRect(lx, ly, 8, 22);

                        ctx.fillStyle = '#ffd700';
                        ctx.fillRect(lx, ly + 2, 8, 3);
                        ctx.fillRect(lx, ly + 17, 8, 3);
                    }
                }

                ctx.fillStyle = '#ffd700';
                ctx.font = 'bold 9.5px sans-serif';
                ctx.textAlign = 'center';
                ctx.fillText('👑 PRAJWAL लवंगी माळ', cx, lY + 36);
                ctx.restore();
            }

            // 7. SNAKE TABLET (साप गोळी) - VISIBLY CONSUMES & SHRINKS
            else if (currentCracker === 'snake') {
                const sTabH = Math.max(3, 16 * snakeTabletScale);
                const sTabRx = Math.max(8, 30 * (0.35 + 0.65 * snakeTabletScale));
                const sTabRy = Math.max(3, 8 * (0.35 + 0.65 * snakeTabletScale));
                const tabY = groundY - (sTabH * 0.5);

                ctx.save();
                ctx.fillStyle = 'rgba(0,0,0,0.6)';
                ctx.beginPath();
                ctx.ellipse(cx, groundY + 4, sTabRx + 4, sTabRy + 2, 0, 0, Math.PI * 2);
                ctx.fill();

                ctx.fillStyle = '#0f172a';
                ctx.fillRect(cx - sTabRx, tabY - (sTabH * 0.5), sTabRx * 2, sTabH);
                ctx.beginPath();
                ctx.ellipse(cx, tabY + (sTabH * 0.5), sTabRx, sTabRy, 0, 0, Math.PI * 2);
                ctx.fill();

                ctx.fillStyle = '#1e293b';
                ctx.beginPath();
                ctx.ellipse(cx, tabY - (sTabH * 0.5), sTabRx, sTabRy, 0, 0, Math.PI * 2);
                ctx.fill();
                ctx.strokeStyle = '#ffd700';
                ctx.lineWidth = 2;
                ctx.stroke();

                if (snakeTabletScale > 0.4) {
                    ctx.fillStyle = '#fde047';
                    ctx.font = 'bold 9px sans-serif';
                    ctx.textAlign = 'center';
                    ctx.fillText('👑 PRAJWAL', cx, tabY - 2);
                }
                ctx.restore();
            }

            // 8. NEXT-LEVEL 7-SHOT ROYAL CAKE BATTERY BOX (TOF)
            else if (currentCracker === 'skyshot') {
                const boxW = 54;
                const boxH = 68;
                const boxY = groundY - boxH;

                ctx.save();
                ctx.fillStyle = 'rgba(0,0,0,0.65)';
                ctx.beginPath();
                ctx.ellipse(cx, groundY + 5, boxW + 8, 14, 0, 0, Math.PI * 2);
                ctx.fill();

                ctx.fillStyle = '#0f172a';
                ctx.fillRect(cx - (boxW + 4), groundY - 8, (boxW + 4) * 2, 10);
                ctx.strokeStyle = '#ffd700';
                ctx.lineWidth = 1.5;
                ctx.strokeRect(cx - (boxW + 4), groundY - 8, (boxW + 4) * 2, 10);

                const cakeGrad = ctx.createLinearGradient(cx - boxW, 0, cx + boxW, 0);
                cakeGrad.addColorStop(0, '#4a044e');
                cakeGrad.addColorStop(0.3, '#86198f');
                cakeGrad.addColorStop(0.7, '#a21caf');
                cakeGrad.addColorStop(1, '#3b0764');

                ctx.fillStyle = cakeGrad;
                ctx.fillRect(cx - boxW, boxY, boxW * 2, boxH - 6);
                ctx.strokeStyle = '#ffd700';
                ctx.lineWidth = 3;
                ctx.strokeRect(cx - boxW, boxY, boxW * 2, boxH - 6);

                ctx.fillStyle = '#1e1b4b';
                ctx.fillRect(cx - boxW, boxY - 10, boxW * 2, 12);
                ctx.strokeStyle = '#fbbf24';
                ctx.lineWidth = 2;
                ctx.strokeRect(cx - boxW, boxY - 10, boxW * 2, 12);

                for (let b = 0; b < 7; b++) {
                    const bx = cx - 42 + (b * 14);
                    const by = boxY - 4;

                    ctx.fillStyle = (activeSkyshotBarrel === b) ? '#ffffff' : '#020617';
                    ctx.beginPath();
                    ctx.arc(bx, by, 5, 0, Math.PI * 2);
                    ctx.fill();

                    ctx.strokeStyle = (activeSkyshotBarrel === b) ? '#ffea00' : '#d97706';
                    ctx.lineWidth = 1.8;
                    ctx.stroke();

                    if (activeSkyshotBarrel === b) {
                        ctx.fillStyle = '#ff6600';
                        ctx.beginPath();
                        ctx.arc(bx, by - 6, 9, 0, Math.PI * 2);
                        ctx.fill();
                    }
                }

                ctx.fillStyle = '#fbbf24';
                ctx.font = 'bold 9.5px sans-serif';
                ctx.textAlign = 'center';
                ctx.fillText('👑 PRAJWAL 7 SHOTS', cx, boxY + 22);
                ctx.font = 'bold 8px sans-serif';
                ctx.fillStyle = '#fde047';
                ctx.fillText('ROYAL PEACOCK BATTERY', cx, boxY + 36);
                ctx.font = '7px sans-serif';
                ctx.fillText('★ 7 AERIAL COLORS ★', cx, boxY + 48);

                ctx.restore();
            }
        }

        function selectCracker(type) {
            resetCracker();
            currentCracker = type;

            document.querySelectorAll('.cracker-card').forEach(c => c.classList.remove('active'));
            const target = Array.from(document.querySelectorAll('.cracker-card')).find(c => c.getAttribute('onclick')?.includes(type));
            if (target) target.classList.add('active');

            applyTranslations();
            const dragHint = document.getElementById('dragHint');
            if (dragHint) {
                dragHint.style.display = (type === 'stick') ? 'flex' : 'none';
            }
        }

        function resetCracker() {
            clearActiveTimers();
            particlePool.clear();
            rockets = [];
            snakeSegments = [];
            isBurning = false;
            rocketInBottle = true;
            snakeTabletScale = 1.0;
            stickBurnProgress = 0.0;
            activeSkyshotBarrel = -1;
            ladiBurstIdx = 0;
            chakriRPM = 0;
            bombExploded = false;
            bombFuseHeight = 36;
            shockwaveRadius = 0;
            shockwaveAlpha = 0;
            stickX = canvas.width / 2;
            stickY = canvas.height * 0.52;
            updateStatusText();
        }

        // ========================================================
        // 100% RELIABLE IGNITION CONTROLLER
        // ========================================================
        function igniteCracker() {
            resizeMainCanvas();

            if (isBurning) {
                clearActiveTimers();
                isBurning = false;
            }
            isBurning = true;
            updateStatusText();
            sfx.playFuse();

            const cx = canvas.width / 2;
            const groundY = canvas.height - 35;

            if (currentCracker === 'anar') {
                // ANAR: SKY-HIGH FOUNTAIN SHOOTING RIGHT TO VERY TOP OF THE BOX SKY!
                const mouthX = cx;
                const mouthY = groundY - 110;
                sfx.playWhoosh();

                let frame = 0;
                const timer = setInterval(() => {
                    frame++;
                    if (frame % 3 === 0) sfx.playCrackle();

                    // High velocity eruption (speed 17.5 to 28.5px/frame!)
                    for (let i = 0; i < 24; i++) {
                        const angle = -Math.PI / 2 + (Math.random() * 0.42 - 0.21);
                        const speed = Math.random() * 11 + 17.5;
                        const isCore = Math.random() > 0.35;
                        particlePool.spawn(
                            mouthX + (Math.random() * 6 - 3),
                            mouthY - 2, // Strictly at or above the top rim!
                            isCore ? '#ffffff' : '#ffd700',
                            Math.cos(angle) * speed,
                            Math.sin(angle) * speed,
                            0.965, 0.16, 0.011, true, 3.0
                        );
                    }

                    if (frame > 160) {
                        clearInterval(timer);
                        setTimeout(resetCracker, 1400);
                    }
                }, 25);
                activeTimerIds.push(timer);
            }
            else if (currentCracker === 'chakri') {
                // CHAKRA: SPARKS ERUPT DIRECTLY FROM THE EXACT NOZZLE TIP (NOK)
                let frame = 0;
                chakriRPM = 0.52;

                const timer = setInterval(() => {
                    frame++;
                    if (frame % 4 === 0) sfx.playWhirr();

                    const jetAngle = chakriAngle - Math.PI / 2;
                    for (let i = 0; i < 12; i++) {
                        const speed = Math.random() * 8.5 + 4.5;
                        const spread = (Math.random() - 0.5) * 0.28;
                        const c = (i % 2 === 0) ? '#ffd700' : '#22c55e';
                        particlePool.spawn(
                            chakriNokX,
                            chakriNokY,
                            c,
                            Math.cos(jetAngle + spread) * speed,
                            Math.sin(jetAngle + spread) * speed * 0.45,
                            0.94, 0.02, 0.022, false, 2.6
                        );
                    }

                    if (frame > 160) {
                        clearInterval(timer);
                        chakriRPM = 0;
                        setTimeout(resetCracker, 1000);
                    }
                }, 25);
                activeTimerIds.push(timer);
            }
            else if (currentCracker === 'stick') {
                // PHULJHADI: BURNS DOWN SMOOTHLY ALONG EXACT CO-AXIAL AXIS
                let frame = 0;
                stickBurnProgress = 0.0;

                const timer = setInterval(() => {
                    frame++;
                    stickBurnProgress = Math.min(1.0, frame / 180);

                    if (frame % 3 === 0) sfx.playCrackle();

                    const currentBurnS = stickBurnProgress * STICK_COAT_LEN;
                    const pBurn = getStickPoint(currentBurnS);

                    for (let i = 0; i < 22; i++) {
                        const angle = Math.random() * Math.PI * 2;
                        const speed = Math.random() * 6.5 + 1.8;
                        const color = Math.random() > 0.3 ? '#ffe066' : '#ffffff';
                        particlePool.spawn(
                            pBurn.x,
                            pBurn.y,
                            color,
                            Math.cos(angle) * speed,
                            Math.sin(angle) * speed,
                            0.93, 0.06, 0.04, true, 2.5
                        );
                    }

                    if (frame > 185) {
                        clearInterval(timer);
                        setTimeout(resetCracker, 900);
                    }
                }, 25);
                activeTimerIds.push(timer);
            }
            else if (currentCracker === 'bomb') {
                // SUTLI BOMB: FUSE BURNS DOWN -> BLINDING FLASH, BASS BOOM & SHATTERING TWINE
                let fuseProgress = 0;
                const bY = groundY - 38;
                const bH = 38;
                const timer = setInterval(() => {
                    fuseProgress++;
                    bombFuseHeight = Math.max(0, 36 - (fuseProgress * 0.95));

                    particlePool.spawn(
                        cx + 6,
                        bY - bH - bombFuseHeight,
                        '#ff4500',
                        (Math.random() - 0.5) * 2,
                        (Math.random() - 0.5) * 2,
                        0.9, 0, 0.08, false, 2.2
                    );

                    if (bombFuseHeight <= 0) {
                        clearInterval(timer);
                        bombExploded = true;

                        triggerScreenFlash();
                        sfx.playBombBang();

                        stageBox.classList.add('shake-box');
                        setTimeout(() => stageBox.classList.remove('shake-box'), 450);

                        shockwaveRadius = 15;
                        shockwaveAlpha = 0.95;

                        for (let i = 0; i < 200; i++) {
                            const angle = Math.random() * Math.PI * 2;
                            const speed = Math.random() * 12 + 2.5;
                            const color = (i % 3 === 0) ? '#1c422c' : ((i % 3 === 1) ? '#ff8c00' : '#ffffff');
                            particlePool.spawn(
                                cx,
                                bY,
                                color,
                                Math.cos(angle) * speed,
                                Math.sin(angle) * speed,
                                0.93, 0.22, 0.02, true, 3.4
                            );
                        }

                        setTimeout(resetCracker, 1800);
                    }
                }, 30);
                activeTimerIds.push(timer);
            }
            else if (currentCracker === 'rocket') {
                // ROCKET: FUSE BURNS -> ACCELERATES UPWARD OUT OF BOTTLE -> MULTI-BREAK DETONATION
                const botY = groundY - 50;

                let fuseStep = 0;
                const fuseTimer = setInterval(() => {
                    fuseStep++;
                    particlePool.spawn(
                        cx + 5, botY - 10,
                        '#ff6600',
                        (Math.random() - 0.5) * 2,
                        (Math.random() - 0.5) * 2,
                        0.9, 0, 0.08, false, 2
                    );

                    if (fuseStep > 12) {
                        clearInterval(fuseTimer);

                        rocketInBottle = false;
                        sfx.playWhoosh();
                        const targetX = cx;
                        const targetY = canvas.height * 0.15;
                        rockets.push(new AscendingRocket(cx, botY - 20, targetX, targetY, false, 0));

                        setTimeout(resetCracker, 2600);
                    }
                }, 30);
                activeTimerIds.push(fuseTimer);
            }
            else if (currentCracker === 'ladi') {
                // LAVANGI MAAL: VISIBLY BURNS DOWN & SHORTENS CRACKER BY CRACKER
                let curIdx = 0;
                ladiBurstIdx = 0;

                const timer = setInterval(() => {
                    sfx.playPop();
                    const lx = cx - 95 + (curIdx * 11);
                    const ly = groundY - 16;

                    // Update burst index so this cracker turns into charred ash
                    ladiBurstIdx = curIdx + 1;

                    for (let i = 0; i < 28; i++) {
                        const angle = Math.random() * Math.PI * 2;
                        const speed = Math.random() * 7 + 2;
                        const col = (i % 3 === 0) ? '#ffffff' : ((i % 3 === 1) ? '#ffd700' : '#ef4444');
                        particlePool.spawn(
                            lx, ly, col,
                            Math.cos(angle) * speed,
                            Math.sin(angle) * speed,
                            0.92, 0.15, 0.035, true, 2.6
                        );
                    }

                    curIdx++;
                    if (curIdx >= 18) {
                        clearInterval(timer);
                        sfx.playBombBang();
                        setTimeout(resetCracker, 1300);
                    }
                }, 90);
                activeTimerIds.push(timer);
            }
            else if (currentCracker === 'snake') {
                // PROCEDURAL UNIQUE SNAKE: TABLET VISIBLY CONSUMES & SHRINKS
                let frame = 0;
                let sY = groundY - 8;
                let sX = cx;
                const seed = Math.random() * 1000 + 10;

                const timer = setInterval(() => {
                    frame++;
                    sfx.playFuse();
                    sY -= Math.random() * 2.2 + 1;

                    snakeTabletScale = Math.max(0.12, 1.0 - (frame / 70));

                    if (wasmEngine && wasmEngine.get_snake_x) {
                        sX = cx + wasmEngine.get_snake_x(frame, seed) * 45;
                    } else {
                        sX += Math.sin(frame * 0.4 + seed) * 3.5;
                    }
                    snakeSegments.push({ x: sX, y: sY, r: Math.random() * 5 + 6.5 });

                    for (let i = 0; i < 4; i++) {
                        particlePool.spawn(
                            sX, sY, '#ff4500',
                            (Math.random() - 0.5) * 2,
                            -Math.random() * 2,
                            0.94, 0.05, 0.08, false, 2
                        );
                    }

                    if (frame > 70) {
                        clearInterval(timer);
                        setTimeout(resetCracker, 2200);
                    }
                }, 35);
                activeTimerIds.push(timer);
            }
            else if (currentCracker === 'skyshot') {
                // NEXT-LEVEL 7-SHOT ROYAL CAKE BATTERY (FAST CADENCE, 7 DISTINCT COLORS)
                let shot = 0;
                const timer = setInterval(() => {
                    if (shot < 7) {
                        activeSkyshotBarrel = shot;
                        sfx.playWhoosh();
                        const bx = cx - 42 + (shot * 14);
                        const by = groundY - 74;

                        for (let f = 0; f < 15; f++) {
                            particlePool.spawn(
                                bx, by,
                                '#ff6600',
                                (Math.random() - 0.5) * 3,
                                -Math.random() * 4 - 2,
                                0.9, 0.1, 0.08, false, 2.5
                            );
                        }

                        const targetX = cx + (Math.random() * 160 - 80);
                        const targetY = canvas.height * 0.14 + (Math.random() * 30 - 15);
                        rockets.push(new AscendingRocket(bx, by, targetX, targetY, true, shot));

                        setTimeout(() => { activeSkyshotBarrel = -1; }, 160);

                        shot++;
                    } else {
                        clearInterval(timer);
                        setTimeout(resetCracker, 2400);
                    }
                }, 520);
                activeTimerIds.push(timer);
            }
        }

        // ========================================================
        // HIGH-SPEED ANIMATION LOOP (ZERO ALLOCATION)
        // ========================================================
        let frameCount = 0;

        function loop() {
            requestAnimationFrame(loop);

            frameCount++;
            if (frameCount < 30 || frameCount % 60 === 0) {
                resizeMainCanvas();
            }

            const groundY = canvas.height - 35;

            ctx.fillStyle = 'rgba(8, 6, 2, 0.28)';
            ctx.fillRect(0, 0, canvas.width, canvas.height);

            if (shockwaveAlpha > 0) {
                shockwaveRadius += 4.5;
                shockwaveAlpha -= 0.04;
            }

            if (chakriRPM > 0) {
                chakriAngle += chakriRPM;
            }

            drawCrackerStudio(groundY);

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

            ctx.globalCompositeOperation = 'lighter';

            for (let i = rockets.length - 1; i >= 0; i--) {
                const r = rockets[i];
                r.update();
                r.draw(ctx);
                if (!r.alive) rockets.splice(i, 1);
            }

            const pool = particlePool.pool;
            for (let i = 0; i < pool.length; i++) {
                const p = pool[i];
                if (!p.active) continue;

                p.trailX = p.x;
                p.trailY = p.y;
                p.vx *= p.friction;
                p.vy *= p.friction;
                p.vy += p.gravity;
                p.x += p.vx;
                p.y += p.vy;

                if (p.y >= groundY) {
                    p.y = groundY;
                    if (p.bounce) {
                        p.vy = -p.vy * 0.35;
                        p.vx *= 0.8;
                    } else {
                        p.vy = 0;
                        p.vx *= 0.9;
                    }
                }

                p.alpha -= p.decay;
                if (p.alpha <= 0) {
                    p.active = false;
                    continue;
                }

                ctx.save();
                ctx.globalAlpha = Math.max(0, p.alpha);

                ctx.strokeStyle = p.color;
                ctx.lineWidth = p.size;
                ctx.beginPath();
                ctx.moveTo(p.x, p.y);
                ctx.lineTo(p.x - p.vx * 2.2, p.y - p.vy * 2.2);
                ctx.stroke();

                ctx.fillStyle = '#ffffff';
                ctx.beginPath();
                ctx.arc(p.x, p.y, p.size * 0.5, 0, Math.PI * 2);
                ctx.fill();

                ctx.restore();
            }

            ctx.globalCompositeOperation = 'source-over';
        }
        loop();

        function updateStickPointer(e) {
            if (currentCracker !== 'stick') return;
            const rect = canvas.getBoundingClientRect();
            stickX = e.clientX - rect.left;
            stickY = e.clientY - rect.top;
        }

        canvas.addEventListener('pointerdown', (e) => {
            isDraggingStick = true;
            updateStickPointer(e);
            if (!isBurning) {
                igniteCracker();
            }
        });

        window.addEventListener('pointermove', (e) => {
            if (isDraggingStick && currentCracker === 'stick') {
                updateStickPointer(e);
            }
        });

        window.addEventListener('pointerup', () => { isDraggingStick = false; });
        window.addEventListener('pointercancel', () => { isDraggingStick = false; });

        const btnIgnite = document.getElementById('btnIgnite');
        btnIgnite.addEventListener('click', (e) => {
            e.preventDefault();
            igniteCracker();
        });

        const btnReset = document.getElementById('btnReset');
        btnReset.addEventListener('click', (e) => {
            e.preventDefault();
            resetCracker();
        });

        applyTranslations();
        selectCracker('anar');
    </script>
</body>
</html>
'''

with open('/data/data/com.termux/files/home/diwali_website/index.html', 'w', encoding='utf-8') as f:
    f.write(html_content)

print("Generated index.html successfully! Size:", len(html_content))
