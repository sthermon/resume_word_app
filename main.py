import streamlit as st


st.title('Improve your resume by tailoring it to a job offer')
st.write('##')

st.write('With just few steps identify the probability to land you new next job')

with st.form('job_description'):
  st.text_area(label='Job description:', placeholder=''
