import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def run_app_ml():
    st.subheader('기종간 비교')

    if st.checkbox('PS4 & XBOX 1천만장 판매된 게임'):
        fig = plt.figure()
    
        x = ['GTA5','CoD:BO3','RDR2','CoD:WW2','FIFA18','FIFA17','Fallout4','CoD:IW','CoD:AW','BattleField 1','StarWars:BF2015','Minecraft','FIFA16','Unchrted4']
        y = [28.11,22.46,19.71,19.63,14.94,14.65,13.51,13.27,12.75,12.39,12.18,11.76,11.47,10.33]

        plt.bar(x,y,color='orange')
        plt.title('2013~2020 PS4 & XBOX 10million Global Total Sales Games')
        plt.xlabel('Game')
        plt.ylabel('Sales(million)')
        plt.xticks(rotation = 90)

        st.pyplot(fig)

    if st.checkbox('양기종간의 비교'):
        fig = plt.figure()

        data = {'Game':['GTA5','CoD:BO3','RDR2','CoD:WW2','FIFA18','FIFA17','Fallout4','CoD:IW','CoD:AW','BattleField 1','StarWars:BF2015','Minecraft','FIFA16','Unchrted4'],
        'PS4_sales': [19.39,15.09,13.94,13.4,11.8,10.94,8.48,8.48,7.53,7.26,8.03,6.33,8.22,10.33],
        'Xbox_sales':[8.72,7.37,5.77,6.23,3.14,3.71,5.03,4.79,5.22,5.13,4.15,5.43,3.25,0]} 
        df_total_global = pd.DataFrame(data)
        bar_width = 0.35
        index = range(len(df_total_global))
        plt.bar(index, df_total_global['PS4_sales'], width=bar_width, label='PS4')
        plt.bar([i + bar_width for i in index], df_total_global['Xbox_sales'], width=bar_width, label='XBOX', color='green')

        plt.xlabel('Game')
        plt.ylabel('Sales (million)')
        plt.title('PS4 & XBOX 10million Global Total Game Sales Comparison')
        plt.xticks([i + bar_width/2 for i in index], df_total_global['Game'],rotation = 90)
        plt.legend()

        st.pyplot(fig)

    

