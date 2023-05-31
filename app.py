from backend.pincone_vdb import *
from backend.chat import *
import logging
import streamlit as st

st.set_page_config(layout="wide")





@st.cache_resource
def pincone_vector_db():
    index = create_pinecone_index("chat-qa-wikipedia")
    logging.info(index.describe_index_stats())

    return index


@st.cache_resource
def chat_func():
    index = pincone_vector_db()
    embeddings = co_embedding()
    vectorstore =  vectorstores(index, embeddings)
    llm = llm_openai()
    qa = retrieval_qa(llm, vectorstore)
    return qa, vectorstore



@st.cache_resource
def run_chat(query,k=3, flag=True):
    qa, vectorstore = chat_func()

    if flag:
        answer = qa.run(query)
        return answer
    else:
        pages = vectorstore.similarity_search(query, k=k)
        result = [page.page_content for page in pages]
        return result


def run_app():
    col1, col2 = st.columns(2)
    options = ("Semantic Search", "Chat QA")
    with col1:
        st.subheader("Response Type")
        radio = st.radio("Select",options)
        st.subheader("Flow of the chatbot")
        st.image("files/flow_app.png", width=500)

    with col2:
        st.subheader("Response")
        if radio == options[0]:
            text = st.text_input("Write your text here:")
            neighbors = st.text_input("Enter number of results to show:")
            button = st.button("Response")

            if button:
                with st.spinner("Searching in Vectot DB with metric cosine.."):
                    try:
                        neighbors = int(neighbors)
                        pages = run_chat(text, k=int(neighbors), flag=False)
                        for page in pages:
                            st.markdown(page)
                    except:
                         st.write("Not supported. Only Positive Integers are supported")
                    
        if radio == options[1]:
            text = st.text_input("Write your question here")
            button = st.button("Response")

            if button:
                with st.spinner("Waiting for response..."):
                    answer = run_chat(text)
                    st.markdown(answer)

if __name__=="__main__":
    page_bg_img = '''<style>body {
        background-image: url("https://cdn.pixabay.com/photo/2014/05/27/23/32/matrix-356024_1280.jpg");
        background-size: cover;
        }
        </style>'''
    st.markdown(page_bg_img, unsafe_allow_html=True)
    run_app()


    


