import streamlit as st
import pandas as pd 

###################### button click
st.button('Reset', type='primary')

def button_write():
    st.write('버튼이 출력되었습니다')
    
st.button('activate', on_click=button_write)

clicked = st.button('activate2', type='primary')
if clicked:
    st.write('버튼2가 클릭되었습니다.')

######################

st.header('같은 버튼 여러개 만들기')
# key 다 다르게 해야 에러 안남 
# activate button 5개 primary
# key=act_btn_{i}
for i in range(5):
    st.button(f'activate{i+1}',type='primary', key=i) 

######################

st.divider()

st.title('Title')
st.header('header')
st.subheader('subheader')

# write, text 차이 
# write안에 다양한 요소 넣기 가능, 색도 줄수있고 동적으로 만드는것도 가능 
# text는 그냥 text 
st.write('write 문장입니다.')
st.text('text 문장압니다.')
# 색도 줄 수 있다!!!
# ___ or \n : 줄바꿈
# **text**: bold, *text*: 이텔릭체 
st.markdown(
    '''
    여기는 메인 텍스트입니다. \n
    퇴근하고 잠자고 싶다.   
    :red[Red], :blue[Blue], :green[Green]   
    **굵게도 할 수 있고** *이탤릭체*로도 표현 가능!!   
    '''
)
# 코드 제공하고 싶을떄, 다른 언어로 주고 싶을떄 : language='python'
st.code(
    '''
    st.title('Title')
    st.header('header')
    st.subheader('subheader')
    ''',
    language='python'
)

st.divider()

# label, type?
st.button('Hello') #secondary type - deafult
st.button('Hello', type='primary')
st.button('Sleepy', type='primary', icon='😴')
st.button('Sleepy', type='primary', icon='😴', key=1)
# 에러!! 버튼의 label.type까지 똑같으멵 에러!!!
st.button('GO HOME', type='primary', icon='😴', disabled=True)

