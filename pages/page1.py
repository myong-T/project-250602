import streamlit as st
import openai
import datetime

# OpenAI API Key 설정
openai.api_key = st.secrets["openai_api_key"]

st.title("🌸 오늘의 꽃 추천")

# 사용자 입력
name = st.text_input("당신의 이름은?", "")
weather = st.selectbox("오늘의 날씨는 어때요?", ["맑음", "흐림", "비", "눈", "바람", "더움", "추움"])
situation = st.text_input("오늘 어떤 일이 있었나요?")
feeling = st.slider("지금 기분은 어떤가요?", 1, 10, 5)

# 날짜
today = datetime.date.today().strftime("%Y년 %m월 %d일")

if st.button("🌺 오늘의 꽃 추천 받기"):
    prompt = f"""
    오늘은 {today}입니다.
    이름: {name}
    날씨: {weather}
    오늘의 상황: {situation}
    기분 점수(1~10): {feeling}

    위의 정보를 바탕으로 오늘의 꽃을 추천해주세요.
    꽃 이름과 그 꽃이 어울리는 이유를 부드럽고 감성적인 문장으로 설명해주세요.
    """
    
    with st.spinner("꽃을 추천 중입니다... 🌷"):
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[{"role": "user", "content": prompt}]
        )
        flower_recommendation = response.choices[0].message["content"]
        st.success("🌼 오늘의 꽃은...")
        st.write(flower_recommendation)
