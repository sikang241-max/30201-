import streamlit as st
import json
import os

# 페이지 기본 설정
st.set_page_config(
    page_title="193개국 세계 음식 여행 가이드",
    page_icon="🍔",
    layout="wide"
)

# JSON 데이터 로드 함수
@st.cache_data
def load_food_data():
    file_path = "countries_food.json"
    if os.path.exists(file_path):
        with open(file_path, "r", encoding="utf-8") as f:
            return json.load(f)
    return {}

FOOD_DATA = load_food_data()

# 헤더 영역
st.title("🌏 193개국 세계 대표 음식 & 맛집 가이드")
st.markdown("원하는 대륙과 국가를 선택하여 전 세계 미식을 탐방해보세요!")
st.divider()

if not FOOD_DATA:
    st.error("`countries_food.json` 파일이 존재하지 않거나 데이터를 불러올 수 없습니다.")
else:
    # 사이드바: 검색 및 필터링
    st.sidebar.header("🗺️ 국가 검색 및 필터")
    
    # 대륙 목록 추출
    continents = ["전체"] + sorted(list(set(info.get("continent", "기타") for info in FOOD_DATA.values())))
    selected_continent = st.sidebar.selectbox("대륙 선택:", continents)
    
    # 대륙별 필터링 적용
    if selected_continent == "전체":
        filtered_countries = list(FOOD_DATA.keys())
    else:
        filtered_countries = [
            country for country, info in FOOD_DATA.items() 
            if info.get("continent") == selected_continent
        ]

    # 국가 선택
    selected_country = st.sidebar.selectbox(
        f"탐방할 국가 선택 ({len(filtered_countries)}개국):",
        filtered_countries
    )

    # 선택된 국가의 데이터 불러오기
    data = FOOD_DATA[selected_country]

    # 메인 화면 레이아웃
    col1, col2 = st.columns([1, 1], gap="large")

    with col1:
        st.subheader(f"🍽️ {selected_country} - {data.get('food_name', '대표 음식')}")
        
        if "image_url" in data and data["image_url"]:
            st.image(data["image_url"], use_container_width=True)
            
        st.write(data.get("description", "설명이 없습니다."))
        st.info(data.get("restaurant", "맛집 정보가 없습니다."))

    with col2:
        st.subheader("💡 맛있게 먹는 법 (How to Eat)")
        how_to_eat = data.get("how_to_eat", [])
        if how_to_eat:
            for i, tip in enumerate(how_to_eat, 1):
                st.markdown(f"**{i}.** {tip}")
        else:
            st.write("먹는 팁 정보가 준비 중입니다.")

        st.divider()
        st.subheader("⭐ 이 음식 평가하기")
        rating = st.slider("이 음식을 얼마나 좋아하시나요?", 1, 5, 5)
        if st.button("평가 제출"):
            st.success(f"{data.get('food_name')}에 {rating}점을 남겨주셨습니다!")
