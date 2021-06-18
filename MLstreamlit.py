#!/usr/bin/env python
# coding: utf-8

# In[4]:


import seaborn as sns
from datetime import datetime, timedelta
import numpy as np
from matplotlib import pyplot as plt
import streamlit as st
import pandas as pd
import plotly.graph_objs as go
import pandas as pd
import plotly.express as px 


# In[6]:


st.subheader("Streamflow prediction results of Indus at Tarbela for XGBoost model")
df=pd.read_excel ("testindus.xlsx",engine='openpyxl')

fig = px.line(df, x='Date', y=df.columns[1:3])
fig.update_layout(
    autosize=False,
    width=1000,
    height=500,
    title={
        'text': "Predicted streamflows at Indus",
        'y':1,
        'x':0.5,
        'xanchor': 'center',
        'yanchor': 'top'},
    xaxis_title="Date",
    yaxis_title="Flow(m3/s)",
   # legend_title="Legend Title",
    font=dict(
        family="Courier New, monospace",
        size=16,
        #color="RebeccaPurple"
    )
    )
fig.update_layout(
    xaxis=dict(
        
        rangeslider=dict(
            visible=True
        ),
        type="date"
    )
)

st.write(fig)


# In[ ]:




