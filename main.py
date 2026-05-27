import streamlit as st
import random

# 1. 페이지 설정
st.set_page_config(
    page_title="🏮 이자카야 MBTI 저녁 추천 🍶",
    page_icon="🏮",
    layout="centered"
)

# 2. 화려한 이자카야 배경 CSS + HTML 🏮🎋
st.markdown("""
<style>
/* 전체 배경: 깊은 밤 골목 */
.stApp {
    background: 
        radial-gradient(ellipse at top, #2d1b4e 0%, #1a1a2e 50%, #0f0c1d 100%);
    background-attachment: fixed;
    color: #f5e6d3 !important;
    overflow-x: hidden;
}

/* ===== 기와 지붕 ===== */
.roof {
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    height: 90px;
    z-index: -2;
}
/* 기와 패턴 (반복되는 원호) */
.roof-tiles {
    position: absolute;
    top: 30px;
    left: 0;
    width: 100%;
    height: 40px;
    background: 
        radial-gradient(circle at 20px 40px, #3d1f1f 0px, #3d1f1f 18px, transparent 19px),
        radial-gradient(circle at 60px 40px, #3d1f1f 0px, #3d1f1f 18px, transparent 19px),
        radial-gradient(circle at 100px 40px, #3d1f1f 0px, #3d1f1f 18px, transparent 19px),
        linear-gradient(180deg, #5a2828 0%, #3d1f1f 100%);
    background-size: 40px 40px, 40px 40px, 40px 40px, 100% 100%;
    box-shadow: 0 4px 15px rgba(0,0,0,0.6);
}
/* 지붕 윗 띠 */
.roof-top {
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 30px;
    background: linear-gradient(180deg, #1a0e08 0%, #3d1f1f 100%);
    box-shadow: 0 2px 8px rgba(0,0,0,0.5);
}
/* 지붕 처마 끝 (장식 띠) */
.roof-bottom {
    position: absolute;
    top: 70px;
    left: 0;
    width: 100%;
    height: 20px;
    background: 
        repeating-linear-gradient(90deg, 
            #8b2c2c 0px, 
            #8b2c2c 30px, 
            #d4af37 30px, 
            #d4af37 32px,
            #8b2c2c 32px,
            #8b2c2c 62px);
    border-bottom: 3px solid #d4af37;
    box-shadow: 0 3px 12px rgba(0,0,0,0.5);
}

/* ===== 가게 벽 (나무) ===== */
.izakaya-wall {
    position: fixed;
    bottom: 0;
    left: 0;
    width: 100%;
    height: 40%;
    background: 
        repeating-linear-gradient(90deg,
            #3d2817 0px,
            #4a2f1c 70px,
            #3d2817 72px,
            #2a1810 74px,
            #3d2817 76px),
        linear-gradient(180deg, #3a2515 0%, #1a0e08 100%);
    z-index: -2;
    box-shadow: inset 0 15px 30px rgba(0,0,0,0.7);
}

/* ===== 일본식 격자창 (왼쪽) ===== */
.window-left {
    position: fixed;
    bottom: 12%;
    left: 3%;
    width: 130px;
    height: 100px;
    background: 
        linear-gradient(180deg, 
            rgba(255, 200, 100, 0.4) 0%, 
            rgba(255, 150, 50, 0.3) 100%);
    border: 4px solid #2a1810;
    box-shadow: 
        0 0 30px rgba(255, 180, 80, 0.4),
        inset 0 0 20px rgba(255, 200, 100, 0.3);
    z-index: -2;
}
/* 격자 패턴 */
.window-left::before {
    content: "";
    position: absolute;
    top: 0; left: 0;
    width: 100%; height: 100%;
    background: 
        linear-gradient(90deg, transparent 32%, #2a1810 32%, #2a1810 35%, transparent 35%,
                              transparent 65%, #2a1810 65%, #2a1810 68%, transparent 68%),
        linear-gradient(0deg, transparent 32%, #2a1810 32%, #2a1810 35%, transparent 35%,
                              transparent 65%, #2a1810 65%, #2a1810 68%, transparent 68%);
}

/* 격자창 (오른쪽) */
.window-right {
    position: fixed;
    bottom: 12%;
    right: 3%;
    width: 130px;
    height: 100px;
    background: 
        linear-gradient(180deg, 
            rgba(255, 200, 100, 0.4) 0%, 
            rgba(255, 150, 50, 0.3) 100%);
    border: 4px solid #2a1810;
    box-shadow: 
        0 0 30px rgba(255, 180, 80, 0.4),
        inset 0 0 20px rgba(255, 200, 100, 0.3);
    z-index: -2;
}
.window-right::before {
    content: "";
    position: absolute;
    top: 0; left: 0;
    width: 100%; height: 100%;
    background: 
        linear-gradient(90deg, transparent 32%, #2a1810 32%, #2a1810 35%, transparent 35%,
                              transparent 65%, #2a1810 65%, #2a1810 68%, transparent 68%),
        linear-gradient(0deg, transparent 32%, #2a1810 32%, #2a1810 35%, transparent 35%,
                              transparent 65%, #2a1810 65%, #2a1810 68%, transparent 68%);
}

/* ===== 노렌 (입구 천) - 가게 중앙 ===== */
.noren {
    position: fixed;
    bottom: 40%;
    left: 50%;
    transform: translateX(-50%);
    width: 320px;
    height: 75px;
    background: 
        linear-gradient(180deg, #a02020 0%, #6b1515 100%);
    z-index: -1;
    border-radius: 3px 3px 0 0;
    box-shadow: 
        0 5px 20px rgba(0,0,0,0.6),
        inset 0 -8px 15px rgba(0,0,0,0.3);
    animation: norenSway 5s ease-in-out infinite;
    transform-origin: top center;
    border-top: 4px solid #d4af37;
}
.noren::before {
    content: "居 酒 屋";
    position: absolute;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);
    color: #f5e6d3;
    font-size: 28px;
    font-weight: bold;
    letter-spacing: 12px;
    text-shadow: 
        0 0 10px rgba(255,200,100,0.6),
        2px 2px 4px rgba(0,0,0,0.5);
}
/* 노렌 갈라진 틈 3개 */
.noren::after {
    content: "";
    position: absolute;
    top: 20%;
    left: 0;
    width: 100%;
    height: 80%;
    background: 
        linear-gradient(90deg, 
            transparent 24%, #1a0e08 24%, #1a0e08 26%, transparent 26%,
            transparent 49%, #1a0e08 49%, #1a0e08 51%, transparent 51%,
            transparent 74%, #1a0e08 74%, #1a0e08 76%, transparent 76%);
}
@keyframes norenSway {
    0%, 100% { transform: translateX(-50%) rotate(-1.5deg); }
    50% { transform: translateX(-50%) rotate(1.5deg); }
}

/* ===== 대나무 장식 (왼쪽) ===== */
.bamboo-left {
    position: fixed;
    bottom: 0;
    left: 0;
    width: 25px;
    height: 50%;
    background: linear-gradient(180deg, #4a6b3a 0%, #2d4220 100%);
    z-index: -2;
    box-shadow: 3px 0 10px rgba(0,0,0,0.4);
}
.bamboo-left::before, .bamboo-left::after {
    content: "";
    position: absolute;
    left: 0;
    width: 100%;
    height: 3px;
    background: #1a2a10;
}
.bamboo-left::before { top: 25%; box-shadow: 0 80px 0 #1a2a10, 0 160px 0 #1a2a10, 0 240px 0 #1a2a10; }

/* 대나무 (오른쪽) */
.bamboo-right {
    position: fixed;
    bottom: 0;
    right: 0;
    width: 25px;
    height: 50%;
    background: linear-gradient(180deg, #4a6b3a 0%, #2d4220 100%);
    z-index: -2;
    box-shadow: -3px 0 10px rgba(0,0,0,0.4);
}
.bamboo-right::before {
    content: "";
    position: absolute;
    top: 25%;
    left: 0;
    width: 100%;
    height: 3px;
    background: #1a2a10;
    box-shadow: 0 80px 0 #1a2a10, 0 160px 0 #1a2a10, 0 240px 0 #1a2a10;
}

/* ===== 등불 (양쪽 끝에 배치) ===== */
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
    top: 90px;
    transform-origin: top center;
    animation: swing 4s ease-in-out infinite;
}

.lantern-string {
    width: 2px;
    height: 60px;
    background: linear-gradient(180deg, #5a3a20 0%, #3d2515 100%);
    margin: 0 auto;
}

.lantern-body {
    width: 65px;
    height: 85px;
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
        0 0 40px rgba(255, 140, 66, 0.8),
        0 0 80px rgba(255, 140, 66, 0.5),
        0 0 140px rgba(255, 140, 66, 0.3),
        inset 0 -12px 25px rgba(0,0,0,0.4),
        inset 0 8px 15px rgba(255, 240, 180, 0.3);
    animation: glow 3s ease-in-out infinite;
}
.lantern-body::before, .lantern-body::after {
    content: "";
    position: absolute;
    left: 50%;
    transform: translateX(-50%);
    width: 38px;
    height: 8px;
    background: linear-gradient(180deg, #2a1810 0%, #1a0e08 100%);
    border-radius: 3px;
}
.lantern-body::before { top: -4px; }
.lantern-body::after { bottom: -4px; }

/* 등불 가로 줄무늬 (더 진하게) */
.lantern-stripes {
    position: absolute;
    top: 25%;
    left: 0;
    width: 100%;
    height: 1.5px;
    background: rgba(0,0,0,0.5);
    box-shadow: 
        0 13px 0 rgba(0,0,0,0.5),
        0 26px 0 rgba(0,0,0,0.5),
        0 39px 0 rgba(0,0,0,0.5);
}
/* 등불 글자 */
.lantern-body span {
    position: absolute;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);
    color: #2a0a0a;
    font-size: 22px;
    font-weight: bold;
    text-shadow: 0 0 3px rgba(255, 220, 150, 0.8);
    z-index: 2;
}

/* 등불 위치: 양쪽 끝 + 살짝 안쪽 */
.lantern-left-1 { left: 5%; }
.lantern-left-1 .lantern-wrap { animation-delay: 0s; }
.lantern-left-2 { left: 18%; }
.lantern-left-2 .lantern-wrap { animation-delay: -1.5s; }
.lantern-right-1 { right: 5%; }
.lantern-right-1 .lantern-wrap { animation-delay: -2s; }
.lantern-right-2 { right: 18%; }
.lantern-right-2 .lantern-wrap { animation-delay: -0.8s; }

@keyframes swing {
    0%, 100% { transform: rotate(-5deg); }
    50% { transform: rotate(5deg); }
}

@keyframes glow {
    0%, 100% { 
        box-shadow: 
            0 0 40px rgba(255, 140, 66, 0.8),
            0 0 80px rgba(255, 140, 66, 0.5),
            0 0 140px rgba(255, 140, 66, 0.3),
            inset 0 -12px 25px rgba(0,0,0,0.4);
    }
    50% { 
        box-shadow: 
            0 0 55px rgba(255, 200, 100, 1),
            0 0 110px rgba(255, 200, 100, 0.7),
            0 0 180px rgba(255, 200, 100, 0.4),
            inset 0 -12px 25px rgba(0,0,0,0.4);
    }
}

/* ===== 벚꽃잎 떨어지는 애니메이션 🌸 ===== */
.sakura {
    position: fixed;
    width: 12px;
    height: 12px;
    background: radial-gradient(circle, #ffb7c5 0%, #ff8fab 100%);
    border-radius: 0 100% 0 100%;
    opacity: 0.7;
    z-index: -1;
    animation: fall linear infinite;
}
@keyframes fall {
    0% { transform: translateY(-10vh) rotate(0deg); opacity: 0; }
    10% { opacity: 0.7; }
    90% { opacity: 0.7; }
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

/* ===== Streamlit 콘텐츠 박스 ===== */
.block-container {
    background: rgba(20, 15, 35, 0.85);
    border-radius: 20px;
    padding: 2rem !important;
    backdrop-filter: blur(10px);
    border: 2px solid rgba(212, 175, 55, 0.4);
    box-shadow: 
        0 8px 32px rgba(0, 0, 0, 0.5),
        0 0 60px rgba(255, 183, 77, 0.15);
    margin-top: 7rem;
}

h1, h2, h3 {
    color: #ffd9a0 !important;
    text-shadow: 0 0 15px rgba(255, 183, 77, 0.6);
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
        0 0 30px rgba(212, 175, 55, 0.3);
    transition: all 0.3s ease;
}
.stButton > button:hover {
    transform: translateY(-3px) scale(1.05);
    box-shadow: 
        0 6px 25px rgba(255, 138, 101, 0.8),
        0 0 50px rgba(212, 175, 55, 0.5);
}

.stAlert {
    background-color: rgba(255, 183, 77, 0.15) !important;
    border-left: 4px solid #ffb74d !important;
}
hr { border-color: rgba(212, 175, 55, 0.4); }
</style>

<!-- 별 -->
<div class="star" style="top: 3%; left: 15%;"></div>
<div class="star" style="top: 5%; left: 35%; animation-delay: 0.5s;"></div>
<div class="star" style="top: 2%; left: 55%; animation-delay: 1s;"></div>
<div class="star" style="top: 6%; left: 78%; animation-delay: 1.5s;"></div>
<div class="star" style="top: 4%; left: 92%; animation-delay: 2s;"></div>

<!-- 벚꽃잎 🌸 -->
<div class="sakura" style="left: 10%; animation-duration: 12s; animation-delay: 0s;"></div>
<div class="sakura" style="left: 30%; animation-duration: 15s; animation-delay: 3s;"></div>
<div class="sakura" style="left: 50%; animation-duration: 10s; animation-delay: 6s;"></div>
<div class="sakura" style="left: 70%; animation-duration: 14s; animation-delay: 2s;"></div>
<div class="sakura" style="left: 85%; animation-duration: 13s; animation-delay: 5s;"></div>
<div class="sakura" style="left: 20%; animation-duration: 16s; animation-delay: 8s;"></div>
<div class="sakura" style="left: 60%; animation-duration: 11s; animation-delay: 10s;"></div>

<!-- 기와 지붕 -->
<div class="roof">
    <div class="roof-top"></div>
    <div class="roof-tiles"></div>
    <div class="roof-bottom"></div>
</div>

<!-- 등불 4개: 양쪽 끝 2개씩 -->
<div class="lantern-container">
    <div class="lantern-left-1">
        <div class="lantern-wrap">
            <div class="lantern-string"></div>
            <div class="lantern-body">
                <div class="lantern-stripes"></div>
                <span>酒</span>
            </div>
        </div>
    </div>
    <div class="lantern-left-2">
        <div class="lantern-wrap">
            <div class="lantern-string"></div>
            <div class="lantern-body">
                <div class="lantern-stripes"></div>
                <span>福</span>
            </div>
        </div>
    </div>
    <div class="lantern-right-1">
        <div class="lantern-wrap">
            <div class="lantern-string"></div>
            <div class="lantern-body">
                <div class="lantern-stripes"></div>
                <span>祭</span>
            </div>
        </div>
    </div>
    <div class="lantern-right-2">
        <div class="lantern-wrap">
            <div class="lantern-string"></div>
            <div class="lantern-body">
                <div class="lantern-stripes"></div>
                <span>味</span>
            </div>
        </div>
    </div>
</div>

<!-- 대나무 장식 -->
<div class="bamboo-left"></div>
<div class="bamboo-right"></div>

<!-- 가게 벽 + 격자창 + 노렌 -->
<div class="izakaya-wall"></div>
<div class="window-left"></div>
<div class="window-right"></div>
<div class="noren"></div>
""", unsafe_allow_html=True)

# 3. 타이틀
st.title("🏮 이자카야 MBTI 저녁 추천 🍶")
st.markdown("### **🌙 어서오세요, 오늘도 수고 많으셨어요.**")
st.write("당신의 MBTI와 오늘 기분을 알려주시면, 따스한 한 끼를 추천해 드릴게요. 🎋✨")
st.write("---")

# 4. MBTI × 기분 조합 데이터
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

# 16가지 MBTI 모두 동일 데이터로 (학생이 직접 커스터마이즈 추천!)
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
