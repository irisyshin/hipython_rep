import streamlit as st 
import pandas as pd 
from datetime import datetime, timedelta
#import seaborn as sns
import plotly.express as px
import matplotlib.pyplot as plt 
import folium
from streamlit_folium import st_folium

st.title('야생동물 현황')

# sidebar 
st.sidebar.header('Menu')
selected_menu = st.sidebar.selectbox(
    '메뉴 선택', ['메인', '분석', '설정']
)

# 
# tab 만들기 
def make_anal_tab():
    
    tab1, tab2, tab3 = st.tabs(['차트', '데이터', '설정'])
    
    with tab1:
        st.subheader('차트')
        # chart type, 속성 선택 할 수 있게 만들기 
        # 양쪽으로 비교 가능하게 
        st.bar_chart({'데이터' : [1,2,3,4,5]})
    
    with tab2:
        st.subheader('차트')
        st.dataframe({'기준' : ['a','b','c','d','e'], '값':[1,2,3,4,5]})
    with tab3:
        st.subheader('체크박스')

col1, col2 = st.columns(2)

test_loc_data = {
    "lat": [37.5662952],
    "lon": [126.9779451]
}
test_loc_df = pd.DataFrame(test_loc_data)

# 시간, 주소, 상태 data 만들기 ----------------------------
# 시작 시간
start_time = datetime(2025, 8, 21, 16, 1)

# 12개의 샘플 데이터 생성
time_list = [start_time + timedelta(minutes=5*i) for i in range(12)]

address_list = [
    "서울시청", "광화문", "남대문", "종각역", "서울역", "명동역",
    "시청역", "덕수궁", "청계천", "숭례문", "을지로입구역", "동대문"
]

status_list = [
    "정상", "점검중", "완료", "정상", "지연", "정상",
    "점검중", "완료", "정상", "점검중", "정상", "완료"
]

time_loc_data = {
    "시간": time_list,
    "주소": address_list,
    "상태": status_list
}

time_loc_df = pd.DataFrame(time_loc_data)
# ----------------------------------------------

# 페이지별 화면구성 
if selected_menu == '메인':
    with col1:
        st.subheader('현재 상황: ')
        # folium 지도 생성
        map = folium.Map(location=test_loc_df, zoom_start=16)
        folium.Marker(location=test_loc_df, popup="서울시청").add_to(map)

        # Streamlit 앱에 표시
        st_map = st_folium(map, width=700, height=500)
    with col2:
        st.subheader('현재 상태: ')
        st.dataframe(time_loc_df)
    st.metric(
        '오늘의 통계',
        value='35건',
        delta='+3'
    )
elif selected_menu == '분석':
    st.subheader('분석보고서')
    make_anal_tab()
else:
    st.subheader('설정 변경')