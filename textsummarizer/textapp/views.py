from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def home(request):
    print(request.POST)
    return render(request, 'index.html')


def post(request):
    # importing libraries
    import nltk
    from nltk.corpus import stopwords
    from nltk.tokenize import word_tokenize, sent_tokenize

    # Input text - to summarize
    text = """Congress leader Rahul Gandhi has been asked to vacate his government-allotted bungalow at 12, Tughlaq Lane by April 22, days after he stood disqualified as a Lok Sabha member. According to the rule, a disqualified parliamentarian isn't entitled to a government accommodation, and is given a 30-day period to vacate the official bungalow. This was Rahul Gandhi's forth term as Lok Sabha MP, first elected in 2004 from Uttar Pradesh's Amethi constituency. In 2019, he lost in Amethi to Union minister Smriti Irani, however managed to win from Kerala's Wayanad seat.

    The Congress leader was disqualified from the Lok Sabha on March 23 after he was convicted for a two-year term in a criminal defamation case. According to the Article 102 1(e) of the Constitution and Section 8(3) of the Representation of People Act, 1951, when read together, a Member of Parliament can be disqualified if he or she is convicted of any offence and sentenced to imprisonment for two or more years. The notice to vacate the bungalow was served by the Housing Committee of Lok Sabha."""

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


    print(sentenceValue)
    sumValues = 0
    for sentence in sentenceValue:
        sumValues += sentenceValue[sentence]

    # Average value of a sentence from the original text

    average = int(sumValues / len(sentenceValue))

    # Storing sentences into our summary.
    summary = ''
    for sentence in sentences:
        print(sentence)
        if (sentence in sentenceValue) and (sentenceValue[sentence] > (1.2 * average)):
            print("INSIDE")  
            summary += " " + sentence
    print(summary)
    print("END")
    person= {'firstname': 'Priska', 'lastname': 'Kashyap'}
    return render(request, 'index.html', person)
