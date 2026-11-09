import streamlit as st
st.header("문제1")
st.write("다리반 장애 였다가 괜찮아졌지만 **에게 차인친구는?")
정답3 = st.text_input("2번 정답 입력")
st.write(정답3)
if 정답3 == "씹주" or 정답3 == "좆주":
    st.success("정답입니다")
elif 정답3 =="":
    st.write("")
else:
    st.error("다시도전해주세요")