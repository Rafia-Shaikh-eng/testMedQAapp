import streamlit as st
from transformers import pipeline

# ----------------------------
# App Title and Description
# ----------------------------
st.set_page_config(page_title="Medical Q/A App", page_icon="🩺", layout="centered")
st.title("🩺 Medical Question-Answering System")
st.write("Ask any medical or healthcare-related question based on the text you provide below.")

# ----------------------------
# Load BioBERT Model
# ----------------------------
@st.cache_resource
def load_model():
    model_name = "dmis-lab/biobert-base-cased-v1.1"
    return pipeline("question-answering", model=model_name, tokenizer=model_name)

qa_pipeline = load_model()

# ----------------------------
# Input Section
# ----------------------------
st.subheader("🧬 Input Text (Context)")
context = st.text_area(
    "Enter your medical or healthcare passage here:",
    "COVID-19 is caused by the SARS-CoV-2 virus. The most common symptoms are fever, cough, fatigue, and loss of taste or smell. Severe cases can cause pneumonia or respiratory failure.",
    height=200
)

st.subheader("💬 Ask Your Question")
question = st.text_input("Enter a medical question related to the above text:")

# ----------------------------
# Q/A Logic
# ----------------------------
if st.button("Get Answer"):
    if not question.strip() or not context.strip():
        st.warning("Please provide both context and a question.")
    else:
        with st.spinner("Analyzing medical context..."):
            try:
                result = qa_pipeline(question=question, context=context)
                st.success("✅ Answer Found:")
                st.markdown(f"**Answer:** {result['answer']}")
                st.markdown(f"**Confidence:** {round(result['score'] * 100, 2)}%")
            except Exception as e:
                st.error(f"Error: {e}")

# ----------------------------
# Footer
# ----------------------------
st.markdown("---")
st.caption("Developed by Rafia Shaikh 🧠 | Powered by BioBERT + Streamlit")
