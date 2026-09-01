import streamlit as st

# 페이지 기본 설정
st.set_page_config(
    page_title="세계 맛집 & 대표 음식 추천기",
    page_icon="🍽️",
    layout="wide"
)

# 25개국 대용량 내장 데이터베이스
DATABASE = {
    # --- 아시아 ---
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
        "rest_desc": "독서실 형태의 1인 좌석으로 유명하며, 취향에 맞게 맛과 면의 익힘을 조절할 수 있습니다.",
        "location": "후쿠오카시 하카타구 나카스 5-3-2",
        "rating": "4.5 / 5.0"
    },
    "중국": {
        "flag": "🇨🇳",
        "food": "베이징 덕 (북경오리)",
        "food_desc": "특제 소스를 바르고 참나무 장작에 구워 바삭한 껍질과 부드러운 살코기를 밀전병에 싸 먹는 요리입니다.",
        "restaurant": "전취덕 (Quanjude)",
        "rest_desc": "1864년에 설립된 160년 전통의 대표적인 전통 북경오리 전문점입니다.",
        "location": "베이징시 둥청구 치엔먼 다지에 30",
        "rating": "4.4 / 5.0"
    },
    "태국": {
        "flag": "🇹🇭",
        "food": "팟타이 (Pad Thai)",
        "food_desc": "쌀국수에 계란, 숙주, 새우, 타마린드 소스를 넣어 달콤하고 새콤하게 볶아낸 국수 요리입니다.",
        "restaurant": "팁싸마이 (Thipsamai)",
        "rest_desc": "방콕에서 가장 유명한 팟타이 전문점으로, 얇은 계란지단으로 감싼 팟타이가 시그니처입니다.",
        "location": "방콕 프라나콘 마하차이 로드 313",
        "rating": "4.3 / 5.0"
    },
    "베트남": {
        "flag": "🇻🇳",
        "food": "소고기 쌀국수 (Pho Bo)",
        "food_desc": "진하게 우려낸 소고기 육수에 쌀국수와 신선한 허브, 양지머리를 올려 먹는 베트남 국민 요리입니다.",
        "restaurant": "퍼10 리꾸옥수 (Pho 10 Ly Quoc Su)",
        "rest_desc": "하노이 3대 쌀국수집 중 하나로 깊은 육수 맛과 미쉐린 빕구르망에 선정된 검증된 맛집입니다.",
        "location": "하노이 환끼엠 리꾸옥수 10",
        "rating": "4.4 / 5.0"
    },
    "인도": {
        "flag": "🇮🇳",
        "food": "버터 치킨 & 난 (Butter Chicken)",
        "food_desc": "부드러운 닭고기를 향신료, 토마토, 버터, 크림으로 만든 달콤하고 고소한 커리에 난을 곁들여 먹습니다.",
        "restaurant": "Moti Mahal",
        "rest_desc": "버터 치킨과 탄두리 치킨이 최초로 시작된 델리의 전설적인 역사적 레스토랑입니다.",
        "location": "뉴델리 다리야간지 3704",
        "rating": "4.5 / 5.0"
    },
    "대만": {
        "flag": "🇹🇼",
        "food": "우육면 (Beef Noodle Soup)",
        "food_desc": "진하게 우려낸 한약재와 소고기 육수에 쫄깃한 면발, 부드러운 아롱사태를 얹어 먹는 대표 면 요리입니다.",
        "restaurant": "임동방 우육면 (Lin Dong Fang)",
        "rest_desc": "타이베이에서 오랜 시간 사랑받은 미쉐린 빕구르망 추천 우육면 명가입니다.",
        "location": "타이베이시 중산구 바더로 2단 325",
        "rating": "4.5 / 5.0"
    },
    "홍콩": {
        "flag": "🇭🇰",
        "food": "딤섬 (Dim Sum - 하가우/쇼마이)",
        "food_desc": "증기에 찌거나 기름에 튀겨 만든 한 입 크기의 만두 요리로 차와 함께 즐깁니다.",
        "restaurant": "팀호완 (Tim Ho Wan)",
        "rest_desc": "세계에서 가장 저렴한 미쉐린 1스타 딤섬집으로 유명한 곳입니다.",
        "location": "홍콩 삼수이포 후쿠윙 스트리트 9-11",
        "rating": "4.6 / 5.0"
    },
    "싱가포르": {
        "flag": "🇸🇬",
        "food": "칠리 크랩 (Chili Crab)",
        "food_desc": "매콤하고 달콤한 토마토 계란 소스에 신선한 게를 볶아 만든 싱가포르의 대표 해산물 요리입니다.",
        "restaurant": "점보 씨푸드 (Jumbo Seafood)",
        "rest_desc": "클락키 리버사이드에 위치해 야경을 보며 정통 칠리크랩을 맛볼 수 있는 대표 맛집입니다.",
        "location": "싱가포르 업퍼 호성 로드 20",
        "rating": "4.5 / 5.0"
    },
    "인도네시아": {
        "flag": "🇮🇩",
        "food": "나시고랭 (Nasi Goreng)",
        "food_desc": "삼발 소스와 낟알이 살아있는 밥, 채소, 고기를 넣고 볶아 달걀후라이를 올린 볶음밥입니다.",
        "restaurant": "Nasi Goreng Kambing Kebon Sirih",
        "rest_desc": "자카르타에서 양고기 나시고랭으로 매우 유명한 스트리트 푸드 명가입니다.",
        "location": "자카르타 중구 케본시리 로드 3",
        "rating": "4.6 / 5.0"
    },

    # --- 유럽 ---
    "이탈리아": {
        "flag": "🇮🇹",
        "food": "나폴리 화덕 피자 (Margherita)",
        "food_desc": "신선한 토마토소스, 모짜렐라 치즈, 바질만으로 본연의 맛을 내는 참나무 화덕 피자입니다.",
        "restaurant": "L'Antica Pizzeria da Michele",
        "rest_desc": "1870년부터 전통을 이어온 나폴리의 전설적인 피자집으로 영화에도 출연했습니다.",
        "location": "Via Cesare Sersale, 1, Naples, Italy",
        "rating": "4.7 / 5.0"
    },
    "프랑스": {
        "flag": "🇫🇷",
        "food": "뵈프 부르기뇽 (Bœuf Bourguignon)",
        "food_desc": "소고기를 레드 와인, 버섯, 양파와 함께 진하게 조려낸 프랑스 정통 스튜입니다.",
        "restaurant": "Au Petit Riche",
        "rest_desc": "1854년에 개업한 파리의 정통 비스트로로 클래식한 프랑스 요리를 선사합니다.",
        "location": "25 Rue Le Peletier, Paris, France",
        "rating": "4.4 / 5.0"
    },
    "스페인": {
        "flag": "🇪🇸",
        "food": "해산물 빠에야 (Paella)",
        "food_desc": "샤프란 향이 배어있는 밥에 올리브유와 다양한 해산물을 넣어 팬에 볶아낸 요리입니다.",
        "restaurant": "7 Portes",
        "rest_desc": "1836년 바르셀로나에 문을 연 역사적인 레스토랑으로 피카소도 즐겨 찾던 곳입니다.",
        "location": "Passeig de Isabel II, 14, Barcelona, Spain",
        "rating": "4.5 / 5.0"
    },
    "독일": {
        "flag": "🇩🇪",
        "food": "학세 (Schweinshaxe)",
        "food_desc": "돼지 족발 부위를 맥주와 향신료로 오랫동안 조린 뒤 겉은 바삭하고 속은 촉촉하게 구워낸 요리입니다.",
        "restaurant": "Hofbräuhaus München",
        "rest_desc": "뮌헨에 위치한 400년 역사의 세계에서 가장 유명한 왕립 맥주집입니다.",
        "location": "Platzl 9, 80331 München, Germany",
        "rating": "4.5 / 5.0"
    },
    "영국": {
        "flag": "🇬🇧",
        "food": "피시 앤 칩스 (Fish and Chips)",
        "food_desc": "두툼한 흰살생선을 바삭하게 튀겨 튀긴 감자칩과 타르타르 소스를 곁들여 먹는 대표 요리입니다.",
        "restaurant": "The Golden Hind",
        "rest_desc": "런던 마릴러본에서 1914년부터 운영되어 온 신선한 정통 피시앤칩스 전문점입니다.",
        "location": "73 Marylebone High St, London, UK",
        "rating": "4.5 / 5.0"
    },
    "터키": {
        "flag": "🇹🇷",
        "food": "이스켄데르 케밥 (Iskender Kebap)",
        "food_desc": "얇게 썬 양고기 케밥 위에 매콤한 토마토소스, 녹인 버터, 요거트를 얹어 먹는 정통 케밥입니다.",
        "restaurant": "Kebapçı İskender",
        "rest_desc": "이누뇌 광장에 위치해 정통 창시자 가문의 손맛을 그대로 유지하는 케밥 명가입니다.",
        "location": "Atatürk Cd. No:60, Bursa, Turkey",
        "rating": "4.6 / 5.0"
    },
    "스위스": {
        "flag": "🇨🇭",
        "food": "치즈 퐁듀 (Cheese Fondue)",
        "food_desc": "그뤼에르 치즈와 와인을 녹인 냄비에 빵 조각을 꼬챙이에 꿰어 찍어 먹는 따뜻한 요리입니다.",
        "restaurant": "Swiss Chuchi Restaurant",
        "rest_desc": "취리히 구시가지에 위치하여 최고의 정통 치즈 퐁듀를 제공하는 인기 맛집입니다.",
        "location": "Rosengasse 10, 8001 Zürich, Switzerland",
        "rating": "4.4 / 5.0"
    },
    "애일랜드": {
        "flag": "🇬🇷",
        "food": "수블라키 & 기로스 (Souvlaki)",
        "food_desc": "향신료로 재운 돼지고기나 닭고기를 꼬치에 구워 피타 빵과 차지키 소스에 싸 먹는 요리입니다.",
        "restaurant": "O Thanasis",
        "rest_desc": "아테네 모나스티라키 광장 근처에서 가장 유명한 수블라키 전문점입니다.",
        "location": "Mitropoleos 69, Monastiraki, Athens, Greece",
        "rating": "4.5 / 5.0"
    },

    # --- 아메리카 ---
    "미국": {
        "flag": "🇺🇸",
        "food": "수제 바비큐 립 (BBQ Ribs)",
        "food_desc": "훈연 칩으로 오랜 시간 천천히 구워내 부드럽고 스모키한 풍미가 진하게 배어있는 바비큐입니다.",
        "restaurant": "Joe's Kansas City Bar-B-Que",
        "rest_desc": "주유소를 개조해 만든 캔자스시티의 명물로 세계적으로 유명한 바비큐 맛집입니다.",
        "location": "3002 W 47th Ave, Kansas City, KS, USA",
        "rating": "4.8 / 5.0"
    },
    "멕시코": {
        "flag": "🇲🇽",
        "food": "스트리트 타코 (Tacos al Pastor)",
        "food_desc": "양념된 돼지고기를 회전 구이틀에서 익혀 또르띠아에 파인애플, 고수, 라임과 함께 싸 먹습니다.",
        "restaurant": "El Farolito",
        "rest_desc": "멕시코시티 현지인들이 최고의 알 파스토르 타코로 손꼽는 숨은 맛집입니다.",
        "location": "Altata 19, Hipódromo Condesa, Mexico City, Mexico",
        "rating": "4.6 / 5.0"
    },
    "브라질": {
        "flag": "🇧🇷",
        "food": "슈하스코 (Churrasco)",
        "food_desc": "소고기, 돼지고기, 닭고기 등 다양한 부위를 꼬챙이에 꿰어 숯불에 구워내는 정통 바비큐입니다.",
        "restaurant": "Fogo de Chão",
        "rest_desc": "상파울루에서 시작되어 세계적인 브랜드가 된 고급 슈하스코 전문점입니다.",
        "location": "R. Augusta, 2077 - Cerqueira César, São Paulo, Brazil",
        "rating": "4.7 / 5.0"
    },
    "캐나다": {
        "flag": "🇨🇦",
        "food": "푸틴 (Poutine)",
        "food_desc": "바삭하게 튀긴 감자튀김 위에 쫄깃한 치즈 커드를 올리고 따뜻한 그레이비 소스를 부어 먹습니다.",
        "restaurant": "La Banquise",
        "rest_desc": "몬트리올에서 24시간 운영하며 30가지가 넘는 다양한 푸틴을 맛볼 수 있는 곳입니다.",
        "location": "994 Rue Rachel E, Montréal, QC, Canada",
        "rating": "4.5 / 5.0"
    },

    # --- 오세아니아 & 아프리카 ---
    "호주": {
        "flag": "🇦🇺",
        "food": "미트 파이 & 미디엄 스테이크",
        "food_desc": "다진 고기와 그레이비 소스로 채워 바삭하게 구워낸 파이와 신선한 청정우 스테이크입니다.",
        "restaurant": "Harry's Cafe de Wheels",
        "rest_desc": "시드니울루물루 해안가에 위치한 80년 전통의 전설적인 파이 수레 맛집입니다.",
        "location": "56 Cowper Wharf Roadway, Woolloomooloo NSW, Australia",
        "rating": "4.4 / 5.0"
    },
    "이집트": {
        "flag": "🇪🇬",
        "food": "쿠샤리 (Koshary)",
        "food_desc": "쌀, 마카로니, 렌틸콩, 병아리콩을 섞은 후 튀긴 양파와 매콤한 토마토소스를 올려 먹는 국민 요리입니다.",
        "restaurant": "Koshary Abou Tarek",
        "rest_desc": "카이로 중심가에 위치한 3층 규모의 쿠샤리 전용 대형 전문점입니다.",
        "location": "Champollion Rd, Marouf, Qasr El Nil, Cairo, Egypt",
        "rating": "4.6 / 5.0"
    },
    "모로코": {
        "flag": "🇲🇦",
        "food": "양고기 타진 (Tajine)",
        "food_desc": "원뿔 모양의 도자기 냄비에 양고기, 채소, 향신료, 말린 과일을 넣어 오랫동안 찌는 요리입니다.",
        "restaurant": "Le Jardin",
        "rest_desc": "마라케시 메디나 전통 정원 내에 위치하여 매력적인 분위기 속에서 타진을 즐길 수 있습니다.",
        "location": "32 Souk El Jdid, Marrakech, Morocco",
        "rating": "4.5 / 5.0"
    }
}

# --- UI 레이아웃 ---
st.title("🌏 세계 맛집 & 대표 음식 추천기")
st.caption("궁금한 국가 이름을 선택하거나 직접 입력해 보세요! 전 세계 25개국 핵심 맛집 정보를 제공합니다.")

st.divider()

col1, col2 = st.columns([1, 2])

with col1:
    st.subheader("🔍 국가 검색")
    
    # 드롭다운
    selected_country = st.selectbox(
        "목록에서 국가 선택",
        options=list(DATABASE.keys())
    )
    
    # 직접 입력
    custom_input = st.text_input("또는 국가 이름 직접 입력", placeholder="예: 한국, 프랑스, 멕시코...")
    
    # 최종 타깃
    target_country = custom_input.strip() if custom_input.strip() else selected_country

with col2:
    if target_country in DATABASE:
        data = DATABASE[target_country]
        
        st.subheader(f"{data['flag']} {target_country} 추천 정보")
        
        # 음식 카드
        with st.container(border=True):
            st.markdown(f"### 🍱 대표 음식: **{data['food']}**")
            st.write(data['food_desc'])
            
        # 맛집 카드
        with st.container(border=True):
            st.markdown(f"### 🏠 추천 맛집: **{data['restaurant']}**")
            st.write(data['rest_desc'])
            
            m1, m2 = st.columns(2)
            with m1:
                st.metric(label="📍 위치 / 주요 도시", value=data['location'].split(',')[0])
            with m2:
                st.metric(label="⭐ 평점", value=data['rating'])
                
            st.caption(f"상세 주소: {data['location']}")
            
    else:
        st.warning(f"⚠️ '{target_country}'에 대한 정보가 준비되지 않았습니다.")
        st.info("💡 지원하는 국가 목록:\n\n" + ", ".join(DATABASE.keys()))

st.divider()
st.caption("💡 외부 라이브러리 없이 Streamlit 표준 기능만으로 작동하므로 Streamlit Cloud에 오류 없이 바로 배포할 수 있습니다.")
