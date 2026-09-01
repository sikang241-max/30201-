import streamlit as st

# 페이지 기본 설정 (와이드 모드)
st.set_page_config(
    page_title="Gourmet World - 미식 세계 여행",
    page_icon="🎨",
    layout="wide"
)

# --- 🎨 웹폰트 및 세련된 감성 CSS 애니메이션 스타일 ---
st.markdown("""
<style>
    /* 구글 폰트 불러오기 */
    @import url('https://fonts.googleapis.com/css2?family=Noto+Sans+KR:wght@300;400;700;900&family=Poppins:wght@600;800&display=swap');

    html, body, [class*="css"] {
        font-family: 'Noto Sans KR', sans-serif;
        background-color: #FAFAFC;
    }
    
    /* 1. 감성 네온 스티커 히어로 배너 */
    .hero-banner {
        background: linear-gradient(135deg, #FF512F 0%, #DD2476 100%);
        border-radius: 28px;
        padding: 3rem 2rem;
        color: white;
        text-align: center;
        box-shadow: 0 20px 40px rgba(221, 36, 118, 0.25);
        margin-bottom: 2.5rem;
        position: relative;
        overflow: hidden;
    }
    .hero-title {
        font-family: 'Poppins', sans-serif;
        font-size: 3.2rem;
        font-weight: 800;
        letter-spacing: -1px;
        margin-bottom: 0.5rem;
        text-shadow: 0 4px 10px rgba(0,0,0,0.15);
    }
    .hero-sub {
        font-size: 1.15rem;
        font-weight: 300;
        opacity: 0.95;
    }
    
    /* 2. 통통 튀는 이모지 스티커 태그 */
    .sticker-tag {
        display: inline-flex;
        align-items: center;
        gap: 6px;
        padding: 6px 14px;
        font-size: 0.88rem;
        font-weight: 700;
        border-radius: 30px;
        margin-right: 6px;
        margin-bottom: 8px;
        transition: transform 0.2s ease;
        box-shadow: 0 4px 10px rgba(0,0,0,0.05);
    }
    .sticker-tag:hover {
        transform: translateY(-3px) rotate(-2deg);
    }
    .tag-asia { background: #E0F2FE; color: #0284C7; }
    .tag-europe { background: #F3E8FF; color: #9333EA; }
    .tag-america { background: #DCFCE7; color: #16A34A; }
    .tag-highlight { background: #FEF08A; color: #CA8A04; }
    .tag-star { background: #FFEDD5; color: #EA580C; }

    /* 3. 호버 모션 입체 카드 */
    .styled-card {
        background: white;
        border-radius: 20px;
        padding: 1.8rem;
        border: 1px solid #F1F5F9;
        box-shadow: 0 10px 25px rgba(0,0,0,0.03);
        margin-bottom: 1.5rem;
        transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
    }
    .styled-card:hover {
        transform: translateY(-5px);
        box-shadow: 0 15px 35px rgba(0,0,0,0.08);
        border-color: #E2E8F0;
    }
    .card-label {
        font-size: 0.8rem;
        text-transform: uppercase;
        letter-spacing: 1px;
        color: #94A3B8;
        font-weight: 700;
        margin-bottom: 4px;
    }
    .card-heading {
        font-size: 1.35rem;
        font-weight: 700;
        color: #0F172A;
        margin-bottom: 12px;
    }
    
    /* 사이드바 커스텀 스타일 */
    .sidebar-box {
        background: white;
        padding: 1.5rem;
        border-radius: 20px;
        border: 1px solid #F1F5F9;
        box-shadow: 0 4px 15px rgba(0,0,0,0.02);
    }
</style>
""", unsafe_allow_html=True)

# --- 📦 고화질 이미지 & 상세 정보 데이터베이스 ---
DATABASE = {
    "한국": {
        "flag": "🇰🇷", "continent": "아시아", "tag": "🌶️ 매콤달콤", "food": "전통 비빔밥",
        "image": "https://images.unsplash.com/photo-1553163147-622ab57be1c7?auto=format&fit=crop&w=1000&q=80",
        "food_desc": "다양한 계절 나물, 볶은 고기, 약고추장을 참기름과 함께 슥슥 비벼 먹는 한국 대표 웰빙 미식입니다.",
        "restaurant": "목멱산방", "rest_desc": "서울 남산 자락의 정갈한 한옥에서 선보이는 미쉐린 가이드 선정 비빔밥 명가입니다.",
        "location": "서울 중구 남산공원길 625", "rating": "4.8 / 5.0", "tip": "고추장은 처음부터 다 넣지 말고 반쯤 넣은 후 간을 보며 조절하세요!"
    },
    "일본": {
        "flag": "🇯🇵", "continent": "아시아", "tag": "🍜 진한 육수", "food": "돈코츠 라멘",
        "image": "https://images.unsplash.com/photo-1569718212165-3a8278d5f624?auto=format&fit=crop&w=1000&q=80",
        "food_desc": "돼지 사골을 오랜 시간 진하게 우려낸 고소한 국물과 야들야들한 차슈가 일품인 전통 일본 라멘입니다.",
        "restaurant": "이치란 (Ichiran) 본점", "rest_desc": "독서실형 1인 독서대 칸막이 좌석에서 오롯이 면발과 국물 맛에 집중할 수 있는 곳입니다.",
        "location": "후쿠오카시 하카타구 나카스 5-3-2", "rating": "4.7 / 5.0", "tip": "비밀 소스를 1.5배~2배 추가하면 느끼함 없이 칼칼하게 즐길 수 있습니다."
    },
    "중국": {
        "flag": "🇨🇳", "continent": "아시아", "tag": "🍗 바삭촉촉", "food": "베이징 덕",
        "image": "https://images.unsplash.com/photo-1518492104633-130d0cc84637?auto=format&fit=crop&w=1000&q=80",
        "food_desc": "장작 가마에서 구워 기름기는 쏙 빠지고 껍질은 바삭, 속살은 촉촉한 황실 전통 오리 요리입니다.",
        "restaurant": "전취덕 (Quanjude)", "rest_desc": "1864년부터 이어져 온 160년 역사와 전통의 베이징 오리 최고 존엄 맛집입니다.",
        "location": "베이징시 둥청구 치엔먼 다지에 30", "rating": "4.5 / 5.0", "tip": "설탕에 바삭한 껍질만 살짝 찍어 입안에서 녹는 식감을 먼저 느껴보세요."
    },
    "태국": {
        "flag": "🇹🇭", "continent": "아시아", "tag": "🍤 새콤달콤", "food": "팟타이 (Pad Thai)",
        "image": "https://images.unsplash.com/photo-1559847844-5315695dadae?auto=format&fit=crop&w=1000&q=80",
        "food_desc": "탱글탱글한 새우와 숙주, 쌀국수를 타마린드 특제 소스에 달콤새콤하게 볶아낸 스트리트 푸드입니다.",
        "restaurant": "팁싸마이 (Thipsamai)", "rest_desc": "방콕 밤거리를 밝히는 명소로, 얇은 계란 지단으로 싸여 나오는 팟타이가 예술입니다.",
        "location": "방콕 프라나콘 마하차이 로드 313", "rating": "4.6 / 5.0", "tip": "식당에서 함께 판매하는 100% 생 오렌지 주스는 필수로 주문하세요!"
    },
    "이탈리아": {
        "flag": "🇮🇹", "continent": "유럽", "tag": "🍕 정통 화덕", "food": "나폴리 마르게리타 피자",
        "image": "https://images.unsplash.com/photo-1513104890138-7c749659a591?auto=format&fit=crop&w=1000&q=80",
        "food_desc": "쫄깃한 도우 위에 신선한 토마토소스, 모짜렐라 치즈, 바질만 올려 400도 화덕에서 순식간에 구워냅니다.",
        "restaurant": "L'Antica Pizzeria da Michele", "rest_desc": "영화 <먹고 기도하고 사랑하라>에 나온 나폴리 최고의 전설적인 피제리아입니다.",
        "location": "Via Cesare Sersale, 1, Naples, Italy", "rating": "4.9 / 5.0", "tip": "메뉴는 마르게리타와 마리나라 단 2개뿐! 도우 끝부분까지 담백합니다."
    },
    "프랑스": {
        "flag": "🇫🇷", "continent": "유럽", "tag": "🍷 와인 스튜", "food": "뵈프 부르기뇽",
        "image": "https://images.unsplash.com/photo-1608897013039-887f21d8c804?auto=format&fit=crop&w=1000&q=80",
        "food_desc": "부르고뉴산 레드 와인에 소고기와 버섯, 야채를 넣어 몇 시간 동안 부드럽게 조려낸 정통 와인 스튜입니다.",
        "restaurant": "Au Petit Riche", "rest_desc": "1854년에 문을 연 파리의 부티크 레스토랑으로 고풍스러운 분위기를 선사합니다.",
        "location": "25 Rue Le Peletier, Paris, France", "rating": "4.6 / 5.0", "tip": "갓 구운 겉바속촉 바게트에 진한 소스를 듬뿍 얹어 드세요."
    },
    "미국": {
        "flag": "🇺🇸", "continent": "아메리카", "tag": "🍖 스모키 훈연", "food": "수제 바비큐 립",
        "image": "https://images.unsplash.com/photo-1544025162-d76694265947?auto=format&fit=crop&w=1000&q=80",
        "food_desc": "참나무 칩 훈연으로 10시간 이상 천천히 익혀 뼈가 쏙 빠질 정도로 부드러운 정통 아메리칸 바비큐입니다.",
        "restaurant": "Joe's Kansas City Bar-B-Que", "rest_desc": "주유소를 개조해 만든 이색 맛집으로 전 미 언론이 극찬한 바비큐 성지입니다.",
        "location": "3002 W 47th Ave, Kansas City, KS, USA", "rating": "4.8 / 5.0", "tip": "시그니처 메뉴인 Z-Man 샌드위치와 감자튀김 조합을 추천합니다."
    }
}

# --- 🎈 1. 상단 감성 히어로 배너 ---
st.markdown("""
<div class="hero-banner">
    <div style="font-size: 2.8rem; margin-bottom: 10px;">✨ ✈️ 🍕 🍤 ✨</div>
    <div class="hero-title">GOURMET WORLD</div>
    <div class="hero-subtitle">손끝에서 펼쳐지는 감성 미식 여행 · 시각과 입맛을 사로잡을 정통 가이드</div>
</div>
""", unsafe_allow_html=True)

# --- 🧭 2. 레이아웃 분할 ---
col_sidebar, col_main = st.columns([1, 2.3], gap="large")

with col_sidebar:
    st.markdown('<div class="sidebar-box">', unsafe_allow_html=True)
    st.markdown("### 🗺️ 여행지 선택")
    
    selected_country = st.selectbox(
        "📌 국가를 선택하세요",
        options=list(DATABASE.keys()),
        index=0
    )
    
    st.markdown("---")
    custom_search = st.text_input("🔍 키워드 검색", placeholder="예: 한국, 이탈리아...")
    
    target = custom_search.strip() if custom_search.strip() else selected_country
    
    st.markdown("---")
    st.markdown("#### 🎨 분위기별 맛집 스티커")
    st.markdown("""
    - 🌶️ **매콤달콤 비주얼:** 한국, 태국
    - 🍷 **로맨틱 클래식:** 프랑스, 이탈리아
    - 🍖 **육즙 폭발 스트리트:** 미국, 중국
    - 🍜 **장인 정신 한 그릇:** 일본
    """)
    st.markdown('</div>', unsafe_allow_html=True)

with col_main:
    if target in DATABASE:
        item = DATABASE[target]
        
        # 대륙별 스티커 클래스 매핑
        continent_class = "tag-asia" if item['continent'] == "아시아" else "tag-europe" if item['continent'] == "유럽" else "tag-america"
        
        # 타이틀 & 스티커 태그 묶음
        st.markdown(f"# {item['flag']} {target}")
        st.markdown(f"""
        <div>
            <span class="sticker-tag {continent_class}">📍 {item['continent']}</span>
            <span class="sticker-tag tag-highlight">{item['tag']}</span>
            <span class="sticker-tag tag-star">⭐ {item['rating']}</span>
        </div>
        """, unsafe_allow_html=True)
        
        st.write("") # 간격 조정
        
        # 📸 비주얼 포토 카드 (사진)
        st.image(item['image'], use_container_width=True, caption=f"📸 {target} 정통 대표 요리 - {item['food']}")
        
        # 🍱 1. 대표 음식 스티커 카드
        st.markdown(f"""
        <div class="styled-card">
            <div class="card-label">SIGNATURE DISH</div>
            <div class="card-heading">🍱 {item['food']}</div>
            <p style="color: #475569; line-height: 1.7; margin: 0;">{item['food_desc']}</p>
        </div>
        """, unsafe_allow_html=True)
        
        # 🏠 2. 대표 맛집 카드
        st.markdown(f"""
        <div class="styled-card">
            <div class="card-label">MUST-VISIT RESTAURANT</div>
            <div class="card-heading">🏠 {item['restaurant']}</div>
            <p style="color: #475569; line-height: 1.7; margin-bottom: 12px;">{item['rest_desc']}</p>
            <div style="background-color: #F8FAFC; padding: 10px 14px; border-radius: 10px; font-size: 0.88rem; color: #64748B;">
                📍 <b>위치:</b> {item['location']}
            </div>
        </div>
        """, unsafe_allow_html=True)
        
        # 💡 3. 여행자 팁 (아코디언 형태)
        with st.expander("💡 현지에서 실패 없는 꿀팁 알아보기"):
            st.info(f"👉 **{item['food']} 더 맛있게 먹는 법:**\n\n{item['tip']}")
            
    else:
        st.error(f"🔍 '{target}'에 대한 검색 결과를 찾지 못했습니다.")
        st.info("💡 **현재 등록된 추천 국가:**\n\n" + ", ".join(DATABASE.keys()))

st.markdown("---")
st.caption("✨ Gourmet World Visual Edition | Powered by Streamlit & Unsplash")
