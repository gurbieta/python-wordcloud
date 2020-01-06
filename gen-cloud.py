#! /usr/bin/env python3

import sys
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from string import punctuation
from nltk.probability import FreqDist
from wordcloud import WordCloud
import matplotlib.pyplot as plt

if len(sys.argv) < 2:
    print("Usage %s file.txt" % sys.argv[0])
    exit(0)

with open (sys.argv[1], 'r') as meuarquivo:
    text = meuarquivo.read()

words = word_tokenize(text.lower()) 

stopwords = set(stopwords.words('portuguese') + list(punctuation) + ["...", "--"])

print(stopwords)

frequency = FreqDist([word for word in words if word not in stopwords])

print(frequency.most_common(1000))

wc = WordCloud(background_color='white', 
                width=1000, height=800, max_words=1000, 
                relative_scaling=0.5, colormap='viridis', 
                normalize_plurals=False).generate_from_frequencies(frequency)

plt.imshow(wc)
plt.axis('off')
#plt.title('Test title', size='xx-small')
#plt.suptitle('Test subtitle', horizontalalignment='center', weight='bold')
#plt.figtext(0.5, 0.05, 'asdad', size='x-small', horizontalalignment='center')
plt.show()
