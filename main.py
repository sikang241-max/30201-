import streamlit as st

# 페이지 기본 설정
st.set_page_config(
    page_title="Gourmet World - 세계 맛집 & 대표 음식 가이드",
    page_icon="✈️",
    layout="wide"
)

# --- 🎨 커스텀 CSS 스타일 ---
st.markdown("""
<style>
    .main {
        background-color: #f8f9fa;
    }
    
    /* 히어로 헤더 디자인 */
    .hero-container {
        background: linear-gradient(135deg, #FF6B6B 0%, #FF8E53 100%);
        padding: 2.5rem 2rem;
        border-radius: 20px;
        color: white;
        text-align: center;
        box-shadow: 0 10px 25px rgba(255, 107, 107, 0.25);
        margin-bottom: 2rem;
    }
    .hero-title {
        font-size: 2.5rem;
        font-weight: 800;
        margin-bottom: 0.5rem;
    }
    .hero-subtitle {
        font-size: 1.1rem;
        opacity: 0.95;
    }

    /* 스티커 태그 스타일 */
    .sticker-badge {
        display: inline-block;
        padding: 0.35em 0.8em;
        font-size: 0.85rem;
        font-weight: 700;
        border-radius: 50px;
        margin-right: 0.4rem;
        margin-bottom: 0.5rem;
        box-shadow: 0 2px 5px rgba(0,0,0,0.08);
    }
    .badge-asia { background-color: #E3F2FD; color: #1565C0; }
    .badge-europe { background-color: #F3E5F5; color: #7B1FA2; }
    .badge-america { background-color: #E8F5E9; color: #2E7D32; }
    .badge-other { background-color: #FFF3E0; color: #E65100; }
    .badge-tag { background-color: #FFF9C4; color: #F57F17; }

    /* 결과 카드 스타일 */
    .content-card {
        background-color: white;
        border-radius: 16px;
        padding: 1.8rem;
        border: 1px solid #eaeaea;
        box-shadow: 0 4px 15px rgba(0,0,0,0.04);
        margin-bottom: 1.2rem;
    }
    .card-title {
        font-size: 1.3rem;
        font-weight: 700;
        color: #2D3748;
        margin-bottom: 0.8rem;
    }
</style>
""", unsafe_allow_html=True)

# --- 📦 이미지 URL 포함 데이터베이스 ---
DATABASE = {
    # 아시아
    "한국": {
        "flag": "🇰🇷", "continent": "아시아", "tag": "🌶️ 매콤달콤", "food": "비빔밥",
        "image": "https://images.unsplash.com/photo-1553163147-622ab57be1c7?auto=format&fit=crop&w=800&q=80",
        "food_desc": "다양한 신선한 나물, 고기, 고추장을 밥과 함께 비벼 먹는 한국의 대표 건강식입니다.",
        "restaurant": "목멱산방", "rest_desc": "서울 남산 자락에 위치한 미쉐린 가이드 선정 비빔밥 전문점으로 정갈한 한상을 제공합니다.",
        "location": "서울 중구 남산공원길 625", "rating": "4.6 / 5.0", "tip": "고추장 양을 취향에 맞게 조절해 비벼 드세요!"
    },
    "일본": {
        "flag": "🇯🇵", "continent": "아시아", "tag": "🍜 진한 육수", "food": "돈코츠 라멘",
        "image": "https://images.unsplash.com/photo-1569718212165-3a8278d5f624?auto=format&fit=crop&w=800&q=80",
        "food_desc": "돼지 뼈를 긴 시간 푹 고아낸 진하고 고소한 국물과 쫄깃한 면발이 특징인 일식 라멘입니다.",
        "restaurant": "이치란 (Ichiran) 본점", "rest_desc": "독서실 형태의 1인 좌석으로 유명하며, 면 익힘 정도와 국물 농도를 조절할 수 있습니다.",
        "location": "후쿠오카시 하카타구 나카스 5-3-2", "rating": "4.5 / 5.0", "tip": "비밀 소스를 1.5배 추가하면 한국인 입맛에 딱 맞습니다."
    },
    "중국": {
        "flag": "🇨🇳", "continent": "아시아", "tag": "🍗 바삭촉촉", "food": "베이징 덕 (북경오리)",
        "image": "https://images.unsplash.com/photo-1518492104633-130d0cc84637?auto=format&fit=crop&w=800&q=80",
        "food_desc": "특제 소스를 바르고 참나무 장작에 구워 바삭한 껍질과 부드러운 살코기를 밀전병에 싸 먹는 요리입니다.",
        "restaurant": "전취덕 (Quanjude)", "rest_desc": "1864년에 설립된 160년 전통의 대표적인 전통 북경오리 전문점입니다.",
        "location": "베이징시 둥청구 치엔먼 다지에 30", "rating": "4.4 / 5.0", "tip": "설탕에 바삭한 오리 껍질을 살짝 찍어 드셔보세요."
    },
    "태국": {
        "flag": "🇹🇭", "continent": "아시아", "tag": "🍤 새콤달콤", "food": "팟타이 (Pad Thai)",
        "image": "https://images.unsplash.com/photo-1559847844-5315695dadae?auto=format&fit=crop&w=800&q=80",
        "food_desc": "쌀국수에 계란, 숙주, 새우, 타마린드 소스를 넣어 달콤하고 새콤하게 볶아낸 대표 국수 요리입니다.",
        "restaurant": "팁싸마이 (Thipsamai)", "rest_desc": "방콕에서 가장 유명한 팟타이 전문점으로 얇은 계란지단으로 감싼 팟타이가 시그니처입니다.",
        "location": "방콕 프라나콘 마하차이 로드 313", "rating": "4.3 / 5.0", "tip": "함께 파는 생오렌지 주스를 꼭 같이 주문하세요!"
    },
    "베트남": {
        "flag": "🇻🇳", "continent": "아시아", "tag": "🌿 깊은 국물", "food": "소고기 쌀국수 (Pho Bo)",
        "image": "https://images.unsplash.com/photo-1582878826629-29b7ad1cdc43?auto=format&fit=crop&w=800&q=80",
        "food_desc": "진하게 우려낸 소고기 육수에 쌀국수와 신선한 허브, 양지머리를 올려 먹는 베트남 국민 요리입니다.",
        "restaurant": "퍼10 리꾸옥수 (Pho 10 Ly Quoc Su)", "rest_desc": "하노이 3대 쌀국수집 중 하나로 깊은 육수 맛과 미쉐린 빕구르망에 선정된 맛집입니다.",
        "location": "하노이 환끼엠 리꾸옥수 10", "rating": "4.4 / 5.0", "tip": "꿔이(튀긴 빵)를 국물에 적셔 함께 드세요."
    },

    # 유럽
    "이탈리아": {
        "flag": "🇮🇹", "continent": "유럽", "tag": "🍕 정통 화덕", "food": "나폴리 화덕 피자",
        "image": "https://images.unsplash.com/photo-1513104890138-7c749659a591?auto=format&fit=crop&w=800&q=80",
        "food_desc": "신선한 토마토소스, 모짜렐라 치즈, 바질만으로 본연의 맛을 내는 참나무 화덕 피자입니다.",
        "restaurant": "L'Antica Pizzeria da Michele", "rest_desc": "1870년부터 전통을 이어온 나폴리의 전설적인 피자집으로 영화에도 등장했습니다.",
        "location": "Via Cesare Sersale, 1, Naples, Italy", "rating": "4.7 / 5.0", "tip": "마르게리타와 마리나라 두 가지만 판매하는 곳입니다."
    },
    "프랑스": {
        "flag": "🇫🇷", "continent": "유럽", "tag": "🍷 와인 스튜", "food": "뵈프 부르기뇽",
        "image": "https://images.unsplash.com/photo-1608897013039-887f21d8c804?auto=format&fit=crop&w=800&q=80",
        "food_desc": "소고기를 레드 와인, 버섯, 양파와 함께 오랜 시간 진하게 조려낸 정통 와인 스튜입니다.",
        "restaurant": "Au Petit Riche", "rest_desc": "1854년에 개업한 파리의 정통 비스트로로 클래식한 프랑스 요리를 선사합니다.",
        "location": "25 Rue Le Peletier, Paris, France", "rating": "4.4 / 5.0", "tip": "프랑스빵(바게트)에 스튜 소스를 남김없이 찍어 드세요."
    },
    "스페인": {
        "flag": "🇪🇸", "continent": "유럽", "tag": "🥘 향긋한 샤프란", "food": "해산물 빠에야",
        "image": "https://images.unsplash.com/photo-1534080564583-6be75777b70a?auto=format&fit=crop&w=800&q=80",
        "food_desc": "샤프란 향이 배어있는 밥에 올리브유와 신선한 해산물을 넣어 넓은 팬에 볶아낸 요리입니다.",
        "restaurant": "7 Portes", "rest_desc": "1836년 바르셀로나에 문을 연 역사적인 레스토랑으로 피카소도 즐겨 찾던 곳입니다.",
        "location": "Passeig de Isabel II, 14, Barcelona, Spain", "rating": "4.5 / 5.0", "tip": "팬 바닥에 눌러붙은 밥(소카랏)이 가장 맛있습니다."
    },

    # 아메리카
    "미국": {
        "flag": "🇺🇸", "continent": "아메리카", "tag": "🍖 스모키 훈연", "food": "수제 바비큐 립",
        "image": "https://images.unsplash.com/photo-1544025162-d76694265947?auto=format&fit=crop&w=800&q=80",
        "food_desc": "훈연 칩으로 오랜 시간 천천히 구워내 부드럽고 스모키한 풍미가 진하게 배어있는 바비큐입니다.",
        "restaurant": "Joe's Kansas City Bar-B-Que", "rest_desc": "주유소를 개조해 만든 캔자스시티의 명물로 세계적으로 유명한 맛집입니다.",
        "location": "3002 W 47th Ave, Kansas City, KS, USA", "rating": "4.8 / 5.0", "tip": "Z-Man 샌드위치가 대기열을 감수할 만큼 유명합니다."
    },
    "멕시코": {
        "flag": "🇲🇽", "continent": "아메리카", "tag": "🌮 정통 스트리트", "food": "스트리트 타코",
        "image": "https://images.unsplash.com/photo-1565299585323-38d6b0865b47?auto=format&fit=crop&w=800&q=80",
        "food_desc": "양념된 고기를 구워 또르띠아에 파인애플, 고수, 라임과 함께 싸 먹는 메인 요리입니다.",
        "restaurant": "El Farolito", "rest_desc": "멕시코시티 현지인들이 최고의 타코로 손꼽는 찐 맛집입니다.",
        "location": "Altata 19, Mexico City, Mexico", "rating": "4.6 / 5.0", "tip": "라임즙을 듬뿍 짜 넣고 살사 소스를 취향껏 올려 드세요."
    }
}

# --- 🎈 히어로 배너 ---
st.markdown("""
<div class="hero-container">
    <div style="font-size: 3rem; margin-bottom: 5px;">✈️ 🍽️ 📍</div>
    <div class="hero-title">GOURMET WORLD</div>
    <div class="hero-subtitle">손끝에서 떠나는 전 세계 미식 여행 - 미쉐린 맛집 & 대표 음식 가이드</div>
</div>
""", unsafe_allow_html=True)

# --- 🔍 메인 검색 레이아웃 ---
col_search, col_display = st.columns([1, 2], gap="large")

with col_search:
    st.markdown("### 🧭 어디로 떠나볼까요?")
    
    selected_country = st.selectbox(
        "📌 추천 국가 선택하기",
        options=list(DATABASE.keys())
    )
    
    custom_input = st.text_input("🔍 직접 국가 검색", placeholder="예: 한국, 일본, 이탈리아...")
    
    target = custom_input.strip() if custom_input.strip() else selected_country
    
    st.markdown("---")
    st.markdown("#### 🌟 빠른 미식 태그")
    st.markdown("""
    - 🌶️ **매콤달콤한 맛**: 한국, 태국
    - 🍕 **화덕 & 피자**: 이탈리아
    - 🥩 **고기 파티**: 미국, 멕시코
    - 🍜 **면 요리 탐방**: 일본, 베트남
    """)

with col_display:
    if target in DATABASE:
        data = DATABASE[target]
        
        cont_class = "badge-asia" if data['continent'] == "아시아" else "badge-europe" if data['continent'] == "유럽" else "badge-america"
        
        # 헤더 타이틀 및 스티커 배지
        st.markdown(f"## {data['flag']} {target}")
        st.markdown(f"""
        <span class="sticker-badge {cont_class}">📍 {data['continent']}</span>
        <span class="sticker-badge badge-tag">{data['tag']}</span>
        <span class="sticker-badge badge-other">⭐ {data['rating']}</span>
        """, unsafe_allow_html=True)
        
        st.write("") # 간격
        
        # 📸 음식 대표 사진 추가 영역
        st.image(data['image'], use_container_width=True, caption=f"{target} 대표 요리 - {data['food']}")
        
        # 대표 음식 설명 카드
        st.markdown(f"""
        <div class="content-card">
            <div class="card-title">🍱 대표 음식: {data['food']}</div>
            <p style="color: #4A5568; line-height: 1.6;">{data['food_desc']}</p>
        </div>
        """, unsafe_allow_html=True)
        
        # 추천 맛집 카드
        st.markdown(f"""
        <div class="content-card">
            <div class="card-title">🏠 추천 맛집: {data['restaurant']}</div>
            <p style="color: #4A5568; line-height: 1.6;">{data['rest_desc']}</p>
            <hr style="border: none; border-top: 1px solid #edf2f7; margin: 10px 0;">
            <p style="font-size: 0.9rem; color: #718096; margin: 0;">📍 <b>위치:</b> {data['location']}</p>
        </div>
        """, unsafe_allow_html=True)
        
        # 💡 여행자 꿀팁
        with st.expander("💡 현지인처럼 즐기는 미식 꿀팁 보기"):
            st.info(data['tip'])
            
    else:
        st.warning(f"⚠️ '{target}'에 대한 정보가 아직 등록되지 않았습니다.")
        st.info("💡 **등록된 국가 목록:**\n\n" + ", ".join(DATABASE.keys()))

st.markdown("---")
st.caption("✨ Gourmet World Guide | Crafted with Streamlit")
