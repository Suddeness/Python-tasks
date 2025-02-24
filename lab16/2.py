import nltk, string
from nltk.corpus import gutenberg, stopwords
import matplotlib.pyplot as plt
from collections import Counter

# nltk.download("gutenberg")
# whitman_text = gutenberg.raw('whitman-leaves.txt')
# with open('whitman-leaves.txt', 'w', encoding='utf-8') as file:
#     file.write
nltk.download('punkt_tab')
def counter(text):
    words = nltk.word_tokenize(text)
    return len(words)

def most_used_words(text, name):
    txt_s = text.split()
    cnt = Counter(txt_s)
    m_u_w = cnt.most_common(10)
    x = [m_u_w[el][0] for el in range(len(m_u_w))]
    y = [m_u_w[el][1] for el in range(len(m_u_w))]
    print(f"words:{x}\nnumber:{y}")
    plt.bar(x,y)
    plt.title(f"10 most used words ({name})")
    plt.xticks(rotation=45)
    plt.savefig(name)
    plt.close()

try:
    with open("whitman-leaves.txt", "r", encoding="utf-8") as file:
        txt = file.read()
        txt_without_p = (txt.translate(str.maketrans("", "", string.punctuation))).lower()
        tokens = nltk.word_tokenize(txt_without_p)
        stop_words = set(stopwords.words('english'))
        clean_txt = " ".join([word for word in tokens if word not in stop_words])
        print(f"text\nnumber of words: {counter(txt)}")
        most_used_words(txt, "txt.png")
        print(f"\nClean text\nnumber of words: {counter(clean_txt)}")
        most_used_words(clean_txt, "clean_txt.png")
except FileNotFoundError:
    print ("NF")




