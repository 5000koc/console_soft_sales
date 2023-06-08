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
    
        if st.checkbox('PS4 2013~2020 사이에 게임을 10개 이상 발매한 업체'):
            fig = plt.figure()

            x = ['BandaiNamco','SIE','Ubisoft','SquareEnix','KoeiTecmo','Activision','Capcom','WB','SCE','EA','NIS','EAsports','DeepSilver','PQube','Bethesda','505','Sega','THQ','Focus','Maximum','Konami','Kalypso','Unknown']
            y = [56,47,45,40,37,30,30,27,25,21,21,19,18,18,17,16,15,15,14,13,12,12,12]

            plt.bar(x,y)
            plt.title('PS4 10 Games Publisher') # 10개 이상 발매한 업체를 기준으로 작성
            plt.xlabel('Publisher')
            plt.ylabel('Published Count')
            plt.xticks(rotation=90)

            st.pyplot(fig)

    if st.checkbox('XBOX 퍼블리셔 확인'):
        st.dataframe(df_xbox['Publisher'].unique())

        if st.checkbox('XBOX 2013~2020 사이에 10개 이상 발매한 업체'):
            fig = plt.figure()

            x = ['Ubisoft','Microsoft','Activision','WB','EA','EAsports','BadaiNamco','Capcom','505 Games','THQ','Bethesda','SquareEnix','DeepSilver','Focus','Telltale']
            y = [44,31,29,26,22,19,19,19,16,16,15,15,13,11,10]

            plt.bar(x,y,color='green')
            plt.title('2013~2020 XBOX 10 Games Published') # 10개 이상 발매한 업체를 기준으로 작성
            plt.xlabel('Publisher')
            plt.ylabel('Published Count')
            plt.xticks(rotation=90)    

            st.pyplot(fig)

    st.subheader('플랫폼 별 발매현황')
    if st.checkbox('PS4 장르별 발매현황'):
        fig = plt.figure()

        x = ['Action','RPG','Shooter','Adventure','Sports','Misc','Racing','ACTADV','Platform','Fighting','Strategy','Simulation','Music','Puzzle','MMO','VNovel','Party']
        y = [205,107,75,71,69,55,48,38,33,32,25,21,18,10,8,8,2]


        plt.bar(x,y)
        plt.title('2013~2020 PS4 Genre Published')
        plt.xlabel('Genre')
        plt.ylabel('Published Count')
        plt.xticks(rotation = 90)

        st.pyplot(fig)

    if st.checkbox('XBOX 장르별 발매현황'):
        fig = plt.figure()

        x = ['Action','Shooter','Sports','Misc','Racing','Adventure','RPG','Platform','ACTADV','Simulation','Strategy','Fighting','Music','Puzzle','MMO','VNovel']
        y = [146,69,59,47,47,46,45,32,31,21,18,17,14,10,2,2]

        plt.bar(x,y,color='green')
        plt.title('2013~2020 XBOX Genre Published')
        plt.xlabel('Genre')
        plt.ylabel('Published Count')
        plt.xticks(rotation = 90)

        st.pyplot(fig)

    st.subheader('2013~2020 플랫폼별 발매된 게임갯수')
    if st.checkbox('PS4'):
        fig = plt.figure()
    
        x = ['2013','2014','2015','2016','2017','2018','2019','2020']
        y = [20,98,172,222,254,39,12,8]

        plt.bar(x,y)
        plt.title('2013~2020 PS4 Published')
        plt.xlabel('Year')
        plt.ylabel('Published Count')

        st.pyplot(fig)

    if st.checkbox('XBOX'):
        fig = plt.figure()

        x = ['2013','2014','2015','2016','2017','2018','2019','2020']
        y = [20,75,108,120,141,24,9,4]

        plt.bar(x,y,color='green')
        plt.title('2013~2020 XBOX Published')
        plt.xlabel('Year')
        plt.ylabel('Published Count')

        st.pyplot(fig)