import streamlit as st
import random

# 1. 페이지 설정
st.set_page_config(
    page_title="🏮 이자카야 MBTI 저녁 추천 🍶",
    page_icon="🏮",
    layout="centered"
)

# 2. 이자카야 배경 + 흔들리는 등불 애니메이션 CSS & HTML 🏮✨
st.markdown("""
<style>
/* 전체 배경: 깊은 밤 골목 느낌 */
.stApp {
    background: linear-gradient(180deg, 
        #0f0c29 0%, 
        #24243e 30%, 
        #302b4d 60%, 
        #1a1a2e 100%);
    background-attachment: fixed;
    color: #f5e6d3 !important;
    overflow-x: hidden;
}

/* 이자카야 가게 외벽 (나무 판자 느낌) */
.izakaya-wall {
    position: fixed;
    bottom: 0;
    left: 0;
    width: 100%;
    height: 35%;
    background: 
        repeating-linear-gradient(90deg,
            #3d2817 0px,
            #4a2f1c 80px,
            #3d2817 82px,
            #2a1810 84px,
            #3d2817 86px),
        linear-gradient(180deg, #2a1810 0%, #1a0e08 100%);
    z-index: -2;
    box-shadow: inset 0 10px 30px rgba(0,0,0,0.6);
}

/* 가게 처마 (위쪽 지붕선) */
.izakaya-roof {
    position: fixed;
    bottom: 35%;
    left: 0;
    width: 100%;
    height: 8px;
    background: linear-gradient(180deg, #1a0e08 0%, #5a3a20 100%);
    z-index: -2;
    box-shadow: 0 -2px 10px rgba(0,0,0,0.5);
}

/* 노렌 (이자카야 입구 천) */
.noren {
    position: fixed;
    bottom: 43%;
    left: 50%;
    transform: translateX(-50%);
    width: 280px;
    height: 60px;
    background: linear-gradient(180deg, #8b2c2c 0%, #5a1a1a 100%);
    z-index: -1;
    border-radius: 3px 3px 0 0;
    box-shadow: 0 3px 15px rgba(0,0,0,0.5);
    animation: norenSway 5s ease-in-out infinite;
    transform-origin: top center;
}
.noren::before {
    content: "居酒屋";
    position: absolute;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);
    color: #f5e6d3;
    font-size: 24px;
    font-weight: bold;
    letter-spacing: 8px;
    text-shadow: 0 0 8px rgba(255,200,100,0.5);
}
/* 노렌 갈라진 틈 */
.noren::after {
    content: "";
    position: absolute;
    top: 30%;
    left: 50%;
    transform: translateX(-50%);
    width: 2px;
    height: 70%;
    background: #1a0e08;
}

@keyframes norenSway {
    0%, 100% { transform: translateX(-50%) rotate(-1deg); }
    50% { transform: translateX(-50%) rotate(1deg); }
}

/* 등불 컨테이너 - 천장에서 줄로 매달림 */
.lantern-container {
    position: fixed;
    top: 0;
    width: 100%;
    height: 100vh;
    pointer-events: none;
    z-index: -1;
}

.lantern {
    position: absolute;
    top: 0;
    transform-origin: top center;
    animation: swing 4s ease-in-out infinite;
}

/* 등불 줄 */
.lantern-string {
    width: 2px;
    height: 80px;
    background: linear-gradient(180deg, transparent 0%, #4a3520 100%);
    margin: 0 auto;
}

/* 등불 본체 (붉은 종이등) */
.lantern-body {
    width: 55px;
    height: 70px;
    background: radial-gradient(ellipse at center, 
        #ffb347 0%, 
        #ff8c42 30%, 
        #d63031 70%, 
        #a02020 100%);
    border-radius: 50%;
    margin: 0 auto;
    position: relative;
    box-shadow: 
        0 0 30px rgba(255, 140, 66, 0.7),
        0 0 60px rgba(255, 140, 66, 0.4),
        0 0 100px rgba(255, 140, 66, 0.2),
        inset 0 -10px 20px rgba(0,0,0,0.3);
    animation: glow 3s ease-in-out infinite;
}

/* 등불 위/아래 받침 */
.lantern-body::before, .lantern-body::after {
    content: "";
    position: absolute;
    left: 50%;
    transform: translateX(-50%);
    width: 30px;
    height: 6px;
    background: #2a1810;
    border-radius: 2px;
}
.lantern-body::before { top: -3px; }
.lantern-body::after { bottom: -3px; }

/* 등불 가로 줄무늬 */
.lantern-stripes {
    position: absolute;
    top: 50%;
    left: 0;
    width: 100%;
    height: 1px;
    background: rgba(0,0,0,0.4);
    box-shadow: 
        0 -15px 0 rgba(0,0,0,0.4),
        0 15px 0 rgba(0,0,0,0.4);
}

/* 등불별 위치 + 흔들림 시간차 */
.lantern-1 { left: 8%; animation-delay: 0s; }
.lantern-1 .lantern { animation-delay: 0s; }
.lantern-2 { left: 25%; animation-delay: -1s; }
.lantern-2 .lantern { animation-delay: -1.2s; }
.lantern-3 { right: 25%; animation-delay: -2s; }
.lantern-3 .lantern { animation-delay: -2.3s; }
.lantern-4 { right: 8%; animation-delay: -0.5s; }
.lantern-4 .lantern { animation-delay: -0.7s; }

/* 흔들림 애니메이션 */
@keyframes swing {
    0%, 100% { transform: rotate(-4deg); }
    50% { transform: rotate(4deg); }
}

/* 빛 깜빡임 애니메이션 */
@keyframes glow {
    0%, 100% { 
        box-shadow: 
            0 0 30px rgba(255, 140, 66, 0.7),
            0 0 60px rgba(255, 140, 66, 0.4),
            0 0 100px rgba(255, 140, 66, 0.2),
            inset 0 -10px 20px rgba(0,0,0,0.3);
    }
    50% { 
        box-shadow: 
            0 0 40px rgba(255, 180, 90, 0.9),
            0 0 80px rgba(255, 180, 90, 0.6),
            0 0 130px rgba(255, 180, 90, 0.3),
            inset 0 -10px 20px rgba(0,0,0,0.3);
    }
}

/* 별 반짝임 (밤하늘) */
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

/* Streamlit 컨텐츠 영역에 반투명 박스 */
.block-container {
    background: rgba(20, 15, 35, 0.75);
    border-radius: 20px;
    padding: 2rem !important;
    backdrop-filter: blur(8px);
    border: 1px solid rgba(255, 183, 77, 0.25);
    box-shadow: 0 8px 32px rgba(0, 0, 0, 0.4);
    margin-top: 2rem;
}

/* 타이틀 등 텍스트 */
h1, h2, h3 {
    color: #ffd9a0 !important;
    text-shadow: 0 0 15px rgba(255, 183, 77, 0.5);
}
p, label, .stMarkdown, span {
    color: #f5e6d3 !important;
}

/* 선택 박스 */
.stSelectbox > div > div, .stRadio > div {
    background-color: rgba(255, 255, 255, 0.08) !important;
    border: 1px solid rgba(255, 183, 77, 0.4) !important;
    color: #f5e6d3 !important;
}

/* 버튼 */
.stButton > button {
    background: linear-gradient(135deg, #ff8a65 0%, #ffb74d 100%);
    color: #2d1b3d;
    font-weight: bold;
    border: none;
    border-radius: 25px;
    padding: 12px 35px;
    box-shadow: 0 4px 20px rgba(255, 138, 101, 0.5);
    transition: all 0.3s ease;
}
.stButton > button:hover {
    transform: translateY(-3px) scale(1.03);
    box-shadow: 0 6px 25px rgba(255, 138, 101, 0.8);
}

.stAlert {
    background-color: rgba(255, 183, 77, 0.15) !important;
    border-left: 4px solid #ffb74d !important;
}
hr { border-color: rgba(255, 183, 77, 0.3); }
</style>

<!-- 밤하늘 별 -->
<div class="star" style="top: 5%; left: 10%;"></div>
<div class="star" style="top: 8%; left: 30%; animation-delay: 0.5s;"></div>
<div class="star" style="top: 12%; left: 55%; animation-delay: 1s;"></div>
<div class="star" style="top: 6%; left: 75%; animation-delay: 1.5s;"></div>
<div class="star" style="top: 15%; left: 90%; animation-delay: 2s;"></div>
<div class="star" style="top: 20%; left: 20%; animation-delay: 0.8s;"></div>
<div class="star" style="top: 18%; left: 65%; animation-delay: 1.8s;"></div>
<div class="star" style="top: 3%; left: 45%; animation-delay: 2.5s;"></div>

<!-- 흔들리는 등불 4개 🏮 -->
<div class="lantern-container">
    <div class="lantern-1">
        <div class="lantern">
            <div class="lantern-string"></div>
            <div class="lantern-body"><div class="lantern-stripes"></div></div>
        </div>
    </div>
    <div class="lantern-2">
        <div class="lantern">
            <div class="lantern-string"></div>
            <div class="lantern-body"><div class="lantern-stripes"></div></div>
        </div>
    </div>
    <div class="lantern-3">
        <div class="lantern">
            <div class="lantern-string"></div>
            <div class="lantern-body"><div class="lantern-stripes"></div></div>
        </div>
    </div>
    <div class="lantern-4">
        <div class="lantern">
            <div class="lantern-string"></div>
            <div class="lantern-body"><div class="lantern-stripes"></div></div>
        </div>
    </div>
</div>

<!-- 이자카야 가게 외벽 + 노렌 -->
<div class="izakaya-wall"></div>
<div class="izakaya-roof"></div>
<div class="noren"></div>
""", unsafe_allow_html=True)

# 3. 타이틀
st.title("🏮 이자카야 MBTI 저녁 추천 🍶")
st.markdown("### **🌙 어서오세요, 오늘 하루도 수고 많으셨어요.**")
st.write("당신의 MBTI와 오늘 기분을 알려주시면, 따스한 한 끼를 추천해 드릴게요. 🍂")
st.write("---")

# 4. MBTI × 기분 조합 데이터 (각 MBTI마다 기분별 3가지 메뉴) 🍽️
mood_list = ["😄 신난다", "😴 피곤하다", "😢 우울하다", "😡 스트레스", "🥰 설렌다"]

mbti_data = {
    "INFP": {
        "😄 신난다": [
            {"menu": "🍣 연어 포케볼", "desc": "기분 좋은 날엔 알록달록 예쁜 한 그릇! 감성과 건강 둘 다 챙겨요. 🌈", "img": "https://images.unsplash.com/photo-1546069901-ba9599a7e63c?w=600"},
            {"menu": "🥞 수플레 팬케이크", "desc": "구름 같은 팬케이크로 동화 속 주인공이 된 기분을 만끽해요. ☁️", "img": "https://images.unsplash.com/photo-1567620905732-2d1ec7ab7445?w=600"},
            {"menu": "🍦 젤라또 디저트", "desc": "달콤한 젤라또로 행복을 한 스푼 더해봐요. 🍨", "img": "https://images.unsplash.com/photo-1488900128323-21503983a07e?w=600"},
        ],
        "😴 피곤하다": [
            {"menu": "🍲 밀푀유나베", "desc": "정성스럽게 쌓인 따뜻한 국물로 지친 마음을 녹여주세요. 🥰", "img": "https://images.unsplash.com/photo-1604908176997-125f25cc6f3d?w=600"},
            {"menu": "🍜 잔치국수", "desc": "잔잔하고 따뜻한 멸치 육수로 몸도 마음도 노곤하게. 🌾", "img": "https://images.unsplash.com/photo-1569718212165-3a8278d5f624?w=600"},
            {"menu": "🥣 호박죽", "desc": "달큰하고 부드러운 호박죽 한 그릇이면 충분해요. 🎃", "img": "https://images.unsplash.com/photo-1547592180-85f173990554?w=600"},
        ],
        "😢 우울하다": [
            {"menu": "🍫 핫초콜릿 & 브라우니", "desc": "달콤함이 마음의 빈자리를 살며시 채워줄 거예요. 💌", "img": "https://images.unsplash.com/photo-1542990253-0b8be4ccea7b?w=600"},
            {"menu": "🍵 말차 라떼와 화과자", "desc": "잔잔한 음악과 함께 천천히, 천천히 위로받아요. 🍃", "img": "https://images.unsplash.com/photo-1536013455834-d2bbf3b2f570?w=600"},
            {"menu": "🍝 크림 파스타", "desc": "부드럽고 진한 크림이 포근하게 안아줄 거예요. 🤍", "img": "https://images.unsplash.com/photo-1621996346565-e3dbc646d9a9?w=600"},
        ],
        "😡 스트레스": [
            {"menu": "🌶️ 매콤 마라샹궈", "desc": "매콤한 한 입에 답답함을 화끈하게 날려버려요! 🔥", "img": "https://images.unsplash.com/photo-1552611052-33e04de081de?w=600"},
            {"menu": "🍗 양념 닭강정", "desc": "달콤매콤한 양념이 스트레스를 잊게 해줘요. ✨", "img": "https://images.unsplash.com/photo-1562967914-608f82629710?w=600"},
            {"menu": "🥟 매운 군만두", "desc": "바삭바삭 깨물면서 기분 전환! 🥢", "img": "https://images.unsplash.com/photo-1496116218417-1a781b1c416c?w=600"},
        ],
        "🥰 설렌다": [
            {"menu": "🍰 딸기 케이크", "desc": "설레는 마음엔 분홍빛 딸기 케이크가 딱이에요. 🌸", "img": "https://images.unsplash.com/photo-1565958011703-44f9829ba187?w=600"},
            {"menu": "🍝 감성 파스타", "desc": "촛불 켜놓고 즐기는 감성 한 접시. 🕯️", "img": "https://images.unsplash.com/photo-1473093295043-cdd812d0e601?w=600"},
            {"menu": "🥐 크루아상 브런치", "desc": "버터향 가득한 크루아상으로 행복한 하루! 🌷", "img": "https://images.unsplash.com/photo-1555507036-ab1f4038808a?w=600"},
        ],
    },
    "ENFP": {
        "😄 신난다": [
            {"menu": "🌮 멕시칸 타코 파티", "desc": "다채로운 맛의 향연! 통통 튀는 당신과 찰떡이에요. 🎉", "img": "https://images.unsplash.com/photo-1565299585323-38d6b0865b47?w=600"},
            {"menu": "🍕 토핑 듬뿍 피자", "desc": "온갖 토핑이 어우러진 피자로 신남 폭발! 🎊", "img": "https://images.unsplash.com/photo-1565299624946-b28f40a0ae38?w=600"},
            {"menu": "🍔 수제 햄버거", "desc": "한 입 가득 베어물고 신난 기분을 즐겨봐요! 🤩", "img": "https://images.unsplash.com/photo-1568901346375-23c9450c58cd?w=600"},
        ],
        "😴 피곤하다": [
            {"menu": "🍜 진한 라멘", "desc": "쫀득한 면발과 진한 국물로 에너지 충전! 🍥", "img": "https://images.unsplash.com/photo-1569718212165-3a8278d5f624?w=600"},
            {"menu": "🍲 우동 한 그릇", "desc": "따끈한 우동으로 노곤한 하루를 풀어줘요. 🥢", "img": "https://images.unsplash.com/photo-1618841557871-b4664fbf0cb3?w=600"},
            {"menu": "🍛 카레라이스", "desc": "한 그릇으로 든든하게 회복! 💪", "img": "https://images.unsplash.com/photo-1604952564555-13119b8b3934?w=600"},
        ],
        "😢 우울하다": [
            {"menu": "🍩 알록달록 도넛", "desc": "기분 전환엔 달콤한 도넛이 최고! 🌈", "img": "https://images.unsplash.com/photo-1551024601-bec78aea704b?w=600"},
            {"menu": "🍕 치즈 폭탄 피자", "desc": "쭉 늘어나는 치즈로 기분을 끌어올려요. 🧀", "img": "https://images.unsplash.com/photo-1513104890138-7c749659a591?w=600"},
            {"menu": "🥤 버블티 & 와플", "desc": "쫀득쫀득 달콤함으로 우울 탈출! 🫧", "img": "https://images.unsplash.com/photo-1558857563-b371033873b8?w=600"},
        ],
        "😡 스트레스": [
            {"menu": "🌶️ 마라탕", "desc": "재료 골라 담는 재미 + 매운맛으로 시원하게! ⚡", "img": "https://images.unsplash.com/photo-1552611052-33e04de081de?w=600"},
            {"menu": "🔥 불닭볶음면", "desc": "매운맛으로 스트레스 정면 돌파! 🥵", "img": "https://images.unsplash.com/photo-1612927601601-6638404737ce?w=600"},
            {"menu": "🍗 매운 양념치킨", "desc": "치킨에 콜라 한 모금이면 행복 그 자체! 🍻", "img": "https://images.unsplash.com/photo-1562967914-608f82629710?w=600"},
        ],
        "🥰 설렌다": [
            {"menu": "🍣 회전 초밥 데이트", "desc": "도란도란 설레는 분위기에 딱! 🐟", "img": "https://images.unsplash.com/photo-1579871494447-9811cf80d66c?w=600"},
            {"menu": "🍰 감성 디저트 카페", "desc": "예쁜 디저트로 설렘을 두 배로! 💝", "img": "https://images.unsplash.com/photo-1565958011703-44f9829ba187?w=600"},
            {"menu": "🥂 브런치 플레이트", "desc": "햇살 가득한 브런치로 설렘 가득! ☀️", "img": "https://images.unsplash.com/photo-1533089860892-a7c6f0a88666?w=600"},
        ],
    },
    "INFJ": {
        "😄 신난다": [
            {"menu": "🍱 한정식 한 상", "desc": "정갈한 한 상으로 좋은 기분을 차분히 음미해요. 🌿", "img": "https://images.unsplash.com/photo-1583224994076-ae3e6a4b5f4d?w=600"},
            {"menu": "🍣 오마카세", "desc": "셰프의 정성을 느끼며 특별한 날을 만끽! ✨", "img": "https://images.unsplash.com/photo-1579871494447-9811cf80d66c?w=600"},
            {"menu": "🥗 그레인 보울", "desc": "건강한 한 그릇으로 균형 잡힌 행복을. 🌱", "img": "https://images.unsplash.com/photo-1512621776951-a57141f2eefd?w=600"},
        ],
        "😴 피곤하다": [
            {"menu": "🍵 따뜻한 죽 한 그릇", "desc": "은은한 위로가 필요한 날, 부드러운 죽이 답이에요. 🤍", "img": "https://images.unsplash.com/photo-1547592180-85f173990554?w=600"},
            {"menu": "🍲 누룽지탕", "desc": "구수한 누룽지로 마음까지 따뜻하게. 🌾", "img": "https://images.unsplash.com/photo-1569058242253-92a9c755a0ec?w=600"},
            {"menu": "🍜 칼국수", "desc": "쫄깃한 면발과 따뜻한 국물로 힐링. 💛", "img": "https://images.unsplash.com/photo-1626804475297-41608ea09aeb?w=600"},
        ],
        "😢 우울하다": [
            {"menu": "🍫 다크초콜릿 디저트", "desc": "쌉싸름한 위로가 깊이 스며들어요. 🖤", "img": "https://images.unsplash.com/photo-1542990253-0b8be4ccea7b?w=600"},
            {"menu": "🍵 차와 다과", "desc": "조용히 차 한 잔, 마음을 정돈하는 시간. ☕", "img": "https://images.unsplash.com/photo-1536013455834-d2bbf3b2f570?w=600"},
            {"menu": "🥧 따뜻한 애플파이", "desc": "포근한 단맛이 우울을 살며시 덮어줘요. 🍎", "img": "https://images.unsplash.com/photo-1568571780765-9276ac8b75a2?w=600"},
        ],
        "😡 스트레스": [
            {"menu": "🍲 얼큰 순두부찌개", "desc": "보글보글 끓는 찌개로 답답함을 풀어내요. 🌶️", "img": "https://images.unsplash.com/photo-1583224964978-2257b960c3d3?w=600"},
            {"menu": "🍜 짬뽕", "desc": "얼큰한 국물이 가슴을 시원하게! 🌊", "img": "https://images.unsplash.com/photo-1626804475297-41608ea09aeb?w=600"},
            {"menu": "🥘 닭볶음탕", "desc": "매콤한 양념으로 스트레스 해소! 🔥", "img": "https://images.unsplash.com/photo-1635363638580-c2809d049eee?w=600"},
        ],
        "🥰 설렌다": [
            {"menu": "🍰 티라미수", "desc": "은은한 커피향과 크림의 조화, 어른의 설렘. 🤎", "img": "https://images.unsplash.com/photo-1571877227200-a0d98ea607e9?w=600"},
            {"menu": "🍷 와인과 치즈 플래터", "desc": "잔잔한 분위기에서 즐기는 우아한 한 끼. 🧀", "img": "https://images.unsplash.com/photo-1510812431401-41d2bd2722f3?w=600"},
            {"menu": "🍝 트러플 파스타", "desc": "고급스러운 향이 설렘을 한 단계 끌어올려요. ✨", "img": "https://images.unsplash.com/photo-1621996346565-e3dbc646d9a9?w=600"},
        ],
    },
    "ENFJ": {
        "😄 신난다": [
            {"menu": "🐷 삼겹살 파티", "desc": "다 함께 모여 노릇한 삼겹살을 구워봐요! 🔥", "img": "https://images.unsplash.com/photo-1632789395770-20e6f63be806?w=600"},
            {"menu": "🍢 모듬 꼬치구이", "desc": "이것저것 골라 먹는 재미가 가득! 🎯", "img": "https://images.unsplash.com/photo-1529193591184-b1d58069ecdd?w=600"},
            {"menu": "🍤 새우 파티 플래터", "desc": "푸짐한 새우로 사람들과 즐거움을 나눠요. 🥳", "img": "https://images.unsplash.com/photo-1625943553852-781c6dd46faa?w=600"},
        ],
        "😴 피곤하다": [
            {"menu": "🍲 설렁탕", "desc": "뽀얀 국물 한 그릇으로 몸을 녹여요. ☁️", "img": "https://images.unsplash.com/photo-1583187854376-e602a4b66b67?w=600"},
            {"menu": "🍚 영양솥밥", "desc": "재료 가득 솥밥으로 건강한 보양. 🌰", "img": "https://images.unsplash.com/photo-1569058242253-92a9c755a0ec?w=600"},
            {"menu": "🍜 쌀국수", "desc": "맑고 깊은 국물이 피로를 풀어줘요. 🌿", "img": "https://images.unsplash.com/photo-1582878826629-29b7ad1cdc43?w=600"},
        ],
        "😢 우울하다": [
            {"menu": "🍰 따뜻한 케이크 한 조각", "desc": "달콤함이 마음을 살며시 안아줘요. 🤗", "img": "https://images.unsplash.com/photo-1565958011703-44f9829ba187?w=600"},
            {"menu": "🍵 호지차 라떼", "desc": "구수하고 따뜻한 한 잔으로 위로받아요. 💛", "img": "https://images.unsplash.com/photo-1536013455834-d2bbf3b2f570?w=600"},
            {"menu": "🍛 카레라이스", "desc": "익숙한 맛이 마음의 안정감을 줘요. 🧡", "img": "https://images.unsplash.com/photo-1604952564555-13119b8b3934?w=600"},
        ],
        "😡 스트레스": [
            {"menu": "🌶️ 매운 갈비찜", "desc": "매콤하게 풀어내는 스트레스 해소법! 💢", "img": "https://images.unsplash.com/photo-1635363638580-c2809d049eee?w=600"},
            {"menu": "🍗 매운 닭발", "desc": "쫄깃하고 매콤한 한 입! 🔥", "img": "https://images.unsplash.com/photo-1562967914-608f82629710?w=600"},
            {"menu": "🍜 비빔냉면", "desc": "새콤매콤한 한 그릇이 답답함을 풀어줘요! ❄️", "img": "https://images.unsplash.com/photo-1626804475297-41608ea09aeb?w=600"},
        ],
        "🥰 설렌다": [
            {"menu": "🥩 스테이크 디너", "desc": "특별한 사람과 함께하는 특별한 한 끼. 💕", "img": "https://images.unsplash.com/photo-1600891964092-4316c288032e?w=600"},
            {"menu": "🍣 스시 오마카세", "desc": "정성스러운 한 점, 한 점에 설렘이 가득. ✨", "img": "https://images.unsplash.com/photo-1579871494447-9811cf80d66c?w=600"},
            {"menu": "🍰 디저트 코스", "desc": "달콤한 마무리로 설렘을 완성! 🍓", "img": "https://images.unsplash.com/photo-1565958011703-44f9829ba187?w=600"},
        ],
    },
}

# 나머지 12개 MBTI도 동일한 구조로 자동 생성 (기본 데이터 활용)
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

# 나머지 MBTI 자동 채우기
remaining_mbti = ["INTJ", "ENTJ", "INTP", "ENTP", "ISFP", "ESFP", "ISTP", "ESTP", "ISFJ", "ESFJ", "ISTJ", "ESTJ"]
for mbti in remaining_mbti:
    mbti_data[mbti] = default_meals

# 5. 사용자 입력 UI
col1, col2 = st.columns(2)
with col1:
    selected_mbti = st.selectbox("🧬 당신의 MBTI는?", sorted(mbti_data.keys()))
with col2:
    selected_mood = st.selectbox("💭 오늘 기분은?", mood_list)

# 6. 추천 버튼
if st.button("🏮 오늘의 저녁 메뉴 추천받기 🍶"):
    st.balloons()
    st.write("---")
    
    # 해당 MBTI + 기분 조합의 메뉴 리스트에서 랜덤 추첨 🎲
    meals = mbti_data[selected_mbti][selected_mood]
    chosen = random.choice(meals)
    
    st.success(f"### 🌟 **{selected_mbti}** × **{selected_mood}** 님께 추천!")
    st.image(chosen["img"], use_container_width=True, caption=chosen["menu"])
    st.subheader(chosen["menu"])
    st.write(chosen["desc"])
    
    st.write("---")
    st.info("💡 다시 누르면 다른 메뉴도 추천받을 수 있어요! 🔄✨")
