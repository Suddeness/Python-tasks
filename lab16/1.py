import nltk, string
from nltk import WordNetLemmatizer
from nltk.corpus import stopwords
nltk.download('punkt_tab')
nltk.download('stopwords')
nltk.download('wordnet')

try:
    with open("text.txt", "r") as file:
        text=file.read()
        # Токенизация
        token_text=nltk.word_tokenize(text)
        print("Tokens:", token_text)
        #Видалення пункуації
        token_without_punct = [word for word in token_text if word not in string.punctuation]
        print("Tokens without punctuation:", token_without_punct)
        #Видалення стоп-слів
        stop_w = set(stopwords.words("english"))
        text_never_stop = [word for word in token_without_punct if word.lower() not in stop_w]
        print("dont stop", text_never_stop)
        # Лемматизація
        lemmatiz = WordNetLemmatizer()
        text_lem = ([lemmatiz.lemmatize(word) for word in text_never_stop])
        print("Lemmatized words:", text_lem)
        new_text = ""
        for i in range(5, len(text_lem), 5):
            new_text += " ".join(text_lem[i-5:i])+"\n"
        with open("new_text.txt", "w") as file2:
                file2.write(new_text)
except FileNotFoundError:
    print("Un luck")



