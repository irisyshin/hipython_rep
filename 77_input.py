import streamlit as st 

# checkbox 
active = st.checkbox('I agree')
if active:
    st.text('Welcome!')
    
# 함수, on_change=checkbox_write 

def checkbox_write():
    st.text('Welcome!')
    
st.checkbox('I agree!', on_change=checkbox_write)

# 세션-상태 값에 저장 
if 'checkbox_state' not in st.session_state:
    st.session_state.checkbox_state = False
    
def checkbox_write1():
    st.session_state.checkbox_state = True

if st.session_state.checkbox_state:
    st.write('응...')
    
st.checkbox('진짜???', on_change=checkbox_write1)

st.divider()
# toggle button
selected = st.toggle('Turn on the switch!!')
if selected:
    st.text('turn on!')
else:
    st.text('turn off!')    
    
# selectbox 선택지 
st.selectbox(
    'your selection is', 
    options=['1','2','3','4']
)

option =st.selectbox(
    '오늘의 점심 메뉴', 
    options=['김밥','떡볶이','우동','쫄면'], 
    index=None, 
    placeholder='네 개 중 하나만 골라!'
)
st.text(f'오늘의 점심은 -> {option}')

# radio
genre = st.radio(
    '무슨 영화를 좋아하세요',
    ['멜로', '스릴러', '판타지'],
    captions=['봄날은 간다', '트리거', '웬즈데이같은']
)

st.text(f'당신이 좋아하는 장르는 {genre}')

# multiselect
menus = st.multiselect(
    '먹고 싶은거 다 골라', ['김밥', '떡볶이', '우동', '쫄면'],
    
)
st.text(f'내가 선택한 메뉴는 {menus}')

#silder
score = st.slider('내 점수 선택', 0, 100, 1) # start, end, init-value 
st.text(f'score : {score}')

from datetime import time 
st_time, end_time = st.slider(
    '공부시간 선택',
    min_value= time(0), max_value=time(11),
    value=(time(8), time(18)),
    format='HH:mm'
)
st.text(f'공부시간 : {st_time} ~ {end_time}')

# text_input
txt1 = st.text_input('영화제목', placeholder='제목을 입력하세요')
txt2 = st.text_input('비밀번호', placeholder='비밀번호를 입력하세요', type='password')
st.text(f'텍스트 입력 결과: {txt1}, {txt2}')

# 파일업로더 
# 로컬에 있는 파일을 올리기
# 업로드한 파일은 사용자의 세션에 있습니다. 화면을 갱신하면 사라집니다.
# 서버에 저장하려면 병도로 구현해야 합니다.
# 데이터베이스에 저장하는 로직도 구현할 수 있습니다. 

file = st.file_uploader(
    '파일 선택', type='csv', accept_multiple_files=False 
)

if file is not None:
    df = pd.read_csv(file)
    st.write(df)

    with open(file.name, 'wb') as out:
        out.write(file.getbuffer())
        
# layout 요소 
# 요소를 밑에 붙이기 -> metric 그냥 혼자 쓰면 
# column 는 요소를 왼쪽 -> 오른쪽으로 배치할 수 있다.
col1, col2, col3  = st.columns(3)
with col1:
    st.metric(
        '오늘의 날씨',
        value='35도',
        delta='+3'
    )
with col2:
    st.metric(
        '미세먼지',
        value='좋음',
        delta='-30',
        delta_color='inverse'
    )

with col3:
    st.metric(
        '습도',
        value = '66%'
    )
    
##
st.markdown('---')

data ={
    '이름': ['홍길동', '김길동', '박길동'],
    '나이': [10,20,30]
}

import pandas as pd
df = pd.DataFrame(data)
# dataframe
st.dataframe(df)

# table
st.divider()
st.table(df)

#json
st.divider()
st.json(data)

# datafile.csv > load > table 출력 > px.box() > st.plotly_chart()

# import csv
CO2_df = pd.read_csv('./data/CO2_Emissions.csv')
st.dataframe(CO2_df)

import plotly.express as px
fig = px.box(CO2_df, x='Cylinders', y='CO2 Emissions(g/km)')
fig.update_xaxes(showline=True, linecolor= 'blue', linewidth=0.5, mirror=True)
fig.update_yaxes(showline=True, linecolor= 'blue', linewidth=0.5, mirror=True) # 매개변수로 설정
fig.update_layout(margin=dict(l=40, r=80, t=40, b=40))  # 오른쪽(r) 여백 늘리기

st.plotly_chart(fig)

import seaborn  as sns
import matplotlib.pyplot as plt


fig, ax = plt.subplots(figsize=(8, 4))  
sns.histplot(CO2_df, x='CO2 Emissions(g/km)', ax=ax)

# streamlit 대시보드에 표현
st.pyplot(fig,) #렌더링


# 위젯을 활용한 interactive 그래프 표현
x_options = ['Make', 'Vehicle Class', 'Model']
y_options = ['Fuel Consumption Comb (L/100 km)','CO2 Emissions(g/km)']
hue_options = ['Vehicle Class', 'Make']

x_option = st.selectbox(
    'Select X-axis',
    index=None,
    options=x_options
)

y_option = st.selectbox(
    'Select Y-axis',
    index=None,
    options=y_options
)

hue_option = st.selectbox(
    'Select Hue',
    index=None,
    options=hue_options
)

if (x_option != None) & (y_option != None):
    if hue_option != None:
        fig4 = px.box(
            data_frame=CO2_df, x=x_option, y=y_option,
            color=hue_option, width=500
        )
    else:
        fig4 = px.box(
            data_frame=CO2_df, x=x_option, y=y_option,
            width=500
        )
    st.plotly_chart(fig4)

