import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
# import seaborn as sns

def run_app_eda():
    st.title('PS4 & XBOX')
    
    df_ps4 = pd.read_csv('data/PS4_GamesSales_utf8.csv')
    df_xbox = pd.read_csv('data/XboxOne_GameSales_utf8.csv')  

    if st.checkbox('PS4 데이터프레임보기'):
        st.dataframe(df_ps4)
        st.subheader('기본 통계 데이터')
        st.dataframe(df_ps4.describe())

    if st.checkbox('XBOX 데이터프레임보기'):    
        st.dataframe(df_xbox)
        st.subheader('기본 통계 데이터')
        st.dataframe(df_xbox.describe())
    
    st.subheader('플랫폼별 퍼블리셔 확인')
    if st.checkbox('PS4 퍼블리셔 확인'):
        st.dataframe(df_ps4['Publisher'].unique())
    
        if st.checkbox('PS4 2013~2020 10개 이상 발매한 업체'):
            fig = plt.figure()

            x = ['BandaiNamco','SIE','Ubisoft','SquareEnix','KoeiTecmo','Activision','Capcom','WB','SCE','EA','NIS','EAsports','DeepSilver','PQube','Bethesda','505','Sega','THQ','Focus','Maximum','Konami','Kalypso','Unknown']
            y = [56,47,45,40,37,30,30,27,25,21,21,19,18,18,17,16,15,15,14,13,12,12,12]

            plt.bar(x,y)
            plt.title('2013~2020 PS4 10 Games Publisher') # 10개 이상 발매한 업체를 기준으로 작성
            plt.xlabel('Publisher')
            plt.ylabel('Published Count')
            plt.xticks(rotation=90)

            st.pyplot(fig)

    if st.checkbox('XBOX 퍼블리셔 확인'):
        st.dataframe(df_xbox['Publisher'].unique())

        if st.checkbox('XBOX 2013~2020 10개 이상 발매한 업체'):
            fig = plt.figure()

            x = ['Ubisoft','Microsoft','Activision','WB','EA','EAsports','BadaiNamco','Capcom','505 Games','THQ','Bethesda','SquareEnix','DeepSilver','Focus','Telltale']
            y = [44,31,29,26,22,19,19,19,16,16,15,15,13,11,10]

            plt.bar(x,y,color='green')
            plt.title('2013~2020 XBOX 10 Games Published') # 10개 이상 발매한 업체를 기준으로 작성
            plt.xlabel('Publisher')
            plt.ylabel('Published Count')
            plt.xticks(rotation=90)    

            st.pyplot(fig)