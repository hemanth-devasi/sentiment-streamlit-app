# 🧠 Sentiment Analysis Web App

A simple and interactive sentiment analysis web app built using **Python**, **NLTK**, and **Streamlit**. This app uses a machine learning model trained on NLTK’s `movie_reviews` dataset to classify text as **positive** or **negative**.

---

## 📸 Demo

![App Screenshot](https://via.placeholder.com/800x400.png?text=Add+Screenshot+Here)

---

## 🚀 Features

- Input any text and get instant sentiment prediction
- Clean and interactive Streamlit UI
- Visualizations of dataset sentiment distribution
- Built from scratch with NLTK and Scikit-learn
- Deployable via Streamlit Cloud

---

## 🧰 Requirements

Install dependencies via:

```bash
pip install -r requirements.txt
```

---

## 📁 Project Structure

```
sentiment-streamlit-app/
├── sentiment_app.py          # Streamlit app code
├── requirements.txt          # Required packages
├── nltk_data/                # Manually downloaded NLTK data
│   ├── corpora/
│   ├── tokenizers/
│   └── ...
└── README.md                 # You're reading it!
```

---

## ⚙️ How to Run Locally

1. **Clone the repository:**

```bash
git clone https://github.com/yourusername/sentiment-streamlit-app.git
cd sentiment-streamlit-app
```

2. **Install Python dependencies:**

```bash
pip install -r requirements.txt
```

3. **Run the app:**

```bash
streamlit run sentiment_app.py
```

---

## ⚠️ Important: NLTK Data Setup

If you're running this in a fresh environment or deploying, make sure:

- The `nltk_data/` folder is present in the root directory.
- Add this line in `sentiment_app.py` to point to it:

```python
import nltk
nltk.data.path.append("nltk_data")
```

---

## ☁️ Deploy to Streamlit Cloud

1. Push the entire project (including `nltk_data/`) to a GitHub repo.
2. Go to [Streamlit Cloud](https://streamlit.io/cloud) and connect your repo.
3. Set `sentiment_app.py` as the main file and deploy!

---

## 💬 Example Sentences to Try

- “I absolutely loved the movie!”
- “This was the worst experience ever.”
- “Not bad, but could have been better.”
- “Such an amazing performance!”

---

## 📄 License

MIT License – do whatever you want with it 😊

---

## 🙌 Credits

Built with ❤️ using:
- [NLTK](https://www.nltk.org/)
- [Streamlit](https://streamlit.io/)
- [Scikit-learn](https://scikit-learn.org/)
