import streamlit as st
st.title('나의 첫 웹 스트림릿 프로젝트!!')
name = st.text_input('프로젝트 이름을 입력해주세요 : ')
menu = st.selectbox('좋아하는 음식을 선택해주세요:', ['파이썬','C언어'])
if st.button('인사말 생성') : 
  st.write(name+' 라는 프로젝트를 만들거군요! '+menu+'을(를) 써서 말이죠, 흥미롭네요!')
