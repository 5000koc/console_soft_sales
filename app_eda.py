import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

def run_app_eda():
    st.title('PS4 & XBOX')
    
    df_ps4 = pd.read_csv('data/PS4_GamesSales_utf8.csv')
    df_xbox = pd.read_csv('data/XboxOne_GameSales_utf8.csv')  

    if st.button('PS4 데이터프레임보기'):
        st.dataframe(df_ps4)
    if st.button('XBOX 데이터프레임보기'):    
        st.dataframe(df_xbox)
    
    

# fig = plt.figure()

#     x = ['BandaiNamco','SIE','Ubisoft','SquareEnix','KoeiTecmo','Activision','Capcom','WB','SCE','EA','NIS','EAsports','DeepSilver','PQube','Bethesda','505','Sega','THQ','Focus','Maximum','Konami','Kalypso','Unknown']
#     y = [56,47,45,40,37,30,30,27,25,21,21,19,18,18,17,16,15,15,14,13,12,12,12]


#     plt.bar(x,y)
#     plt.title('2013~2020 PS4 10 Games Publisher') # 10개 이상 발매한 업체를 기준으로 작성
#     plt.xlabel('Publisher')
#     plt.ylabel('Published Count')
#     plt.xticks(rotation=90)

#     st.pyplot(fig)