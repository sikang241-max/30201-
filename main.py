import streamlit as st

import streamlit as st

# 페이지 기본 설정
st.set_page_config(
    page_title="세계 맛집 & 대표 음식 추천기",
    page_icon="🍽️",
    layout="wide"
)

# 국가별 추천 데이터베이스
DATABASE = {
    "한국": {
        "flag": "🇰🇷",
        "food": "비빔밥",
        "food_desc": "다양한 신선한 나물, 고기, 고추장을 밥과 함께 비벼 먹는 한국의 대표 건강식입니다.",
        "restaurant": "목멱산방",
        "rest_desc": "서울 남산 자락에 위치한 미쉐린 가이드 선정 비빔밥 전문점으로, 깔끔하고 정갈한 한상을 제공합니다.",
        "location": "서울 중구 남산공원길 625",
        "rating": "4.6 / 5.0"
    },
    "일본": {
        "flag": "🇯🇵",
        "food": "돈코츠 라멘",
        "food_desc": "돼지 뼈를 긴 시간 푹 고아낸 진하고 고소한 국물과 쫄깃한 면발이 특징인 일식 라멘입니다.",
        "restaurant": "이치란 (Ichiran) 본점",
        "rest_desc": "독서실 형태의 1인 독서대 좌석으로 유명하며, 취향에 맞게 맛과 면의 익힘을 조절할 수 있습니다.",
        "location": "후쿠오카시 하카타구 나카스 5-3-2",
        "rating": "4.5 / 5.0"
    },
    "이탈리아": {
        "flag": "🇮🇹",
        "food": "나폴리 화덕 피자 (Margherita)",
        "food_desc": "신선한 토마토소스, 모짜렐라 치즈, 바질만으로 본연의 맛을 내는 참나무 화덕 피자입니다.",
        "restaurant": "L'Antica Pizzeria da Michele",
        "rest_desc": "1870년부터 전통을 이어온 나폴리의 전설적인 피자집으로, 영화 '먹고 기도하고 사랑하라'에 등장했습니다.",
        "location": "Via Cesare Sersale, 1, 80139 Napoli NA, Italy",
        "rating": "4.7 / 5.0"
    },
    "프랑스": {
        "flag": "🇫🇷",
        "food": "뵈프 부르기뇽 (Bœuf Bourguignon)",
        "food_desc": "소고기를 레드 와인, 버섯, 양파와 함께 진하게 조려낸 프랑스 부르고뉴 지방의 전통 스튜입니다.",
        "restaurant": "Au Petit Riche",
        "rest_desc": "1854년에 개업한 파리의 정통 부용(Bouillon) 스타일 비스트로로, 클래식한 프랑스 요리를 맛볼 수 있습니다.",
        "location": "25 Rue Le Peletier, 75009 Paris, France",
        "rating": "4.4 / 5.0"
    },
    "태국": {
        "flag": "🇹🇭",
        "food": "팟타이 (Pad Thai)",
        "food_desc": "쌀국수에 계란, 숙주, 새우, 타마린드 소스를 넣어 달콤하고 새콤하게 볶아낸 태국의 대표 국수 요리입니다.",
        "restaurant": "팁싸마이 (Thipsamai)",
        "rest_desc": "방콕에서 가장 유명한 팟타이 전문점으로, 얇은 계란지단으로 감싼 오렌지 에그 팟타이가 시그니처입니다.",
        "location": "313 315 Maha Chai Rd, Samran Rat, Phra Nakhon, Bangkok 10200",
        "rating": "4.3 / 5.0"
    },
    "미국": {
        "flag": "🇺🇸",
        "food": "수제 스모크 바비큐 립",
        "food_desc": "훈연 칩으로 오랜 시간 천천히 구워내 부드럽고 스모키한 풍미가 진하게 배어있는 바비큐입니다.",
        "restaurant": "Joe's Kansas City Bar-B-Que",
        "rest_desc": "주유소를 개조해 만든 캔자스시티의 명물로, 세계적으로 손꼽히는 바비큐 맛집입니다.",
        "location": "3002 W 47th Ave, Kansas City, KS 66103",
        "rating": "4.8 / 5.0"
    },
    "베트남": {
        "flag": "🇻🇳",
        "food": "소고기 쌀국수 (Pho Bo)",
        "food_desc": "진하게 우려낸 소고기 육수에 쌀국수와 신선한 허브, 양지머리를 올려 먹는 베트남의 국민 요리입니다.",
        "restaurant": "퍼10 리꾸옥수 (Pho 10 Ly Quoc Su)",
        "rest_desc": "하노이 3대 쌀국수집 중 하나로, 깊은 육수 맛과 미쉐린 빕구르망에 선정된 검증된 맛집입니다.",
        "location": "10 P. Lý Quốc Sư, Hàng Trống, Hoàn Kiếm, Hà Nội",
        "rating": "4.4 / 5.0"
    },
    "스페인": {
        "flag": "🇪🇸",
        "food": "해산물 빠에야 (Paella)",
        "food_desc": "샤프란 향이 배어있는 밥에 신선한 올리브유, 새우, 홍합 등 해산물을 넣어 팬에 볶아낸 요리입니다.",
        "restaurant": "7 Portes",
        "rest_desc": "1836년 바르셀로나에 문을 연 역사적인 레스토랑으로, 피카소와 미로도 즐겨 찾았던 빠에야 명가입니다.",
        "location": "Passeig de Isabel II, 14, 08003 Barcelona, Spain",
        "rating": "4.5 / 5.0"
    }
}

# 헤더 영역
st.title("🌏 세계 맛집 & 대표 음식 추천기")
st.caption("궁금한 나라의 이름을 입력하거나 선택하시면 대표 음식과 명품 맛집을 찾아드립니다.")

st.divider()

# 검색 영역 (사이드바 또는 메인 화면)
col1, col2 = st.columns([1, 2])

with col1:
    st.subheader("🔍 국가 검색")
    
    # 드롭다운 선택 또는 직접 입력
    selected_country = st.selectbox(
        "목록에서 선택하기",
        options=list(DATABASE.keys())
    )
    
    custom_input = st.text_input("또는 직접 입력하기", placeholder="예: 한국, 일본, 태국...")
    
    # 최종 선택 국가 결정
    target_country = custom_input.strip() if custom_input.strip() else selected_country

with col2:
    if target_country in DATABASE:
        data = DATABASE[target_country]
        
        st.subheader(f"{data['flag']} {target_country} 추천 결과")
        
        # 대표 음식 카드리
        with st.container(border=True):
            st.markdown(f"### 🍱 대표 음식: **{data['food']}**")
            st.write(data['food_desc'])
            
        # 맛집 카드
        with st.container(border=True):
            st.markdown(f"### 🏠 추천 맛집: **{data['restaurant']}**")
            st.write(data['rest_desc'])
            
            # 메트릭 표시
            m_col1, m_col2 = st.columns(2)
            with m_col1:
                st.metric(label="📍 위치/주소", value=data['location'].split(',')[0])
            with m_col2:
                st.metric(label="⭐ 평점", value=data['rating'])
                
            st.caption(f"전체 주소: {data['location']}")
            
    else:
        st.warning(f"⚠️ '{target_country}'에 대한 데이터가 아직 준비되지 않았습니다.")
        st.info("현재 지원 가능한 국가: " + ", ".join(DATABASE.keys()))

# 하단 안내 메시지
st.divider()
st.caption("💡 Streamlit으로 제작된 서비스입니다. `pip install streamlit` 후 `streamlit run app.py`로 실행할 수 있습니다.")
