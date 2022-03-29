# https://www.geeksforgeeks.org/introduction-to-natural-language-processing/
import nltk
# required nltk resources - uncomment if needed
# nltk.download('punkt')
# nltk.download('stopwords')
# nltk.download('averaged_perceptron_tagger')
# nltk.download('wordnet')
# nltk.download('omw-1.4')
from nltk.corpus import stopwords
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.stem import WordNetLemmatizer
from nltk.probability import FreqDist
from nltk.tag.util import untag
from nltk.util import ngrams


# Initialize FreqDist and Lemmatizer for further usage
fdist = FreqDist()
wn = WordNetLemmatizer()
stop_words = set(stopwords.words('English'))
stop_words.update([',', '-', ':', ';', '&', '@', '/', '(', ')'])

# **********************************************************************************


# function in charge to filter and list words from parsed text.
def filter_text(txt):
    filtered_list = []
    # Removes any extra brackets from text and returns a string to clean data
    target = {39: None, 91: None, 93: None}
    a = (str(txt).translate(target))  # taken from: https://www.pythonpool.com
    tokenize_word = word_tokenize(a)
    # Iterate each word from text while removing stop words and punctuation
    tkn_lst = [word.lower().strip(',').strip('/').strip()
               for word in tokenize_word if word not in stop_words]
    tagged_words = nltk.pos_tag(tkn_lst)  # SATIfaction
    for w in tagged_words:
        if w[1] == 'NN' or w[1] == 'NNS' or w[1] == 'NNP' or w[1] == 'NNPS' or w[1] == 'JJ' or w[1] == 'JJS' or w[1] == 'JJR':
            filtered_list.append(w)

    # Untag and print list of words applying lemmas for clean visibility
    def clean_text(lst):
        remove_tag = untag(lst)
        lem_list = []
        for tag in remove_tag:
            lem_list.append(wn.lemmatize(tag))
        return lem_list

    org_list = clean_text(filtered_list)
    return org_list

    # ***********************************************************************************


def clean_file(file):
    with open(file, encoding='utf-8') as new_doc:
        page = new_doc.read()
    return filter_text(page)

    # filter and list most frequent words with use of fdist


def top_frequent_words(list_1):
    sorted_list = fdist
    freq_words = list_1
    for word in freq_words:
        fdist[word] += 1
    return sorted_list

    # compute and set percentage of accuracy between lists
    # https://www.geeksforgeeks.org/python-percentage-similarity-of-lists/?ref=gcse
    # match = len(set(resume_list) & set(job_list)) / float(len(set(resume_list) | set(job_list))) * 100
    # **********************************************************************************
    
 # words can be separated in grams for displaying most common sentences in job offer and suggest recommended terms
def find_bigrams(txt, n=2):
    bigrams_list = []
    text = sent_tokenize(txt)
    for word in text:
        token = nltk.word_tokenize(word)
        bigram = (list(ngrams(token, n)))
        bigrams_list.extend(bigram)

    # Filter bigram removing stopwords and punctuation
    filtered_sent = [x.lower().strip(',').strip('/').strip()
                     for x in text.split() if x.lower() not in stop_words]
    new_text = find_bigrams(' '.join(filtered_sent))

    # Creates a dictionary to assign frequency of sentences
    def sort_bigrams(sents):
        ngrams_freq = {}
        for wrd in sents:
            if wrd not in ngrams_freq:
                ngrams_freq[wrd] = 0
            ngrams_freq[wrd] += 1
        # Sort dictionay per key-values
        sorted_ngrams_freq = sorted(
            ngrams_freq.items(), key=lambda n: n[1], reverse=True)

        # Groups most common sentences and join them with its relation
        ngram_joins = []
        for n in range(len(sorted_ngrams_freq[:20])):
            ngram_join = '_'.join(sorted_ngrams_freq[n][0])
            ngram_joins.append(ngram_join)
        ngram_joins = ' '.join(ngram_joins)
        return ngram_joins

    sort_bigrams(new_text)

