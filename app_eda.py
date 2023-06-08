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

    st.subheader('지역별 최다판매량')
    st.text('PS4')
    if st.checkbox('PS4 북미지역에서 250만장 이상 판매된 게임'):
        fig = plt.figure()

        x = ['CoD:BO3','GTA5','RDR2','CoD:WW2','Uncahrted4','SpiderMan','StarWars:BF2015','CoD:IW','Fallout4','CoD:AW','God of War','The Last of Us','NBA2016','Uncharted Collection']
        y = [6.18,6.06,5.26,4.67,4.49,3.64,3.31,3.11,2.91,2.84,2.83,2.7,2.56,2.55]

        plt.bar(x,y)
        plt.title('2013~2020 PS4 North America 2.5milion Sales Games ')
        plt.xlabel('Game')
        plt.ylabel('Sales(million)')
        plt.xticks(rotation = 90)

        st.pyplot(fig)
    
    if st.checkbox('PS4 유럽지역에서 300만장 이상 판매된 게임'):
        fig = plt.figure()

        x = ['GTA5','FIFA18','FIFA17','RDR2','CoD:WW2','CoD:BO3','FIFA16','FIFA15','Fallout4','Uncharted4','CoD:IW','Battlefield 1','SpiderMan','CoD:AW','StarWars:BF2015','Minecraft']
        y = [9.71,8.64,7.95,6.21,6.21,6.05,5.77,4.49,3.97,3.93,3.83,3.65,3.39,3.34,3.19,3.13]

        plt.bar(x,y)
        plt.title('2013~2020 PS4 Europe 3million Sales Games ')
        plt.xlabel('Game')
        plt.ylabel('Sales(million)')
        plt.xticks(rotation = 90)
    
        st.pyplot(fig)

    if st.checkbox('PS4 일본지역에서 50만장 이상 판매된 게임'):
        fig = plt.figure()

        x = ['MonsterHunter:W','DragonQuest11','Final Fantasy XV','GTA5','MGS5','Persona5','DarkSouls3','NierAutomata','Knack','CoD:BO3','Biohazard7']
        y = [2.17,1.43,1.05,0.6,0.5,0.48,0.44,0.42,0.42,0.41,0.41]

        plt.bar(x,y)
        plt.title('2013~2020 PS4 Japan Half-million Sales Games ')
        plt.xlabel('Game')
        plt.ylabel('Sales(million)')
        plt.xticks(rotation = 90)    

        st.pyplot(fig)

    if st.checkbox('PS4 그외의 지역에서 100만장 이상 판매된 게임'):
        fig = plt.figure()

        x = ['GTA5','CoD:BO3','CoD:WW2','RDR2','FIFA18','Uncharted4','FIFA17','SpiderMan','CoD:IW','Fallout4','StarWars:BF2015','FIFA16','CoD:AW','Battlefield 1','The Last of Us','God of War']
        y = [3.02,2.44,2.26,2.12,1.73,1.7,1.61,1.41,1.36,1.34,1.3,1.23,1.22,1.12,1.1,1.02]

        plt.bar(x,y)
        plt.title('2013~2020 PS4 Other Country million Sales Games')
        plt.xlabel('Game')
        plt.ylabel('Sales(million)')
        plt.xticks(rotation = 90)

        st.pyplot(fig)

    st.text('XBOX')
    if st.checkbox('XBOX 북미지역 2백만장 이상 판매된 게임'):
        fig = plt.figure()

        x = ['GTA5','CoD:BO3','RDR2','CoD:WW2','Battlefield 1','CoD:AW','Minecraft','Fallout4','Halo5','CoD:IW','Gears of War:UE','SrarWars:BF2015','Assassin Creed:U','Destiny','Gears of War4','NFL17','NFL16','Halo:Collection','NBA2016']
        y = [4.7,4.63,3.76,3.75,3.37,3.25,3.23,2.94,2.94,2.91,2.88,2.49,2.34,2.17,2.17,2.14,2.13,2.06,2.01]

        plt.bar(x,y,color='green')
        plt.title('2013~2020 XBOX North America 2million Sales Games')
        plt.xlabel('Game')
        plt.ylabel('Sales(million)')
        plt.xticks(rotation = 90)

        st.pyplot(fig)

    if st.checkbox('XBOX 유럽지역 1백만장 이상 판매된 게임'):
        fig = plt.figure()

        x = ['GTA5','FIFA17','FIFA16','CoD:BO3','ForzaHorizon3','FIFA18','CoD:WW2','Minecraft','Fallout4','Halo5','CoD:AW','RDR2','CoD:IW','FIFA15','Battlefield 1','StarWars:BF2015','Halo:Collection']
        y = [3.25,2.4,2.1,2.04,1.96,1.92,1.91,1.71,1.62,1.49,1.49,1.47,1.44,1.39,1.26,1.26,1.04]

        plt.bar(x,y,color='green')
        plt.title('2013~2020 XBOX Europe Million Sales Games')
        plt.xlabel('Game')
        plt.ylabel('Sales(million)')
        plt.xticks(rotation = 90)

        st.pyplot(fig)

    if st.checkbox('XBOX 일본지역 판매된 게임'):
        fig = plt.figure()

        x = ['ForzaMotorsport6','Titanfall','Tombraider:Rise','Halo5','Halo:Collection','ForzaHorizon3','Farcry4','KinectSports','CoD:BO3','PsychoPass','MGS5','StarWars:BF2015','Fallout4','Battlefield 1','Quantumbreak']
        y = [0.04,0.04,0.03,0.03,0.03,0.02,0.02,0.02,0.02,0.02,0.02,0.02,0.02,0.02,0.02]

        plt.bar(x,y,color='green')
        plt.title('2013~2020 XBOX Japan Sales Games')
        plt.xlabel('Game')
        plt.ylabel('Sales(million)')
        plt.xticks(rotation = 90)

        st.pyplot(fig)

    if st.checkbox('XBOX 그외의 지역 판매된 게임'):
        fig = plt.figure()

        x = ['GTA5','CoD:BO3','CoD:WW2','RDR2','Minecraft','CoD:AW','Battlefield 1','Fallout4','Halo5','CoD:IW','StarWars:BF2015','Gears of War:UE','Assassin Creed:U','Gears of War4','Destiny','ForzaHorizon3','Halo:Collection']
        y = [0.76,0.68,0.57,0.54,0.49,0.48,0.48,0.45,0.45,0.44,0.38,0.37,0.34,0.32,0.32,0.32,0.31]

        plt.bar(x,y, color='green')
        plt.title('2013~2020 XBOX Other Country Sales Games')
        plt.xlabel('Game')
        plt.ylabel('Sales(million)')
        plt.xticks(rotation = 90)

        st.pyplot(fig)

    st.subheader('플랫폼별 전세계 최다 판매량')
    if st.checkbox('PS4 전세계 1천만장 이상 판매된 게임'):
        fig = plt.figure()

        x = ['GTA5','CoD:BO3','RDR2','CoD:WW2','FIFA18','FIFA17','Uncharted4']
        y = [19.39,15.09,13.94,13.4,11.8,10.94,10.33]

        plt.bar(x,y)
        plt.title('2013~2020 PS4 10million Global Sales Games')
        plt.xlabel('Game')
        plt.ylabel('Sales(million)')
        plt.xticks(rotation = 90)

        st.pyplot(fig)
    
    if st.checkbox('XBOX 전세계 5백만장 이상 판매된 게임'):
        fig = plt.figure()

        x = ['GTA5','CoD:BO3','CoD:WW2','RDR2','Minecraft','CoD:AW','Battlefied ONE','Fallout4']
        y = [8.72,7.37,6.23,5.77,5.43,5.22,5.13,5.03]

        plt.bar(x,y,color='green')
        plt.title('2013~2020 XBOX 5million Global Sales Games')
        plt.xlabel('Game')
        plt.ylabel('Sales(million)')
        plt.xticks(rotation = 90)

        st.pyplot(fig)

    
