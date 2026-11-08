# -*- coding: utf-8 -*-
"""
Generator for High-End 3D Digital Diwali Cracker Studio
Features:
- Local Three.js (r128) 100% offline
- Authentic 3D procedural models for 8 Indian crackers
- Strict animation cleanup (zero bleed between crackers)
- Dual language support (Marathi & English) with instant toggle
- Large commanding 3D Cracker Box with realistic lighting & floor reflections
- Rich Diwali greeting animation with animated Diyas and dynamic Subhechha ticker
- Web Audio procedural sound synthesizer (sub-bass bombs, whirrs, crackles)
- 100% Zero-Lag, single-screen locked (no scroll, no zoom)
"""

html_content = r'''<!DOCTYPE html>
<html lang="mr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no, viewport-fit=cover">
    <title>शुभ दीपावली २०२६ | 3D फटाका स्टुडिओ</title>

    <!-- Google Fonts -->
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Rozha+One&family=Yatra+One&family=Poppins:wght@400;600;700;800;900&family=Tiro+Devanagari+Marathi:ital@0;1&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">

    <!-- Three.js (Offline Local Copy with CDN Fallback) -->
    <script src="js/three.min.js"></script>
    <script>
        if (typeof THREE === 'undefined') {
            document.write('<script src="https://cdnjs.cloudflare.com/ajax/libs/three.js/r128/three.min.js"><\/script>');
        }
    </script>

    <style>
        :root {
            --gold-grad: linear-gradient(135deg, #ffd700 0%, #ff8c00 50%, #f59e0b 100%);
            --royal-bg: radial-gradient(circle at 50% 12%, #240c38 0%, #0d0418 60%, #05010a 100%);
            --card-border: rgba(255, 215, 0, 0.4);
            --card-glow: 0 12px 35px rgba(0, 0, 0, 0.8), 0 0 25px rgba(255, 140, 0, 0.18);
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
            padding: 8px 10px 10px;
            position: relative;
        }

        /* Ambient floating golden dust background */
        .ambient-canvas {
            position: absolute;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            pointer-events: none;
            z-index: 1;
        }

        /* Top Action Utility Bar (Language Toggle + Sound Toggle) */
        .top-utility-bar {
            position: relative;
            z-index: 20;
            width: 100%;
            max-width: 760px;
            display: flex;
            justify-content: space-between;
            align-items: center;
            padding: 2px 4px;
            flex-shrink: 0;
        }

        .lang-switch-btn {
            background: rgba(255, 215, 0, 0.12);
            border: 1.5px solid var(--card-border);
            color: #ffd700;
            padding: 5px 12px;
            border-radius: 20px;
            font-size: 0.76rem;
            font-weight: 700;
            cursor: pointer;
            display: flex;
            align-items: center;
            gap: 6px;
            backdrop-filter: blur(6px);
            transition: all 0.2s cubic-bezier(0.34, 1.56, 0.64, 1);
            box-shadow: 0 2px 10px rgba(0, 0, 0, 0.4);
        }

        .lang-switch-btn:hover {
            background: var(--gold-grad);
            color: #000;
            transform: scale(1.05);
            box-shadow: 0 4px 15px rgba(255, 215, 0, 0.5);
        }

        .sound-switch-btn {
            background: rgba(255, 215, 0, 0.12);
            border: 1.5px solid var(--card-border);
            color: #ffd700;
            padding: 5px 12px;
            border-radius: 20px;
            font-size: 0.76rem;
            font-weight: 700;
            cursor: pointer;
            display: flex;
            align-items: center;
            gap: 6px;
            backdrop-filter: blur(6px);
            transition: all 0.2s;
        }

        .sound-switch-btn.active {
            background: var(--gold-grad);
            color: #000;
            box-shadow: 0 2px 12px rgba(255, 215, 0, 0.5);
        }

        /* ========================================================
           UPPER FESTIVE GREETINGS & DIYA ANIMATION SECTION
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
            margin-top: -2px;
        }

        .header-row {
            display: flex;
            align-items: center;
            justify-content: center;
            gap: 14px;
            width: 100%;
        }

        /* Animated Glowing Brass Diyas */
        .diya-wrapper {
            display: flex;
            flex-direction: column;
            align-items: center;
            position: relative;
            width: 38px;
            height: 38px;
            flex-shrink: 0;
        }

        .diya-flame {
            width: 14px;
            height: 22px;
            background: radial-gradient(ellipse at 50% 85%, #ffffff 0%, #fffb00 35%, #ff5500 70%, transparent 95%);
            border-radius: 50% 50% 35% 35% / 70% 70% 30% 30%;
            filter: drop-shadow(0 0 8px #ff7700) drop-shadow(0 0 16px #ffbb00);
            animation: flameFlicker 1.4s infinite alternate ease-in-out;
            transform-origin: center bottom;
        }

        .diya-base {
            width: 34px;
            height: 14px;
            background: linear-gradient(180deg, #d97706 0%, #78350f 100%);
            border-radius: 0 0 20px 20px;
            border-top: 2px solid #fde68a;
            box-shadow: 0 3px 8px rgba(0,0,0,0.6);
            margin-top: -3px;
            position: relative;
        }

        .diya-base::after {
            content: '';
            position: absolute;
            top: 2px;
            left: 50%;
            transform: translateX(-50%);
            width: 20px;
            height: 3px;
            background: #f59e0b;
            border-radius: 3px;
        }

        @keyframes flameFlicker {
            0% { transform: scale(1) rotate(-2deg); filter: drop-shadow(0 0 8px #ff7700) drop-shadow(0 0 14px #ffbb00); }
            50% { transform: scale(1.1, 0.95) rotate(2deg); filter: drop-shadow(0 0 11px #ff5500) drop-shadow(0 0 20px #ffd700); }
            100% { transform: scale(0.96, 1.06) rotate(-1deg); filter: drop-shadow(0 0 7px #ff8800) drop-shadow(0 0 13px #ffaa00); }
        }

        .title-block {
            display: flex;
            flex-direction: column;
            align-items: center;
        }

        .shloka-text {
            font-family: 'Rozha One', 'Tiro Devanagari Marathi', serif;
            font-size: 0.75rem;
            color: #fde68a;
            letter-spacing: 1.5px;
            text-shadow: 0 0 8px rgba(255, 215, 0, 0.6);
            margin-bottom: -2px;
        }

        .main-title {
            font-family: 'Yatra One', 'Rozha One', cursive, sans-serif;
            font-size: 1.95rem;
            line-height: 1.1;
            background: var(--gold-grad);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            filter: drop-shadow(0 2px 14px rgba(255, 140, 0, 0.7));
            letter-spacing: 1px;
        }

        /* Animated Subhechha Greeting Ticker */
        .subhechha-card {
            background: rgba(255, 215, 0, 0.08);
            border: 1px solid rgba(255, 215, 0, 0.25);
            border-radius: 12px;
            padding: 3px 14px;
            max-width: 96%;
            backdrop-filter: blur(5px);
            margin-top: 2px;
            min-height: 24px;
            display: flex;
            align-items: center;
            justify-content: center;
            box-shadow: inset 0 0 12px rgba(255, 215, 0, 0.05);
        }

        .subhechha-text {
            font-size: 0.74rem;
            font-weight: 600;
            color: #fef08a;
            text-align: center;
            transition: opacity 0.4s ease, transform 0.4s ease;
            letter-spacing: 0.5px;
            white-space: nowrap;
            overflow: hidden;
            text-overflow: ellipsis;
        }

        /* ========================================================
           CENTRAL COMMANDING 3D CRACKER BOX (LARGE & PROMINENT)
           ======================================================== */
        .stage-container {
            position: relative;
            z-index: 10;
            width: 100%;
            max-width: 760px;
            flex: 1;
            min-height: 280px;
            max-height: 52vh;
            background: radial-gradient(circle at 50% 85%, #230f35 0%, #11051e 75%, #080210 100%);
            border: 2px solid var(--card-border);
            border-radius: 22px;
            box-shadow: var(--card-glow);
            overflow: hidden;
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            margin: 4px 0;
        }

        #threeCanvas {
            width: 100%;
            height: 100%;
            display: block;
            touch-action: none;
            cursor: pointer;
        }

        /* Badges & Status overlay inside box */
        .stage-hud {
            position: absolute;
            top: 10px;
            left: 12px;
            right: 12px;
            display: flex;
            justify-content: space-between;
            align-items: center;
            pointer-events: none;
            z-index: 15;
        }

        .cracker-badge {
            background: rgba(13, 4, 24, 0.75);
            border: 1px solid var(--card-border);
            padding: 4px 12px;
            border-radius: 14px;
            font-size: 0.75rem;
            font-weight: 700;
            color: #ffd700;
            display: flex;
            align-items: center;
            gap: 6px;
            backdrop-filter: blur(6px);
            box-shadow: 0 3px 10px rgba(0, 0, 0, 0.6);
        }

        .status-badge {
            font-size: 0.7rem;
            font-weight: 600;
            color: #e2e8f0;
            background: rgba(0, 0, 0, 0.6);
            border: 1px solid rgba(255, 255, 255, 0.15);
            padding: 3px 10px;
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
            animation: pulseDot 0.6s infinite alternate;
        }

        @keyframes pulseDot {
            0% { transform: scale(0.8); opacity: 0.6; }
            100% { transform: scale(1.3); opacity: 1; }
        }

        /* Drag Hint for Phuljhadi Stick */
        .drag-hint {
            position: absolute;
            bottom: 12px;
            left: 50%;
            transform: translateX(-50%);
            background: rgba(0,0,0,0.65);
            border: 1px solid rgba(255,215,0,0.3);
            color: #fef08a;
            font-size: 0.7rem;
            padding: 3px 12px;
            border-radius: 12px;
            pointer-events: none;
            display: none;
            align-items: center;
            gap: 6px;
            z-index: 15;
        }

        /* ========================================================
           ACTION CONTROLS ROW
           ======================================================== */
        .controls-row {
            position: relative;
            z-index: 10;
            display: flex;
            gap: 10px;
            width: 100%;
            max-width: 760px;
            flex-shrink: 0;
            margin-top: 2px;
        }

        .btn-ignite {
            flex: 2.2;
            padding: 11px 16px;
            background: linear-gradient(135deg, #f59e0b 0%, #ef4444 60%, #b91c1c 100%);
            color: #fff;
            border: none;
            border-radius: 16px;
            font-weight: 800;
            font-size: 0.95rem;
            cursor: pointer;
            display: flex;
            align-items: center;
            justify-content: center;
            gap: 8px;
            box-shadow: 0 4px 18px rgba(239, 68, 68, 0.45);
            transition: all 0.2s cubic-bezier(0.34, 1.56, 0.64, 1);
            letter-spacing: 0.5px;
        }

        .btn-ignite:hover {
            transform: translateY(-2px);
            box-shadow: 0 6px 24px rgba(245, 158, 11, 0.65);
        }

        .btn-ignite:active {
            transform: translateY(1px);
        }

        .btn-reset {
            flex: 1;
            padding: 11px 12px;
            background: rgba(255, 215, 0, 0.1);
            color: #ffd700;
            border: 1.5px solid var(--card-border);
            border-radius: 16px;
            font-weight: 700;
            font-size: 0.85rem;
            cursor: pointer;
            display: flex;
            align-items: center;
            justify-content: center;
            gap: 6px;
            backdrop-filter: blur(5px);
            transition: all 0.2s;
        }

        .btn-reset:hover {
            background: rgba(255, 215, 0, 0.2);
            transform: translateY(-2px);
        }

        /* ========================================================
           CRACKER SELECTOR TRAY (8 AUTHENTIC CRACKERS)
           ======================================================== */
        .picker-container {
            position: relative;
            z-index: 10;
            width: 100%;
            max-width: 760px;
            flex-shrink: 0;
            margin-top: 4px;
        }

        .picker-header {
            font-size: 0.7rem;
            font-weight: 700;
            color: #fde68a;
            text-transform: uppercase;
            letter-spacing: 1px;
            margin-bottom: 4px;
            display: flex;
            align-items: center;
            gap: 6px;
            padding-left: 2px;
        }

        .cracker-dock {
            display: flex;
            gap: 8px;
            overflow-x: auto;
            padding-bottom: 4px;
            scrollbar-width: none;
            -webkit-overflow-scrolling: touch;
        }

        .cracker-dock::-webkit-scrollbar { display: none; }

        .cracker-card {
            flex-shrink: 0;
            background: rgba(255, 215, 0, 0.05);
            border: 1.5px solid rgba(255, 215, 0, 0.18);
            border-radius: 14px;
            padding: 7px 11px;
            color: #cbd5e1;
            cursor: pointer;
            display: flex;
            flex-direction: column;
            align-items: center;
            gap: 3px;
            min-width: 74px;
            transition: all 0.2s cubic-bezier(0.34, 1.56, 0.64, 1);
        }

        .cracker-card i {
            font-size: 1.25rem;
            color: #f59e0b;
            transition: transform 0.2s;
        }

        .cracker-card .cracker-lbl {
            font-size: 0.72rem;
            font-weight: 700;
            white-space: nowrap;
        }

        .cracker-card .cracker-sub {
            font-size: 0.58rem;
            color: #94a3b8;
            white-space: nowrap;
        }

        .cracker-card.active {
            background: var(--gold-grad);
            color: #000;
            border-color: #ffd700;
            box-shadow: 0 4px 18px rgba(255, 215, 0, 0.5);
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

        /* Footer greetings banner */
        .footer-banner {
            position: relative;
            z-index: 10;
            display: flex;
            align-items: center;
            justify-content: center;
            gap: 8px;
            font-size: 0.68rem;
            color: rgba(255, 215, 0, 0.75);
            letter-spacing: 0.8px;
            flex-shrink: 0;
            margin-top: 2px;
        }

        /* Box shake effect for bomb explosion */
        .shake-box {
            animation: boxShake 0.4s cubic-bezier(.36,.07,.19,.97) both;
        }

        @keyframes boxShake {
            10%, 90% { transform: translate3d(-3px, 1px, 0); }
            20%, 80% { transform: translate3d(5px, -2px, 0); }
            30%, 50%, 70% { transform: translate3d(-6px, 3px, 0); }
            40%, 60% { transform: translate3d(6px, -3px, 0); }
        }
    </style>
</head>
<body>

    <!-- Ambient floating golden stars/dust -->
    <canvas class="ambient-canvas" id="ambientCanvas"></canvas>

    <!-- Top Utility Bar: Language Switcher + Sound Toggle -->
    <div class="top-utility-bar">
        <button class="lang-switch-btn" id="btnLangSwitch" title="Switch Language">
            <i class="fas fa-language"></i> <span id="lblLang">मराठी / English</span>
        </button>
        <button class="sound-switch-btn active" id="btnSoundSwitch" title="Sound FX Toggle">
            <i class="fas fa-volume-high"></i> <span id="lblSound">आवाज सुरु</span>
        </button>
    </div>

    <!-- UPPER FESTIVE GREETINGS SECTION -->
    <header class="festive-hero">
        <div class="header-row">
            <!-- Left Animated Diya -->
            <div class="diya-wrapper">
                <div class="diya-flame"></div>
                <div class="diya-base"></div>
            </div>

            <!-- Central Golden Calligraphy -->
            <div class="title-block">
                <div class="shloka-text" id="headerShloka">॥ तमसो मा ज्योतिर्गमय ॥</div>
                <h1 class="main-title" id="headerMainTitle">शुभ दीपावली</h1>
            </div>

            <!-- Right Animated Diya -->
            <div class="diya-wrapper">
                <div class="diya-flame"></div>
                <div class="diya-base"></div>
            </div>
        </div>

        <!-- Dynamic Subhechha Greeting Card -->
        <div class="subhechha-card">
            <div class="subhechha-text" id="subhechhaBanner">
                दीपावलीच्या तुम्हाला व तुमच्या संपूर्ण परिवारास मनःपूर्वक हार्दिक शुभेच्छा!
            </div>
        </div>
    </header>

    <!-- CENTRAL COMMANDING 3D CRACKER BOX -->
    <main class="stage-container" id="stageBox">
        <div class="stage-hud">
            <div class="cracker-badge" id="hudBadge">
                <i class="fas fa-volcano"></i> <span id="hudBadgeName">फटाका पाऊस (Paus)</span>
            </div>
            <div class="status-badge" id="hudStatus">
                <div class="dot"></div> <span id="hudStatusText">तयार आहे • पेटवा</span>
            </div>
        </div>

        <div class="drag-hint" id="dragHint">
            <i class="fas fa-hand-pointer"></i> <span id="lblDragHint">फुलबाजा फिरवण्यासाठी स्क्रीनवर ड्रॅग करा</span>
        </div>

        <canvas id="threeCanvas"></canvas>
    </main>

    <!-- ACTION BUTTONS -->
    <div class="controls-row">
        <button class="btn-ignite" id="btnIgnite">
            <i class="fas fa-fire"></i> <span id="lblBtnIgnite">फटाका पेटवा (IGNITE)</span>
        </button>
        <button class="btn-reset" id="btnReset">
            <i class="fas fa-rotate-left"></i> <span id="lblBtnReset">नवा फटाका</span>
        </button>
    </div>

    <!-- 8 AUTHENTIC CRACKER SELECTOR TRAY -->
    <section class="picker-container">
        <div class="picker-header" id="lblPickerTitle">
            <i class="fas fa-boxes-stacked"></i> फटाका निवडा (SELECT CRACKER):
        </div>
        <div class="cracker-dock">
            <!-- 1. Paus / Anar -->
            <div class="cracker-card active" onclick="selectCracker('anar')">
                <i class="fas fa-volcano"></i>
                <span class="cracker-lbl" id="cardLbl_anar">फटाका पाऊस</span>
                <span class="cracker-sub" id="cardSub_anar">Paus / Anar</span>
            </div>
            <!-- 2. Bhuichakra -->
            <div class="cracker-card" onclick="selectCracker('chakri')">
                <i class="fas fa-compact-disc"></i>
                <span class="cracker-lbl" id="cardLbl_chakri">भुईचक्र</span>
                <span class="cracker-sub" id="cardSub_chakri">Chakra</span>
            </div>
            <!-- 3. Phulbaja / Stick -->
            <div class="cracker-card" onclick="selectCracker('stick')">
                <i class="fas fa-wand-magic-sparkles"></i>
                <span class="cracker-lbl" id="cardLbl_stick">फुलबाजा</span>
                <span class="cracker-sub" id="cardSub_stick">Phuljhadi</span>
            </div>
            <!-- 4. Sky Rocket -->
            <div class="cracker-card" onclick="selectCracker('rocket')">
                <i class="fas fa-rocket"></i>
                <span class="cracker-lbl" id="cardLbl_rocket">आकाशी रॉकेट</span>
                <span class="cracker-sub" id="cardSub_rocket">Sky Rocket</span>
            </div>
            <!-- 5. Sutli Bomb -->
            <div class="cracker-card" onclick="selectCracker('bomb')">
                <i class="fas fa-bomb"></i>
                <span class="cracker-lbl" id="cardLbl_bomb">सुतळी बॉम्ब</span>
                <span class="cracker-sub" id="cardSub_bomb">Sutli Bomb</span>
            </div>
            <!-- 6. Lavangi Ladi -->
            <div class="cracker-card" onclick="selectCracker('ladi')">
                <i class="fas fa-meteor"></i>
                <span class="cracker-lbl" id="cardLbl_ladi">लवंगी लड</span>
                <span class="cracker-sub" id="cardSub_ladi">1000 Ladi</span>
            </div>
            <!-- 7. Saap Tablet -->
            <div class="cracker-card" onclick="selectCracker('snake')">
                <i class="fas fa-worm"></i>
                <span class="cracker-lbl" id="cardLbl_snake">साप गोळी</span>
                <span class="cracker-sub" id="cardSub_snake">Snake Tablet</span>
            </div>
            <!-- 8. Sky Shots (7-Shot) -->
            <div class="cracker-card" onclick="selectCracker('skyshot')">
                <i class="fas fa-burst"></i>
                <span class="cracker-lbl" id="cardLbl_skyshot">आकाशी तोफ</span>
                <span class="cracker-sub" id="cardSub_skyshot">7 Sky Shots</span>
            </div>
        </div>
    </section>

    <!-- FOOTER -->
    <footer class="footer-banner" id="lblFooterWish">
        🪔 प्रदूषणमुक्त डिजिटल दिवाळी २०२६ • Happy Diwali! 🪔
    </footer>

    <!-- ========================================================
         JAVASCRIPT ENGINE (TRANSLATION + AUDIO + 3D SIMULATION)
         ======================================================== -->
    <script>
        // ========================================================
        // 1. DUAL LANGUAGE (MARATHI & ENGLISH) DICTIONARY & LOGIC
        // ========================================================
        let currentLang = 'mr'; // default Marathi

        const I18N = {
            mr: {
                langBtn: "मराठी (MR)",
                soundOn: "आवाज सुरु",
                soundOff: "आवाज बंद",
                shloka: "॥ तमसो मा ज्योतिर्गमय ॥",
                mainTitle: "शुभ दीपावली २०२६",
                subhechhas: [
                    "दीपावलीच्या तुम्हाला व तुमच्या संपूर्ण परिवारास मनःपूर्वक हार्दिक शुभेच्छा!",
                    "सुख, समृद्धी, उत्तम आरोग्य आणि ऐश्वर्याचे दीप तुमच्या आयुष्यात सदैव तेवत राहो!",
                    "प्रकाशाचा हा पावन दीपोत्सव आपल्या जीवनात नवीन उमेद व आनंद घेऊन येवो!",
                    "लक्ष्मी मातेच्या असीम आशीर्वादाने आपल्या घरी अखंड धन-धान्य व भरभराट लाभो!"
                ],
                igniteBtn: "फटाका पेटवा (IGNITE)",
                resetBtn: "नवा फटाका",
                readyStatus: "तयार आहे • पेटवा",
                burningStatus: "धडाका सुरू आहे...!",
                dragHint: "फुलबाजा फिरवण्यासाठी स्क्रीनवर ड्रॅग करा",
                pickerTitle: "फटाका निवडा (SELECT CRACKER):",
                footerWish: "🪔 प्रदूषणमुक्त डिजिटल दिवाळी २०२६ • शुभ दीपावली! 🪔",
                crackers: {
                    anar: { name: "फटाका पाऊस", sub: "Paus / Anar", badge: "फटाका पाऊस (Paus)" },
                    chakri: { name: "भुईचक्र", sub: "Chakra", badge: "भुईचक्र (Bhuichakra)" },
                    stick: { name: "फुलबाजा", sub: "Phuljhadi", badge: "फुलबाजा (Phuljhadi)" },
                    rocket: { name: "आकाशी रॉकेट", sub: "Sky Rocket", badge: "आकाशी रॉकेट (Rocket)" },
                    bomb: { name: "सुतळी बॉम्ब", sub: "Sutli Bomb", badge: "सुतळी बॉम्ब (Sutli Bomb)" },
                    ladi: { name: "लवंगी लड", sub: "1000 Ladi", badge: "लवंगी लड (1000 Ladi)" },
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
                footerWish: "🪔 100% Eco-Friendly Digital Diwali 2026 • Happy Diwali! 🪔",
                crackers: {
                    anar: { name: "Flower Pot", sub: "Paus Fountain", badge: "Flower Pot (Paus / Anar)" },
                    chakri: { name: "Ground Chakra", sub: "Whirling Spinner", badge: "Ground Spinner (Chakri)" },
                    stick: { name: "Sparkler Stick", sub: "Handheld Sizzler", badge: "Sparkler Stick (Phuljhadi)" },
                    rocket: { name: "Sky Rocket", sub: "High Altitude", badge: "Sky Rocket (Rocket)" },
                    bomb: { name: "Sutli Bomb", sub: "Bass Explosion", badge: "Sutli Bomb (Jute Bomb)" },
                    ladi: { name: "1000 Ladi", sub: "Garland Firecracker", badge: "Garland Ladi (1000 Ladi)" },
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
            document.getElementById('headerMainTitle').innerText = data.mainTitle;
            document.getElementById('lblBtnIgnite').innerText = data.igniteBtn;
            document.getElementById('lblBtnReset').innerText = data.resetBtn;
            document.getElementById('lblDragHint').innerText = data.dragHint;
            document.getElementById('lblPickerTitle').innerHTML = `<i class="fas fa-boxes-stacked"></i> ${data.pickerTitle}`;
            document.getElementById('lblFooterWish').innerText = data.footerWish;

            // Update Cracker Pills
            for (let [key, c] of Object.entries(data.crackers)) {
                const elLbl = document.getElementById(`cardLbl_${key}`);
                const elSub = document.getElementById(`cardSub_${key}`);
                if (elLbl) elLbl.innerText = c.name;
                if (elSub) elSub.innerText = c.sub;
            }

            // Update Badge
            const curCrackerData = data.crackers[currentCracker];
            if (curCrackerData) {
                document.getElementById('hudBadgeName').innerText = curCrackerData.badge;
            }

            // Update status text
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

        // Toggle Language Button
        document.getElementById('btnLangSwitch').addEventListener('click', () => {
            currentLang = (currentLang === 'mr') ? 'en' : 'mr';
            applyTranslations();
            updateSubhechha(true);
        });

        // Dynamic Subhechha Rotating Banner
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
            elSubhechha.style.transform = 'translateY(6px)';
            setTimeout(() => {
                subhechhaIdx = (subhechhaIdx + 1) % list.length;
                elSubhechha.innerText = list[subhechhaIdx];
                elSubhechha.style.opacity = '1';
                elSubhechha.style.transform = 'translateY(0)';
            }, 400);
        }
        setInterval(() => updateSubhechha(false), 4500);

        // ========================================================
        // 2. PROCEDURAL WEB AUDIO SYNTHESIZER (ZERO LATENCY)
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

            // Fizzing fuse sound
            playFuse() {
                if (!this.enabled) return;
                this.init();
                const now = this.ctx.currentTime;
                const dur = 0.22;
                const buf = this.ctx.createBuffer(1, Math.floor(this.ctx.sampleRate * dur), this.ctx.sampleRate);
                const d = buf.getChannelData(0);
                for (let i = 0; i < d.length; i++) d[i] = (Math.random() * 2 - 1) * Math.exp(-i / (d.length * 0.4));
                const src = this.ctx.createBufferSource();
                src.buffer = buf;
                const filter = this.ctx.createBiquadFilter();
                filter.type = 'highpass';
                filter.frequency.setValueAtTime(2200, now);
                const gain = this.ctx.createGain();
                gain.gain.setValueAtTime(0.08, now);
                gain.gain.linearRampToValueAtTime(0.001, now + dur);
                src.connect(filter); filter.connect(gain); gain.connect(this.ctx.destination);
                src.start(now);
            }

            // Sharp crackle pop (Paus, Phuljhadi)
            playCrackle() {
                if (!this.enabled) return;
                this.init();
                const now = this.ctx.currentTime;
                const osc = this.ctx.createOscillator();
                const gain = this.ctx.createGain();
                osc.type = 'square';
                osc.frequency.setValueAtTime(800 + Math.random() * 2400, now);
                gain.gain.setValueAtTime(0.06, now);
                gain.gain.exponentialRampToValueAtTime(0.001, now + 0.05);
                osc.connect(gain); gain.connect(this.ctx.destination);
                osc.start(now); osc.stop(now + 0.05);
            }

            // Whirring & whistling aerodynamic sound (Chakra)
            playWhirr() {
                if (!this.enabled) return;
                this.init();
                const now = this.ctx.currentTime;
                const osc = this.ctx.createOscillator();
                const gain = this.ctx.createGain();
                osc.type = 'triangle';
                osc.frequency.setValueAtTime(260 + Math.random() * 80, now);
                osc.frequency.linearRampToValueAtTime(420, now + 0.1);
                gain.gain.setValueAtTime(0.07, now);
                gain.gain.exponentialRampToValueAtTime(0.001, now + 0.1);
                osc.connect(gain); gain.connect(this.ctx.destination);
                osc.start(now); osc.stop(now + 0.1);
            }

            // Rocket whoosh whistle ascent
            playWhoosh() {
                if (!this.enabled) return;
                this.init();
                const now = this.ctx.currentTime;
                const dur = 0.9;
                const osc = this.ctx.createOscillator();
                const gain = this.ctx.createGain();
                osc.type = 'sawtooth';
                osc.frequency.setValueAtTime(220, now);
                osc.frequency.exponentialRampToValueAtTime(1400, now + dur);
                gain.gain.setValueAtTime(0.01, now);
                gain.gain.linearRampToValueAtTime(0.12, now + dur * 0.7);
                gain.gain.exponentialRampToValueAtTime(0.001, now + dur);
                osc.connect(gain); gain.connect(this.ctx.destination);
                osc.start(now); osc.stop(now + dur);
            }

            // Deep Sutli Bomb / Explosion Bang (Sub-bass rumble)
            playBombBang() {
                if (!this.enabled) return;
                this.init();
                const now = this.ctx.currentTime;
                const dur = 0.7;

                // Sub-bass punch
                const osc = this.ctx.createOscillator();
                const oscGain = this.ctx.createGain();
                osc.type = 'sine';
                osc.frequency.setValueAtTime(130, now);
                osc.frequency.exponentialRampToValueAtTime(28, now + dur);
                oscGain.gain.setValueAtTime(0.7, now);
                oscGain.gain.exponentialRampToValueAtTime(0.001, now + dur);
                osc.connect(oscGain); oscGain.connect(this.ctx.destination);
                osc.start(now); osc.stop(now + dur);

                // Explosive white noise crack
                const buf = this.ctx.createBuffer(1, Math.floor(this.ctx.sampleRate * 0.5), this.ctx.sampleRate);
                const d = buf.getChannelData(0);
                for (let i = 0; i < d.length; i++) d[i] = (Math.random() * 2 - 1) * Math.exp(-i / (d.length * 0.2));
                const noise = this.ctx.createBufferSource();
                noise.buffer = buf;
                const filter = this.ctx.createBiquadFilter();
                filter.type = 'lowpass';
                filter.frequency.setValueAtTime(500, now);
                filter.frequency.exponentialRampToValueAtTime(50, now + 0.5);
                const nGain = this.ctx.createGain();
                nGain.gain.setValueAtTime(0.65, now);
                nGain.gain.exponentialRampToValueAtTime(0.001, now + 0.5);
                noise.connect(filter); filter.connect(nGain); nGain.connect(this.ctx.destination);
                noise.start(now);
            }

            // Quick sharp pop (Ladi mini crackers)
            playPop() {
                if (!this.enabled) return;
                this.init();
                const now = this.ctx.currentTime;
                const osc = this.ctx.createOscillator();
                const gain = this.ctx.createGain();
                osc.type = 'square';
                osc.frequency.setValueAtTime(950, now);
                osc.frequency.exponentialRampToValueAtTime(120, now + 0.06);
                gain.gain.setValueAtTime(0.18, now);
                gain.gain.exponentialRampToValueAtTime(0.001, now + 0.06);
                osc.connect(gain); gain.connect(this.ctx.destination);
                osc.start(now); osc.stop(now + 0.06);
            }

            // Aerial sky burst boom (Sky shots & rocket burst)
            playAerialBurst() {
                if (!this.enabled) return;
                this.init();
                const now = this.ctx.currentTime;
                const dur = 0.55;

                const osc = this.ctx.createOscillator();
                const gain = this.ctx.createGain();
                osc.type = 'triangle';
                osc.frequency.setValueAtTime(240, now);
                osc.frequency.exponentialRampToValueAtTime(45, now + dur);
                gain.gain.setValueAtTime(0.4, now);
                gain.gain.exponentialRampToValueAtTime(0.001, now + dur);
                osc.connect(gain); gain.connect(this.ctx.destination);
                osc.start(now); osc.stop(now + dur);
            }
        }
        const sfx = new SoundSynth();

        // Sound Toggle Button
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

        // ========================================================
        // 3. BACKGROUND AMBIENT GOLDEN DUST CANVAS
        // ========================================================
        const ambCanvas = document.getElementById('ambientCanvas');
        const ambCtx = ambCanvas.getContext('2d');
        let ambStars = [];

        function initAmbientStars() {
            ambCanvas.width = window.innerWidth;
            ambCanvas.height = window.innerHeight;
            ambStars = [];
            for (let i = 0; i < 45; i++) {
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
                ambCtx.fillStyle = `rgba(255, 215, 0, ${a * 0.6})`;
                ambCtx.beginPath();
                ambCtx.arc(s.x, s.y, s.r, 0, Math.PI * 2);
                ambCtx.fill();
            }
            requestAnimationFrame(renderAmbientStars);
        }
        renderAmbientStars();

        // ========================================================
        // 4. PROCEDURAL TEXTURE GENERATORS FOR 3D MODELS
        // ========================================================
        // Glowing Golden Rangoli Floor Mandala Texture
        function createRangoliTexture() {
            const tc = document.createElement('canvas');
            tc.width = 512; tc.height = 512;
            const tctx = tc.getContext('2d');
            const cx = 256, cy = 256;

            // Deep Royal Dark Marble floor
            tctx.fillStyle = '#10051e';
            tctx.fillRect(0, 0, 512, 512);

            // Subtle floor grid
            tctx.strokeStyle = 'rgba(255, 215, 0, 0.08)';
            tctx.lineWidth = 1;
            for (let i = 0; i < 512; i += 32) {
                tctx.beginPath(); tctx.moveTo(i, 0); tctx.lineTo(i, 512); tctx.stroke();
                tctx.beginPath(); tctx.moveTo(0, i); tctx.lineTo(512, i); tctx.stroke();
            }

            // Golden Mandala Rings
            tctx.strokeStyle = '#ffd700';
            tctx.lineWidth = 3;
            tctx.beginPath(); tctx.arc(cx, cy, 210, 0, Math.PI * 2); tctx.stroke();

            tctx.strokeStyle = 'rgba(255, 140, 0, 0.7)';
            tctx.lineWidth = 2;
            tctx.beginPath(); tctx.arc(cx, cy, 180, 0, Math.PI * 2); tctx.stroke();

            // Lotus Petals
            for (let i = 0; i < 16; i++) {
                const angle = (i * Math.PI * 2) / 16;
                const px = cx + Math.cos(angle) * 140;
                const py = cy + Math.sin(angle) * 140;
                tctx.fillStyle = (i % 2 === 0) ? '#ff4500' : '#ffd700';
                tctx.beginPath();
                tctx.arc(px, py, 14, 0, Math.PI * 2);
                tctx.fill();
            }

            // Center Diya circle
            tctx.fillStyle = 'rgba(255, 215, 0, 0.2)';
            tctx.beginPath(); tctx.arc(cx, cy, 70, 0, Math.PI * 2); tctx.fill();
            tctx.strokeStyle = '#ffd700';
            tctx.lineWidth = 3;
            tctx.stroke();

            return new THREE.CanvasTexture(tc);
        }

        // Terracotta Paus Cone Label Texture
        function createPausTexture() {
            const tc = document.createElement('canvas');
            tc.width = 256; tc.height = 256;
            const tctx = tc.getContext('2d');
            tctx.fillStyle = '#b45309';
            tctx.fillRect(0, 0, 256, 256);

            // Gold foil bands
            tctx.fillStyle = '#ffd700';
            tctx.fillRect(0, 40, 256, 20);
            tctx.fillRect(0, 180, 256, 20);

            // Label text
            tctx.fillStyle = '#ffffff';
            tctx.font = 'bold 28px sans-serif';
            tctx.textAlign = 'center';
            tctx.fillText('⭐ पाऊस 3D ⭐', 128, 120);
            tctx.fillStyle = '#fef08a';
            tctx.font = '18px sans-serif';
            tctx.fillText('SPECIAL PAUS', 128, 150);

            return new THREE.CanvasTexture(tc);
        }

        // Green Jute Twine Rope Texture for Sutli Bomb
        function createJuteTexture() {
            const tc = document.createElement('canvas');
            tc.width = 256; tc.height = 256;
            const tctx = tc.getContext('2d');
            tctx.fillStyle = '#22543d';
            tctx.fillRect(0, 0, 256, 256);

            // Jute threads pattern
            tctx.strokeStyle = '#276749';
            tctx.lineWidth = 4;
            for (let i = -256; i < 512; i += 12) {
                tctx.beginPath(); tctx.moveTo(i, 0); tctx.lineTo(i + 256, 256); tctx.stroke();
                tctx.beginPath(); tctx.moveTo(i, 256); tctx.lineTo(i + 256, 0); tctx.stroke();
            }
            tctx.strokeStyle = '#ecc94b';
            tctx.lineWidth = 2;
            for (let i = 0; i < 256; i += 24) {
                tctx.strokeRect(i, 0, 12, 256);
            }
            return new THREE.CanvasTexture(tc);
        }

        // Swirling Spiral Chakra Texture
        function createChakraTexture() {
            const tc = document.createElement('canvas');
            tc.width = 256; tc.height = 256;
            const tctx = tc.getContext('2d');
            const cx = 128, cy = 128;
            tctx.fillStyle = '#ef4444';
            tctx.fillRect(0, 0, 256, 256);

            // Swirl spiral arms
            tctx.lineWidth = 12;
            for (let i = 0; i < 6; i++) {
                tctx.strokeStyle = (i % 2 === 0) ? '#39ff14' : '#ffd700';
                tctx.beginPath();
                for (let a = 0; a < Math.PI * 2; a += 0.1) {
                    const r = a * 18;
                    const x = cx + Math.cos(a + (i * Math.PI / 3)) * r;
                    const y = cy + Math.sin(a + (i * Math.PI / 3)) * r;
                    if (a === 0) tctx.moveTo(x, y); else tctx.lineTo(x, y);
                }
                tctx.stroke();
            }

            // Center gold circle
            tctx.fillStyle = '#ffd700';
            tctx.beginPath(); tctx.arc(cx, cy, 25, 0, Math.PI * 2); tctx.fill();
            tctx.fillStyle = '#000';
            tctx.beginPath(); tctx.arc(cx, cy, 8, 0, Math.PI * 2); tctx.fill();

            return new THREE.CanvasTexture(tc);
        }

        // Particle Glow Texture (Soft spherical light)
        function createParticleGlowTexture() {
            const tc = document.createElement('canvas');
            tc.width = 64; tc.height = 64;
            const tctx = tc.getContext('2d');
            const grad = tctx.createRadialGradient(32, 32, 0, 32, 32, 32);
            grad.addColorStop(0, 'rgba(255, 255, 255, 1)');
            grad.addColorStop(0.2, 'rgba(255, 230, 150, 0.9)');
            grad.addColorStop(0.6, 'rgba(255, 100, 20, 0.4)');
            grad.addColorStop(1, 'rgba(0, 0, 0, 0)');
            tctx.fillStyle = grad;
            tctx.fillRect(0, 0, 64, 64);
            return new THREE.CanvasTexture(tc);
        }
        const particleTexture = createParticleGlowTexture();

        // ========================================================
        // 5. THREE.JS 3D SCENE SETUP & ENGINE (HARDWARE-ACCELERATED)
        // ========================================================
        const canvas = document.getElementById('threeCanvas');
        const stageBox = document.getElementById('stageBox');

        const scene = new THREE.Scene();
        scene.fog = new THREE.FogExp2(0x11051e, 0.025);

        const camera = new THREE.PerspectiveCamera(45, 1, 0.1, 100);
        camera.position.set(0, 3.8, 8.5);
        camera.lookAt(0, 1.0, 0);

        const renderer = new THREE.WebGLRenderer({
            canvas: canvas,
            antialias: true,
            alpha: false,
            powerPreference: 'high-performance'
        });
        renderer.setPixelRatio(Math.min(window.devicePixelRatio, 1.5));
        renderer.toneMapping = THREE.ACESFilmicToneMapping;
        renderer.toneMappingExposure = 1.1;

        // Ground Floor with Glowing Rangoli Texture
        const floorGeo = new THREE.PlaneGeometry(16, 16);
        const rangoliTex = createRangoliTexture();
        const floorMat = new THREE.MeshStandardMaterial({
            map: rangoliTex,
            roughness: 0.4,
            metalness: 0.2
        });
        const floorMesh = new THREE.Mesh(floorGeo, floorMat);
        floorMesh.rotation.x = -Math.PI / 2;
        floorMesh.position.y = 0;
        scene.add(floorMesh);

        // Ambient & Directional Scene Lighting
        const ambLight = new THREE.AmbientLight(0xffeedd, 0.85);
        scene.add(ambLight);

        const dirLight = new THREE.DirectionalLight(0xffe6a3, 1.2);
        dirLight.position.set(4, 8, 5);
        scene.add(dirLight);

        // Cracker Dynamic Point Light (Flickers during firing)
        const crackerLight = new THREE.PointLight(0xffa500, 0, 15);
        crackerLight.position.set(0, 1.5, 0);
        scene.add(crackerLight);

        function resizeThree() {
            const w = stageBox.clientWidth;
            const h = stageBox.clientHeight;
            camera.aspect = w / h;
            camera.updateProjectionMatrix();
            renderer.setSize(w, h);
        }
        window.addEventListener('resize', resizeThree);
        resizeThree();

        // ========================================================
        // 6. HIGH-PERFORMANCE 3D PARTICLE SYSTEM (SINGLE DRAW CALL)
        // ========================================================
        const MAX_PARTICLES = 2500;
        const particleGeo = new THREE.BufferGeometry();
        const pPositions = new Float32Array(MAX_PARTICLES * 3);
        const pColors = new Float32Array(MAX_PARTICLES * 3);
        const pSizes = new Float32Array(MAX_PARTICLES);

        particleGeo.setAttribute('position', new THREE.BufferAttribute(pPositions, 3));
        particleGeo.setAttribute('color', new THREE.BufferAttribute(pColors, 3));
        particleGeo.setAttribute('size', new THREE.BufferAttribute(pSizes, 1));

        const particleMat = new THREE.PointsMaterial({
            size: 0.35,
            vertexColors: true,
            map: particleTexture,
            transparent: true,
            blending: THREE.AdditiveBlending,
            depthWrite: false
        });

        const particleSystem = new THREE.Points(particleGeo, particleMat);
        scene.add(particleSystem);

        // Active particles pool
        let activeParticles = [];

        function spawnParticle(x, y, z, vx, vy, vz, colorHex, size = 0.35, gravity = 0.08, decay = 0.02) {
            if (activeParticles.length >= MAX_PARTICLES) return;
            const c = new THREE.Color(colorHex);
            activeParticles.push({
                x, y, z, vx, vy, vz,
                r: c.r, g: c.g, b: c.b,
                size, gravity, decay,
                life: 1.0
            });
        }

        function clearAllParticles() {
            activeParticles = [];
            for (let i = 0; i < MAX_PARTICLES; i++) {
                pPositions[i * 3 + 1] = -999;
                pSizes[i] = 0;
            }
            particleGeo.attributes.position.needsUpdate = true;
            particleGeo.attributes.size.needsUpdate = true;
        }

        // ========================================================
        // 7. CRACKER STATE & 3D MODEL BUILDER (STRICT CLEANUP)
        // ========================================================
        let currentCracker = 'anar';
        let isBurning = false;
        let activeTimerIds = [];
        let currentModelGroup = new THREE.Group();
        scene.add(currentModelGroup);

        // Stick (Phuljhadi) interactive drag variables
        let stickTargetPos = new THREE.Vector3(0, 1.8, 0);
        let isDraggingStick = false;

        function clearActiveTimers() {
            for (let id of activeTimerIds) {
                clearInterval(id);
                clearTimeout(id);
            }
            activeTimerIds = [];
        }

        function build3DModel(type) {
            // Clean previous model
            while (currentModelGroup.children.length > 0) {
                const obj = currentModelGroup.children[0];
                currentModelGroup.remove(obj);
                if (obj.geometry) obj.geometry.dispose();
                if (obj.material) {
                    if (Array.isArray(obj.material)) obj.material.forEach(m => m.dispose());
                    else obj.material.dispose();
                }
            }

            crackerLight.intensity = 0;
            const dragHint = document.getElementById('dragHint');
            dragHint.style.display = (type === 'stick') ? 'flex' : 'none';

            if (type === 'anar') {
                // Terracotta / Gold Paus Cone
                const coneGeo = new THREE.CylinderGeometry(0.18, 0.85, 1.8, 32);
                const pausTex = createPausTexture();
                const coneMat = new THREE.MeshStandardMaterial({
                    map: pausTex,
                    roughness: 0.35,
                    metalness: 0.4
                });
                const cone = new THREE.Mesh(coneGeo, coneMat);
                cone.position.set(0, 0.9, 0);
                currentModelGroup.add(cone);

                // Base clay ring
                const baseGeo = new THREE.CylinderGeometry(0.95, 1.05, 0.22, 32);
                const baseMat = new THREE.MeshStandardMaterial({ color: 0x78350f, roughness: 0.8 });
                const baseMesh = new THREE.Mesh(baseGeo, baseMat);
                baseMesh.position.set(0, 0.11, 0);
                currentModelGroup.add(baseMesh);

                // Top wick fuse
                const fuseGeo = new THREE.CylinderGeometry(0.02, 0.02, 0.35, 12);
                const fuseMat = new THREE.MeshStandardMaterial({ color: 0xf3f4f6 });
                const fuseMesh = new THREE.Mesh(fuseGeo, fuseMat);
                fuseMesh.position.set(0, 1.95, 0);
                currentModelGroup.add(fuseMesh);
            }
            else if (type === 'chakri') {
                // Ground Spinner Bhuichakra
                const chakraGeo = new THREE.CylinderGeometry(1.2, 1.2, 0.22, 36);
                const chakraTex = createChakraTexture();
                const chakraMat = [
                    new THREE.MeshStandardMaterial({ color: 0xb91c1c }), // side
                    new THREE.MeshStandardMaterial({ map: chakraTex, roughness: 0.3, metalness: 0.5 }), // top
                    new THREE.MeshStandardMaterial({ color: 0x78350f }) // bottom
                ];
                const chakraMesh = new THREE.Mesh(chakraGeo, chakraMat);
                chakraMesh.position.set(0, 0.11, 0);
                chakraMesh.name = 'chakraWheel';
                currentModelGroup.add(chakraMesh);
            }
            else if (type === 'stick') {
                // Phuljhadi Stick Sparkler
                stickTargetPos.set(0, 1.8, 0);

                const stickGeo = new THREE.CylinderGeometry(0.025, 0.025, 3.2, 16);
                const stickMat = new THREE.MeshStandardMaterial({ color: 0xd1d5db, metalness: 0.9, roughness: 0.2 });
                const stickMesh = new THREE.Mesh(stickGeo, stickMat);

                // Grey pyrotechnic chemical coating
                const coatGeo = new THREE.CylinderGeometry(0.065, 0.065, 1.8, 16);
                const coatMat = new THREE.MeshStandardMaterial({ color: 0x9ca3af, roughness: 0.7 });
                const coatMesh = new THREE.Mesh(coatGeo, coatMat);
                coatMesh.position.set(0, 0.65, 0);
                stickMesh.add(coatMesh);

                stickMesh.rotation.z = Math.PI / 6;
                stickMesh.position.copy(stickTargetPos);
                stickMesh.name = 'stickMesh';
                currentModelGroup.add(stickMesh);
            }
            else if (type === 'rocket') {
                // Glass Launch Bottle + Wooden Stick & Red Rocket
                const bottleGeo = new THREE.CylinderGeometry(0.35, 0.45, 1.8, 24);
                const bottleMat = new THREE.MeshPhysicalMaterial({
                    color: 0x38bdf8,
                    transparent: true,
                    opacity: 0.55,
                    roughness: 0.1,
                    transmission: 0.7
                });
                const bottleMesh = new THREE.Mesh(bottleGeo, bottleMat);
                bottleMesh.position.set(0, 0.9, 0);
                currentModelGroup.add(bottleMesh);

                const rocketGroup = new THREE.Group();
                rocketGroup.name = 'rocketBody';

                // Bamboo stick
                const stickGeo = new THREE.CylinderGeometry(0.03, 0.03, 3.4, 8);
                const stickMat = new THREE.MeshStandardMaterial({ color: 0xd97706 });
                const stickMesh = new THREE.Mesh(stickGeo, stickMat);
                stickMesh.position.set(0.12, 1.4, 0);
                rocketGroup.add(stickMesh);

                // Red Cylindrical Body
                const bodyGeo = new THREE.CylinderGeometry(0.16, 0.16, 1.1, 24);
                const bodyMat = new THREE.MeshStandardMaterial({ color: 0xdc2626, metalness: 0.4, roughness: 0.3 });
                const bodyMesh = new THREE.Mesh(bodyGeo, bodyMat);
                bodyMesh.position.set(0, 2.3, 0);
                rocketGroup.add(bodyMesh);

                // Golden Nose Cone
                const coneGeo = new THREE.ConeGeometry(0.22, 0.5, 24);
                const coneMat = new THREE.MeshStandardMaterial({ color: 0xffd700, metalness: 0.8, roughness: 0.2 });
                const coneMesh = new THREE.Mesh(coneGeo, coneMat);
                coneMesh.position.set(0, 3.05, 0);
                rocketGroup.add(coneMesh);

                currentModelGroup.add(rocketGroup);
            }
            else if (type === 'bomb') {
                // Sutli Bomb (Jute wrapped cylinder block)
                const bombGeo = new THREE.CylinderGeometry(0.7, 0.7, 1.1, 24);
                const juteTex = createJuteTexture();
                const bombMat = new THREE.MeshStandardMaterial({ map: juteTex, roughness: 0.9 });
                const bombMesh = new THREE.Mesh(bombGeo, bombMat);
                bombMesh.position.set(0, 0.55, 0);
                bombMesh.name = 'bombMesh';
                currentModelGroup.add(bombMesh);

                // White Fuse cord
                const fuseGeo = new THREE.CylinderGeometry(0.03, 0.03, 0.5, 12);
                const fuseMat = new THREE.MeshStandardMaterial({ color: 0xffffff });
                const fuseMesh = new THREE.Mesh(fuseGeo, fuseMat);
                fuseMesh.position.set(0.12, 1.3, 0);
                fuseMesh.rotation.z = -Math.PI / 8;
                fuseMesh.name = 'bombFuse';
                currentModelGroup.add(fuseMesh);
            }
            else if (type === 'ladi') {
                // 1000 Lavangi Ladi (Red string garland on floor)
                const ladiGroup = new THREE.Group();
                ladiGroup.name = 'ladiGroup';

                for (let i = 0; i < 20; i++) {
                    const lx = -2.2 + (i * 0.23);
                    const lz = Math.sin(i * 0.6) * 0.25;

                    const miniGeo = new THREE.CylinderGeometry(0.065, 0.065, 0.32, 12);
                    const miniMat = new THREE.MeshStandardMaterial({ color: 0xef4444, metalness: 0.3 });
                    const miniMesh = new THREE.Mesh(miniGeo, miniMat);
                    miniMesh.rotation.x = Math.PI / 2;
                    miniMesh.position.set(lx, 0.07, lz);
                    miniMesh.name = `ladi_${i}`;
                    ladiGroup.add(miniMesh);
                }
                currentModelGroup.add(ladiGroup);
            }
            else if (type === 'snake') {
                // Black Snake Tablet
                const tabGeo = new THREE.CylinderGeometry(0.55, 0.55, 0.22, 24);
                const tabMat = new THREE.MeshStandardMaterial({ color: 0x1e293b, roughness: 0.95 });
                const tabMesh = new THREE.Mesh(tabGeo, tabMat);
                tabMesh.position.set(0, 0.11, 0);
                tabMesh.name = 'snakeTab';
                currentModelGroup.add(tabMesh);
            }
            else if (type === 'skyshot') {
                // 7-Shot Launcher Mortar Tube
                const tubeGeo = new THREE.CylinderGeometry(0.38, 0.38, 1.6, 24);
                const tubeMat = new THREE.MeshStandardMaterial({ color: 0x0284c7, metalness: 0.6, roughness: 0.3 });
                const tubeMesh = new THREE.Mesh(tubeGeo, tubeMat);
                tubeMesh.position.set(0, 0.8, 0);
                currentModelGroup.add(tubeMesh);

                // Heavy base plate
                const plateGeo = new THREE.BoxGeometry(1.2, 0.15, 1.2);
                const plateMat = new THREE.MeshStandardMaterial({ color: 0x334155, metalness: 0.8 });
                const plateMesh = new THREE.Mesh(plateGeo, plateMat);
                plateMesh.position.set(0, 0.075, 0);
                currentModelGroup.add(plateMesh);
            }
        }

        function selectCracker(type) {
            if (isBurning) {
                resetCracker();
            }
            currentCracker = type;

            document.querySelectorAll('.cracker-card').forEach(c => c.classList.remove('active'));
            const target = Array.from(document.querySelectorAll('.cracker-card')).find(c => c.getAttribute('onclick')?.includes(type));
            if (target) target.classList.add('active');

            applyTranslations();
            build3DModel(type);
        }

        function resetCracker() {
            clearActiveTimers();
            clearAllParticles();
            isBurning = false;
            updateStatusText();
            build3DModel(currentCracker);
        }

        // ========================================================
        // 8. CRACKER IGNITION & ACCURATE 3D PHYSICS SIMULATION
        // ========================================================
        function igniteCracker() {
            if (isBurning) return;
            isBurning = true;
            updateStatusText();
            sfx.playFuse();

            if (currentCracker === 'anar') {
                // Paus Spark Fountain (Accurate Parabolic Gravity)
                let frame = 0;
                crackerLight.color.setHex(0xffaa00);
                const timer = setInterval(() => {
                    frame++;
                    if (frame % 3 === 0) sfx.playCrackle();
                    crackerLight.intensity = 2.5 + Math.random() * 2.0;

                    // 12 Sparks per interval shooting upwards
                    for (let i = 0; i < 12; i++) {
                        const angle = Math.random() * Math.PI * 2;
                        const spread = Math.random() * 0.16;
                        const vy = 0.28 + Math.random() * 0.25;
                        spawnParticle(
                            (Math.random() - 0.5) * 0.1,
                            1.9,
                            (Math.random() - 0.5) * 0.1,
                            Math.cos(angle) * spread,
                            vy,
                            Math.sin(angle) * spread,
                            (Math.random() > 0.4) ? 0xffd700 : 0xffffff,
                            0.4,
                            0.012, // gentle gravity
                            0.02
                        );
                    }

                    if (frame > 140) {
                        clearInterval(timer);
                        setTimeout(resetCracker, 1400);
                    }
                }, 25);
                activeTimerIds.push(timer);
            }
            else if (currentCracker === 'chakri') {
                // Bhuichakra Spinner (Spins on Y, Sparks tangentially from edge)
                const wheel = currentModelGroup.getObjectByName('chakraWheel');
                let frame = 0;
                crackerLight.color.setHex(0x39ff14);

                const timer = setInterval(() => {
                    frame++;
                    if (wheel) wheel.rotation.y += 0.55;
                    if (frame % 4 === 0) sfx.playWhirr();
                    crackerLight.intensity = 1.8 + Math.random() * 1.5;

                    // Tangential sparks from wheel rim
                    for (let i = 0; i < 8; i++) {
                        const a = (wheel ? wheel.rotation.y : 0) + (i * Math.PI / 4);
                        const r = 1.15;
                        const spd = 0.18 + Math.random() * 0.12;
                        spawnParticle(
                            Math.cos(a) * r,
                            0.12,
                            Math.sin(a) * r,
                            -Math.sin(a) * spd, // Tangent X
                            0.02 + Math.random() * 0.04,
                            Math.cos(a) * spd,  // Tangent Z
                            (i % 2 === 0) ? 0x39ff14 : 0xffd700,
                            0.38,
                            0.005,
                            0.035
                        );
                    }

                    if (frame > 150) {
                        clearInterval(timer);
                        setTimeout(resetCracker, 1000);
                    }
                }, 25);
                activeTimerIds.push(timer);
            }
            else if (currentCracker === 'stick') {
                // Phuljhadi Stick Sizzler (Follows Stick Mesh tip)
                let frame = 0;
                crackerLight.color.setHex(0xffea00);

                const timer = setInterval(() => {
                    frame++;
                    if (frame % 3 === 0) sfx.playCrackle();
                    const stickMesh = currentModelGroup.getObjectByName('stickMesh');
                    let tipX = 0.6, tipY = 2.4, tipZ = 0;
                    if (stickMesh) {
                        tipX = stickMesh.position.x + 0.6;
                        tipY = stickMesh.position.y + 0.6;
                        tipZ = stickMesh.position.z;
                        crackerLight.position.set(tipX, tipY, tipZ);
                    }
                    crackerLight.intensity = 1.8 + Math.random() * 1.2;

                    // Radial star sparks
                    for (let i = 0; i < 10; i++) {
                        const theta = Math.random() * Math.PI * 2;
                        const phi = Math.random() * Math.PI;
                        const spd = 0.12 + Math.random() * 0.15;
                        spawnParticle(
                            tipX, tipY, tipZ,
                            Math.sin(phi) * Math.cos(theta) * spd,
                            Math.sin(phi) * Math.sin(theta) * spd,
                            Math.cos(phi) * spd,
                            (Math.random() > 0.3) ? 0xffea00 : 0xffffff,
                            0.35,
                            0.008,
                            0.045
                        );
                    }

                    if (frame > 200) {
                        clearInterval(timer);
                        setTimeout(resetCracker, 1000);
                    }
                }, 25);
                activeTimerIds.push(timer);
            }
            else if (currentCracker === 'rocket') {
                // Sky Rocket Ascent & Aerial Starburst
                const rocket = currentModelGroup.getObjectByName('rocketBody');
                sfx.playWhoosh();
                crackerLight.color.setHex(0xff5500);

                let ascentY = 0;
                let vy = 0.05;
                const timer = setInterval(() => {
                    vy += 0.02;
                    ascentY += vy;
                    if (rocket) rocket.position.y = ascentY;

                    // Rocket exhaust smoke & fire trail
                    spawnParticle(
                        (Math.random() - 0.5) * 0.1,
                        ascentY + 2.0,
                        (Math.random() - 0.5) * 0.1,
                        (Math.random() - 0.5) * 0.03,
                        -0.12,
                        (Math.random() - 0.5) * 0.03,
                        0xff6600,
                        0.32,
                        0.002,
                        0.06
                    );

                    if (ascentY >= 9.5) {
                        clearInterval(timer);
                        if (rocket) rocket.visible = false;
                        sfx.playAerialBurst();

                        // Giant Spherical Sky Burst
                        const colors = [0xffd700, 0xef4444, 0x39ff14, 0x38bdf8, 0xff00cc];
                        for (let i = 0; i < 160; i++) {
                            const theta = Math.random() * Math.PI * 2;
                            const phi = Math.random() * Math.PI;
                            const spd = 0.2 + Math.random() * 0.35;
                            const c = colors[Math.floor(Math.random() * colors.length)];
                            spawnParticle(
                                0, 11.5, 0,
                                Math.sin(phi) * Math.cos(theta) * spd,
                                Math.sin(phi) * Math.sin(theta) * spd,
                                Math.cos(phi) * spd,
                                c,
                                0.45,
                                0.007,
                                0.018
                            );
                        }
                        setTimeout(resetCracker, 1600);
                    }
                }, 25);
                activeTimerIds.push(timer);
            }
            else if (currentCracker === 'bomb') {
                // Sutli Bomb (Fuse burns -> Box Shake + Sub-bass Boom!)
                const fuse = currentModelGroup.getObjectByName('bombFuse');
                let count = 0;

                const timer = setInterval(() => {
                    count++;
                    sfx.playFuse();
                    // Spark on fuse tip
                    spawnParticle(
                        0.12, 1.45, 0,
                        (Math.random() - 0.5) * 0.06,
                        (Math.random() - 0.5) * 0.06,
                        (Math.random() - 0.5) * 0.06,
                        0xff4500,
                        0.3,
                        0,
                        0.08
                    );

                    if (count > 30) {
                        clearInterval(timer);
                        sfx.playBombBang();

                        // Blinding light flash
                        crackerLight.color.setHex(0xffffff);
                        crackerLight.intensity = 12;
                        setTimeout(() => crackerLight.intensity = 0, 120);

                        // Trigger box shake animation
                        stageBox.classList.add('shake-box');
                        setTimeout(() => stageBox.classList.remove('shake-box'), 450);

                        // Remove bomb mesh
                        const bomb = currentModelGroup.getObjectByName('bombMesh');
                        if (bomb) bomb.visible = false;
                        if (fuse) fuse.visible = false;

                        // Massive debris & smoke cloud
                        for (let i = 0; i < 180; i++) {
                            const theta = Math.random() * Math.PI * 2;
                            const phi = Math.random() * Math.PI;
                            const spd = 0.25 + Math.random() * 0.45;
                            spawnParticle(
                                0, 0.6, 0,
                                Math.sin(phi) * Math.cos(theta) * spd,
                                Math.abs(Math.sin(phi) * Math.sin(theta) * spd),
                                Math.cos(phi) * spd,
                                (Math.random() > 0.5) ? 0x22543d : 0xf59e0b,
                                0.42,
                                0.015,
                                0.02
                            );
                        }
                        setTimeout(resetCracker, 1600);
                    }
                }, 30);
                activeTimerIds.push(timer);
            }
            else if (currentCracker === 'ladi') {
                // Lavangi 1000-Ladi (Sequential machine-gun bursts along fuse)
                const ladiGroup = currentModelGroup.getObjectByName('ladiGroup');
                let curIdx = 0;

                const timer = setInterval(() => {
                    if (ladiGroup && curIdx < 20) {
                        const mini = ladiGroup.getObjectByName(`ladi_${curIdx}`);
                        if (mini) mini.visible = false;
                        sfx.playPop();

                        const lx = -2.2 + (curIdx * 0.23);
                        crackerLight.position.set(lx, 0.2, 0);
                        crackerLight.intensity = 2.5;
                        setTimeout(() => crackerLight.intensity = 0, 50);

                        for (let i = 0; i < 22; i++) {
                            const a = Math.random() * Math.PI * 2;
                            const spd = 0.1 + Math.random() * 0.18;
                            spawnParticle(
                                lx, 0.1, 0,
                                Math.cos(a) * spd,
                                0.08 + Math.random() * 0.12,
                                Math.sin(a) * spd,
                                (i % 2 === 0) ? 0xef4444 : 0xffd700,
                                0.35,
                                0.01,
                                0.04
                            );
                        }
                        curIdx++;
                    } else {
                        clearInterval(timer);
                        sfx.playBombBang();
                        setTimeout(resetCracker, 1400);
                    }
                }, 130);
                activeTimerIds.push(timer);
            }
            else if (currentCracker === 'snake') {
                // Black Snake Tablet (Organic rising ash segments)
                let count = 0;
                let sy = 0.15;
                let sx = 0, sz = 0;

                const timer = setInterval(() => {
                    count++;
                    sfx.playFuse();
                    sy += 0.04 + Math.random() * 0.03;
                    sx += (Math.random() - 0.5) * 0.06;
                    sz += (Math.random() - 0.5) * 0.06;

                    // 3D Ash segment mesh
                    const segGeo = new THREE.SphereGeometry(0.12 + Math.random() * 0.06, 8, 8);
                    const segMat = new THREE.MeshStandardMaterial({ color: 0x334155, roughness: 1.0 });
                    const segMesh = new THREE.Mesh(segGeo, segMat);
                    segMesh.position.set(sx, sy, sz);
                    currentModelGroup.add(segMesh);

                    // Glowing ember particles on snake head
                    for (let i = 0; i < 3; i++) {
                        spawnParticle(
                            sx, sy, sz,
                            (Math.random() - 0.5) * 0.02,
                            0.03,
                            (Math.random() - 0.5) * 0.02,
                            0xff4500,
                            0.25,
                            0.002,
                            0.07
                        );
                    }

                    if (count > 55) {
                        clearInterval(timer);
                        setTimeout(resetCracker, 2200);
                    }
                }, 40);
                activeTimerIds.push(timer);
            }
            else if (currentCracker === 'skyshot') {
                // 7-Color Aerial Sky Shots (7 successive shell bursts)
                let shot = 0;
                const colors = [0xffd700, 0xef4444, 0x10b981, 0x3b82f6, 0xa855f7, 0xf97316, 0xffffff];

                const timer = setInterval(() => {
                    if (shot < 7) {
                        sfx.playPop(); // Launch thud
                        const shellColor = colors[shot];
                        shot++;

                        // Shell ascending streak
                        let shellY = 1.0;
                        const ascentTimer = setInterval(() => {
                            shellY += 0.45;
                            spawnParticle(0, shellY, 0, 0, -0.05, 0, shellColor, 0.35, 0.002, 0.08);

                            if (shellY >= 10.5) {
                                clearInterval(ascentTimer);
                                sfx.playAerialBurst();

                                // Chrysanthemum burst
                                for (let i = 0; i < 90; i++) {
                                    const theta = Math.random() * Math.PI * 2;
                                    const phi = Math.random() * Math.PI;
                                    const spd = 0.18 + Math.random() * 0.28;
                                    spawnParticle(
                                        0, 10.5, 0,
                                        Math.sin(phi) * Math.cos(theta) * spd,
                                        Math.sin(phi) * Math.sin(theta) * spd,
                                        Math.cos(phi) * spd,
                                        shellColor,
                                        0.45,
                                        0.008,
                                        0.02
                                    );
                                }
                            }
                        }, 25);
                    } else {
                        clearInterval(timer);
                        setTimeout(resetCracker, 2200);
                    }
                }, 750);
                activeTimerIds.push(timer);
            }
        }

        // ========================================================
        // 9. ANIMATION LOOP & INTERACTIVE DRAG (60 FPS BUTTER SMOOTH)
        // ========================================================
        function animate() {
            requestAnimationFrame(animate);

            // Update stick lerp position if stick active
            if (currentCracker === 'stick') {
                const stick = currentModelGroup.getObjectByName('stickMesh');
                if (stick) {
                    stick.position.lerp(stickTargetPos, 0.15);
                }
            }

            // Update Particle System Buffers
            let writeIdx = 0;
            for (let i = activeParticles.length - 1; i >= 0; i--) {
                const p = activeParticles[i];
                p.x += p.vx;
                p.y += p.vy;
                p.z += p.vz;
                p.vy -= p.gravity;
                p.life -= p.decay;

                if (p.life <= 0) {
                    activeParticles.splice(i, 1);
                    continue;
                }

                pPositions[writeIdx * 3] = p.x;
                pPositions[writeIdx * 3 + 1] = p.y;
                pPositions[writeIdx * 3 + 2] = p.z;

                pColors[writeIdx * 3] = p.r * p.life;
                pColors[writeIdx * 3 + 1] = p.g * p.life;
                pColors[writeIdx * 3 + 2] = p.b * p.life;

                pSizes[writeIdx] = p.size * (0.4 + p.life * 0.6);
                writeIdx++;
            }

            // Clear remaining inactive points in buffer
            for (let j = writeIdx; j < MAX_PARTICLES; j++) {
                pPositions[j * 3 + 1] = -999;
                pSizes[j] = 0;
            }

            particleGeo.attributes.position.needsUpdate = true;
            particleGeo.attributes.color.needsUpdate = true;
            particleGeo.attributes.size.needsUpdate = true;

            renderer.render(scene, camera);
        }

        // Phuljhadi Stick Interactive Drag Controller
        function updateStickPointer(e) {
            if (currentCracker !== 'stick') return;
            const rect = canvas.getBoundingClientRect();
            const clientX = e.touches ? e.touches[0].clientX : e.clientX;
            const clientY = e.touches ? e.touches[0].clientY : e.clientY;

            const ndcX = ((clientX - rect.left) / rect.width) * 2 - 1;
            const ndcY = -(((clientY - rect.top) / rect.height) * 2 - 1);

            // Project to 3D plane at z = 0
            stickTargetPos.x = ndcX * 3.2;
            stickTargetPos.y = Math.max(0.6, ndcY * 2.2 + 2.0);
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

        // Action Buttons Event Listeners
        document.getElementById('btnIgnite').addEventListener('click', igniteCracker);
        document.getElementById('btnReset').addEventListener('click', resetCracker);

        // Initial Setup
        applyTranslations();
        build3DModel(currentCracker);
        animate();
    </script>
</body>
</html>
'''

with open('/data/data/com.termux/files/home/diwali_website/index.html', 'w', encoding='utf-8') as f:
    f.write(html_content)

print("Generated index.html successfully with length:", len(html_content))
