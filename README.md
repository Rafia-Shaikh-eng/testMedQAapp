# 🩺 Medical Question-Answering App

This is a simple **healthcare Q/A system** powered by the **BioBERT** model.  
It takes a paragraph of medical text as input and answers user questions related to it.

---

## 🚀 Features
- Domain-specific Biomedical Q/A  
- Uses `dmis-lab/biobert-base-cased-v1.1`
- CPU-friendly and deployable on **Streamlit Cloud**

---

## 💻 Run Locally
```bash
pip install -r requirements.txt
streamlit run app.py
```

---

## ☁️ Deploy on Streamlit Cloud
1. Push this project to a **GitHub repository**
2. Go to [streamlit.io/cloud](https://streamlit.io/cloud)
3. Click **“New App” → Connect GitHub → Select Repo**
4. Choose the `main` branch and file `app.py`
5. Click **Deploy**

---

## 🧠 Example Use
**Context:**  
> Diabetes mellitus is a chronic metabolic disease characterized by high blood sugar levels over a prolonged period.

**Question:**  
> What disease is caused by high blood sugar levels?

**Answer:**  
> Diabetes mellitus
