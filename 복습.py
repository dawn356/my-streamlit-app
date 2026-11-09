import streamlit as st
st.header("문제1")
st.write("다리반 장애 였다가 괜찮아졌지만 **에게 차인친구는?")
정답3 = st.text_input("1번 정답 입력")
st.write(정답3)
if 정답3 == "씹주" or 정답3 == "좆주":
    st.success("정답입니다")
elif 정답3 =="":
    st.write("")
else:
    st.error("다시도전해주세요")


st.header("문제2")
st.image("1_sp.png")
st.write("이사진의 이름은?")
정답2 = st.text_input("2번 정답 입력")
st.write(정답2)
if 정답2 == "김민" or 정답2 == "씹민":
    st.success("정답입니다")
elif 정답2 =="":
    st.write("")
else:
    st.error("다시도전해주세요")




st.header("문제3")
st.write("어떤 누나에게 고백한다음 차인새끼는?")
정답1 = st.text_input("3번 정답 입력")
st.write(정답1)
if 정답1 == "근성진" or 정답1 == "씹성진" or 정답1 == "좆성진":
    st.success("정답입니다")
elif 정답1 =="":
    st.write("")
else:
    st.error("다시도전해주세요")


