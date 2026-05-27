import streamlit as st

# 1. 페이지 설정
st.set_page_config(
    page_title="MBTI 저녁 추천기 🏮",
    page_icon="🍶",
    layout="centered"
)

# 2. 잔잔한 밤의 이자카야 감성 배경 CSS 적용 🏮
st.markdown("""
    <style>
    /* 전체 배경: 깊은 밤 + 따뜻한 등불 그라데이션 */
    .stApp {
        background: radial-gradient(circle at 20% 20%, rgba(255, 183, 77, 0.25) 0%, transparent 40%),
                    radial-gradient(circle at 80% 70%, rgba(255, 138, 101, 0.20) 0%, transparent 40%),
                    linear-gradient(135deg, #1a1a2e 0%, #2d1b3d 50%, #1a1a2e 100%);
        background-attachment: fixed;
        color: #f5e6d3 !important;
    }
    
    /* 타이틀, 부제목 등 텍스트 컬러 (따뜻한 등불 빛 느낌) */
    h1, h2, h3, h4, h5, h6 {
        color: #ffd9a0 !important;
        text-shadow: 0 0 10px rgba(255, 183, 77, 0.3);
    }
    
    p, label, .stMarkdown {
        color: #f5e6d3 !important;
    }
    
    /* 선택 박스 스타일 */
    .stSelectbox > div > div {
        background-color: rgba(255, 255, 255, 0.08);
        border: 1px solid rgba(255, 183, 77, 0.4);
        color: #f5e6d3;
    }
    
    /* 버튼 스타일 (따뜻한 등불 색) */
    .stButton > button {
        background: linear-gradient(135deg, #ff8a65 0%, #ffb74d 100%);
        color: #2d1b3d;
        font-weight: bold;
        border: none;
        border-radius: 25px;
        padding: 10px 30px;
        box-shadow: 0 4px 15px rgba(255, 138, 101, 0.4);
        transition: all 0.3s ease;
    }
    .stButton > button:hover {
        transform: translateY(-2px);
        box-shadow: 0 6px 20px rgba(255, 138, 101, 0.6);
    }
    
    /* success, info 박스 살짝 어둡고 따뜻하게 */
    .stAlert {
        background-color: rgba(255, 183, 77, 0.15) !important;
        border-left: 4px solid #ffb74d !important;
    }
    
    /* 구분선 */
    hr {
        border-color: rgba(255, 183, 77, 0.3);
    }
    </style>
""", unsafe_allow_html=True)

# 3. 멋진 타이틀과 소개글 (이자카야 분위기)
st.title("🏮 MBTI 저녁 추천 이자카야 🍶")
st.write("---")
st.markdown("### **🌙 오늘 저녁, 뭐 먹지?**")
st.write("따스한 등불 아래, 당신의 MBTI에 꼭 맞는 오늘의 저녁 메뉴를 추천해 드려요. 🍂✨")

# 4. MBTI별 데이터 (메뉴 + 설명 + 음식 이미지 URL)
mbti_menu = {
    "INFP": {
        "menu": "따끈하고 감성 가득한 '밀푀유나베' 🍲",
        "desc": "혼자만의 고요하고 따뜻한 시간이 필요한 당신! 정성스럽게 겹겹이 쌓인 밀푀유나베로 감성을 충전하며 힐링해봐요. 🥰",
        "img": "https://images.unsplash.com/photo-1604908176997-125f25cc6f3d?w=600"
    },
    "ENFP": {
        "menu": "짜릿하고 다채로운 '마라탕' 🌶️",
        "desc": "통통 튀는 아이디어만큼이나 다양한 재료를 골라 담는 재미! 매콤함으로 오늘의 에너지를 즐겁게 발산해봐요! ⚡",
        "img": "https://images.unsplash.com/photo-1552611052-33e04de081de?w=600"
    },
    "INFJ": {
        "menu": "마음이 정갈해지는 '한정식 한 상' 🍱",
        "desc": "깊은 생각과 따뜻한 마음을 가진 INFJ! 자극적이지 않고 정성이 듬뿍 들어간 한정식으로 몸과 마음을 조용히 다독여주세요. 🌿",
        "img": "https://images.unsplash.com/photo-1583224994076-ae3e6a4b5f4d?w=600"
    },
    "ENFJ": {
        "menu": "사람들과 나눠 먹기 좋은 '삼겹살 구이' 🐷",
        "desc": "정 많고 사교성 넘치는 당신! 소중한 사람들과 도란도란 둘러앉아 노릇한 삼겹살을 구우며 사랑을 나눠봐요. 💬",
        "img": "https://images.unsplash.com/photo-1632789395770-20e6f63be806?w=600"
    },
    "INTJ": {
        "menu": "효율성과 영양의 정석 '포케 & 샐러드' 🥗",
        "desc": "체계적이고 합리적인 INTJ를 위한 최적의 메뉴! 탄단지가 완벽하게 설계된 포케 한 그릇으로 군더더기 없는 저녁을 즐기세요. 📐",
        "img": "https://images.unsplash.com/photo-1546069901-ba9599a7e63c?w=600"
    },
    "ENTJ": {
        "menu": "성공의 맛을 느끼는 '스테이크' 🥩",
        "desc": "야망 넘치는 리더 ENTJ! 열정적으로 하루를 보낸 나 자신을 위해 오늘 저녁은 고급스러운 스테이크로 최고의 보상을 선사하세요. 👑",
        "img": "https://images.unsplash.com/photo-1600891964092-4316c288032e?w=600"
    },
    "INTP": {
        "menu": "조리도 설거지도 최소화! '배달 피자' 🍕",
        "desc": "귀찮은 건 딱 질색이지만 맛은 타협할 수 없는 똑똑한 게으름쟁이 INTP! 피자 한 조각 베어 물며 나만의 탐구를 시작해봐요. 💻",
        "img": "https://images.unsplash.com/photo-1565299624946-b28f40a0ae38?w=600"
    },
    "ENTP": {
        "menu": "지루함을 탈피할 이색 메뉴 '멕시칸 타코' 🌮",
        "desc": "도전정신이 강하고 늘 새로운 것을 찾는 ENTP! 알록달록한 재료와 매콤새콤한 살사 소스로 신선한 자극을 느껴보세요! 🗺️",
        "img": "https://images.unsplash.com/photo-1565299585323-38d6b0865b47?w=600"
    },
    "ISFP": {
        "menu": "분위기 있는 예술적 집밥 '알리오 올리오' 🍝",
        "desc": "예술가적 기질을 소소하게 품고 사는 평화주의자! 잔잔한 음악과 함께 직접 만든 파스타로 아늑한 낭만을 즐겨보세요. 🎨",
        "img": "https://images.unsplash.com/photo-1621996346565-e3dbc646d9a9?w=600"
    },
    "ESFP": {
        "menu": "언제 어디서나 축제 분위기! '치킨과 콜라' 🍗🥤",
        "desc": "인생이 축제인 ESFP에게 치킨은 진리! 바삭한 튀김옷에 시원한 탄산 한 모금이면 세상 부러울 게 없죠. 🎉",
        "img": "https://images.unsplash.com/photo-1562967914-608f82629710?w=600"
    },
    "ISTP": {
        "menu": "심플하지만 확실하고 든든한 '국밥' 🍲",
        "desc": "말보다 행동으로 보여주는 쿨가이 ISTP! 구구절절한 메뉴 고민 대신 뚝배기 한 그릇 시원하게 비우고 빠르게 자유시간을! 🤫",
        "img": "https://images.unsplash.com/photo-1583187854376-e602a4b66b67?w=600"
    },
    "ESTP": {
        "menu": "짜릿하고 화끈한 '매콤한 불족발' 🌶️🔥",
        "desc": "도전을 두려워하지 않는 정열적인 행동파! 화끈한 불맛으로 오늘 하루의 스트레스를 통쾌하게 날려버려요! 🏃💨",
        "img": "https://images.unsplash.com/photo-1635363638580-c2809d049eee?w=600"
    },
    "ISFJ": {
        "menu": "정성이 가득 담긴 따뜻한 '김치찌개' 🥘",
        "desc": "주변 사람들을 살뜰하게 챙기는 배려왕 ISFJ! 오늘 저녁은 익숙하고 따뜻한 집밥 찌개로 편안한 위로를 선물하세요. 🧸",
        "img": "https://images.unsplash.com/photo-1583224964978-2257b960c3d3?w=600"
    },
    "ESFJ": {
        "menu": "다 같이 행복을 끓여내는 '즉석 떡볶이' 🍢",
        "desc": "분위기 메이커이자 다정한 친선도모형! 친구, 가족과 둘러앉아 보글보글 끓는 떡볶이로 이야기꽃을 피워보세요. 🌸",
        "img": "https://images.unsplash.com/photo-1635963662063-88589beac403?w=600"
    },
    "ISTJ": {
        "menu": "절대 실패 없는 정석 '돈카츠 정식' 🍱",
        "desc": "철저하고 계획적인 당신에겐 흐트러짐 없는 안정적인 선택이 딱! 겉바속촉 돈카츠로 완벽한 행복을 맛보세요. 📐",
        "img": "https://images.unsplash.com/photo-1607330289024-1535c6b4e1c1?w=600"
    },
    "ESTJ": {
        "menu": "에너지를 고속 충전하는 '제육볶음' 🍛",
        "desc": "강한 책임감과 효율성을 중시하는 현실주의자! 한국인의 소울푸드 제육볶음으로 든든히 충전하고 목표를 향해 달려가요! 💪",
        "img": "https://images.unsplash.com/photo-1635363638580-c2809d049eee?w=600"
    }
}

# 5. 사용자 입력 UI
mbti_list = sorted(list(mbti_menu.keys()))
selected_mbti = st.selectbox("👉 당신의 MBTI를 선택해 주세요 🏮", mbti_list)

# 6. 추천 버튼
if st.button("🍶 오늘의 저녁 메뉴 보기"):
    st.balloons()
    
    st.write("---")
    st.success(f"### 🌟 **{selected_mbti}**님을 위한 오늘의 저녁 추천!")
    
    info = mbti_menu[selected_mbti]
    
    # 음식 이미지 가운데 큼직하게 띄우기 🍽️
    st.image(info["img"], use_container_width=True, caption=info["menu"])
    
    # 메뉴 이름 & 추천 이유
    st.subheader(info["menu"])
    st.write(info["desc"])
    
    st.write("---")
    st.info("💡 마음에 드는 메뉴인가요? 오늘 저녁은 이걸로 결정! 🥢✨")
