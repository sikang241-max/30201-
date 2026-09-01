import streamlit as st

# 페이지 기본 설정
st.set_page_config(
    page_title="Gourmet World - 세계 미식 여행",
    page_icon="✈️",
    layout="wide"
)

# --- 🎨 배경색 추가 및 럭셔리 트래블 매거진 디자인 CSS ---
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Noto+Sans+KR:wght@300;400;600;700;900&family=Poppins:wght@600;800&display=swap');

    /* 1. 전체 화면 배경색 설정 (따뜻한 고급 크림 톤 + 부드러운 그러데이션) */
    .stApp {
        background: linear-gradient(135deg, #FDFBF7 0%, #EEF2F5 100%) !important;
        font-family: 'Noto Sans KR', sans-serif;
    }

    /* 2. 상단 히어로 배너 (선명한 트로피컬 그러데이션 & 스티커 비행기) */
    .hero-banner {
        background: linear-gradient(135deg, #FF6B6B 0%, #556270 100%);
        border-radius: 28px;
        padding: 3.5rem 2rem;
        color: white;
        text-align: center;
        box-shadow: 0 20px 40px rgba(0, 0, 0, 0.12);
        margin-bottom: 2.5rem;
        position: relative;
        overflow: hidden;
    }
    .hero-title {
        font-family: 'Poppins', sans-serif;
        font-size: 3.4rem;
        font-weight: 800;
        letter-spacing: -1px;
        margin-bottom: 0.5rem;
        text-shadow: 0 4px 15px rgba(0,0,0,0.2);
    }
    .hero-sub {
        font-size: 1.2rem;
        font-weight: 300;
        opacity: 0.95;
    }

    /* 3. 사이드바 영역 전용 배경 스타일 */
    [data-testid="stSidebar"] {
        background-color: #F8FAF9 !important;
        border-right: 1px solid #E2E8F0;
    }
    
    .sidebar-card {
        background: rgba(255, 255, 255, 0.9);
        border-radius: 20px;
        padding: 1.5rem;
        border: 1px solid #E2E8F0;
        box-shadow: 0 8px 20px rgba(0, 0, 0, 0.03);
    }

    /* 4. 입체적인 스티커 태그 디자인 */
    .sticker-tag {
        display: inline-flex;
        align-items: center;
        gap: 6px;
        padding: 8px 16px;
        font-size: 0.9rem;
        font-weight: 700;
        border-radius: 30px;
        margin-right: 8px;
        margin-bottom: 8px;
        box-shadow: 0 4px 12px rgba(0, 0, 0, 0.06);
        transition: transform 0.2s ease;
    }
    .sticker-tag:hover {
        transform: translateY(-3px) scale(1.02);
    }
    
    .tag-asia { background: #E0F2FE; color: #0369A1; border: 1px solid #BAE6FD; }
    .tag-europe { background: #F3E8FF; color: #7E22CE; border: 1px solid #E9D5FF; }
    .tag-america { background: #DCFCE7; color: #15803D; border: 1px solid #BBF7D0; }
    .tag-other { background: #FEF3C7; color: #B45309; border: 1px solid #FDE68A; }
    .tag-star { background: #FFEDD5; color: #C2410C; border: 1px solid #FED7AA; }

    /* 5. 메인 입체 카드 (글래스모피즘 효과 + 따뜻한 흰색 카드) */
    .styled-card {
        background: rgba(255, 255, 255, 0.95);
        backdrop-filter: blur(10px);
        border-radius: 24px;
        padding: 2rem;
        border: 1px solid #E2E8F0;
        box-shadow: 0 12px 30px rgba(0, 0, 0, 0.05);
        margin-bottom: 1.8rem;
        transition: all 0.3s ease;
    }
    .styled-card:hover {
        transform: translateY(-6px);
        box-shadow: 0 20px 40px rgba(0, 0, 0, 0.09);
    }
    
    .card-label {
        font-size: 0.8rem;
        text-transform: uppercase;
        letter-spacing: 1.5px;
        color: #FF6B6B;
        font-weight: 800;
        margin-bottom: 6px;
    }
    .card-heading {
        font-size: 1.5rem;
        font-weight: 700;
        color: #1E293B;
        margin-bottom: 12px;
    }
    
    /* 이미지 모서리 라운딩 및 그림자 */
    .stImage img {
        border-radius: 20px !important;
        box-shadow: 0 10px 25px rgba(0, 0, 0, 0.1) !important;
    }
</style>
""", unsafe_allow_html=True)

# --- 📦 20개국 미식 데이터베이스 ---
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
    "베트남": {
        "flag": "🇻🇳", "continent": "아시아", "tag": "🌿 깊은 국물", "food": "소고기 쌀국수 (Pho Bo)",
        "image": "https://images.unsplash.com/photo-1582878826629-29b7ad1cdc43?auto=format&fit=crop&w=1000&q=80",
        "food_desc": "진하게 우려낸 소고기 육수에 신선한 허브와 쌀국수, 두툼한 양지머리가 어우러진 요리입니다.",
        "restaurant": "퍼10 리꾸옥수", "rest_desc": "하노이 3대 쌀국수 명가이자 미쉐린 빕구르망에 선정된 깔끔하고 진한 맛집입니다.",
        "location": "하노이 환끼엠 리꾸옥수 10", "rating": "4.6 / 5.0", "tip": "바삭하게 튀긴 빵 '꿔이'를 추가해 국물에 적셔 드셔보세요."
    },
    "대만": {
        "flag": "🇹🇼", "continent": "아시아", "tag": "🥩 진한 육수", "food": "대만 우육면",
        "image": "https://images.unsplash.com/photo-1541832676-9b763b0239ab?auto=format&fit=crop&w=1000&q=80",
        "food_desc": "두툼하고 부드러운 소고기 아롱사태와 한약재 향이 나는 칼칼한 소고기 육수의 면 요리입니다.",
        "restaurant": "임동방 우육면", "rest_desc": "타이베이 현지인과 여행자 모두에게 오랜 시간 사랑받은 우육면의 대명사입니다.",
        "location": "타이베이시 중산구 바더로 2단 325", "rating": "4.5 / 5.0", "tip": "테이블 위의 특제 우지(소기름) 버터를 한 스푼 넣으면 고소함이 늘어납니다."
    },
    "홍콩": {
        "flag": "🇭🇰", "continent": "아시아", "tag": "🥟 육즙 폭발", "food": "정통 딤섬",
        "image": "https://images.unsplash.com/photo-1563245372-f21724e3856d?auto=format&fit=crop&w=1000&q=80",
        "food_desc": "증기 찜기에 갓 쪄낸 하가우(새우딤섬), 쇼마이, 차슈바오 등 한 입의 행복을 주는 만두 요리입니다.",
        "restaurant": "팀호완 (Tim Ho Wan)", "rest_desc": "세계에서 가장 저렴한 미쉐린 스타 딤섬집으로 유명한 홍콩 대표 맛집입니다.",
        "location": "홍콩 삼수이포 후쿠윙 스트리트 9-11", "rating": "4.7 / 5.0", "tip": "달콤바삭한 차슈바오(BBQ 소보로 번)는 무조건 인당 1개 이상 필수!"
    },
    "싱가포르": {
        "flag": "🇸🇬", "continent": "아시아", "tag": "🦀 중독성 소스", "food": "칠리 크랩",
        "image": "https://images.unsplash.com/photo-1559847844-5315695dadae?auto=format&fit=crop&w=1000&q=80",
        "food_desc": "매콤달콤한 토마토 계란 소스에 살이 통통하게 오른 머드 크랩을 볶아낸 요리입니다.",
        "restaurant": "점보 씨푸드 (Jumbo Seafood)", "rest_desc": "클락키 강변 야경을 바라보며 시원한 맥주와 칠리크랩을 즐길 수 있는 필수 코스입니다.",
        "location": "싱가포르 업퍼 호성 로드 20", "rating": "4.6 / 5.0", "tip": "갓 튀겨낸 만두(번)를 꼭 추가해서 소스에 남김없이 비벼 드세요."
    },
    "인도": {
        "flag": "🇮🇳", "continent": "아시아", "tag": "🍛 풍부한 향신료", "food": "치킨 티카 마살라",
        "image": "https://images.unsplash.com/photo-1565557623262-b51c2513a641?auto=format&fit=crop&w=1000&q=80",
        "food_desc": "화덕에 구운 닭고기를 향긋한 마살라 향신료와 부드러운 커리 소스에 조려낸 대표 인도 요리입니다.",
        "restaurant": "Bukhara", "rest_desc": "뉴델리 ITC 마우리아 호텔에 위치한 세계적인 명성의 전통 북인도 요리 전문점입니다.",
        "location": "ITC Maurya, Diplomatic Enclave, New Delhi, India", "rating": "4.8 / 5.0", "tip": "갓 구워 나온 버터 난을 커리에 찍어 손으로 먹어야 제맛입니다."
    },
    "이탈리아": {
        "flag": "🇮🇹", "continent": "유럽", "tag": "🍕 정통 화덕", "food": "나폴리 피자",
        "image": "https://images.unsplash.com/photo-1513104890138-7c749659a591?auto=format&fit=crop&w=1000&q=80",
        "food_desc": "쫄깃한 도우 위에 신선한 토마토소스, 모짜렐라 치즈, 바질만 올려 화덕에 순식간에 구워냅니다.",
        "restaurant": "L'Antica Pizzeria da Michele", "rest_desc": "영화 <먹고 기도하고 사랑하라>에 나온 나폴리 최고의 전설적인 피제리아입니다.",
        "location": "Via Cesare Sersale, 1, Naples, Italy", "rating": "4.9 / 5.0", "tip": "메뉴는 마르게리타와 마리나라 단 2개뿐! 도우 끝까지 담백합니다."
    },
    "프랑스": {
        "flag": "🇫🇷", "continent": "유럽", "tag": "🍷 와인 스튜", "food": "뵈프 부르기뇽",
        "image": "https://images.unsplash.com/photo-1608897013039-887f21d8c804?auto=format&fit=crop&w=1000&q=80",
        "food_desc": "부르고뉴산 레드 와인에 소고기와 버섯, 야채를 넣어 몇 시간 동안 부드럽게 조려낸 정통 스튜입니다.",
        "restaurant": "Au Petit Riche", "rest_desc": "1854년에 문을 연 파리의 부티크 레스토랑으로 고풍스러운 분위기를 선사합니다.",
        "location": "25 Rue Le Peletier, Paris, France", "rating": "4.6 / 5.0", "tip": "갓 구운 겉바속촉 바게트에 진한 소스를 듬뿍 얹어 드세요."
    },
    "스페인": {
        "flag": "🇪🇸", "continent": "유럽", "tag": "🥘 향긋한 샤프란", "food": "해산물 빠에야",
        "image": "https://images.unsplash.com/photo-1534080564583-6be75777b70a?auto=format&fit=crop&w=1000&q=80",
        "food_desc": "귀한 샤프란 향이 배어있는 밥에 신선한 홍합, 새우, 오징어를 얹어 커다란 팬에 볶아낸 요리입니다.",
        "restaurant": "7 Portes", "rest_desc": "1836년 바르셀로나에 문을 연 역사적인 레스토랑으로 피카소도 자주 찾던 맛집입니다.",
        "location": "Passeig de Isabel II, 14, Barcelona, Spain", "rating": "4.7 / 5.0", "tip": "팬 바닥에 고소하게 눌러붙은 밥 '소카랏(Socarrat)'을 꼭 긁어 드세요!"
    },
    "독일": {
        "flag": "🇩🇪", "continent": "유럽", "tag": "🍺 맥주 절친", "food": "슈바인학세 (Schweinshaxe)",
        "image": "https://images.unsplash.com/photo-1544025162-d76694265947?auto=format&fit=crop&w=1000&q=80",
        "food_desc": "돼지 족발을 맥주와 향신료로 조린 뒤 오븐에 구워 겉은 과자처럼 바삭하고 속은 촉촉한 요리입니다.",
        "restaurant": "Hofbräuhaus München", "rest_desc": "뮌헨에 위치한 400년 역사의 세계에서 가장 유명한 독일 왕립 맥주집입니다.",
        "location": "Platzl 9, 80331 München, Germany", "rating": "4.6 / 5.0", "tip": "독일 정통 시원한 라거 맥주 1리터(Maß)와 함께 즐기는 것이 국룰입니다."
    },
    "영국": {
        "flag": "🇬🇧", "continent": "유럽", "tag": "🐟 바삭 담백", "food": "피시 앤 칩스",
        "image": "https://images.unsplash.com/photo-1579202673506-ca3ce28943ef?auto=format&fit=crop&w=1000&q=80",
        "food_desc": "두툼하고 부드러운 대구살을 반죽에 적셔 바삭하게 튀긴 후 감자튀김과 함께 먹는 영국 요리입니다.",
        "restaurant": "The Golden Hind", "rest_desc": "런던 마릴러본에서 1914년부터 100년 넘게 고집스럽게 맛을 이어온 전문점입니다.",
        "location": "73 Marylebone High St, London, UK", "rating": "4.5 / 5.0", "tip": "현지인처럼 몰트 식초(Malt Vinegar)를 살짝 뿌려 드시면 느끼함이 싹 사라집니다."
    },
    "스위스": {
        "flag": "🇨🇭", "continent": "유럽", "tag": "🧀 고소한 치즈", "food": "치즈 퐁뒤 (Cheese Fondue)",
        "image": "https://images.unsplash.com/photo-1541529086526-db283c563270?auto=format&fit=crop&w=1000&q=80",
        "food_desc": "에멘탈과 그뤼에르 치즈를 화이트 와인과 함께 녹여 빵이나 감자를 콕 찍어 먹는 따뜻한 겨울 음식입니다.",
        "restaurant": "Le Dézaley", "rest_desc": "취리히 구시가지 알트슈타트에 위치해 깊은 정통 치즈 퐁뒤의 풍미를 자랑하는 곳입니다.",
        "location": "Römergasse 7, 8001 Zürich, Switzerland", "rating": "4.5 / 5.0", "tip": "치즈 퐁뒤를 먹을 땐 차가운 물보다 따뜻한 차나 화이트 와인을 곁들이는 게 좋습니다."
    },
    "터키": {
        "flag": "🇹🇷", "continent": "중동/유럽", "tag": "🥙 불향 가득", "food": "도네르 케밥",
        "image": "https://images.unsplash.com/photo-1529006557810-274b9b2fc783?auto=format&fit=crop&w=1000&q=80",
        "food_desc": "회전 틀에서 불에 노릇하게 구워낸 고기를 얇게 쓸어 채소, 소스와 함께 난이나 빵에 싸 먹는 요리입니다.",
        "restaurant": "Hafız Mustafa 1864", "rest_desc": "이스탄불의 전통 케밥 및 160년 전통의 터키 디저트를 함께 맛볼 수 있는 명소입니다.",
        "location": "Hobyar, Hamidiye Cd. No:84, Fatih/İstanbul, Turkey", "rating": "4.7 / 5.0", "tip": "매콤한 고추 소스(Acı Biber)를 곁들이면 훨씬 깔끔합니다."
    },
    "미국": {
        "flag": "🇺🇸", "continent": "아메리카", "tag": "🍖 스모키 훈연", "food": "수제 바비큐 립",
        "image": "https://images.unsplash.com/photo-1544025162-d76694265947?auto=format&fit=crop&w=1000&q=80",
        "food_desc": "참나무 칩 훈연으로 10시간 이상 slow & low로 구워 부드럽고 스모키한 정통 바비큐입니다.",
        "restaurant": "Joe's Kansas City Bar-B-Que", "rest_desc": "주유소를 개조해 만든 이색 맛집으로 전 미 언론이 극찬한 바비큐 성지입니다.",
        "location": "3002 W 47th Ave, Kansas City, KS, USA", "rating": "4.8 / 5.0", "tip": "시그니처 메뉴인 Z-Man 샌드위치와 감자튀김 조합을 강력 추천합니다."
    },
    "멕시코": {
        "flag": "🇲🇽", "continent": "아메리카", "tag": "🌮 정통 스트리트", "food": "스트리트 타코 (Al Pastor)",
        "image": "https://images.unsplash.com/photo-1565299585323-38d6b0865b47?auto=format&fit=crop&w=1000&q=80",
        "food_desc": "옥수수 토르티야 위에 양념 고기, 상큼한 파인애플, 고수, 라임을 얹어 먹는 멕시코 국민 요리입니다.",
        "restaurant": "El Farolito", "rest_desc": "멕시코시티 현지인들이 최고의 타코로 첫손에 꼽는 찐 로컬 맛집입니다.",
        "location": "Altata 19, Mexico City, Mexico", "rating": "4.7 / 5.0", "tip": "생 라임즙을 듬뿍 짜 넣고 그린 살사 소스를 올려 드세요."
    },
    "브라질": {
        "flag": "🇧🇷", "continent": "아메리카", "tag": "🥩 육즙 폭발", "food": "슈하스코 (Churrasco)",
        "image": "https://images.unsplash.com/photo-1555939594-58d7cb561ad1?auto=format&fit=crop&w=1000&q=80",
        "food_desc": "소의 다양한 부위를 긴 꼬챙이에 꿰어 숯불에 구운 후 셰프가 직접 테이블에서 썰어주는 요리입니다.",
        "restaurant": "Fogo de Chão", "rest_desc": "리우데자네이루와 상파울루를 대표하는 프리미엄 정통 브라질리언 슈하스코 전문점입니다.",
        "location": "Botafogo, Rio de Janeiro, Brazil", "rating": "4.8 / 5.0", "tip": "우둔살 부위인 '피카냐(Picanha)'가 가장 부드럽고 고소합니다."
    },
    "페루": {
        "flag": "🇵🇪", "continent": "아메리카", "tag": "🍋 상큼 깔끔", "food": "세비체 (Ceviche)",
        "image": "https://images.unsplash.com/photo-1535399831218-d5bd36d1a6b3?auto=format&fit=crop&w=1000&q=80",
        "food_desc": "신선한 회를 상큼한 라임 즙, 양파, 고추에 절여 차갑게 먹는 남미 최고의 해산물 요리입니다.",
        "restaurant": "Central", "rest_desc": "2023 세계 50대 레스토랑 1위에 빛나는 리마의 미쉐린 3스타 페루 모던 다이닝입니다.",
        "location": "Av. Pedro de Osma 301, Barranco, Lima, Peru", "rating": "4.9 / 5.0", "tip": "라임 소스 국물인 '호랑이의 젖(Leche de Tigre)'까지 함께 마셔보세요."
    }
}

# --- 🎈 1. 상단 감성 히어로 배너 ---
st.markdown("""
<div class="hero-banner">
    <div style="font-size: 2.5rem; margin-bottom: 12px;">🛫 🍕 🍤 🌮 🍷</div>
    <div class="hero-title">GOURMET WORLD</div>
    <div class="hero-sub">전 세계 20개국 미식 여행 매거진 · 세계 요리 & 대표 명소 가이드</div>
</div>
""", unsafe_allow_html=True)

# --- 🧭 2. 레이아웃 분할 ---
col_sidebar, col_main = st.columns([1, 2.3], gap="large")

with col_sidebar:
    st.markdown('<div class="sidebar-card">', unsafe_allow_html=True)
    st.markdown("### 🗺️ 여행지 선택 (20개국)")
    
    selected_country = st.selectbox(
        "📌 목적지를 선택하세요",
        options=list(DATABASE.keys()),
        index=0
    )
    
    st.markdown("---")
    custom_search = st.text_input("🔍 국가 직접 검색", placeholder="예: 스페인, 브라질...")
    
    target = custom_search.strip() if custom_search.strip() else selected_country
    
    st.markdown("---")
    st.markdown("#### 🎨 대륙별 한눈에 보기")
    st.markdown("""
    * **🌏 아시아:** 한국, 일본, 중국, 태국, 베트남, 대만, 홍콩, 싱가포르, 인도
    * **🌍 유럽:** 이탈리아, 프랑스, 스페인, 독일, 영국, 스위스, 터키
    * **🌎 아메리카:** 미국, 멕시코, 브라질, 페루
    """)
    st.markdown('</div>', unsafe_allow_html=True)

with col_main:
    if target in DATABASE:
        item = DATABASE[target]
        
        # 대륙별 스티커 클래스 매핑
        cont = item['continent']
        continent_class = "tag-asia" if "아시아" in cont else "tag-europe" if "유럽" in cont else "tag-america" if "아메리카" in cont else "tag-other"
        
        # 타이틀 & 스티커 태그
        st.markdown(f"# {item['flag']} {target}")
        st.markdown(f"""
        <div>
            <span class="sticker-tag {continent_class}">📍 {item['continent']}</span>
            <span class="sticker-tag tag-other">{item['tag']}</span>
            <span class="sticker-tag tag-star">⭐ {item['rating']}</span>
        </div>
        """, unsafe_allow_html=True)
        
        st.write("") 
        
        # 📸 메인 음식 이미지
        st.image(item['image'], use_container_width=True, caption=f"📸 {target} 정통 대표 요리 - {item['food']}")
        
        # 🍱 1. 대표 음식 카드
        st.markdown(f"""
        <div class="styled-card">
            <div class="card-label">SIGNATURE DISH</div>
            <div class="card-heading">🍱 {item['food']}</div>
            <p style="color: #334155; line-height: 1.8; margin: 0; font-size: 1.05rem;">{item['food_desc']}</p>
        </div>
        """, unsafe_allow_html=True)
        
        # 🏠 2. 대표 맛집 카드
        st.markdown(f"""
        <div class="styled-card">
            <div class="card-label">MUST-VISIT RESTAURANT</div>
            <div class="card-heading">🏠 {item['restaurant']}</div>
            <p style="color: #334155; line-height: 1.8; margin-bottom: 14px; font-size: 1.02rem;">{item['rest_desc']}</p>
            <div style="background-color: #F1F5F9; padding: 12px 16px; border-radius: 12px; font-size: 0.9rem; color: #475569;">
                📍 <b>위치:</b> {item['location']}
            </div>
        </div>
        """, unsafe_allow_html=True)
        
        # 💡 3. 여행자 팁 (아코디언)
        with st.expander("💡 현지에서 실패 없는 꿀팁 알아보기"):
            st.info(f"👉 **{item['food']} 더 맛있게 먹는 법:**\n\n{item['tip']}")
            
    else:
        st.error(f"🔍 '{target}'에 대한 검색 결과를 찾지 못했습니다.")
        st.info("💡 **현재 등록된 20개 추천 국가:**\n\n" + ", ".join(DATABASE.keys()))

st.markdown("---")
st.caption("✨ Gourmet World Premium Edition | Powered by Streamlit & Custom Style")
