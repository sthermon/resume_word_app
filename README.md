# JOB FIT 4 ME
#### Video Demo:  <https://youtu.be/no9nU1RgPAA>
#### Description:
Allow you to compare and analyze your resume and a job offer in order to improve chances to pass through an ATS system.
In the first python file I decided to code a fucntion which will receive some kind of text, parse it through Natural Language Toolkit, in order to filter some words not pertaining to the job search.
  First after some research I found NLTK library so decided to work with stopwords, tags and lemmas. This in order to ensure the filtered words will have relevance for the search and will provide a set of words with relevance to categorize.
  Then after categorizing the lemmas, found out necessary to untag the words as well as to check the frequency, in nltk fdist is capable of filtering and categorizing from most recurrent words to less reccurrent one. It just requires a list of words in order to do so.
  Created another function to use with sentences for future display and assigment in the app. Currently is not set in the app with functionality.
  
  For deployment, decided to use Streamlit as the fast operability, ~~simplicity~~ and similarity with python promised to be a good fit for the end result I was looking for.
  Throughout the process, unfortunately, noticed there are certain limitations with Strreamlit and some functionality is yet to be implemented or not compatible, this lead me to reorganize and modify the code from the first file as well as the streamlit file in order to display the results the analysis was capable of.
  In the end I was able to display the information I was looking for, but I had to remove some effects I wanted to give to the app. I might continue to work on it as I continue to study streamlit and python.
