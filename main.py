import streamlit as st
st.title('로제마라떡볶이')
a=st.text_input('이름.')
b=st.selectbox('선호하는음식',['치킨','피자','떡볶이','스테이크','햄버거','파스타'])
if st.button('인사말 생성하기'):
  st.write(a+', hola! como tu estas?')
  st.info('반갑습니다')
  st.warning(b+', 이것을 선호하시나봐요?ㅋ')
