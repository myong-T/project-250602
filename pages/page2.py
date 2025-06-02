import streamlit as st
from openai import OpenAI
import datetime

# OpenAI API Key
try:
    OPENAI_KEY = st.secrets["openai"]["api_key"]
except KeyError:
    OPENAI_KEY = ""
    st.error("❌ OpenAI API 키가 설정되지 않았습니다.")
    st.stop()

client = OpenAI(api_key=OPENAI_KEY)

st.title("🎂 생일로 알아보는 탄생화")

# 생일 입력
birthdate = st.date_input("당신의 생일은 언제인가요?", datetime.date(2000, 1, 1))

# 월-일 추출
month = birthdate.month
day = birthdate.day

# 간단한 탄생화 사전 (예시)
birth_flowers = {
    (1, 1): "수선화",
    (2, 14): "붉은 장미",
    (3, 1): "프리지아",
    (4, 10): "튤립",
    (5, 5): "은방울꽃",
    (6, 21): "해바라기",
    (7, 7): "라벤더",
    (8, 15): "글라디올러스",
    (9, 9): "달리아",
    (10, 31): "금잔화",
    (11, 11): "국화",
    (12, 25): "포인세티아",
}

flower_name = birth_flowers.get((month, day), "🌸 해당 날짜의 탄생화 정보가 없습니다.")

# 결과 출력
if st.button("탄생화 알아보기"):
    if "없습니다" in flower_name:
        st.warning(flower_name)
    else:
        st.success(f"🎉 {month}월 {day}일의 탄생화는 '{flower_name}'입니다!")

        prompt = f"""
        {month}월 {day}일은 탄생화로 '{flower_name}'이(가) 알려져 있습니다.
        이 꽃의 특징과 의미, 꽃말을 감성적인 문장으로 설명해주세요.
        """

        with st.spinner("꽃말 설명 생성 중..."):
            try:
                response = client.chat.completions.create(
                    model="gpt-4",
                    messages=[{"role": "user", "content": prompt}]
                )
                explanation = response.choices[0].message.content
                st.write(explanation)
            except Exception as e:
                st.error(f"❌ 오류 발생: {e}")
