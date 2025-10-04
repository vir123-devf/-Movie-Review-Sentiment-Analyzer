# 🎬 Movie Review Sentiment Analyzer  

This project is a **Movie Review Sentiment Analysis App** built with **TensorFlow, Keras, and Streamlit**.  
It classifies movie reviews as **Positive** or **Negative** using a pre-trained **Simple RNN model** trained on the IMDb dataset.  

---

## 🚀 Features
- ✅ User-friendly **Streamlit Web App** interface  
- ✅ Pre-trained **RNN model** (`Simple_rnn_imdb.h5`)  
- ✅ Real-time text input & classification  
- ✅ Confidence score with progress bar visualization  
- ✅ Custom-styled UI with gradient background and result cards  

---

## 📂 Project Structure
```

.
├── Simple_rnn_imdb.h5        # Pre-trained RNN model
├── app.py                    # Streamlit app code
├── requirements.txt          # Python dependencies
└── README.md                 # Project documentation

````

---

## ⚙️ Installation

Clone this repository:
```bash
git clone https://github.com/<your-username>/<repo-name>.git
cd <repo-name>
````

Create and activate a virtual environment (optional but recommended):

```bash
python -m venv venv
source venv/bin/activate   # On Mac/Linux
venv\Scripts\activate      # On Windows
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## ▶️ Run the App

```bash
streamlit run app.py
```

Then open the given local URL in your browser (default: `http://localhost:8501`).

---

## 🛠 Requirements

* Python 3.8+
* TensorFlow / Keras
* NumPy
* Streamlit

(Install automatically with `requirements.txt`.)

---

## 📊 Model Details

* Dataset: **IMDb Movie Reviews** (50,000 reviews, labeled positive/negative).
* Preprocessing: Tokenization + Padding (maxlen=500).
* Model: **Simple RNN** with ReLU activation.
* Output: Binary sentiment classification (Positive/Negative).

---

## 📷 Screenshots

Here’s how the app looks in action:
<img width="1915" height="859" alt="image" src="https://github.com/user-attachments/assets/6381a4d4-6812-4801-984b-93b334d53830" />

---

## 🎨 UI Preview

* Gradient background
* Custom styled input box
* Colored result cards:

  * 🟢 Green for Positive reviews
  * 🔴 Red for Negative reviews
* Progress bar showing confidence

---

## 👨‍💻 Author

**Virendra Badgotya**

* [GitHub](https://github.com/vir123-devf)
* [LinkedIn](https://www.linkedin.com/in/virendra-badgotya-ai/)


