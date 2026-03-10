import streamlit as st
from rag_arch import create_add_load, query_index
from document_loader import load_pdfs_from_folder
from groq import Groq



st.title(" RAG Document Chatbot")

# API KEY
client = Groq(api_key=st.secrets["GROQ_API_KEY"])



folder_path = "data"

chunks = load_pdfs_from_folder(folder_path)

index, chunks = create_add_load(chunks)



if "chat_history" not in st.session_state:
    st.session_state.chat_history = []



user_input = st.text_input("Ask a question about the documents")

if user_input:

    results = query_index(index, user_input, chunks)

    if not results:
        st.write("No relevant information found in the documents.")
    else:

        context = "\n".join([r["text"] for r in results])

        memory_context = ""

        for turn in st.session_state.chat_history[-3:]:
            memory_context += f"User: {turn['question']}\n"
            memory_context += f"Assistant: {turn['answer']}\n"

        prompt = f"""
You are an AI assistant.

Answer the question using ONLY the context below.

Conversation History:
{memory_context}

Context:
{context}

Question:
{user_input}

Answer:
"""

        response = client.chat.completions.create(
            model="llama3-8b-8192",
            messages=[{"role": "user", "content": prompt}]
        )

        answer = response.choices[0].message.content

        st.session_state.chat_history.append({
            "question": user_input,
            "answer": answer
        })

        st.write("### 🤖 Answer")
        st.write(answer)



if st.session_state.chat_history:

    st.write("### 💬 Chat History")

    for chat in st.session_state.chat_history[::-1]:
        st.write("**You:**", chat["question"])

        st.write("**Bot:**", chat["answer"])

