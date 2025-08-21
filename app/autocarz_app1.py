import streamlit as st 
import pandas as pd 
from datetime import datetime, timedelta
import seaborn as sns
import plotly.express as px
import matplotlib.pyplot as plt 
import folium
from streamlit_folium import st_folium
import plotly.graph_objects as go
from streamlit_autorefresh import st_autorefresh
import time

# -------전체 레이아웃 폭 넓히기
st.set_page_config(page_title="야생동물 현황", layout="wide", initial_sidebar_state="expanded")

# 메인 컨테이너 폭/정렬 커스텀
st.markdown("""
    <style>
      .block-container{
        max-width:1500px;
        margin-left:0 !important;
        margin-right:auto !important;
        padding:1rem 1.25rem; /* top, lr */
      }
    </style>
    """,
    unsafe_allow_html=True
)
st.markdown(
    "<style>h1,h2,h3{letter-spacing:normal!important;line-height:1.2!important;}</style>",
    unsafe_allow_html=True
)

st.title('야생동물 현황 ')

# sidebar
st.sidebar.header('Menu')
selected_menu = st.sidebar.selectbox(
    '메뉴 선택', ['메인', '분석', '설정']
)

# 1초마다 새로고침
st_autorefresh(interval=1000, limit=None, key="time_refresh")

# 현재 날짜와 시간
now_date = datetime.now().strftime("%Y-%m-%d")
now_time = datetime.now().strftime("%H:%M:%S")

st.sidebar.markdown(
    f"""
    <div style="font-size:18px; font-weight:bold; margin-bottom:10px;">현재 시각</div>
    <div style="font-size:16px; color:#333;">{now_date} {now_time}</div>
    """,
    unsafe_allow_html=True
)

# data analysis 탭 함수
def make_anal_tab(data):
    # 인터랙티브 박스플롯
    x_options = ['Make', 'Vehicle Class', 'Model']
    y_options = ['Fuel Consumption Comb (L/100 km)','CO2 Emissions(g/km)']
    hue_options = ['Vehicle Class', 'Make', None]

    col1, col2, col3 = st.columns(3)
    with col1:
        x_option = st.selectbox('Select X-axis', options=x_options, index=0)
    with col2:
        y_option = st.selectbox('Select Y-axis', options=y_options, index=1)
    with col3:
        hue_option = st.selectbox('Select Hue', options=hue_options, index=0)

    if x_option and y_option:
        if hue_option:
            fig4 = px.box(data, x=x_option, y=y_option, color=hue_option, width=500)
        else:
            fig4 = px.box(data, x=x_option, y=y_option, width=500)
        st.plotly_chart(fig4, use_container_width=True)

CO2_df = pd.read_csv('hipython_rep/data/CO2_Emissions.csv')

# analysis tab
def analysis_tab(co2_df):
# tab 만들기 
    tab1, tab2, tab3 = st.tabs(['차트', '데이터', '설정'])
    with tab1:
        st.subheader('차트')
        # chart type, 속성 선택 할 수 있게 만들기 
        # 양쪽으로 비교 가능하게 
        left, right = st.columns([2,1])
        with left:
            make_anal_tab(CO2_df)      # ✅ 함수 호출은 tab1 안에서만
        with right:
            st.bar_chart({'데이터':[1,2,3,4,5]})
    
    with tab2:
        st.subheader('데이터')
        st.dataframe({'기준' : ['a','b','c','d','e'], '값':[1,2,3,4,5]})
    with tab3:
        st.subheader('체크박스')

def donut(pct, color='#178236'):
    fig = px.pie(
        values=[pct, 100-pct],
        hole=0.7,
        color_discrete_sequence=[color, "#e5e7eb"]
    )
    fig.update_traces(textinfo="none", sort=False, showlegend=False)
    fig.update_layout(
        annotations=[dict(text=f"{pct}%", x=0.5, y=0.5, showarrow=False, font_size=30)],
        margin=dict(l=0, r=0, t=0, b=0),
        width=200, height=200
    )
    return fig

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

today_count = len(time_loc_df)   # 또는 DB에서 불러오기, API 호출 등
delta_value = "+3"
# ----------------------------------------------

k1, k2, k3, kcolock = st.columns(4)
col1, col2 = st.columns(2)
# 페이지별 화면구성 
if selected_menu == '메인':
    with k1:\
        st.markdown(
        f"""
        <div style="font-size:28px; font-weight:bold; margin-bottom:10px;">오늘의 통계</div>
        <div style="font-size:48px; font-weight:bold; color:#333;">{today_count}건</div>
        <div style="font-size:20px; color:green;">{delta_value}</div>
        """,
        unsafe_allow_html=True)
    with k2:
        st.plotly_chart(donut(50, color="#ff7a3d"), use_container_width=False)
        st.caption("처리율")
    with k3:
        st.plotly_chart(donut(72, color="#10b981"), use_container_width=False)
        st.caption("성공률")
    with kcolock:
         now_date = datetime.now().strftime("%Y-%m-%d")   # 날짜
         now_time = datetime.now().strftime("%H:%M:%S")   # 시:분:초
         st.markdown(
            f"""
            <div style="font-size:24px; font-weight:bold; margin-bottom:10px;">현재 시간</div>
            <div style="font-size:28px; font-weight:bold; color:#2563eb;">{now_date}</div>
            <div style="font-size:36px; font-weight:bold; color:#2563eb;">{now_time}</div>
            """,
            unsafe_allow_html=True
        )
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
     # 아래 행: 메트릭 + 도넛 2개
elif selected_menu == '분석':
    st.subheader('분석보고서')
    analysis_tab(analysis_tab)
else:
    st.subheader('설정 변경')