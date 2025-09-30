# Importing all the dependencies
# import numpy as np
# import tensorflow as tf
# from tensorflow.keras.datasets import imdb
# from tensorflow.keras.preprocessing import sequence
# from tensorflow.keras.models import load_model
#
#
#
# # load the imdb dataset word index
# # Mapping of word index to words
# word_index = imdb.get_word_index()
# # word_index
# reverse_word_index={value:key for key,value in word_index.items()}
#
# # Load the pre-trained model with RELU activation
# model = load_model("Simple_rnn_imdb.h5")
#
# #Helper Functions
# # Fxn to decode reviews
# def decode_review(encoded_review):
#     return ' '.join([reverse_word_index.get(i-3,"?")for i in encoded_review])
#     """Keras IMDB shifts all real word indices by +3 to leave room for special tokens.
# When decoding, you subtract 3 (i-3) to map back to the original word index"""
# # function to preprocess user input
# def preprocess_text(text):
#     words = text.lower().split()
#     encoded_review = [word_index.get(word,2)+3 for word in words]
#     padded_review = sequence.pad_sequences([encoded_review],maxlen=500)
#     return padded_review
#
# # Prediction Fxn:-
#
# def predict_sentiment(review):
#     preprocessed_input = preprocess_text(review)
#     prediction = model.predict(preprocessed_input)
#     sentiment = "Postive" if prediction[0][0] > 0.5 else 'Negative'
#     return sentiment,prediction[0][0]
#
#
# ## Streamlit App
# import streamlit as st
# st.title = "Movie Review Analysis"
# st.write("Enter a Movie Review to classify it as postive or negative")
#
# # user input
# user_input = st.text_area("Movie-Review")
#
# if st.button('Classify The Review'):
#     sentiment,score = predict_sentiment(user_input)
#     # Display the result
#     st.write(f"Sentiment:- {sentiment}")
#     st.write(f"Prediction %:-  {score*100}")
# else:
#     st.write('~#u#~ Please Enter A Movie Review ~#u#~')



import numpy as np
import tensorflow as tf
from tensorflow.keras.datasets import imdb
from tensorflow.keras.preprocessing import sequence
from tensorflow.keras.models import load_model
import streamlit as st

# Load IMDb word index
word_index = imdb.get_word_index()
reverse_word_index = {value: key for key, value in word_index.items()}

# Load the pre-trained model
model = load_model("Simple_rnn_imdb.h5")

# Helper functions
def decode_review(encoded_review):
    return ' '.join([reverse_word_index.get(i - 3, "?") for i in encoded_review])

def preprocess_text(text):
    words = text.lower().split()
    encoded_review = [word_index.get(word, 2) + 3 for word in words]
    padded_review = sequence.pad_sequences([encoded_review], maxlen=500)
    return padded_review

def predict_sentiment(review):
    preprocessed_input = preprocess_text(review)
    prediction = model.predict(preprocessed_input)
    sentiment = "Positive 😊" if prediction[0][0] > 0.5 else "Negative 😞"
    return sentiment, prediction[0][0]

# Streamlit Config
st.set_page_config(page_title="🎬 Movie Review Sentiment Analyzer", layout="centered")

# Custom CSS for styling
st.markdown("""
    <style>
    body {
        background: linear-gradient(135deg, #ffecd2 0%, #fcb69f 100%);
        font-family: 'Arial', sans-serif;
    }
    .stTextArea textarea {
        color: black !important;
        background-color: #fff8f0;
        border: 2px solid #4CAF50;
        border-radius: 10px;
        font-size: 16px;
    }
    .stButton>button {
        background-color: #4CAF50;
        color: white;
        border-radius: 12px;
        height: 3em;
        width: 100%;
        font-size: 18px;
        font-weight: bold;
    }
    .stButton>button:hover {
        background-color: #45a049;
    }
    .result-box {
        padding: 20px;
        border-radius: 12px;
        text-align: center;
        font-size: 20px;
        font-weight: bold;
        margin-top: 20px;
    }
    .positive {
        background-color: #e0f7e9;
        color: #2e7d32;
        border: 2px solid #2e7d32;
    }
    .negative {
        background-color: #fdecea;
        color: #c62828;
        border: 2px solid #c62828;
    }
    </style>
""", unsafe_allow_html=True)

# App Title
st.markdown("<h1 style='text-align: center; color: #4CAF50;'>🎬 Movie Review Sentiment Analyzer</h1>", unsafe_allow_html=True)
st.write("Type in a movie review below and find out whether it's **Positive** or **Negative**.")

# Sidebar info
st.sidebar.header("ℹ️ About the App")
st.sidebar.write("""
This app uses a pre-trained **RNN model** on the IMDb dataset 
to classify movie reviews as **Positive or Negative**.  
""")

# User input
user_input = st.text_area("✍️ Enter your movie review:", height=150, placeholder="e.g. The movie was fantastic with brilliant acting!")

if st.button("🔮 Classify Review"):
    if user_input.strip() == "":
        st.warning("⚠️ Please enter a review before classification.")
    else:
        sentiment, score = predict_sentiment(user_input)
        confidence = score * 100 if "Positive" in sentiment else (1 - score) * 100

        if "Positive" in sentiment:
            st.markdown(f"<div class='result-box positive'>✅ Sentiment: {sentiment}<br>Confidence: {confidence:.2f}%</div>", unsafe_allow_html=True)
            st.progress(int(confidence))
        else:
            st.markdown(f"<div class='result-box negative'>❌ Sentiment: {sentiment}<br>Confidence: {confidence:.2f}%</div>", unsafe_allow_html=True)
            st.progress(int(confidence))
else:
    st.info("💡 Enter a review and click **Classify Review** to see results.")
