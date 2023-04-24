import streamlit as st
import pandas as pd
import plotly.express as px
import altair as alt
import numpy as np
from st_btn_select import st_btn_select

@st.cache_data
def load_data(url):
    df = pd.read_csv(url)
    return df

@st.cache_data
def load_datas(url):
    df1 = pd.read_excel(url)
    return df1  

nasa = load_data("nasa-annual-budget.csv")
visit = load_datas('annual-space-visits.xlsx')
exo = load_data("cumulative-exoplanets-by-method.csv")
ice = load_datas("Ice Cap's Level.xlsx")
carbon = load_datas("Carbon Dioxide Levels.xlsx")

st.header("Benefits of Space Exploration")

page = st_btn_select(
  # The different pages
  ('Home Page', 'Space Exploration','Space Discoveries', 'Conclusion'),
  # Enable navbar
  nav=False
)


if page == 'Home Page':
    st.image('Space_ST.jpeg', width = 750)
    st.write('The development and exploration of space is an important topic to understand because it encompasses many aspects of our lives. Many insights about natural events on Earth can be captured through space technologies as well as finding ways to refit these technolgoies to support society beyond their initial use.')
    

if page == 'Space Exploration':
    tab1, tab2 = st.tabs(['NASA Budget','Space Launches'])

    with tab1:
        st.line_chart(nasa, height=600,  width= 700, x = "Year", y = "Budget")
        st.write("At NASA's inception in 1958 there was an initial boom in budget. A majority of this budget went towards the research and design of rocket technology.")
   
    with tab2:
        clist = visit['Entity'].unique()
        country = st.selectbox("Select a country:",clist,index=40)

        df = visit[visit['Entity'] == country]

        ASV_Chart = alt.Chart(df,title = 'Annuals Space Visits', height= 600, width= 700).mark_bar().encode(
            x = 'Year',
            y = 'annual_visits',
            ).interactive()
        st.altair_chart(ASV_Chart)
       
        st.write('Make World my Default Choice')
        st.write('In the 1980s, the world had a large increase in Rocket Launches with the US and Russia having the most. This carried on till the late 2000s. After this the space industry became more privatized leading to independent venture and contracts to space.')

if page == 'Space Discoveries':
    tab1, tab2, tab3 = st.tabs(['Ice Melt','Exoplanets','Carbon Dioxide'])
    with tab1:
        y_val = st.selectbox("Pick your y-axis",ice.select_dtypes(include=np.number).columns.tolist())
        
        ice_c = alt.Chart(ice,title = 'Ice Melt',height= 600, width= 700).mark_line().encode(
        x='Date',
        y= y_val
        ).interactive()
        st.altair_chart(ice_c)

        st.write('How to change which y variables I want?')

    with tab2:

        name = ['Microlensing', 'Other methods', 'Radial velocity', 'Transit']
        color = ['black', 'white', 'green', 'red']

        exo_c = alt.Chart(exo, title= 'Exoplants Discovered by strategy' , height= 600, width= 700).mark_bar().encode(
        x="Year",
        y=alt.Y("cumulative_exoplanets"),
        color=alt.Color('Entity',scale=alt.
                    Scale(domain=name, range=color))
                    )
        st.altair_chart(exo_c)
        
        link1 ='To better understand methods of finding exoplanents use this [link](https://exoplanets.nasa.gov/alien-worlds/ways-to-find-a-planet/)'
        st.markdown(link1,unsafe_allow_html=True)

    with tab3:
        carbon_c = alt.Chart(carbon, title= 'Carbon Dioxide Levels' , height= 700, width= 700).mark_line().encode(
            x='Year',
            y=alt.Y('Monthly Average',scale=alt.Scale(domain=[300, 450]))
         )
        st.altair_chart(carbon_c)

if page == 'Conclusion':
    st.write("There has been a misconception that 'space' spending does not have application on Earth but that is untrue. Major discoveries in space have led to the creation of firefighting equipment, iphone cameras, and water filtration devices. Better understanding of natural events like Carbon Dioxide levels and Ice Cap melt can be fully captures through discoveries made in space.  ")
    
    link='For more information on this topic check out this [link](https://www.nasa.gov/specials/value-of-nasa/#:~:text=Dollars%20spent%20for%20space%20exploration,support%20disaster%20response%2C%20and%20more.)'
   
    agree = st.checkbox('Do you better understand how space is beneficial for society.')
    if agree:
        st.markdown(link,unsafe_allow_html=True)
