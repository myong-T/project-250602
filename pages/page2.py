# page2.py

import streamlit as st
from openai import OpenAI

# OpenAI API Key 설정
try:
    OPENAI_KEY = st.secrets["openai"]["api_key"]
except KeyError:
    OPENAI_KEY = ""
    st.error("❌ OpenAI API 키가 설정되지 않았습니다.")
    st.stop()

# OpenAI 클라이언트 생성 (v1.82.1 방식)
client = OpenAI(api_key=OPENAI_KEY)

# 월 목록
months = [
    "1월", "2월", "3월", "4월", "5월", "6월",
    "7월", "8월", "9월", "10월", "11월", "12월"
]

st.title("🌸 월별 탄생화 설명 (AI 버전)")

# 사용자 입력
selected_month = st.selectbox("태어난 달을 선택하세요.", months)

if st.button("🌼 탄생화 설명 보기"):
    prompt = f"""
    너는 꽃 전문가야. 사용자가 '{selected_month}'을 선택했어.
    이 달의 대표 탄생화 이름, 꽃말, 상징적 의미, 계절적 특징 등을 아름답고 감성적으로 3~5문장 이내로 설명해줘.
    친근하고 따뜻한 말투로 알려줘.
    """

    with st.spinner("🌷 AI가 꽃말을 전해주는 중..."):
        response = client.chat.completions.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "당신은 친절한 꽃 전문가입니다."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.8
        )

        flower_description = response.choices[0].message.content
        st.subheader(f"🌼 {selected_month}의 탄생화")
        st.write(flower_description)
