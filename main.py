import streamlit as st


st.title('Improve your resume by tailoring it to a job offer')
st.write('##')

st.write('With just few steps identify the probability to land you new next job')

with st.form('job_description'):
  st.text_area(label='Job description:', height=200, 
               placeholder='''
               Paste a job description here you wish to analyze.
               
               For example, paste qualifications, responsibilities, highlights 
               but exclude information about the company (About Us), or benefits.
               '''
              )
  st.form_submit_button('Analyze')
  
 with st.container():
  st.file_uploader(label='Resume', accept_multiple_files=False, on_change='upload')
  
 st.write('---')

