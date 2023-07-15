#!/usr/bin/env python
# coding: utf-8

# In[7]:


import streamlit as st

st.title('Welcome to my Streamlit app!')

name = st.text_input('What is your name?')

if name:
    st.write(f'Hello, {name}!')


# In[6]:


from streamlit_webrtc import webrtc_streamer as web


# In[ ]:




