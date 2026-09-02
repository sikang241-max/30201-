import streamlit as st

# 페이지 기본 설정
st.set_page_config(
    page_title="세계 음식 여행 가이드",
    page_icon="🍔",
    layout="wide"
)

# 국가별 음식 데이터 구조화
FOOD_DATA = {
    "대한민국 🇰🇷": {
        "food_name": "비빔밥 (Bibimbap)",
        "image_url": "https://images.unsplash.com/photo-1553163147-622ab57be1c7?w=800",
        "description": "밥 위에 각종 나물, 고기, 고추장, 계란 후라이를 올려 쓱쓱 비벼 먹는 한국의 대표 건강식입니다.",
        "restaurant": "📍 **소문난 맛집**: 전주 중앙회관 / 서울 목멱산방",
        "how_to_eat": [
            "고추장은 처음부터 너무 많이 넣지 말고 반 숟가락씩 넣어가며 간을 맞춥니다.",
            "숟가락 대신 젓가락으로 비비면 밥알과 나물의 숨이 죽지 않아 더 식감이 살아납니다.",
            "돌솥비빔밥인 경우, 밑에 눌러붙은 누룽지는 가장 마지막에 긁어먹는 것이 별미입니다."
        ]
    },
    "일본 🇯🇵": {
        "food_name": "라멘 (Ramen)",
        "image_url": "https://images.unsplash.com/photo-1569718212165-3a8278d5f624?w=800",
        "description": "진하게 우려낸 돼지뼈나 닭육수에 차슈, 아지타마고(간장계란), 면을 더한 일본의 대표 면 요리입니다.",
        "restaurant": "📍 **소문난 맛집**: 도쿄 이치란 라멘 / 후쿠오카 신신라멘",
        "how_to_eat": [
            "면이 불기 전에 국물 맛을 먼저 한 숟가락 보고 깊은 풍미를 느낍니다.",
            "일본에서는 면을 후루룩(Slurping) 소리 내어 먹는 것이 면과 공기가 함께 들어와 풍미를 더해줍니다.",
            "중간쯤 먹었을 때 마늘이나 고추기름, 후추를 더해 변화된 맛을 즐깁니다."
        ]
    },
    "이탈리아 🇮🇹": {
        "food_name": "나폴리 피자 (Neapolitan Pizza)",
        "image_url": "https://images.unsplash.com/photo-1513104890138-7c749659a591?w=800",
        "description": "장작 화덕에서 고온으로 빠르게 구워내 겉은 바삭하고 속은 쫄깃한 이탈리아 정통 피자입니다.",
        "restaurant": "📍 **소문난 맛집**: 나폴리 L'Antica Pizzeria da Michele",
        "how_to_eat": [
            "포크와 칼을 사용하기보다 조각을 반으로 접어(지갑 모양) 토핑이 떨어지지 않게 손으로 먹습니다.",
            "크러스트(테두리) 부분인 '코르니초네'의 쫄깃함을 느끼며 끝까지 맛봅니다.",
            "신선한 바질과 모짜렐라 치즈가 식기 전에 따뜻할 때 바로 먹는 것이 좋습니다."
        ]
    },
    "베트남 🇻🇳": {
        "food_name": "쌀국수 (Pho)",
        "image_url": "https://images.unsplash.com/photo-1582878826629-29b7ad1cdc43?w=800",
        "description": "소고기나 닭고기로 푹 끓여낸 맑고 깊은 육수에 쌀면과 신선한 야채, 고수를 얹어 먹는 요리입니다.",
        "restaurant": "📍 **소문난 맛집**: 하노이 퍼틴(Pho Thin) / 호치민 퍼하아(Pho Hoa)",
        "how_to_eat": [
            "소스를 먼저 치지 말고, 레몬(라임)즙만 살짝 짜 넣은 순수한 국물 맛을 즐깁니다.",
            "숙주와 바질, 고수를 따뜻한 국물 아래로 푹 넣어 숨을 죽입니다.",
            "해선장 소스와 칠리 소스는 국물에 풀지 말고, 작은 종지에 1:1로 섞어 고기를 찍어 먹습니다."
        ]
    }
}

# 헤더 영역
st.title("🌏 세계 대표 음식 & 맛집 가이드")
st.markdown("원하는 국가를 선택하고, 대표 음식과 맛있게 먹는 팁을 확인해보세요!")
st.divider()

# 사이드바: 국가 선택
st.sidebar.header("🗺️ 국가 선택")
selected_country = st.sidebar.selectbox(
    "탐방할 국가를 선택하세요:",
    list(FOOD_DATA.keys())
)

# 선택된 국가의 데이터 불러오기
data = FOOD_DATA[selected_country]

# 메인 화면 레이아웃 (2개 컬럼 구성)
col1, col2 = st.columns([1, 1], gap="large")

with col1:
    st.subheader(f"🍽️ {selected_country} - {data['food_name']}")
    # use_container_width 적용
    st.image(data["image_url"], use_container_width=True)
    st.write(data["description"])
    st.info(data["restaurant"])

with col2:
    st.subheader("💡 맛있게 먹는 법 (How to Eat)")
    for i, tip in enumerate(data["how_to_eat"], 1):
        st.markdown(f"**{i}.** {tip}")

    st.divider()
    # 사용자 반응 섹션
    st.subheader("⭐ 이 음식 평가하기")
    rating = st.slider("이 음식을 얼마나 좋아하시나요?", 1, 5, 5)
    if st.button("평가 제출"):
        st.success(f"{data['food_name']}에 {rating}점을 남겨주셨습니다!")
