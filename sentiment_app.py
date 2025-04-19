
import streamlit as st
import nltk
import string
import matplotlib.pyplot as plt
import seaborn as sns
from nltk.corpus import movie_reviews, stopwords
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
import random

# Download NLTK data
nltk.download('movie_reviews')
nltk.download('punkt')
nltk.download('stopwords')

# Load and preprocess the dataset
@st.cache_resource
def load_data_and_model():
    documents = [(movie_reviews.raw(fileid), category)
                 for category in movie_reviews.categories()
                 for fileid in movie_reviews.fileids(category)]
    random.shuffle(documents)

    texts = [text for text, label in documents]
    labels = [label for text, label in documents]

    stop_words = set(stopwords.words('english'))

    def preprocess_text(text):
        text = text.lower()
        text = text.translate(str.maketrans('', '', string.punctuation))
        tokens = nltk.word_tokenize(text)
        filtered = [word for word in tokens if word not in stop_words]
        return ' '.join(filtered)

    clean_texts = [preprocess_text(t) for t in texts]

    vectorizer = CountVectorizer()
    X = vectorizer.fit_transform(clean_texts)
    y = labels

    model = MultinomialNB()
    model.fit(X, y)

    return model, vectorizer, preprocess_text

# Load model
model, vectorizer, preprocess_text = load_data_and_model()

# Streamlit UI
st.title("🎯 Sentiment Analysis App")
st.write("Enter a movie review and I'll tell you if it's **positive** or **negative**!")

user_input = st.text_area("Enter your review here:")

if st.button("Analyze"):
    if user_input.strip() == "":
        st.warning("Please enter a review!")
    else:
        processed = preprocess_text(user_input)
        vec = vectorizer.transform([processed])
        prediction = model.predict(vec)[0]
        proba = model.predict_proba(vec)[0]

        # Show result
        if prediction == 'pos':
            st.success("🌟 Positive Sentiment!")
        else:
            st.error("⚠️ Negative Sentiment!")

        # Show prediction probabilities
        st.subheader("📊 Prediction Confidence")
        prob_df = {
            'Sentiment': ['Negative', 'Positive'],
            'Probability': [proba[0], proba[1]]
        }

        sns.set(style="whitegrid")
        fig, ax = plt.subplots()
        sns.barplot(x=prob_df['Sentiment'], y=prob_df['Probability'], palette='pastel', ax=ax)
        ax.set_ylim(0, 1)
        for i, v in enumerate(prob_df['Probability']):
            ax.text(i, v + 0.02, f"{v:.2f}", ha='center', fontweight='bold')
        st.pyplot(fig)
