# st: 브라우저의 페이지 
import streamlit as st

# 타이틀 
st.title('Hello streamlit :)')
# 본문
st.write('hello!!!!!')

st.divider()

# input, 함수형 api
name = st.text_input('name: ')
if name:
    st.write(f'안녕하세요! {name}님 :)')
    
import pandas as pd
df = pd.read_csv('./data/ABNB_stock.csv')
print(df)
df