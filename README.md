# 🚀 Anapan AI Competitor Search Task

This project is a submission for the **Anapan AI Assignment**. It provides a solution to identify the top 5 competitors of a given brand based on textual similarity using NLP and cosine similarity. The goal was to create a functional, AI-enabled, and easy-to-use solution using open-source tools without relying on paid services or no-code platforms.

---

## 🔍 Project Objective

Build an intelligent search engine that allows users to enter a **brand name** and get the **top 5 most relevant competitors** from a dataset based on keywords and semantic similarity.

---

## 📁 Project Structure

anapan_ai_assignment/ ├── app.py # Streamlit app for UI ├── requirements.txt # Required Python libraries │ ├── data/ │ └── competitors.csv # Brand and keyword dataset │ ├── results/ │ └── virgin_collab_results.csv # Sample results │ └── utils/ ├── search.py # Core logic using TF-IDF & cosine similarity └── pycache/extract.pycd (compiled cache)


---

## ⚙️ How It Works

- Uses **TF-IDF vectorization** to convert brand keywords into numerical representations.
- Calculates **cosine similarity** between the input brand and other brands in the dataset.
- Returns the **top 5 most similar brands** as competitors.
- A simple and effective **Streamlit UI** is provided for real-time search.

---

## 🌐 Live Demo

🚀 Try the model here:  
**🔗 [Hugging Face Space: anapan_ai_Competitor_Task](https://huggingface.co/spaces/Satyam0077/anapan_ai_Competitor_Task)**

---

## 🧪 How to Run Locally

```bash
# Clone the repository
git clone https://github.com/Satyam0775/frombuggen.git
cd frombuggen

# Install dependencies
pip install -r requirements.txt

# Launch the app
streamlit run app.py

Tech Stack Used
Python 🐍

Streamlit for UI

Scikit-learn for TF-IDF and cosine similarity

Pandas for data manipulation

No paid services or no-code tools were used.

📜 Guidelines Followed
✅ Open-source only

✅ Full functionality using real AI models (TF-IDF)

✅ No paid APIs or platforms

✅ Clean code structure with reusability

📦 Submission
GitHub Repo: https://github.com/Satyam0775/frombuggen

Live URL: https://huggingface.co/spaces/Satyam0077/anapan_ai_Competitor_Task

👨‍💻 Author
Satyam Kumar Feroma

GitHub: Satyam0775

Hugging Face: Satyam0077
