import streamlit as st
from gensim.summarization.summarizer import summarize
from gensim.summarization import keywords

st.title('Summarization program rev01')
text = st.sidebar.text_input('Please input your paragraph : ')
rat = st.sidebar.slider('Ratio',0.0,1.0,step = 0.1) 

st.write('Original Text')
st.write(text)

text_sum = summarize(text, ratio=rat)

st.write('Summarized Text',100 - round(100*(len(text_sum)/len(text)),2), '% reduction')
st.write(text_sum)