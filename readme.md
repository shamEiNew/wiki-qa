# Retrieval Question Answering Chatbot ![](https://img.shields.io/badge/-OpenAI%20GPT%203.5-black) ![](https://img.shields.io/badge/-Cohere-purple) ![](https://img.shields.io/badge/-Pincone-black) ![](https://img.shields.io/badge/-langchain-red)

This repository contains the code for a Language Model (LLM) QA Chat Bot developed using Choere for vector embedding of Wikipedia-English. The Langchain framework is utilized to convert questions to embeddings using Cohere. The embeddings are then pushed to Pincone Vector Database.

The project incorporates semantic search and QA retrieval using Langchain and Pincone. To provide context-based answers, the OpenAI Large Language Model (LLM) GPT-3.5 Turbo is employed. 

## Deployment

The project is deployed on Streamlit and can be accessed using the following link: [LLm QA Chat Bot - Streamlit App](https://shameinew-wiki-qa-app-streamlit-app-4kc3ka.streamlit.app/)

## Components
The repository consists of the following components:

1. `cohere`: Contains the code for embedding Wikipedia-English using Choere.
2. `langchain`: Implements the Langchain framework for converting questions to embeddings using Cohere.
3. `pincone`: Handles the integration with Pincone Vector Database for storing and retrieving embeddings.
4. `semantic_search`: Implements semantic search and QA retrieval using Langchain and Pincone.
5. `llm_gpt_3_5_turbo`: Utilizes the OpenAI Large Language Model (LLM) GPT-3.5 Turbo to generate context-based answers.

### Components Graph
![Flow Diagram](files\flow_app.png)



## Usage

To use the LLm QA Chat Bot, follow these steps:

1. Clone the repository: `git clone https://github.com/shamEiNew/wiki-qa.git`
2. Install the required dependencies: `pip install -r requirements.txt`
3. Run the application: `streamlit run app.py`

Once the application is running, open a web browser and navigate to `http://localhost:5000` to access the wiki QA Chat Bot.

## Contributions

Contributions to this project are welcome. If you find any issues or have suggestions for improvements, please feel free to submit a pull request or open an issue.

## License

This project is licensed under the [MIT License](LICENSE).







