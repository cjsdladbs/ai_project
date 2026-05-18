import streamlit as st
st.title('로제마라떡볶이')
a=st.text_input('이름.')
b=st.selectbox('선호하는음식',['치킨','피자','떡볶이','귀칼','톱맨','주술회전'])
if st.button('북딱 흔드르라'):
  st.write(a+'ㅎㅇ')
