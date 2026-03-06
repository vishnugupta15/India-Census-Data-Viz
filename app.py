import streamlit as st
import numpy as np
import pandas as pd
import plotly.express as px

df = pd.read_csv('india_data.csv')
list_of_states = list(df['State'].unique())
list_of_states.insert(0,'Whole India')

st.set_page_config(layout='wide')
st.sidebar.title('India Ka Data Visualizer')
selected_state = st.sidebar.selectbox('Select a state',list_of_states)
primary = st.sidebar.selectbox('Select Primary Parameter',sorted(df.columns[5:]))
secondary = st.sidebar.selectbox('Select Secondary Parameter',sorted(df.columns[5:]))

plot = st.sidebar.button('Plot Graph')

if plot:
    if selected_state == 'Whole India':
        fig = px.scatter_mapbox(df,lat ="Latitude",lon="Longitude",size = primary,color=secondary,zoom=4,mapbox_style="carto-positron",size_max=30,width=1200,height=700,hover_name='District')
        st.plotly_chart(fig,use_container_width=True)
    else:
        
        state_df = df[df['State']==selected_state]
        fig = px.scatter_mapbox(state_df,lat ="Latitude",lon="Longitude",size = primary,color=secondary,zoom=4,mapbox_style="carto-positron",size_max=30,width=1200,height=700,hover_name='District')
        st.plotly_chart(fig,use_container_width=True)