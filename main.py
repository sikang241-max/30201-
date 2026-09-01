import json
import streamlit as st
from openai import OpenAI

# 페이지 기본 설정
st.set_page_config(
    page_title="AI 세계 맛집 & 대표 음식 추천기",
    page_icon="🍽️",
    layout="wide"
)

# 사이드바에서 API 키 입력 받기 (또는 st.secrets 활용 가능)
st.sidebar.title("⚙️ 설정")
api_key_input = st.sidebar.text_input(
    "OpenAI API Key 입력",
    type="password",
    help="sk-... 로 시작하는 OpenAI API 키를 입력하세요. 입력하지 않을 경우 기본 데이터베이스 내의 국가만 작동합니다."
)

# 기본 내장 데이터베이스 (API 키 없이도 동작 가능한 캐시 데이터)
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
    }
}


def fetch_country_info_from_ai(country_name: str, api_key: str):
    """OpenAI API를 사용하여 특정 국가/지역의 대표 음식과 맛집 추천 데이터를 JSON 형태로 반환"""
    client = OpenAI(api_key=api_key)

    prompt = f"""
    사용자가 검색한 국가/지역: "{country_name}"
    
    위 국가(또는 지역)의 대표 음식 1개와 그 음식을 가장 잘하는 유명 맛집 1곳을 추천해주세요.
    반드시 아래 JSON 형식으로만 정확히 응답해주세요. 불필요한 인사말이나 서론, 마크다운 코드 블록 표기(```json) 없이 Pure JSON만 출력하세요.

    {{
        "flag": "국가 국기 이모지",
        "food": "대표 음식 이름",
        "food_desc": "대표 음식에 대한 설명 (2~3문장)",
        "restaurant": "추천 맛집 이름",
        "rest_desc": "추천 맛집에 대한 설명 및 특징 (2~3문장)",
        "location": "맛집의 실제 도시 및 주소",
        "rating": "평점 (예: 4.6 / 5.0)"
    }}
    """

    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {
                    "role": "system",
                    "content": "You are an expert global food critic and travel guide.",
                },
                {"role": "user", "content": prompt},
            ],
            temperature=0.7,
        )

        content = response.choices[0].message.content.strip()
        # 혹시 마크다운 코드가 섞여 들어올 경우 제거
        if content.startswith("```"):
            content = content.replace("```json", "").replace("```", "").strip()

        data = json.loads(content)
        return data, None
    except Exception as e:
        return None, str(e)


# 헤더 영역
st.title("🤖 AI 세계 맛집 & 대표 음식 추천기")
st.caption(
    "궁금한 국가나 지역을 입력하세요. 내장 데이터에 없는 국가도 OpenAI가 실시간으로 분석해 추천해 줍니다."
)

st.divider()

# 레이아웃 구성
col1, col2 = st.columns([1, 2])

with col1:
    st.subheader("🔍 국가 / 지역 검색")

    selected_country = st.selectbox(
        "기존 등록 국가 선택", options=["직접 입력"] + list(DATABASE.keys())
    )

    custom_input = st.text_input(
        "국가/지역 직접 입력",
        placeholder="예: 멕시코, 칠레, 몽골, 아이슬란드...",
    )

    # 검색 대상 결정
    if custom_input.strip():
        target_country = custom_input.strip()
    elif selected_country != "직접 입력":
        target_country = selected_country
    else:
        target_country = ""

    search_button = st.button("🚀 맛집 검색하기", use_container_width=True)

with col2:
    if target_country:
        # 1. 내장 데이터베이스에 있는 경우
        if target_country in DATABASE:
            data = DATABASE[target_country]
            st.success(f"📌 내장 데이터베이스에서 '{target_country}' 정보를 가져왔습니다.")

            st.subheader(f"{data['flag']} {target_country} 추천 결과")

            with st.container(border=True):
                st.markdown(f"### 🍱 대표 음식: **{data['food']}**")
                st.write(data['food_desc'])

            with st.container(border=True):
                st.markdown(f"### 🏠 추천 맛집: **{data['restaurant']}**")
                st.write(data['rest_desc'])

                m1, m2 = st.columns(2)
                with m1:
                    st.metric(
                        label="📍 위치/주소",
                        value=data["location"].split(",")[0],
                    )
                with m2:
                    st.metric(label="⭐ 평점", value=data["rating"])

                st.caption(f"전체 주소: {data['location']}")

        # 2. 내장 데이터베이스에 없어 OpenAI API를 사용하는 경우
        else:
            if not api_key_input:
                st.warning(
                    f"⚠️ '{target_country}'은(는) 기본 데이터베이스에 없는 국가입니다."
                )
                st.info(
                    "👈 왼쪽 사이드바에 **OpenAI API Key**를 입력하시면 AI가 실시간으로 해당 국가의 맛집을 분석해 드립니다!"
                )
            else:
                with st.spinner(
                    f"🤖 AI가 '{target_country}'의 대표 음식과 맛집을 분석 중입니다..."
                ):
                    data, error = fetch_country_info_from_ai(
                        target_country, api_key_input
                    )

                if error:
                    st.error(f"❌ 데이터 분석 중 오류가 발생했습니다: {error}")
                elif data:
                    st.success(
                        f"✨ AI가 '{target_country}'의 맞춤 정보를 실시간 생성했습니다!"
                    )

                    st.subheader(
                        f"{data.get('flag', '🌐')} {target_country} 추천 결과"
                    )

                    with st.container(border=True):
                        st.markdown(
                            f"### 🍱 대표 음식: **{data.get('food', '정보 없음')}**"
                        )
                        st.write(data.get("food_desc", ""))

                    with st.container(border=True):
                        st.markdown(
                            f"### 🏠 추천 맛집: **{data.get('restaurant', '정보 없음')}**"
                        )
                        st.write(data.get("rest_desc", ""))

                        m1, m2 = st.columns(2)
                        with m1:
                            st.metric(
                                label="📍 위치/주소",
                                value=data.get("location", "정보 없음").split(
                                    ","
                                )[0],
                            )
                        with m2:
                            st.metric(
                                label="⭐ 평점",
                                value=data.get("rating", "4.5 / 5.0"),
                            )

                        st.caption(
                            f"전체 주소: {data.get('location', '정보 없음')}"
                        )

    else:
        st.info("👈 왼쪽에 국가 이름을 입력하거나 선택한 후 검색 버튼을 눌러주세요.")

st.divider()
st.caption(
    "💡 설치 필요 라이브러리: `pip install streamlit openai` | 실행 방법: `streamlit run app.py`"
)
