import streamlit as st


def run_app_home():

    st.subheader('환영합니다')
    st.text('2013~2020 PS4 & XBOX 판매된 게임의 판매량을 볼 수 있습니다')

    img_url='https://www.expertreviews.co.uk/sites/expertreviews/files/styles/er_main_wide/public/2018/09/xbox_one_vs_ps4_primary.jpg?itok=UsGJtLX-'
    st.image(img_url)
