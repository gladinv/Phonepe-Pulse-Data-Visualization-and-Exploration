#!/usr/bin/env python
# coding: utf-8

# In[1]:


import streamlit as st
from PIL import Image
import os
import json
from streamlit_option_menu import option_menu
import pandas as pd
import sqlite3
import plotly.express as px
#import requests
#os.walk

# To clone the data directly from github to current working directory
#response = requests.get('https://api.github.com/repos/PhonePe/pulse')
#repo = response.json()
#clone_url = repo['clone_url']
#repo_name = "pulse"
#clone_dir = os.path.join(os.getcwd(), repo_name)


phn=Image.open('images/phonepe-logo.png')
phn1=Image.open('images/phonepe.png')
mypic=Image.open('images/me.png')
video_file = open('videos/Phonepe.mp4', 'rb')
video1 = video_file.read()
video_file1=open('videos/phonepevid.mp4','rb')
video2=video_file1.read()
st.set_page_config(page_title='PhonePe Pulse',page_icon=phn,layout='wide')
st.title(':violet[ PhonePe Pulse Data Visualization ]')

# reading the data from csv files
df_aggregated_transactions=pd.read_csv('Aggregated_Transactions.csv')

# TO GET THE DATA-FRAME OF AGGREGATED <--> USER
df_aggregated_users=pd.read_csv('Aggregated_Users.csv')

# TO GET THE DATA-FRAME OF MAP <--> TRANSACTION
df_map_transactions=pd.read_csv('Map_Transactions.csv')

# TO GET THE DATA-FRAME OF MAP <--> USER
df_map_users=pd.read_csv('Map_Users.csv')

# TO GET THE DATA-FRAME OF TOP <--> TRANSACTION
df_top_transactions=pd.read_csv('Top_Transactions.csv')

# TO GET THE DATA-FRAME OF TOP <--> USER
df_top_users=pd.read_csv('Top_Users.csv')

# CHECKING FOR MISSING VALUES,NULL VALUES
# df_aggregated_transactions.info()
# df_aggregated_users.info()
# df_map_transactions.info()
# df_map_users.info()
# df_top_transactions.info()
# df_top_users.info()

# CREATING CONNECTION WITH SQL SERVER
connection = sqlite3.connect("phonepe pulse.db")
cursor = connection.cursor()

# Inserting each Data frame into sql server
df_aggregated_transactions.to_sql('aggregated_transactions', connection, if_exists='replace')
df_aggregated_users.to_sql('aggregated_users', connection, if_exists='replace')
df_map_transactions.to_sql('map_transactions', connection, if_exists='replace')
df_map_users.to_sql('map_users', connection, if_exists='replace')
df_top_transactions.to_sql('top_transactions', connection, if_exists='replace')
df_top_users.to_sql('top_users', connection, if_exists='replace')

# Creating Options in app
#with st.sidebar:
SELECT = option_menu(
        menu_title = None,
        options = ["About","Search","Home","Basic insights","Contact"],
        icons =["bar-chart","search","house","toggles","at"],
        default_index=2,
        orientation="horizontal",
        styles={
            "container": {"padding": "0!important", "background-color": "white","size":"cover"},
            "icon": {"color": "black", "font-size": "20px"},
            "nav-link": {"font-size": "20px", "text-align": "center", "margin": "-2px", "--hover-color": "#6F36AD"},
            "nav-link-selected": {"background-color": "#6F36AD"}
        }

    )


if SELECT == "Basic insights":
    st.title("BASIC INSIGHTS")
    #st.write("----")
    st.subheader("Let's know some basic insights about the data")
    options = ["--select--","Top 10 states based on year and amount of transaction","Least 10 states based on type and amount of transaction",
               "Top 10 mobile brands based on percentage of transaction","Top 10 Registered-users based on States and District(pincode)",
               "Top 10 Districts based on states and amount of transaction","Least 10 Districts based on states and amount of transaction",
               "Least 10 registered-users based on Districts and states","Top 10 transactions_type based on states and transaction_amount"]
    select = st.selectbox("Select the option",options)
    if select=="Top 10 states based on year and amount of transaction":
        cursor.execute("SELECT DISTINCT State,Transaction_amount,Year,Quarter FROM top_transactions GROUP BY State ORDER BY transaction_amount DESC LIMIT 10");
        df = pd.DataFrame(cursor.fetchall(),columns=['State','Transaction_amount','Year','Quarter'])
        col1,col2 = st.columns(2)
        with col1:
            st.write(df)
        with col2:
            st.subheader("Top 10 states based on type and amount of transaction")
            fig=px.bar(df,x="State",y="Transaction_amount")
            tab1, tab2 = st.tabs(["Streamlit theme (default)", "Plotly native theme"])
            with tab1:
                st.plotly_chart(fig, theme="streamlit", use_container_width=True)
            with tab2:
                st.plotly_chart(fig, theme=None, use_container_width=True)

    elif select=="Least 10 states based on type and amount of transaction":
        cursor.execute("SELECT DISTINCT State,Transaction_amount,Year,Quarter FROM top_transactions GROUP BY State ORDER BY transaction_amount ASC LIMIT 10");
        df = pd.DataFrame(cursor.fetchall(),columns=['State','Transaction_amount','Year','Quarter'])
        col1,col2 = st.columns(2)
        with col1:
            st.write(df)
        with col2:
            st.subheader("Least 10 states based on type and amount of transaction")
            fig=px.bar(df,x="State",y="Transaction_amount")
            tab1, tab2 = st.tabs(["Streamlit theme (default)", "Plotly native theme"])
            with tab1:
                st.plotly_chart(fig, theme="streamlit", use_container_width=True)
            with tab2:
                st.plotly_chart(fig, theme=None, use_container_width=True)

    elif select=="Top 10 mobile brands based on percentage of transaction":
        cursor.execute("SELECT DISTINCT brands,Percentage FROM aggregated_users GROUP BY brands ORDER BY Percentage DESC LIMIT 10");
        df = pd.DataFrame(cursor.fetchall(),columns=['brands','Percentage'])
        col1,col2 = st.columns(2)
        with col1:
            st.write(df)
        with col2:
            st.subheader("Top 10 mobile brands based on percentage of transaction")
            fig=px.bar(df,x="brands",y="Percentage")
            tab1, tab2 = st.tabs(["Streamlit theme (default)", "Plotly native theme"])
            with tab1:
                st.plotly_chart(fig, theme="streamlit", use_container_width=True)
            with tab2:
                st.plotly_chart(fig, theme=None, use_container_width=True)

    elif select=="Top 10 Registered-users based on States and District(pincode)":
        cursor.execute("SELECT DISTINCT State,District,RegisteredUser FROM top_users GROUP BY State,District ORDER BY RegisteredUser DESC LIMIT 10");
        df = pd.DataFrame(cursor.fetchall(),columns=['State','District','RegisteredUser'])
        col1,col2 = st.columns(2)
        with col1:
            st.write(df)
        with col2:
            st.subheader("Top 10 Registered-users based on States and District(pincode)")
            fig=px.bar(df,x="State",y="RegisteredUser")
            tab1, tab2 = st.tabs(["Streamlit theme (default)", "Plotly native theme"])
            with tab1:
                st.plotly_chart(fig, theme="streamlit", use_container_width=True)
            with tab2:
                st.plotly_chart(fig, theme=None, use_container_width=True)

    elif select=="Top 10 Districts based on states and amount of transaction":
        cursor.execute("SELECT DISTINCT State,District,amount FROM map_transactions GROUP BY State,District ORDER BY amount DESC LIMIT 10");
        df = pd.DataFrame(cursor.fetchall(),columns=['State','District','Transaction_amount'])
        col1,col2 = st.columns(2)
        with col1:
            st.write(df)
        with col2:
            st.subheader("Top 10 Districts based on states and amount of transaction")
            fig=px.bar(df,x="State",y="Transaction_amount")
            tab1, tab2 = st.tabs(["Streamlit theme (default)", "Plotly native theme"])
            with tab1:
                st.plotly_chart(fig, theme="streamlit", use_container_width=True)
            with tab2:
                st.plotly_chart(fig, theme=None, use_container_width=True)

    elif select=="Least 10 Districts based on states and amount of transaction":
        cursor.execute("SELECT DISTINCT State,District,amount FROM map_transactions GROUP BY State,District ORDER BY amount ASC LIMIT 10");
        df = pd.DataFrame(cursor.fetchall(),columns=['State','District','Transaction_amount'])
        col1,col2 = st.columns(2)
        with col1:
            st.write(df)
        with col2:
            st.subheader("Least 10 Districts based on states and amount of transaction")
            fig=px.bar(df,x="State",y="Transaction_amount")
            tab1, tab2 = st.tabs(["Streamlit theme (default)", "Plotly native theme"])
            with tab1:
                st.plotly_chart(fig, theme="streamlit", use_container_width=True)
            with tab2:
                st.plotly_chart(fig, theme=None, use_container_width=True)

    elif select=="Least 10 registered-users based on Districts and states":
        cursor.execute("SELECT DISTINCT State,District,RegisteredUser FROM top_users GROUP BY State,District ORDER BY RegisteredUser ASC LIMIT 10");
        df = pd.DataFrame(cursor.fetchall(),columns=['State','District','RegisteredUser'])
        col1,col2 = st.columns(2)
        with col1:
            st.write(df)
        with col2:
            st.subheader("Least 10 registered-users based on Districts and states")
            fig=px.bar(df,x="State",y="RegisteredUser")
            tab1, tab2 = st.tabs(["Streamlit theme (default)", "Plotly native theme"])
            with tab1:
                st.plotly_chart(fig, theme="streamlit", use_container_width=True)
            with tab2:
                st.plotly_chart(fig, theme=None, use_container_width=True)

    elif select=="Top 10 transactions_type based on states and transaction_amount":
        cursor.execute("SELECT DISTINCT State,Transaction_type,Transaction_amount FROM aggregated_transactions GROUP BY State,Transaction_type ORDER BY Transaction_amount DESC LIMIT 10");
        df = pd.DataFrame(cursor.fetchall(),columns=['State','Transaction_type','Transaction_amount'])
        col1,col2 = st.columns(2)
        with col1:
            st.write(df)
        with col2:
            st.subheader("Top 10 transactions_type based on states and transaction_amount")
            fig=px.bar(df,x="State",y="Transaction_amount")
            tab1, tab2 = st.tabs(["Streamlit theme (default)", "Plotly native theme"])
            with tab1:
                st.plotly_chart(fig, theme="streamlit", use_container_width=True)
            with tab2:
                st.plotly_chart(fig, theme=None, use_container_width=True)

if SELECT == "Home":
    st.subheader(
        "PhonePe is an Indian digital payments and financial technology company headquartered in Bengaluru, Karnataka, India. PhonePe was founded in December 2015, by Sameer Nigam, Rahul Chari and Burzin Engineer. The PhonePe app, based on the Unified Payments Interface (UPI), went live in August 2016. It is owned by Flipkart, a subsidiary of Walmart.")
    col1,col2, = st.columns(2)
    with col1:
        st.image(phn)
    with col2:
        st.video(video1)
        st.download_button("DOWNLOAD THE APP NOW", "https://www.phonepe.com/app-download/")

if SELECT == "About":
    st.subheader("The Indian digital payments story has truly captured the world's imagination."
                 " From the largest towns to the remotest villages, there is a payments revolution being driven by the penetration of mobile phones, mobile internet and state-of-the-art payments infrastructure built as Public Goods championed by the central bank and the government."
                 " Founded in December 2015, PhonePe has been a strong beneficiary of the API driven digitisation of payments in India. When we started, we were constantly looking for granular and definitive data sources on digital payments in India. "
                 "PhonePe Pulse is our way of giving back to the digital payments ecosystem.")
    col1,col2 = st.columns(2)
    with col1:
        st.image(phn1)
        st.download_button("DOWNLOAD THE APP NOW", "https://www.phonepe.com/app-download/")

    with col2:
        st.subheader("Phonepe Now Everywhere..!")
        st.video(video2)

if SELECT == "Contact":
    name = " GLADIN VARGHESE "
    mail = (f'{"Mail :"}  {"gladinv@gmail.com"}')
    social_media = {"GITHUB": "https://github.com/gladinv ",
                    "LINKEDIN": "https://www.linkedin.com/in/gladin/"
                    }
    col1,  col2 = st.columns(2)
    with col1:
        st.image(mypic)
    with col2:
        st.title(name)
        st.subheader("Data Science Professional")
        st.write("---")
        st.subheader(mail)
    #st.write("#")
    cols = st.columns(len(social_media))
    for index, (platform, link) in enumerate(social_media.items()):
        cols[index].write(f"[{platform}]({link})")

if SELECT =="Search":
    Topic = ["","Brand","District","Registered-users","Top-Transactions","Transaction-Type"]
    choice_topic = st.selectbox("Search by",Topic)

#creating functions for query search in sqlite to get the data
    def type_(type):
        cursor.execute(f"SELECT DISTINCT State,Quarter,Year,Transaction_type,Transaction_amount FROM aggregated_transactions WHERE Transaction_type = '{type}' ORDER BY State,Quarter,Year");
        df = pd.DataFrame(cursor.fetchall(), columns=['State','Quarter', 'Year', 'Transaction_type', 'Transaction_amount'])
        return df
    def type_year(year,type):
        cursor.execute(f"SELECT DISTINCT State,Year,Quarter,Transaction_type,Transaction_amount FROM aggregated_transactions WHERE Year = '{year}' AND Transaction_type = '{type}' ORDER BY State,Quarter,Year");
        df = pd.DataFrame(cursor.fetchall(), columns=['State', 'Year',"Quarter", 'Transaction_type', 'Transaction_amount'])
        return df
    def type_state(state,year,type):
        cursor.execute(f"SELECT DISTINCT State,Year,Quarter,Transaction_type,Transaction_amount FROM aggregated_transactions WHERE State = '{state}' AND Transaction_type = '{type}' And Year = '{year}' ORDER BY State,Quarter,Year");
        df = pd.DataFrame(cursor.fetchall(), columns=['State', 'Year',"Quarter", 'Transaction_type', 'Transaction_amount'])
        return df
    def district_choice_state(_state):
        cursor.execute(f"SELECT DISTINCT State,Year,Quarter,District,amount FROM map_transactions WHERE State = '{_state}' ORDER BY State,Year,Quarter,District");
        df = pd.DataFrame(cursor.fetchall(), columns=['State', 'Year',"Quarter", 'District', 'amount'])
        return df
    def dist_year_state(year,_state):
        cursor.execute(f"SELECT DISTINCT State,Year,Quarter,District,amount FROM map_transactions WHERE Year = '{year}' AND State = '{_state}' ORDER BY State,Year,Quarter,District");
        df = pd.DataFrame(cursor.fetchall(), columns=['State', 'Year',"Quarter", 'District', 'amount'])
        return df
    def district_year_state(_dist,year,_state):
        cursor.execute(f"SELECT DISTINCT State,Year,Quarter,District,amount FROM map_transactions WHERE District = '{_dist}' AND State = '{_state}' AND Year = '{year}' ORDER BY State,Year,Quarter,District");
        df = pd.DataFrame(cursor.fetchall(), columns=['State', 'Year',"Quarter", 'District', 'amount'])
        return df
    def brand_(brand_type):
        cursor.execute(f"SELECT State,Year,Quarter,brands,Percentage FROM aggregated_users WHERE brands='{brand_type}' ORDER BY State,Year,Quarter,brands,Percentage DESC");
        df = pd.DataFrame(cursor.fetchall(), columns=['State', 'Year',"Quarter", 'brands', 'Percentage'])
        return df
    def brand_year(brand_type,year):
        cursor.execute(f"SELECT State,Year,Quarter,brands,Percentage FROM aggregated_users WHERE Year = '{year}' AND brands='{brand_type}' ORDER BY State,Year,Quarter,brands,Percentage DESC");
        df = pd.DataFrame(cursor.fetchall(), columns=['State', 'Year',"Quarter", 'brands', 'Percentage'])
        return df
    def brand_state(state,brand_type,year):
        cursor.execute(f"SELECT State,Year,Quarter,brands,Percentage FROM aggregated_users WHERE State = '{state}' AND brands='{brand_type}' AND Year = '{year}' ORDER BY State,Year,Quarter,brands,Percentage DESC");
        df = pd.DataFrame(cursor.fetchall(), columns=['State', 'Year',"Quarter", 'brands', 'Percentage'])
        return df
    def transaction_state(_state):
        cursor.execute(f"SELECT State,Year,Quarter,District,Transaction_count,Transaction_amount FROM top_transactions WHERE State = '{_state}' GROUP BY State,Year,Quarter")
        df = pd.DataFrame(cursor.fetchall(), columns=['State', 'Year',"Quarter", 'District', 'Transaction_count', 'Transaction_amount'])
        return df
    def transaction_year(_state,_year):
        cursor.execute(f"SELECT State,Year,Quarter,District,Transaction_count,Transaction_amount FROM top_transactions WHERE Year = '{_year}' AND State = '{_state}' GROUP BY State,Year,Quarter")
        df = pd.DataFrame(cursor.fetchall(), columns=['State', 'Year',"Quarter", 'District', 'Transaction_count', 'Transaction_amount'])
        return df
    def transaction_quarter(_state,_year,_quarter):
        cursor.execute(f"SELECT State,Year,Quarter,District,Transaction_count,Transaction_amount FROM top_transactions WHERE Year = '{_year}' AND Quarter = '{_quarter}' AND State = '{_state}' GROUP BY State,Year,Quarter")
        df = pd.DataFrame(cursor.fetchall(), columns=['State', 'Year',"Quarter", 'District', 'Transaction_count', 'Transaction_amount'])
        return df
    def registered_user_state(_state):
        cursor.execute(f"SELECT State,Year,Quarter,District,RegisteredUser FROM map_users WHERE State = '{_state}' ORDER BY State,Year,Quarter,District")
        df = pd.DataFrame(cursor.fetchall(), columns=['State', 'Year',"Quarter", 'District', 'RegisteredUser'])
        return df
    def registered_user_year(_state,_year):
        cursor.execute(f"SELECT State,Year,Quarter,District,RegisteredUser FROM map_users WHERE Year = '{_year}' AND State = '{_state}' ORDER BY State,Year,Quarter,District")
        df = pd.DataFrame(cursor.fetchall(), columns=['State', 'Year',"Quarter", 'District', 'RegisteredUser'])
        return df
    def registered_user_district(_state,_year,_dist):
        cursor.execute(f"SELECT State,Year,Quarter,District,RegisteredUser FROM map_users WHERE Year = '{_year}' AND State = '{_state}' AND District = '{_dist}' ORDER BY State,Year,Quarter,District")
        df = pd.DataFrame(cursor.fetchall(), columns=['State', 'Year',"Quarter", 'District', 'RegisteredUser'])
        return df
    
    if choice_topic == "Transaction-Type":
        select = st.selectbox('SELECT VIEW', ['Tabular view', 'Plotly View'], 0)
        if select=='Tabular view':
            col1, col2, col3 = st.columns(3)
            with col1:
                st.subheader(" SELECT TYPE OF TRANSACTION ")
                transaction_type = st.selectbox("search by", ["Peer-to-peer payments","Merchant payments", "Financial Services","Recharge & bill payments", "Others"], 0)
            with col2:
                st.subheader("SELECT YEAR ")
                choice_year = st.selectbox("Year", ["", "2018", "2019", "2020", "2021", "2022"], 0)
            with col3:
                st.subheader(" SELECT STATES ")
                menu_state = ['', 'andaman-&-nicobar-islands', 'andhra-pradesh', 'arunachal-pradesh', 'assam', 'bihar', 'chandigarh', 'chhattisgarh','dadra-&-nagar-haveli-&-daman-&-diu', 
                              'delhi', 'goa', 'gujarat', 'haryana', 'himachal-pradesh', 'jammu-&-kashmir', 'jharkhand', 'karnataka', 'kerala', 'ladakh','lakshadweep', 'madhya-pradesh', 
                              'maharashtra', 'manipur', 'meghalaya', 'mizoram', 'nagaland', 'odisha', 'puducherry', 'punjab', 'rajasthan', 'sikkim', 
                              'tamil-nadu', 'telangana', 'tripura', 'uttar-pradesh', 'uttarakhand', 'west-bengal']
                choice_state = st.selectbox("State", menu_state, 0)

            if transaction_type:
                col1, col2, col3, = st.columns(3)
                with col1:
                    st.subheader(f'Table view of {transaction_type}')
                    st.write(type_(transaction_type))

            if transaction_type and choice_year:
                with col2:
                    st.subheader(f' in {choice_year}')
                    st.write(type_year(choice_year, transaction_type))
            if transaction_type and choice_state and choice_year:
                with col3:
                    st.subheader(f' in {choice_state}')
                    st.write(type_state(choice_state, choice_year, transaction_type))
        else:
            col1, col2,col3 = st.columns(3)
            with col1:
                st.subheader(" SELECT TYPE OF TRANSACTION ")
                transaction_type = st.selectbox("search by", ["Peer-to-peer payments","Merchant payments", "Financial Services","Recharge & bill payments", "Others"], 0)
                if transaction_type:
                    df = type_(transaction_type)
                    fig = px.bar(df, x="State", y="Transaction_amount", title=f'Plotly view of {transaction_type}',color='Year')
                    st.plotly_chart(fig, theme=None, use_container_width=True)
            with col2:
                st.subheader(" SELECT YEAR ")
                choice_year = st.selectbox("Year", ["", "2018", "2019", "2020", "2021", "2022"], 0)
                if transaction_type and choice_year:
                    df = type_year(choice_year, transaction_type)
                    fig = px.bar(df, x="State", y="Transaction_amount",title=f"Plotly view of {transaction_type} in {choice_year}",color='Quarter')
                    st.plotly_chart(fig, theme=None, use_container_width=True)
            with col3:
                st.subheader(" SELECT STATE ")
                menu_state = ['', 'andaman-&-nicobar-islands', 'andhra-pradesh', 'arunachal-pradesh', 'assam', 'bihar', 'chandigarh', 'chhattisgarh','dadra-&-nagar-haveli-&-daman-&-diu', 
                              'delhi', 'goa', 'gujarat', 'haryana', 'himachal-pradesh', 'jammu-&-kashmir', 'jharkhand', 'karnataka', 'kerala', 'ladakh','lakshadweep', 'madhya-pradesh', 
                              'maharashtra', 'manipur', 'meghalaya', 'mizoram', 'nagaland', 'odisha', 'puducherry', 'punjab', 'rajasthan', 'sikkim', 
                              'tamil-nadu', 'telangana', 'tripura', 'uttar-pradesh', 'uttarakhand', 'west-bengal']
                choice_state = st.selectbox("State", menu_state, 0)
                if transaction_type and choice_state and choice_year:
                    df = type_state(choice_state, choice_year, transaction_type)
                    fig = px.bar(df, x="Quarter", y="Transaction_amount",title=f" {transaction_type} in {choice_year} at {choice_state}",color="Quarter")
                    st.plotly_chart(fig, theme=None, use_container_width=True)
    if choice_topic == "District":
        select = st.selectbox('View', ['Tabular view', 'Plotly View'], 0)
        if select == 'Tabular view':
            col1, col2, col3 = st.columns(3)
            with col1:
                st.subheader(" SELECT STATE ")
                menu_state =['', 'andaman-&-nicobar-islands', 'andhra-pradesh', 'arunachal-pradesh', 'assam', 'bihar', 'chandigarh', 'chhattisgarh', 'dadra-&-nagar-haveli-&-daman-&-diu',
                             'delhi', 'goa', 'gujarat', 'haryana', 'himachal-pradesh', 'jammu-&-kashmir', 'jharkhand', 'karnataka', 'kerala', 'ladakh', 'lakshadweep', 'madhya-pradesh', 
                             'maharashtra', 'manipur', 'meghalaya', 'mizoram', 'nagaland','odisha', 'puducherry', 'punjab', 'rajasthan', 'sikkim', 'tamil-nadu', 'telangana', 'tripura', 
                             'uttar-pradesh', 'uttarakhand', 'west-bengal']
                choice_state = st.selectbox("State", menu_state, 0)
            with col2:
                st.subheader(" SELECT YEAR ")
                choice_year = st.selectbox("Year", ["", "2018", "2019", "2020", "2021", "2022"], 0)
            with col3:
                st.subheader(" SELECT DISTRICT ")
                dist=df_map_transactions["District"].unique().tolist()
                dist.sort()
                district = st.selectbox("search by", dist)
            if choice_state:
                col1, col2, col3 = st.columns(3)
                with col1:
                    st.subheader(f'{choice_state}')
                    st.write(district_choice_state(choice_state))
            if choice_year and choice_state:
                with col2:
                    st.subheader(f'in {choice_year} ')
                    st.write(dist_year_state(choice_year, choice_state))
            if district and choice_state and choice_year:
                with col3:
                    st.subheader(f'in {district} ')
                    st.write(district_year_state(district, choice_year, choice_state))
        else:
            col1, col2, col3 = st.columns(3)
            with col1:
                st.subheader(" SELECT STATE ")
                menu_state = ['', 'andaman-&-nicobar-islands', 'andhra-pradesh', 'arunachal-pradesh', 'assam', 'bihar', 'chandigarh', 'chhattisgarh', 'dadra-&-nagar-haveli-&-daman-&-diu',
                             'delhi', 'goa', 'gujarat', 'haryana', 'himachal-pradesh', 'jammu-&-kashmir', 'jharkhand', 'karnataka', 'kerala', 'ladakh', 'lakshadweep', 'madhya-pradesh', 
                             'maharashtra', 'manipur', 'meghalaya', 'mizoram', 'nagaland','odisha', 'puducherry', 'punjab', 'rajasthan', 'sikkim', 'tamil-nadu', 'telangana', 'tripura', 
                             'uttar-pradesh', 'uttarakhand', 'west-bengal']
                choice_state = st.selectbox("State", menu_state, 0)
                if choice_state:
                    df=district_choice_state(choice_state)
                    fig = px.bar(df, x="District", y="amount", title=f'Users in {choice_state}',color='Year')
                    st.plotly_chart(fig, theme=None, use_container_width=True)

            with col2:
                st.subheader(" SELECT YEAR ")
                choice_year = st.selectbox("Year", ["", "2018", "2019", "2020", "2021", "2022"], 0)
                df=dist_year_state(choice_year, choice_state)
                fig = px.bar(df, x="District", y="amount", title=f'Users in  {choice_state} in {choice_year}',color='Quarter')
                st.plotly_chart(fig, theme=None, use_container_width=True)
            with col3:
                st.subheader(" SELECT DISTRICT ")
                dist=df_map_transactions["District"].unique().tolist()
                dist.sort()
                district = st.selectbox("search by",dist )
                df=district_year_state(district, choice_year, choice_state)
                fig = px.bar(df, x="Quarter", y="amount",title=f"Users {district} in {choice_year} at {choice_state}",color='Quarter')
                st.plotly_chart(fig, theme=None, use_container_width=True)
    if choice_topic == "Brand":
        select = st.selectbox('View', ['Tabular view', 'Plotly View'], 0)
        if select == 'Tabular view':
            col1, col2, col3 = st.columns(3)
            with col1:
                st.subheader(" SELECT BRAND ")
                mobiles = ['', 'Apple', 'Asus', 'COOLPAD', 'Gionee', 'HMD Global', 'Huawei', 'Infinix', 'Lava', 'Lenovo', 
                           'Lyf', 'Micromax', 'Motorola', 'OnePlus', 'Oppo', 'Others', 'Realme', 'Samsung', 'Tecno', 'Vivo', 'Xiaomi']
                brand_type = st.selectbox("search by", mobiles, 0)
            with col2:
                st.subheader(" SELECT YEAR")
                choice_year = st.selectbox("Year", ["", "2018", "2019", "2020", "2021", "2022"], 0)
            with col3:
                st.subheader(" SELECT STATE ")
                menu_state = ['', 'andaman-&-nicobar-islands', 'andhra-pradesh', 'arunachal-pradesh', 'assam', 'bihar', 'chandigarh', 'chhattisgarh', 'dadra-&-nagar-haveli-&-daman-&-diu', 
                              'delhi', 'goa', 'gujarat', 'haryana', 'himachal-pradesh', 'jammu-&-kashmir', 'jharkhand', 'karnataka', 'kerala', 'ladakh', 'lakshadweep', 'madhya-pradesh', 
                              'maharashtra', 'manipur', 'meghalaya', 'mizoram', 'nagaland', 'odisha',
                              'puducherry', 'punjab', 'rajasthan', 'sikkim', 'tamil-nadu', 'telangana', 'tripura', 'uttar-pradesh', 'uttarakhand', 'west-bengal']
                choice_state = st.selectbox("State", menu_state, 0)
            if brand_type:
                col1, col2, col3, = st.columns(3)
                with col1:
                    st.subheader(f'{brand_type}')
                    st.write(brand_(brand_type))
            if brand_type and choice_year:
                with col2:
                    st.subheader(f' in {choice_year}')
                    st.write(brand_year(brand_type, choice_year))
            if brand_type and choice_state and choice_year:
                with col3:
                    st.subheader(f' in {choice_state}')
                    st.write(brand_state(choice_state, brand_type, choice_year))
        else:
            col1, col2, col3 = st.columns(3)
            with col1:
                st.subheader(" SELECT BRAND ")
                mobiles =  ['', 'Apple', 'Asus', 'COOLPAD', 'Gionee', 'HMD Global', 'Huawei', 'Infinix', 'Lava', 'Lenovo', 
                           'Lyf', 'Micromax', 'Motorola', 'OnePlus', 'Oppo', 'Others', 'Realme', 'Samsung', 'Tecno', 'Vivo', 'Xiaomi']
                brand_type = st.selectbox("search by", mobiles, 0)
                if brand_type:
                    df=brand_(brand_type)
                    fig = px.bar(df, x="State", y="Percentage",title=f" {brand_type} Users ",color='Year')
                    st.plotly_chart(fig, theme=None, use_container_width=True)

            with col2:
                st.subheader(" SELECT YEAR")
                choice_year = st.selectbox("Year", ["", "2018", "2019", "2020", "2021", "2022"], 0)
                if brand_type and choice_year:
                    df=brand_year(brand_type, choice_year)
                    fig = px.bar(df, x="State", y="Percentage",title=f"{brand_type} Users in {choice_year}",color='Quarter')
                    st.plotly_chart(fig, theme=None, use_container_width=True)
            with col3:
                st.subheader(" SELECT STATE ")
                menu_state = ['', 'andaman-&-nicobar-islands', 'andhra-pradesh', 'arunachal-pradesh', 'assam', 'bihar', 'chandigarh', 'chhattisgarh', 'dadra-&-nagar-haveli-&-daman-&-diu', 
                              'delhi', 'goa', 'gujarat', 'haryana', 'himachal-pradesh', 'jammu-&-kashmir', 'jharkhand', 'karnataka', 'kerala', 'ladakh', 'lakshadweep', 'madhya-pradesh', 
                              'maharashtra', 'manipur', 'meghalaya', 'mizoram', 'nagaland', 'odisha',
                              'puducherry', 'punjab', 'rajasthan', 'sikkim', 'tamil-nadu', 'telangana', 'tripura', 'uttar-pradesh', 'uttarakhand', 'west-bengal']
                choice_state = st.selectbox("State", menu_state, 0)
                if brand_type and choice_state and choice_year:
                    df=brand_state(choice_state, brand_type, choice_year)
                    fig = px.bar(df, x="Quarter", y="Percentage",title=f"{brand_type} Users in {choice_year} at {choice_state}",color='Quarter')
                    st.plotly_chart(fig, theme=None, use_container_width=True)

    if choice_topic == "Top-Transactions":
        select = st.selectbox('View', ['Tabular view', 'Plotly View'], 0)
        if select == 'Tabular view':
            col1, col2, col3 = st.columns(3)
            with col1:
                st.subheader(" SELECT STATE ")
                menu_state = ['', 'andaman-&-nicobar-islands', 'andhra-pradesh', 'arunachal-pradesh', 'assam', 'bihar', 'chandigarh', 'chhattisgarh', 'dadra-&-nagar-haveli-&-daman-&-diu',
                              'delhi', 'goa', 'gujarat', 'haryana', 'himachal-pradesh', 'jammu-&-kashmir', 'jharkhand', 'karnataka', 'kerala', 'ladakh', 'lakshadweep', 'madhya-pradesh',
                              'maharashtra', 'manipur', 'meghalaya', 'mizoram', 'nagaland', 'odisha', 'puducherry', 'punjab', 'rajasthan',
                              'sikkim', 'tamil-nadu', 'telangana', 'tripura', 'uttar-pradesh', 'uttarakhand', 'west-bengal']
                choice_state = st.selectbox("State", menu_state, 0)
            with col2:
                st.subheader(" SELECT  YEAR ")
                choice_year = st.selectbox("Year", ["", "2018", "2019", "2020", "2021", "2022"], 0)
            with col3:
                st.subheader(" SELECT Quarter ")
                menu_quarter = ["", "1", "2", "3", "4"]
                choice_quarter = st.selectbox("Quarter", menu_quarter, 0)

            if choice_state:
                with col1:
                    st.subheader(f'{choice_state}')
                    st.write(transaction_state(choice_state))
            if choice_state and choice_year:
                with col2:
                    st.subheader(f'{choice_year}')
                    st.write(transaction_year(choice_state, choice_year))
            if choice_state and choice_quarter:
                with col3:
                    st.subheader(f'{choice_quarter}')
                    st.write(transaction_quarter(choice_state, choice_year, choice_quarter))
        else:
            col1, col2, col3 = st.columns(3)
            with col1:
                st.subheader(" SELECT STATE ")
                menu_state = ['', 'andaman-&-nicobar-islands', 'andhra-pradesh', 'arunachal-pradesh', 'assam', 'bihar', 'chandigarh', 'chhattisgarh', 'dadra-&-nagar-haveli-&-daman-&-diu',
                              'delhi', 'goa', 'gujarat', 'haryana', 'himachal-pradesh', 'jammu-&-kashmir', 'jharkhand', 'karnataka', 'kerala', 'ladakh', 'lakshadweep', 'madhya-pradesh',
                              'maharashtra', 'manipur', 'meghalaya', 'mizoram', 'nagaland', 'odisha', 'puducherry', 'punjab', 'rajasthan',
                              'sikkim', 'tamil-nadu', 'telangana', 'tripura', 'uttar-pradesh', 'uttarakhand', 'west-bengal']
                choice_state = st.selectbox("State", menu_state, 0)
                if choice_state:
                    df=transaction_state(choice_state)
                    fig = px.bar(df, x="Year", y="Transaction_count",title=f"Transactions in {choice_state}", color='Quarter')
                    st.plotly_chart(fig, theme=None, use_container_width=True)

            with col2:
                st.subheader(" SELECT  YEAR ")
                choice_year = st.selectbox("Year", ["", "2018", "2019", "2020", "2021", "2022"], 0)
                if choice_state and choice_year:
                    df=transaction_year(choice_state, choice_year)
                    fig = px.bar(df, x="Year", y="Transaction_count",title=f"Transactions{choice_year} at {choice_state}", color='Quarter')
                    st.plotly_chart(fig, theme=None, use_container_width=True)

            with col3:
                st.subheader(" SELECT Quarter ")
                menu_quarter = ["", "1", "2", "3", "4"]
                choice_quarter = st.selectbox("Quarter", menu_quarter, 0)
                if choice_state and choice_quarter:
                    df=transaction_quarter(choice_state, choice_year, choice_quarter)
                    fig = px.bar(df, x="Quarter", y="Transaction_count",title=f"Transactions in {choice_year} at {choice_state} in Quarter {choice_quarter}", color='Quarter')
                    st.plotly_chart(fig, theme=None, use_container_width=True)

    if choice_topic == "Registered-users":
        select = st.selectbox('View', ['Tabular view', 'Plotly View'], 0)
        if select == 'Tabular view':
            col1, col2, col3 = st.columns(3)
            with col1:
                st.subheader(" SELECT STATE ")
                menu_state = ['', 'andaman-&-nicobar-islands', 'andhra-pradesh', 'arunachal-pradesh', 'assam', 'bihar', 'chandigarh', 'chhattisgarh', 'dadra-&-nagar-haveli-&-daman-&-diu',
                              'delhi', 'goa', 'gujarat', 'haryana', 'himachal-pradesh', 'jammu-&-kashmir', 'jharkhand', 'karnataka', 'kerala', 'ladakh', 'lakshadweep', 'madhya-pradesh', 
                              'maharashtra', 'manipur', 'meghalaya', 'mizoram', 'nagaland', 'odisha', 'puducherry', 'punjab',
                              'rajasthan', 'sikkim', 'tamil-nadu', 'telangana', 'tripura', 'uttar-pradesh', 'uttarakhand', 'west-bengal']
                choice_state = st.selectbox("State", menu_state, 0)
            with col2:
                st.subheader(" SELECT YEAR ")
                choice_year = st.selectbox("Year", ["", "2018", "2019", "2020", "2021", "2022"], 0)
            with col3:
                st.subheader(" SELECT DISTRICT ")
                dist=df_map_transactions["District"].unique().tolist()
                dist.sort()
                district = st.selectbox("search by",dist )

            if choice_state:
                with col1:
                    st.subheader(f'{choice_state}')
                    st.write(registered_user_state(choice_state))
            if choice_state and choice_year:
                with col2:
                    st.subheader(f'{choice_year}')
                    st.write(registered_user_year(choice_state, choice_year))
            if choice_state and choice_year and district:
                with col3:
                    st.subheader(f'{district}')
                    st.write(registered_user_district(choice_state, choice_year, district))
        else:
            col1, col2, col3 = st.columns(3)
            with col1:
                st.subheader(" SELECT STATE ")
                menu_state = ['', 'andaman-&-nicobar-islands', 'andhra-pradesh', 'arunachal-pradesh', 'assam', 'bihar', 'chandigarh', 'chhattisgarh', 'dadra-&-nagar-haveli-&-daman-&-diu',
                              'delhi', 'goa', 'gujarat', 'haryana', 'himachal-pradesh', 'jammu-&-kashmir', 'jharkhand', 'karnataka', 'kerala', 'ladakh', 'lakshadweep', 'madhya-pradesh', 
                              'maharashtra', 'manipur', 'meghalaya', 'mizoram', 'nagaland', 'odisha', 'puducherry', 'punjab',
                              'rajasthan', 'sikkim', 'tamil-nadu', 'telangana', 'tripura', 'uttar-pradesh', 'uttarakhand', 'west-bengal']
                choice_state = st.selectbox("State", menu_state, 0)
                if choice_state:
                    df=registered_user_state(choice_state)
                    fig = px.bar(df, x="District", y="RegisteredUser",title=f"Registered users at {choice_state} ",color='Year')
                    st.plotly_chart(fig, theme=None, use_container_width=True)
            with col2:
                st.subheader(" SELECT YEAR ")
                choice_year = st.selectbox("Year", ["", "2018", "2019", "2020", "2021", "2022"], 0)
                if choice_state and choice_year:
                    df=registered_user_year(choice_state, choice_year)
                    fig = px.bar(df, x="District", y="RegisteredUser",title=f"Registered users in {choice_state} in {choice_year}",color='Quarter')
                    st.plotly_chart(fig, theme=None, use_container_width=True)
            with col3:
                st.subheader("SELECT DISTRICT ")
                dist=df_map_transactions["District"].unique().tolist()
                dist.sort()
                district = st.selectbox("search by",dist)
                if choice_state and choice_year and district:
                    df=registered_user_district(choice_state, choice_year, district)
                    fig = px.bar(df, x="Quarter", y="RegisteredUser",title=f"Registered users at {choice_state} in {choice_year} in {district}",color='Quarter')
                    st.plotly_chart(fig, theme=None, use_container_width=True)


# In[ ]:




