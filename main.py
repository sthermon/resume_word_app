from word_selector import clean_file, filter_text
from word_selector import top_frequent_words
import streamlit as st
from streamlit_lottie import st_lottie
import requests
from pdf2docx import parse
import docx
import copy


# function to animate upload icon
def animate_icon(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()


# Initialize session to keep cached returned fuction
if 'text' not in st.session_state:
    st.session_state.text = ''


@st.cache
def doc_reader(file):
    doc = docx.Document(file)
    pages = [p.text for p in doc.paragraphs]
    parse_doc = str(pages)
    return parse_doc


@st.cache
def pass_file(txt):
    with open('text_transc.txt', 'w', encoding='utf-8') as f:
        f.write(txt)


# icon from https://lottiefiles.com/
lottie_icon = animate_icon(
    'https://assets2.lottiefiles.com/packages/lf20_ir6xNQ.json')

def main():

    # Page description, icon and layout
    st.set_page_config(page_title='Job fit 4 me', page_icon='📃', layout='centered')
    title_1, title_2, title_3 = st.columns([1, 2, 1])
    with title_1:
        st.empty()
    with title_2:
        st.title('Job fit 4 me')
    with title_3:
        st.empty()
    st.write('---')

    st.write('##')
    st.header('Improve your resume by targeting it to a job offer in just 3 steps')
    st.write('##')

    st.write('##')

    # container to process text for job description and handle with function from word selector
    with st.container():

        with st.form(key='form', clear_on_submit=False):
            st.write('##')
            st.subheader(
                'Analyze a job offer by entering it to the text field:')
            descr = st.text_area(label='Job description:', height=250, key='text',
                                placeholder='''Paste a job description here you wish to analyze its skills. 

    For example, paste qualifications, responsibilities, highlights 
    but exclude information about the company (About us, diversity, or benefits) as it will reduce probability.
    Job descriptions in English only...'''
                                )
            st.subheader(
                'Compare your resume against this job offer to see your match percentage to be selected by a system')
            pass_file(descr)
            st.write('##')
            mid_col, right_col = st.columns([2, 2])
            with mid_col:
                doc_file = st.file_uploader('Please submit .docx or .pdf files only', key='file', accept_multiple_files=False,
                                            help='Drag and drop your file or hit "Browse files"', type=['pdf', 'docx'])
                if doc_file is not None:
                    if doc_file.type == 'application/pdf':
                        file_details = {
                            'Filename': doc_file.name, 'Filesize': doc_file.size, 'Filetype': doc_file.type}
                        # ******************* optional *********************************
                        st.write(file_details)
                        try:
                            pdf_file = doc_file
                            new_file = 'doc_from_pdf.docx'
                            parse(pdf_file=pdf_file,
                                docx_file=new_file, start=0, end=None)
                            result = doc_reader(new_file)
                        except (TypeError):
                            st.warning('Unable to read file')
                    else:
                        result = doc_reader(doc_file)
                    with right_col:
                        st_lottie(lottie_icon, height=150, key='icon')
                    pass_file(result)

            st.write('##')
            submit = st.form_submit_button(
                'Analyze')
            if not submit:
                st.info('Upload your resume and click Analyze to continue')
            if submit:
                st.spinner('Processing data...')
    st.write('---')
    if st.session_state['FormSubmitter:form-Analyze'] is not False:
        with st.container():
            st.subheader('Match percentage')
            description = filter_text(descr)
            resume = clean_file('text_transc.txt')
            # https://www.geeksforgeeks.org/python-percentage-similarity-of-lists/?ref=gcse
            match = len(set(resume) & set(description)) / \
                float(len(set(resume) | set(description))) * 100
            st.write(match)
            st.caption(
                'An ideal percentage should be close to 70%, a higher percentage will also decrease the chances of being selected by a system')

        # dropdown selection to show the top 10 and top 20 most common words found in the offer
        with st.container():
            st.subheader('Top words of your analysis')
        with st.expander('Job description'):
            descript_1 = copy.deepcopy(description)
            top_words = list(top_frequent_words(descript_1))
            top_30 = top_words[:30]
            st.write(top_30)
            
        with st.expander('Resume'):
            resum_1 = copy.deepcopy(resume)
            top_words2 = list(top_frequent_words(resum_1))
            
            top_30_1 = top_words2[:30]
            st.write(top_30_1)

        # Clear cached items and functions to prepare for new usage
        new_analysis = st.button('New analysis')
        if new_analysis:
            for key in st.session_state.keys():
                del st.session_state[key]
                st.experimental_memo.clear()

if __name__ =='__main__':
    main()
