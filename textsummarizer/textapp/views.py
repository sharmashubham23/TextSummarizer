from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
import nltk
nltk.download('stopwords')
nltk.download('punkt')
def home(request):
    print(request.POST)
    return render(request, 'index.html')


def post(request):
    # importing libraries
    

    from nltk.corpus import stopwords
    from nltk.tokenize import word_tokenize, sent_tokenize
    # print(request.POST['mtext'])
    # Input text - to summarize
    text = request.POST['mtext']

    # Tokenizing the text
    stopWords = set(stopwords.words("english"))
    words = word_tokenize(text)

    # Creating a frequency table to keep the
    # score of each word

    freqTable = dict()
    for word in words:
        word = word.lower()
        if word in stopWords:
            continue
        if word in freqTable:
            freqTable[word] += 1
        else:
            freqTable[word] = 1

    # Creating a dictionary to keep the score
    # of each sentence
    sentences = sent_tokenize(text)
    sentenceValue = dict()

    for sentence in sentences:
        for word, freq in freqTable.items():
            if word in sentence.lower():
                if sentence in sentenceValue:
                    sentenceValue[sentence] += freq
                else:
                    sentenceValue[sentence] = freq


    # print(sentenceValue)
    sumValues = 0
    for sentence in sentenceValue:
        sumValues += sentenceValue[sentence]

    # Average value of a sentence from the original text

    average = int(sumValues / len(sentenceValue))

    # Storing sentences into our summary.
    summary = ''
    for sentence in sentences:
        if (sentence in sentenceValue) and (sentenceValue[sentence] > (1.2 * average)):
            summary += " " + sentence
    # print(summary)
    print("END")
    person= {'resultmain': summary, 'lastname': 'Kashyap'}
    return render(request, 'result.html', person)
