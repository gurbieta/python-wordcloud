#! /usr/bin/env python3

import sys
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from string import punctuation
from nltk.probability import FreqDist
from wordcloud import WordCloud
import matplotlib.pyplot as plt

lang = "portuguese"

if len(sys.argv) < 2:
    print("Usage %s file.txt" % sys.argv[0])
    exit(0)

with open (sys.argv[1], 'r') as textFile:
    text = textFile.read()

if len(sys.argv) == 3:
    lang = sys.argv[2]

words = word_tokenize(text.lower()) 

stopwords = set(stopwords.words(lang) + list(punctuation) + ["...", "--", "á"])

frequency = FreqDist([word for word in words if word not in stopwords])

print(frequency.most_common(1000))

wc = WordCloud(background_color='white', 
                width=1000, height=800, max_words=1000, 
                relative_scaling=0.5, colormap='viridis', 
                normalize_plurals=False).generate_from_frequencies(frequency)

plt.imshow(wc, interpolation="bilinear")
plt.axis('off')
plt.margins(x=0, y=0)
plt.show()
