import streamlit as st

# 1. 페이지 기본 설정
st.set_page_config(
    page_title="세계 40개국 미식 여행 가이드",
    page_icon="✈️",
    layout="wide"
)

# 🔑 [필수] 구글 AI Studio에서 발급받은 API 키를 아래 따옴표 안에 넣으세요.
# 예시: GEMINI_API_KEY = "AIzaSy..."
GEMINI_API_KEY = "여기에_발급받은_API_KEY를_붙여넣으세요"

# 2. 인기 여행지 40개국 리스트
COUNTRIES = [
    "일본", "베트남", "태국", "대만", "필리핀", "싱가포르", "인도네시아", "말레이시아", 
    "홍콩", "마카오", "몽골", "라오스", "캄보디아", "인도", "미국", "캐나다", 
    "멕시코", "브라질", "아르헨티나", "영국", "프랑스", "이탈리아", "스페인", "포르투갈", 
    "독일", "스위스", "오스트리아", "체코", "헝가리", "크로아티아", "그리스", "튀르키예", 
    "네덜란드", "벨기에", "이집트", "모로코", "남아프리카공화국", "호주", "뉴질랜드", "괌"
]

# 3. LLM 프롬프트 템플릿 생성 함수
def generate_prompt(country_name):
    return f"""
당신은 전 세계 미식 문화에 정통한 글로벌 푸드 도슨트입니다.
사용자가 선택한 [{country_name}]의 대표 음식과 특징을 아래 양식에 맞추어 명확하고 흥미롭게 설명해 주세요.

[출력 양식]
# 🍽️ {country_name} 대표 미식 가이드

## 1. 대표 음식 (Signature Dishes)
- **[음식명 1 (원어/영문)]**: 음식에 대한 간략한 설명 (1~2문장)
- **[음식명 2 (원어/영문)]**: 음식에 대한 간략한 설명 (1~2문장)

## 2. 음식 문화 및 맛의 특징
- **주요 재료 및 향신료**: (예: 고수, 올리브유, 특정 양념 등)
- **맛의 스펙트럼**: (예: 매콤달콤함, 담백함, 감칠맛 등)
- **조리법 및 특징**: (이 국가만의 독특한 식문화나 조리 방식 2~3문장 설명)

## 3. 현지 미식 팁 (Tips)
- 현지에서 해당 음식을 더욱 맛있게 즐기는 방법이나 문화적 주의사항 1~2가지
"""

# 4. 메인 UI 화면
st.title("✈️ 세계 40개국 대표 음식 & 특징 가이드")
st.write("원하는 여행 국가를 선택하시면 해당 국가의 대표 음식과 미식 특징을 AI가 실시간으로 안내합니다.")

st.markdown("---")

# 5. 사이드바 구성 (국가 선택만 존재)
with st.sidebar:
    st.header("⚙️ 국가 선택")
    
    selected_country = st.selectbox(
        "여행할 국가를 선택하세요 (총 40개국)",
        COUNTRIES
    )
    
    search_btn = st.button("🍽️ 음식 정보 조회하기", use_container_width=True)

# 6. 버튼 클릭 시 자동 조회 및 결과 출력
if search_btn:
    if GEMINI_API_KEY == "여기에_발급받은_API_KEY를_붙여넣으세요" or not GEMINI_API_KEY:
        st.error("⚠️ 코드 상단의 `GEMINI_API_KEY` 변수에 본인의 Gemini API 키를 넣어야 정상 작동합니다.")
    else:
        prompt = generate_prompt(selected_country)
        result_text = ""
        
        with st.spinner(f"'{selected_country}'의 맛있는 음식 정보를 가져오는 중입니다..."):
            try:
                # 최신 SDK 사용
                from google import genai
                client = genai.Client(api_key=GEMINI_API_KEY)
                response = client.models.generate_content(
                    model='gemini-2.5-flash',
                    contents=prompt
                )
                result_text = response.text
            except Exception:
                try:
                    # 기존 SDK 호환
                    import google.generativeai as legacy_genai
                    legacy_genai.configure(api_key=GEMINI_API_KEY)
                    model = legacy_genai.GenerativeModel('gemini-2.5-flash')
                    response = model.generate_content(prompt)
                    result_text = response.text
                except Exception as e:
                    st.error(f"❌ 오류 발생: {e}")
            
            if result_text:
                st.markdown(result_text)
else:
    st.info("👈 왼쪽 사이드바에서 국가를 선택한 뒤 **[음식 정보 조회하기]** 버튼을 누르세요.")
