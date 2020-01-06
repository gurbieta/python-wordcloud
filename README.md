# python-wordcloud

## Installing pip packages

```bash
pip3 install --user -U matplotlib

pip3 install --user -U wordcloud

pip3 install --user -U nltk
```

## Installing nltk packages

In a python3 interpreter run

```python3
import nltk

nltk.download("averaged_perceptron_tagger")
nltk.download("floresta")
nltk.download("mac_morpho")
nltk.download("machado")
nltk.download("punkt")
nltk.download("stopwords")
nltk.download("wordnet")
nltk.download("words")
```

## Running

./gen-cloud.py casmurro.txt
