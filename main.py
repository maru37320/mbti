import streamlit as st
import random

# 1. 페이지 설정
st.set_page_config(
    page_title="🏮 이자카야 MBTI 저녁 추천 🍶",
    page_icon="🏮",
    layout="centered"
)

# 2. 초화려 이자카야 배경 🎆🏮🎋
st.markdown("""
<style>
/* ===== 밤하늘 배경 (그라데이션 + 보름달) ===== */
.stApp {
    background: 
        radial-gradient(circle at 85% 12%, rgba(255, 240, 180, 0.15) 0%, transparent 8%),
        radial-gradient(circle at 85% 12%, #fff4c4 0%, #f5d76e 3%, transparent 4%),
        radial-gradient(ellipse at top, #3d2466 0%, #1a1a3e 40%, #0a0a1e 100%);
    background-attachment: fixed;
    color: #f5e6d3 !important;
    overflow-x: hidden;
}

/* ===== 멀리 보이는 후지산 실루엣 🗻 ===== */
.mountain {
    position: fixed;
    bottom: 38%;
    left: 50%;
    transform: translateX(-50%);
    width: 0;
    height: 0;
    border-left: 200px solid transparent;
    border-right: 200px solid transparent;
    border-bottom: 150px solid #1a1535;
    z-index: -3;
    opacity: 0.6;
    filter: drop-shadow(0 0 20px rgba(100, 80, 150, 0.4));
}
.mountain::before {
    content: "";
    position: absolute;
    top: 20px;
    left: -40px;
    width: 80px;
    height: 30px;
    background: rgba(255, 255, 255, 0.4);
    clip-path: polygon(0 100%, 20% 60%, 40% 80%, 60% 50%, 80% 70%, 100% 100%);
}

/* ===== 멀리 보이는 도시 실루엣 (왼쪽) ===== */
.city-left {
    position: fixed;
    bottom: 38%;
    left: 0;
    width: 30%;
    height: 100px;
    background: 
        linear-gradient(90deg,
            #0f0a25 0px, #0f0a25 30px, transparent 30px, transparent 35px,
            #0f0a25 35px, #0f0a25 80px, transparent 80px, transparent 88px,
            #0f0a25 88px, #0f0a25 120px, transparent 120px, transparent 130px,
            #0f0a25 130px, #0f0a25 170px, transparent 170px, transparent 178px,
            #0f0a25 178px, #0f0a25 220px, transparent 220px, transparent 230px,
            #0f0a25 230px, #0f0a25 280px);
    z-index: -3;
    opacity: 0.8;
    mask: linear-gradient(180deg, transparent 0%, black 30%);
    -webkit-mask: linear-gradient(180deg, transparent 0%, black 30%);
}

/* 도시 (오른쪽) */
.city-right {
    position: fixed;
    bottom: 38%;
    right: 0;
    width: 30%;
    height: 100px;
    background: 
        linear-gradient(90deg,
            #0f0a25 0px, #0f0a25 40px, transparent 40px, transparent 50px,
            #0f0a25 50px, #0f0a25 95px, transparent 95px, transparent 105px,
            #0f0a25 105px, #0f0a25 145px, transparent 145px, transparent 155px,
            #0f0a25 155px, #0f0a25 200px, transparent 200px, transparent 210px,
            #0f0a25 210px, #0f0a25 260px);
    z-index: -3;
    opacity: 0.8;
}

/* ===== 폭죽 (밤하늘 불꽃놀이) 🎆 ===== */
.firework {
    position: fixed;
    width: 4px;
    height: 4px;
    border-radius: 50%;
    z-index: -2;
    animation: explode 3s ease-out infinite;
}
@keyframes explode {
    0% { transform: scale(0); opacity: 1; box-shadow: 0 0 0 0 transparent; }
    50% { 
        transform: scale(1); 
        opacity: 1;
        box-shadow: 
            0 -40px 0 #ff6b9d, 0 40px 0 #ff6b9d,
            40px 0 0 #ff6b9d, -40px 0 0 #ff6b9d,
            28px -28px 0 #ffd93d, -28px -28px 0 #ffd93d,
            28px 28px 0 #ffd93d, -28px 28px 0 #ffd93d,
            0 -60px 0 #6bcf7f, 0 60px 0 #6bcf7f,
            60px 0 0 #6bcf7f, -60px 0 0 #6bcf7f;
    }
    100% { transform: scale(1.5); opacity: 0; }
}
.firework-1 { top: 8%; left: 15%; animation-delay: 0s; }
.firework-2 { top: 12%; right: 20%; animation-delay: 1.5s; }
.firework-3 { top: 18%; left: 45%; animation-delay: 2.8s; }

/* ===== 기와 지붕 (더 화려하게) ===== */
.roof {
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    height: 110px;
    z-index: -2;
}
.roof-top {
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 35px;
    background: linear-gradient(180deg, #0a0408 0%, #3d1f1f 100%);
    box-shadow: 0 2px 8px rgba(0,0,0,0.6);
}
/* 지붕 위 황금 장식 (시비) */
.roof-top::before, .roof-top::after {
    content: "";
    position: absolute;
    top: -15px;
    width: 25px;
    height: 35px;
    background: linear-gradient(180deg, #ffd700 0%, #b8860b 100%);
    clip-path: polygon(50% 0%, 100% 50%, 80% 100%, 20% 100%, 0% 50%);
    box-shadow: 0 0 15px rgba(255, 215, 0, 0.6);
}
.roof-top::before { left: 10%; }
.roof-top::after { right: 10%; }

.roof-tiles {
    position: absolute;
    top: 35px;
    left: 0;
    width: 100%;
    height: 45px;
    background: 
        radial-gradient(circle at 20px 45px, #4a2424 0px, #4a2424 18px, transparent 19px),
        radial-gradient(circle at 60px 45px, #4a2424 0px, #4a2424 18px, transparent 19px),
        radial-gradient(circle at 100px 45px, #4a2424 0px, #4a2424 18px, transparent 19px),
        linear-gradient(180deg, #6b2c2c 0%, #3d1f1f 100%);
    background-size: 40px 45px, 40px 45px, 40px 45px, 100% 100%;
    box-shadow: 0 4px 15px rgba(0,0,0,0.6);
}
.roof-bottom {
    position: absolute;
    top: 80px;
    left: 0;
    width: 100%;
    height: 25px;
    background: 
        repeating-linear-gradient(90deg, 
            #8b2c2c 0px, #8b2c2c 25px, 
            #d4af37 25px, #d4af37 28px,
            #8b2c2c 28px, #8b2c2c 53px,
            #1a0e08 53px, #1a0e08 55px);
    border-bottom: 4px solid #d4af37;
    box-shadow: 0 3px 12px rgba(0,0,0,0.5), 0 0 20px rgba(212, 175, 55, 0.3);
}

/* ===== 가게 벽 (나무 + 디테일) ===== */
.izakaya-wall {
    position: fixed;
    bottom: 0;
    left: 0;
    width: 100%;
    height: 40%;
    background: 
        repeating-linear-gradient(90deg,
            #3d2817 0px, #4a2f1c 70px,
            #3d2817 72px, #2a1810 74px, #3d2817 76px),
        linear-gradient(180deg, #3a2515 0%, #1a0e08 100%);
    z-index: -2;
    box-shadow: inset 0 15px 30px rgba(0,0,0,0.7);
}

/* 가게 벽 위 황금 띠 장식 */
.wall-trim {
    position: fixed;
    bottom: 40%;
    left: 0;
    width: 100%;
    height: 8px;
    background: linear-gradient(90deg, 
        #d4af37 0%, #ffd700 50%, #d4af37 100%);
    z-index: -1;
    box-shadow: 
        0 0 15px rgba(255, 215, 0, 0.5),
        0 2px 8px rgba(0,0,0,0.4);
}

/* ===== 일본식 격자창 (왼쪽 2개) ===== */
.window-l1, .window-l2, .window-r1, .window-r2 {
    position: fixed;
    bottom: 15%;
    width: 110px;
    height: 90px;
    background: 
        radial-gradient(ellipse at center,
            rgba(255, 220, 130, 0.6) 0%, 
            rgba(255, 150, 50, 0.3) 100%);
    border: 4px solid #2a1810;
    box-shadow: 
        0 0 35px rgba(255, 180, 80, 0.5),
        inset 0 0 25px rgba(255, 220, 130, 0.4);
    z-index: -2;
    animation: windowFlicker 4s ease-in-out infinite;
}
.window-l1 { left: 3%; }
.window-l2 { left: 17%; animation-delay: -1s; }
.window-r1 { right: 3%; animation-delay: -2s; }
.window-r2 { right: 17%; animation-delay: -3s; }

.window-l1::before, .window-l2::before, .window-r1::before, .window-r2::before {
    content: "";
    position: absolute;
    top: 0; left: 0;
    width: 100%; height: 100%;
    background: 
        linear-gradient(90deg, transparent 23%, #2a1810 23%, #2a1810 26%, transparent 26%,
                              transparent 48%, #2a1810 48%, #2a1810 51%, transparent 51%,
                              transparent 73%, #2a1810 73%, #2a1810 76%, transparent 76%),
        linear-gradient(0deg, transparent 30%, #2a1810 30%, #2a1810 33%, transparent 33%,
                              transparent 65%, #2a1810 65%, #2a1810 68%, transparent 68%);
}
/* 창문 안 사람 그림자 (특정 창에만) */
.window-l2::after, .window-r1::after {
    content: "";
    position: absolute;
    bottom: 10%;
    left: 50%;
    transform: translateX(-50%);
    width: 30px;
    height: 50px;
    background: rgba(0, 0, 0, 0.5);
    border-radius: 50% 50% 20% 20%;
}

@keyframes windowFlicker {
    0%, 100% { box-shadow: 0 0 35px rgba(255, 180, 80, 0.5), inset 0 0 25px rgba(255, 220, 130, 0.4); }
    50% { box-shadow: 0 0 45px rgba(255, 200, 100, 0.7), inset 0 0 30px rgba(255, 230, 150, 0.6); }
}

/* ===== 노렌 (입구 천) ===== */
.noren {
    position: fixed;
    bottom: 40%;
    left: 50%;
    transform: translateX(-50%);
    width: 340px;
    height: 80px;
    background: 
        linear-gradient(180deg, #a02020 0%, #6b1515 100%);
    z-index: -1;
    border-radius: 3px 3px 0 0;
    box-shadow: 
        0 5px 25px rgba(0,0,0,0.7),
        inset 0 -10px 20px rgba(0,0,0,0.4),
        0 0 30px rgba(160, 32, 32, 0.4);
    animation: norenSway 5s ease-in-out infinite;
    transform-origin: top center;
    border-top: 5px solid #d4af37;
}
.noren::before {
    content: "居 酒 屋";
    position: absolute;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);
    color: #f5e6d3;
    font-size: 30px;
    font-weight: bold;
    letter-spacing: 14px;
    text-shadow: 
        0 0 12px rgba(255,200,100,0.8),
        2px 2px 4px rgba(0,0,0,0.6);
}
.noren::after {
    content: "";
    position: absolute;
    top: 20%;
    left: 0;
    width: 100%;
    height: 80%;
    background: 
        linear-gradient(90deg, 
            transparent 19%, #1a0e08 19%, #1a0e08 21%, transparent 21%,
            transparent 39%, #1a0e08 39%, #1a0e08 41%, transparent 41%,
            transparent 59%, #1a0e08 59%, #1a0e08 61%, transparent 61%,
            transparent 79%, #1a0e08 79%, #1a0e08 81%, transparent 81%);
}
@keyframes norenSway {
    0%, 100% { transform: translateX(-50%) rotate(-1.5deg); }
    50% { transform: translateX(-50%) rotate(1.5deg); }
}

/* ===== 작은 사이드 노렌 (양옆) ===== */
.mini-noren-left, .mini-noren-right {
    position: fixed;
    bottom: 40%;
    width: 80px;
    height: 50px;
    background: linear-gradient(180deg, #1a4d8c 0%, #0d2e57 100%);
    z-index: -1;
    border-top: 3px solid #d4af37;
    box-shadow: 0 3px 12px rgba(0,0,0,0.5);
    animation: norenSway 6s ease-in-out infinite;
    transform-origin: top center;
}
.mini-noren-left { left: 32%; animation-delay: -1s; }
.mini-noren-right { right: 32%; animation-delay: -2s; }
.mini-noren-left::before, .mini-noren-right::before {
    content: "祭";
    position: absolute;
    top: 50%; left: 50%;
    transform: translate(-50%, -50%);
    color: #f5e6d3;
    font-size: 22px;
    font-weight: bold;
    text-shadow: 0 0 8px rgba(255,200,100,0.6);
}

/* ===== 대나무 (양쪽) ===== */
.bamboo-left, .bamboo-right {
    position: fixed;
    bottom: 0;
    width: 28px;
    height: 50%;
    background: linear-gradient(180deg, #5a7d44 0%, #2d4220 100%);
    z-index: -2;
    box-shadow: 3px 0 12px rgba(0,0,0,0.5);
}
.bamboo-left { left: 0; }
.bamboo-right { right: 0; }
.bamboo-left::before, .bamboo-right::before {
    content: "";
    position: absolute;
    top: 15%; left: 0;
    width: 100%; height: 4px;
    background: #1a2a10;
    box-shadow: 
        0 70px 0 #1a2a10, 
        0 140px 0 #1a2a10, 
        0 210px 0 #1a2a10,
        0 280px 0 #1a2a10;
}
/* 대나무 잎사귀 */
.bamboo-left::after, .bamboo-right::after {
    content: "🎋";
    position: absolute;
    top: -25px;
    left: -10px;
    font-size: 40px;
    transform: rotate(-15deg);
}
.bamboo-right::after { left: auto; right: -10px; transform: rotate(15deg); }

/* ===== 등불 (양쪽 4개, 더 화려하게) ===== */
.lantern-container {
    position: fixed;
    top: 0;
    width: 100%;
    height: 100vh;
    pointer-events: none;
    z-index: -1;
}

.lantern-wrap {
    position: absolute;
    top: 110px;
    transform-origin: top center;
    animation: swing 4s ease-in-out infinite;
}

.lantern-string {
    width: 2px;
    height: 50px;
    background: linear-gradient(180deg, #5a3a20 0%, #3d2515 100%);
    margin: 0 auto;
}
/* 등불 위 매듭 */
.lantern-string::before {
    content: "";
    position: absolute;
    bottom: 0;
    left: -3px;
    width: 8px;
    height: 8px;
    background: #d4af37;
    border-radius: 50%;
    box-shadow: 0 0 8px rgba(212, 175, 55, 0.6);
}

.lantern-body {
    width: 70px;
    height: 90px;
    background: radial-gradient(ellipse at center, 
        #fff2a8 0%, 
        #ffb347 25%, 
        #ff7043 55%, 
        #c62828 85%, 
        #8b1a1a 100%);
    border-radius: 50%;
    margin: 0 auto;
    position: relative;
    box-shadow: 
        0 0 50px rgba(255, 140, 66, 0.9),
        0 0 100px rgba(255, 140, 66, 0.6),
        0 0 160px rgba(255, 140, 66, 0.3),
        inset 0 -15px 25px rgba(0,0,0,0.4),
        inset 0 10px 20px rgba(255, 240, 180, 0.3);
    animation: glow 3s ease-in-out infinite;
}
.lantern-body::before, .lantern-body::after {
    content: "";
    position: absolute;
    left: 50%;
    transform: translateX(-50%);
    width: 42px;
    height: 9px;
    background: linear-gradient(180deg, #2a1810 0%, #1a0e08 100%);
    border-radius: 3px;
    box-shadow: 0 0 5px rgba(0,0,0,0.5);
}
.lantern-body::before { top: -5px; }
.lantern-body::after { bottom: -5px; }

.lantern-stripes {
    position: absolute;
    top: 22%;
    left: 0;
    width: 100%;
    height: 1.5px;
    background: rgba(0,0,0,0.5);
    box-shadow: 
        0 14px 0 rgba(0,0,0,0.5),
        0 28px 0 rgba(0,0,0,0.5),
        0 42px 0 rgba(0,0,0,0.5);
}
.lantern-body span {
    position: absolute;
    top: 50%; left: 50%;
    transform: translate(-50%, -50%);
    color: #2a0a0a;
    font-size: 26px;
    font-weight: bold;
    text-shadow: 0 0 4px rgba(255, 220, 150, 0.9);
    z-index: 2;
}

/* 등불 술(태슬) 장식 */
.lantern-body .tassel {
    position: absolute;
    bottom: -35px;
    left: 50%;
    transform: translateX(-50%);
    width: 4px;
    height: 25px;
    background: linear-gradient(180deg, #d4af37 0%, #b8860b 100%);
    font-size: 0;
}
.lantern-body .tassel::before {
    content: "";
    position: absolute;
    bottom: -8px;
    left: -8px;
    width: 20px;
    height: 15px;
    background: 
        repeating-linear-gradient(90deg, #d4af37 0px, #d4af37 2px, #b8860b 2px, #b8860b 4px);
    border-radius: 0 0 50% 50%;
}

.lantern-left-1 { left: 4%; }
.lantern-left-1 .lantern-wrap { animation-delay: 0s; }
.lantern-left-2 { left: 16%; }
.lantern-left-2 .lantern-wrap { animation-delay: -1.5s; }
.lantern-right-1 { right: 4%; }
.lantern-right-1 .lantern-wrap { animation-delay: -2s; }
.lantern-right-2 { right: 16%; }
.lantern-right-2 .lantern-wrap { animation-delay: -0.8s; }

@keyframes swing {
    0%, 100% { transform: rotate(-5deg); }
    50% { transform: rotate(5deg); }
}
@keyframes glow {
    0%, 100% { 
        box-shadow: 
            0 0 50px rgba(255, 140, 66, 0.9),
            0 0 100px rgba(255, 140, 66, 0.6),
            0 0 160px rgba(255, 140, 66, 0.3),
            inset 0 -15px 25px rgba(0,0,0,0.4);
    }
    50% { 
        box-shadow: 
            0 0 70px rgba(255, 200, 100, 1),
            0 0 140px rgba(255, 200, 100, 0.8),
            0 0 220px rgba(255, 200, 100, 0.5),
            inset 0 -15px 25px rgba(0,0,0,0.4);
    }
}

/* ===== 가랜드 (오색 깃발 줄) 🎏 ===== */
.garland {
    position: fixed;
    top: 130px;
    left: 0;
    width: 100%;
    height: 40px;
    z-index: -1;
    display: flex;
    justify-content: space-around;
    padding: 0 5%;
}
.flag {
    width: 0;
    height: 0;
    border-left: 12px solid transparent;
    border-right: 12px solid transparent;
    border-top: 20px solid;
    animation: flagWave 3s ease-in-out infinite;
}
.flag:nth-child(1) { border-top-color: #ff6b9d; animation-delay: 0s; }
.flag:nth-child(2) { border-top-color: #ffd93d; animation-delay: 0.2s; }
.flag:nth-child(3) { border-top-color: #6bcf7f; animation-delay: 0.4s; }
.flag:nth-child(4) { border-top-color: #4ecdc4; animation-delay: 0.6s; }
.flag:nth-child(5) { border-top-color: #c780ff; animation-delay: 0.8s; }
.flag:nth-child(6) { border-top-color: #ff6b9d; animation-delay: 1s; }
.flag:nth-child(7) { border-top-color: #ffd93d; animation-delay: 1.2s; }
.flag:nth-child(8) { border-top-color: #6bcf7f; animation-delay: 1.4s; }
.flag:nth-child(9) { border-top-color: #4ecdc4; animation-delay: 1.6s; }
.flag:nth-child(10) { border-top-color: #c780ff; animation-delay: 1.8s; }
.flag:nth-child(11) { border-top-color: #ff6b9d; animation-delay: 2s; }
.flag:nth-child(12) { border-top-color: #ffd93d; animation-delay: 2.2s; }

@keyframes flagWave {
    0%, 100% { transform: translateY(0) rotate(0deg); }
    50% { transform: translateY(-5px) rotate(5deg); }
}
/* 가랜드 줄 */
.garland::before {
    content: "";
    position: absolute;
    top: 0;
    left: 5%;
    width: 90%;
    height: 2px;
    background: #5a3a20;
    box-shadow: 0 0 5px rgba(0,0,0,0.4);
}

/* ===== 길거리 등 (지면 가까이) 🏮 ===== */
.street-lamp-l, .street-lamp-r {
    position: fixed;
    bottom: 5%;
    width: 8px;
    height: 120px;
    background: linear-gradient(180deg, #2a1810 0%, #1a0e08 100%);
    z-index: -1;
}
.street-lamp-l { left: 6%; }
.street-lamp-r { right: 6%; }
.street-lamp-l::before, .street-lamp-r::before {
    content: "";
    position: absolute;
    top: -20px;
    left: -15px;
    width: 38px;
    height: 50px;
    background: radial-gradient(ellipse at center, 
        #fff2a8 0%, #ffb347 50%, #c62828 100%);
    border-radius: 50% 50% 30% 30%;
    box-shadow: 
        0 0 30px rgba(255, 180, 80, 0.8),
        0 0 60px rgba(255, 180, 80, 0.5);
    animation: glow 3s ease-in-out infinite;
}

/* ===== 사케 통 (벽 앞 장식) 🍶 ===== */
.sake-barrel-l, .sake-barrel-r {
    position: fixed;
    bottom: 5%;
    width: 60px;
    height: 70px;
    background: 
        repeating-linear-gradient(180deg,
            #8b6f47 0px, #8b6f47 8px,
            #2a1810 8px, #2a1810 10px,
            #8b6f47 10px, #8b6f47 18px);
    border-radius: 8px;
    border: 3px solid #2a1810;
    z-index: -1;
    box-shadow: 0 5px 15px rgba(0,0,0,0.5);
}
.sake-barrel-l { left: 28%; }
.sake-barrel-r { right: 28%; }
.sake-barrel-l::before, .sake-barrel-r::before {
    content: "酒";
    position: absolute;
    top: 50%; left: 50%;
    transform: translate(-50%, -50%);
    color: #2a1810;
    font-size: 24px;
    font-weight: bold;
    background: #f5e6d3;
    width: 40px; height: 40px;
    border-radius: 50%;
    display: flex;
    align-items: center;
    justify-content: center;
    border: 2px solid #2a1810;
}

/* ===== 벚꽃잎 ===== */
.sakura {
    position: fixed;
    width: 12px;
    height: 12px;
    background: radial-gradient(circle, #ffb7c5 0%, #ff8fab 100%);
    border-radius: 0 100% 0 100%;
    opacity: 0.8;
    z-index: -1;
    animation: fall linear infinite;
}
@keyframes fall {
    0% { transform: translateY(-10vh) rotate(0deg); opacity: 0; }
    10% { opacity: 0.8; }
    90% { opacity: 0.8; }
    100% { transform: translateY(110vh) rotate(720deg); opacity: 0; }
}

/* 별 */
.star {
    position: fixed;
    width: 2px;
    height: 2px;
    background: #fff;
    border-radius: 50%;
    z-index: -3;
    animation: twinkle 3s ease-in-out infinite;
}
@keyframes twinkle {
    0%, 100% { opacity: 0.3; }
    50% { opacity: 1; }
}

/* ===== 콘텐츠 박스 ===== */
.block-container {
    background: rgba(20, 15, 35, 0.88);
    border-radius: 20px;
    padding: 2rem !important;
    backdrop-filter: blur(10px);
    border: 2px solid rgba(212, 175, 55, 0.5);
    box-shadow: 
        0 8px 32px rgba(0, 0, 0, 0.6),
        0 0 80px rgba(255, 183, 77, 0.2),
        inset 0 0 30px rgba(212, 175, 55, 0.05);
    margin-top: 9rem;
}

h1, h2, h3 {
    color: #ffd9a0 !important;
    text-shadow: 0 0 18px rgba(255, 183, 77, 0.7);
}
p, label, .stMarkdown, span:not(.lantern-body span) {
    color: #f5e6d3 !important;
}

.stSelectbox > div > div {
    background-color: rgba(255, 255, 255, 0.08) !important;
    border: 1px solid rgba(255, 183, 77, 0.4) !important;
    color: #f5e6d3 !important;
}

.stButton > button {
    background: linear-gradient(135deg, #ff8a65 0%, #ffb74d 50%, #d4af37 100%);
    color: #2d1b3d;
    font-weight: bold;
    border: 2px solid #d4af37;
    border-radius: 25px;
    padding: 12px 35px;
    box-shadow: 
        0 4px 20px rgba(255, 138, 101, 0.5),
        0 0 35px rgba(212, 175, 55, 0.4);
    transition: all 0.3s ease;
}
.stButton > button:hover {
    transform: translateY(-3px) scale(1.05);
    box-shadow: 
        0 6px 30px rgba(255, 138, 101, 0.9),
        0 0 60px rgba(212, 175, 55, 0.7);
}

.stAlert {
    background-color: rgba(255, 183, 77, 0.15) !important;
    border-left: 4px solid #ffb74d !important;
}
hr { border-color: rgba(212, 175, 55, 0.4); }
</style>

<!-- 별 -->
<div class="star" style="top: 3%; left: 8%;"></div>
<div class="star" style="top: 6%; left: 22%; animation-delay: 0.5s;"></div>
<div class="star" style="top: 2%; left: 38%; animation-delay: 1s;"></div>
<div class="star" style="top: 5%; left: 55%; animation-delay: 1.5s;"></div>
<div class="star" style="top: 7%; left: 70%; animation-delay: 2s;"></div>
<div class="star" style="top: 4%; left: 88%; animation-delay: 2.5s;"></div>
<div class="star" style="top: 18%; left: 30%; animation-delay: 0.8s;"></div>
<div class="star" style="top: 22%; left: 65%; animation-delay: 1.8s;"></div>
<div class="star" style="top: 15%; left: 50%; animation-delay: 2.2s;"></div>

<!-- 불꽃놀이 🎆 -->
<div class="firework firework-1"></div>
<div class="firework firework-2"></div>
<div class="firework firework-3"></div>

<!-- 멀리 풍경 -->
<div class="city-left"></div>
<div class="city-right"></div>
<div class="mountain"></div>

<!-- 벚꽃잎 🌸 -->
<div class="sakura" style="left: 5%; animation-duration: 12s; animation-delay: 0s;"></div>
<div class="sakura" style="left: 18%; animation-duration: 15s; animation-delay: 3s;"></div>
<div class="sakura" style="left: 30%; animation-duration: 10s; animation-delay: 6s;"></div>
<div class="sakura" style="left: 42%; animation-duration: 14s; animation-delay: 2s;"></div>
<div class="sakura" style="left: 55%; animation-duration: 13s; animation-delay: 5s;"></div>
<div class="sakura" style="left: 68%; animation-duration: 16s; animation-delay: 8s;"></div>
<div class="sakura" style="left: 80%; animation-duration: 11s; animation-delay: 10s;"></div>
<div class="sakura" style="left: 92%; animation-duration: 13s; animation-delay: 4s;"></div>

<!-- 기와 지붕 -->
<div class="roof">
    <div class="roof-top"></div>
    <div class="roof-tiles"></div>
    <div class="roof-bottom"></div>
</div>

<!-- 가랜드 (오색 깃발) 🎏 -->
<div class="garland">
    <div class="flag"></div><div class="flag"></div><div class="flag"></div>
    <div class="flag"></div><div class="flag"></div><div class="flag"></div>
    <div class="flag"></div><div class="flag"></div><div class="flag"></div>
    <div class="flag"></div><div class="flag"></div><div class="flag"></div>
</div>

<!-- 등불 4개 -->
<div class="lantern-container">
    <div class="lantern-left-1">
        <div class="lantern-wrap">
            <div class="lantern-string"></div>
            <div class="lantern-body">
                <div class="lantern-stripes"></div>
                <span>酒</span>
                <div class="tassel"></div>
            </div>
        </div>
    </div>
    <div class="lantern-left-2">
        <div class="lantern-wrap">
            <div class="lantern-string"></div>
            <div class="lantern-body">
                <div class="lantern-stripes"></div>
                <span>福</span>
                <div class="tassel"></div>
            </div>
        </div>
    </div>
    <div class="lantern-right-1">
        <div class="lantern-wrap">
            <div class="lantern-string"></div>
            <div class="lantern-body">
                <div class="lantern-stripes"></div>
                <span>祭</span>
                <div class="tassel"></div>
            </div>
        </div>
    </div>
    <div class="lantern-right-2">
        <div class="lantern-wrap">
            <div class="lantern-string"></div>
            <div class="lantern-body">
                <div class="lantern-stripes"></div>
                <span>味</span>
                <div class="tassel"></div>
            </div>
        </div>
    </div>
</div>

<!-- 대나무 -->
<div class="bamboo-left"></div>
<div class="bamboo-right"></div>

<!-- 가게 벽 + 격자창 + 노렌 -->
<div class="izakaya-wall"></div>
<div class="wall-trim"></div>
<div class="window-l1"></div>
<div class="window-l2"></div>
<div class="window-r1"></div>
<div class="window-r2"></div>
<div class="mini-noren-left"></div>
<div class="mini-noren-right"></div>
<div class="noren"></div>

<!-- 길거리 등 + 사케 통 -->
<div class="street-lamp-l"></div>
<div class="street-lamp-r"></div>
<div class="sake-barrel-l"></div>
<div class="sake-barrel-r"></div>
""", unsafe_allow_html=True)

# 3. 타이틀
st.title("🏮 이자카야 MBTI 저녁 추천 🍶")
st.markdown("### **🌙 어서오세요, 오늘도 수고 많으셨어요.**")
st.write("당신의 MBTI와 오늘 기분을 알려주시면, 따스한 한 끼를 추천해 드릴게요. 🎋🎆")
st.write("---")

# 4. 메뉴 데이터
mood_list = ["😄 신난다", "😴 피곤하다", "😢 우울하다", "😡 스트레스", "🥰 설렌다"]

default_meals = {
    "😄 신난다": [
        {"menu": "🍕 페퍼로니 피자", "desc": "신난 기분엔 피자가 진리! 🎉", "img": "https://images.unsplash.com/photo-1565299624946-b28f40a0ae38?w=600"},
        {"menu": "🍔 더블 치즈버거", "desc": "기분 좋게 한 입 가득! 🤤", "img": "https://images.unsplash.com/photo-1568901346375-23c9450c58cd?w=600"},
        {"menu": "🍗 후라이드 치킨", "desc": "바삭함이 신난 기분을 두 배로! 🥳", "img": "https://images.unsplash.com/photo-1562967914-608f82629710?w=600"},
    ],
    "😴 피곤하다": [
        {"menu": "🍲 국밥 한 그릇", "desc": "든든하고 따뜻한 한 그릇으로 회복! 💪", "img": "https://images.unsplash.com/photo-1583187854376-e602a4b66b67?w=600"},
        {"menu": "🍜 따끈한 우동", "desc": "부드러운 면발이 피로를 풀어줘요. 🌾", "img": "https://images.unsplash.com/photo-1618841557871-b4664fbf0cb3?w=600"},
        {"menu": "🍚 영양솥밥", "desc": "꽉 찬 영양으로 에너지 충전! 🌰", "img": "https://images.unsplash.com/photo-1569058242253-92a9c755a0ec?w=600"},
    ],
    "😢 우울하다": [
        {"menu": "🍫 초콜릿 디저트", "desc": "달콤함이 위로가 되어줄 거예요. 🤍", "img": "https://images.unsplash.com/photo-1542990253-0b8be4ccea7b?w=600"},
        {"menu": "🍝 크림 파스타", "desc": "부드럽고 진한 크림이 안아줘요. 💛", "img": "https://images.unsplash.com/photo-1621996346565-e3dbc646d9a9?w=600"},
        {"menu": "🍰 치즈케이크", "desc": "한 입의 달콤함이 마음을 녹여줘요. 🌸", "img": "https://images.unsplash.com/photo-1565958011703-44f9829ba187?w=600"},
    ],
    "😡 스트레스": [
        {"menu": "🌶️ 마라탕", "desc": "매콤하게 스트레스 날려버려요! 🔥", "img": "https://images.unsplash.com/photo-1552611052-33e04de081de?w=600"},
        {"menu": "🍗 매운 양념치킨", "desc": "맵단의 조화로 기분 전환! ⚡", "img": "https://images.unsplash.com/photo-1562967914-608f82629710?w=600"},
        {"menu": "🍜 짬뽕", "desc": "얼큰한 국물로 가슴이 뻥! 🌊", "img": "https://images.unsplash.com/photo-1626804475297-41608ea09aeb?w=600"},
    ],
    "🥰 설렌다": [
        {"menu": "🥩 스테이크", "desc": "특별한 날의 특별한 한 끼! ✨", "img": "https://images.unsplash.com/photo-1600891964092-4316c288032e?w=600"},
        {"menu": "🍝 감성 파스타", "desc": "촛불과 함께 즐기는 낭만. 🕯️", "img": "https://images.unsplash.com/photo-1473093295043-cdd812d0e601?w=600"},
        {"menu": "🍣 스시 플래터", "desc": "한 점 한 점 특별한 설렘. 💕", "img": "https://images.unsplash.com/photo-1579871494447-9811cf80d66c?w=600"},
    ],
}

all_mbti = ["INFP","ENFP","INFJ","ENFJ","INTJ","ENTJ","INTP","ENTP",
            "ISFP","ESFP","ISTP","ESTP","ISFJ","ESFJ","ISTJ","ESTJ"]
mbti_data = {m: default_meals for m in all_mbti}

# 5. 사용자 입력
col1, col2 = st.columns(2)
with col1:
    selected_mbti = st.selectbox("🧬 당신의 MBTI는?", sorted(mbti_data.keys()))
with col2:
    selected_mood = st.selectbox("💭 오늘 기분은?", mood_list)

# 6. 추천 버튼
if st.button("🏮 오늘의 저녁 메뉴 추천받기 🍶"):
    st.balloons()
    st.write("---")
    meals = mbti_data[selected_mbti][selected_mood]
    chosen = random.choice(meals)
    
    st.success(f"### 🌟 **{selected_mbti}** × **{selected_mood}** 님께 추천!")
    st.image(chosen["img"], use_container_width=True, caption=chosen["menu"])
    st.subheader(chosen["menu"])
    st.write(chosen["desc"])
    
    st.write("---")
    st.info("💡 다시 누르면 다른 메뉴도 추천받을 수 있어요! 🔄✨")
