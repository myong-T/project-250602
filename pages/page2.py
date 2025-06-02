# page2.py

import streamlit as st
import openai

# API 키 설정 (secrets.toml 또는 직접 입력)
openai.api_key = st.secrets["openai"]["api_key"]

# 월 목록
months = [
    "1월", "2월", "3월", "4월", "5월", "6월",
    "7월", "8월", "9월", "10월", "11월", "12월"
]

st.title("🌸 월별 탄생화 설명 (AI 버전)")

# 사용자 입력
selected_month = st.selectbox("태어난 달을 선택하세요.", months)

if st.button("🌼 탄생화 설명 보기"):
    # 프롬프트 구성
    prompt = f"""
    너는 꽃 전문가야. 사용자가 '{selected_month}'을 선택했어.
    이 달의 대표 탄생화 이름, 꽃말, 상징적 의미, 계절적 특징 등을 아름답고 감성적으로 3~5문장 이내로 설명해줘.
    친근하고 따뜻한 말투로 알려줘.
    """

    with st.spinner("🌷 AI가 꽃말을 전해주는 중..."):
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "당신은 친절한 꽃 전문가입니다."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.8
        )

        flower_description = response['choices'][0]['message']['content']
        st.subheader(f"🌼 {selected_month}의 탄생화")
        st.write(flower_description)
