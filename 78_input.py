import streamlit as st
from PIL import Image
#sidebar, columns, tabs, expander

st.title('스트림릿 앱 페이지 구성하기')

st.sidebar.header('웰컴메뉴')
selected_menu = st.sidebar.selectbox(
    '메뉴선택', ['메인', '분석', '설정']
)
img1 = Image.open('./image/dog.jpg')
img2 = Image.open('./image/cat.png')

col1, col2  = st.columns(2)

def make_anal_tab():

    tab1, tab2, tab3 = st.tabs(['차트', '데이터', '설정'])
    with tab1:
        st.subheader('차트 탭')
        st.bar_chart({'데이터' : [1,2,3,4,5]})

    with tab2:
        st.subheader('차트 탭')
        st.dataframe({'기준' : ['a','b','c','d','e'], '값':[1,2,3,4,5]})

    # 3번쨰 설정 탭: 체크박스(활성화 여부), 슬라이더(업데이트 주기 sec)
    with tab3:
        st.subheader('체크박스')
        st.checkbox('자동 업데이트 활성화 여부')
        st.slider('업데이트 주기 (sec)', 0, 60, 30)
        
    st.divider()
    
#페이지별 화면구성 
if selected_menu == '메인':
    st.header('*메인페이지*')
    with col1:
        st.image(img1, width=300, caption='강아지!!!!!!')
    with col2:
        st.image(img2, width=300, caption='고양이!!!!!')

elif selected_menu == '분석':
    st.subheader('분석 보고서')
    make_anal_tab()
    
else:
    st.subheader('설정 변경')

if st.sidebar.button('선택'):
    st.sidebar.write('선택을 클릭하셨습니다. ')


# 슬라이드바 추가 0-100, 50
st.sidebar.slider('0-100', 0, 100, 50)

    
    # 확장영역 추가 
st.header('expander 추가')
with st.expander('숨긴 영역'):
    st.write('여기는 보이지 않습니다. 클릭해야 보입니다.')
        
