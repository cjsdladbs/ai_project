import streamlit as st
st.title('로제마라떡볶이')
a=st.text_input('이름.')
b=st.selectbox('좋아하는 애니를 선택하세요',['그비돌','나히아','향꽃늠피','귀칼','톱맨','주술회전'])
if st.button('북딱 흔드르라'):
  st.write(a+'ㅎㅇ')
