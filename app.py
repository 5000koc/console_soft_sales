import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from app_home import run_app_home
from app_eda import run_app_eda
from app_ml import run_app_ml

def main():
    st.title('2013~2020 PS4 & XBOX 게임 판매량 및 비교')

    img_url='https://www.expertreviews.co.uk/sites/expertreviews/files/styles/er_main_wide/public/2018/09/xbox_one_vs_ps4_primary.jpg?itok=UsGJtLX-'
    st.image(img_url)

    menu = ['Home','Data Analysis','Behind']
    choice = st.sidebar.selectbox('메뉴', menu)
    if choice == menu[0]:
        run_app_home()

    # elif choice == menu[1]:
    #     run_app_eda()
    
    # else:
    #     run_app_ml()




if __name__ == '__main__':
    main()
