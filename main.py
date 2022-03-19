import word_selector
from word_selector import top_words
import streamlit as st
from streamlit_lottie import st_lottie
import requests
from pdf2docx import parse
import docx

# Page description, icon and layout
st.set_page_config(page_title='Job fit 4 me', page_icon='📃', layout='centered')

# function to animate upload icon


def animate_icon(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()


@st.cache
def load_description(text):
    data = ''
    with open('job_desc.txt', w) as job:
        job.write(text)
    pass

# send_data = word_selector.filter_text()


@st.cache
def load_resume():
    # pdfreader = pdfreaderfile(file)
    # all_page_text = ''
    # for i in range(count):
    #     page = pdfreader.getpage(i)
    #     all_page_text += page.extracttext()
    # return all_page_text
    pass


# icon from https://lottiefiles.com/
lottie_icon = animate_icon(
    'https://assets2.lottiefiles.com/packages/lf20_ir6xNQ.json')

title_1, title_2, title_3 = st.columns([1, 2, 1])
with title_1:
    st.empty()
with title_2:
    st.title('Job fit 4 me')
with title_3:
    st.empty()

st.write('##')
st.header('Improve your resume by targeting it to a job offer')
st.write('##')


# container to process text for job description and handle with function from word selector
with st.container():
    st.subheader(
        'Analyze a job description and identify important skills and keywords:')

    with st.form(key='job_desc', clear_on_submit=True):
        descr = st.text_area(label='Job description:', height=250,
                             placeholder='''Paste a job description here you wish to analyze its skills. 

For example, paste qualifications, responsibilities, highlights 
but exclude information about the company (About us, diversity, or benefits) as it will reduce probability.
Job descriptions in English only...'''
                             )
        send_desc = st.form_submit_button('Analyze')
        if not send_desc:
            st.info('Please enter a job description')
            # st.stop()
        if send_desc:
            st.spinner('Processing data...')
            data = load_description(send_desc)
            st.success('Data sent!')
            # if animation can be added to compare text and doc: https://assets2.lottiefiles.com/private_files/lf30_1j94r4tx.json

st.write('##')
st.write('---')
# container to uploaded file and further handling
with st.container():
    st.subheader(
        'Compare your resume against this job offer to see your chances of being considered')

    mid_col, right_col = st.columns([2, 2])
    with mid_col:
        doc_file = st.file_uploader('', accept_multiple_files=False,
                                    help='Only .docx or .pdf files', type=['pdf', 'docx'], )
        st.markdown('Drag and drop your file or hit "Browse files"')
    with right_col:
        st_lottie(lottie_icon, height=200, key='doc')

    if not doc_file:
        st.info('Upload your resume in .pdf or .docx format only')
        # st.stop()'''
    if doc_file is not None:
        if doc_file.type == 'application/pdf':
            pdf_file = doc_file
            new_file = 'doc_from_pdf.docx'
            parse(pdf_file='pdf_file', docx_file='new_file', start=0, end=None)
        else:
            doc = docx.Document(doc_file)
            pages = [p.text for p in doc.paragrahps]
            parse_doc = str(pages)

st.write('---')


show_match = st.button('Show match')
if not show_match:
    st.stop()
    st.success('success')

# TODO Use pandas or matplotlib to visualize the similarities found for resume and offer

with st.container():
    st.subheader('Match percentage')
    st.write('plot pie char here')
    st.caption(
        'An ideal percentage should be close to 70%, higher changes will decrease also the chances of being selected')


# dropdown selection to show the top 10 and top 20 most common words found in the offer
with st.container():
    st.subheader('Select your top words')

    top_25 = (top_words[:25])
    top_10 = (top_words[:10])
    top_5 = (top_words[:5])

    top_word_select = st.selectbox(
        'Pick one option', ['None', 'Top 5', 'Top 10', 'Top 25'])
    if top_word_select == 'Top 5':
        st.write(top_5)
    if top_word_select == 'Top 10':
        st.write(top_10)
    if top_word_select == 'Top 25':
        st.write(top_25)
    else:
        ''
