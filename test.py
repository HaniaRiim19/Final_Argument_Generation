import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

nltk.download('punkt')
nltk.download('stopwords')

def calculate_similarity(original_text, summary_text):
    # Tokenize and preprocess the text
    stop_words = set(stopwords.words('english'))

    def preprocess_text(text):
        text = text.replace("\n", " ")
        words = word_tokenize(text)
        words = [word.lower() for word in words if word.isalnum()]
        words = [word for word in words if word not in stop_words]
        return " ".join(words)

    original_text = preprocess_text(original_text)
    summary_text = preprocess_text(summary_text)

    # Compute TF-IDF vectors
    vectorizer = TfidfVectorizer()
    tfidf_matrix = vectorizer.fit_transform([original_text, summary_text])

    # Compute cosine similarity
    cosine_sim = cosine_similarity(tfidf_matrix[0], tfidf_matrix[1])

    # Return the cosine similarity score
    return cosine_sim[0][0]

def read_text_from_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()
