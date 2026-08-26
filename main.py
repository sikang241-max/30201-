import streamlit as st

# 페이지 기본 설정
st.set_page_config(
    page_title="어둠의 MBTI 진로 상담소",
    page_icon="💀",
    layout="centered"
)

# 헤더 영역
st.title("💀 어둠의 MBTI 진로 상담소 💀")
st.write("너의 운명은 이미 결정되어 있다... 네 유형을 선택해라.")

# 테마 이미지 (웹 상의 무서운 이미지 URL 활용)
scary_image_url = "https://images.unsplash.com/photo-1509248961158-e54f6934749c?q=80&w=800&auto=format&fit=crop"
st.image(scary_image_url, caption="너를 지켜보고 있다...", use_container_width=True)

st.markdown("---")

# MBTI별 진로 데이터
mbti_careers = {
    "INTJ": {"career": "AI 연구원, 사이버 보안 전문가, 데이터 분석가", "warning": "너의 치밀한 계획이 세상을 지배할지도 모른다..."},
    "INTP": {"career": "이론 물리학자, 소프트웨어 엔지니어, 철학자", "warning": "너무 깊은 생각은 심연을 불러오는 법."},
    "ENTJ": {"career": "기업 CEO, 경영 컨설턴트, 정치가", "warning": "권력을 향한 집착이 너를 삼키지 않도록 조심해라."},
    "ENTP": {"career": "벤처 창업가, 변호사, 기획자", "warning": "선 넘는 토론은 끝없는 혼돈을 가져온다."},
    "INFJ": {"career": "심리치료사, 작가, 인권 운동가", "warning": "타인의 어둠을 치유하다 너 자신이 물들 것이다."},
    "INFP": {"career": "소설가, 시인, 그래픽 디자이너", "warning": "너의 머릿속 환상이 현실을 침식하고 있다."},
    "ENFJ": {"career": "교사, 사회복지사, 인사팀 담당자", "warning": "모두를 구하려는 욕망이 너를 파멸로 이끈다."},
    "ENFP": {"career": "크리에이터, 마케터, 이벤트 기획자", "warning": "넘치는 에너지가 산산조각 나지 않게 잡아라."},
    "ISTJ": {"career": "회계사, 공무원, 법률 사무원", "warning": "규칙에 갇혀 영혼이 마모되어 가고 있다."},
    "ISFJ": {"career": "간호사, 초등교사, 사회복지사", "warning": "희생만 하다가는 껍데기만 남게 될 것이다."},
    "ESTJ": {"career": "프로젝트 매니저, 경찰관, 금융 분석가", "warning": "통제하려는 집착이 주변을 피로 물들인다."},
    "ESFJ": {"career": "승무원, 영양사, 고객만족 팀장", "warning": "타인의 시선에 갇힌 기괴한 인형이 되지 마라."},
    "ISTP": {"career": "기계 공학자, 응급구조사, 데이터 엔지니어", "warning": "침묵 속에서 다듬는 감정이 무기가 된다."},
    "ISFP": {"career": "화가, 사진작가, 수의사 테크니션", "warning": "조용한 감성 뒤에 숨겨진 그늘을 경계해라."},
    "ESTP": {"career": "응급의학 의사, 펀드매니저, 스포츠 감독", "warning": "자극만을 쫓다가는 벼랑 끝으로 떨어진다."},
    "ESFP": {"career": "배우, 이벤트 MC, 패션 디자이너", "warning": "조명이 꺼진 뒤 찾아올 지독한 고독을 견뎌라."}
}

# 사용자 입력 받기
selected_mbti = st.selectbox(
    "너의 MBTI 유형을 고르거라:",
    list(mbti_careers.keys())
)

# 결과 출력 버튼
if st.button("운명의 진로 확인하기 🔮"):
    info = mbti_careers[selected_mbti]
    
    st.subheader(f"🕯️ [{selected_mbti}] 너에게 지정된 지옥의 과업")
    st.success(f"**추천 진로:** {info['career']}")
    st.warning(f"**경고:** {info['warning']}")
