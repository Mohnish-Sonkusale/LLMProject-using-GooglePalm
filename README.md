# Q&A Chatbot-using-GooglePalm/LLM/FaissDB/streamlit
## PDF-Chatbot
PDF Q&A chatbot using LangChain and Gemini Pro

## LangChain:
LangChain is a orchestration framework for LLMs. It give us whole flexibility to use LLMs and utilize its intelligence as per our usecase.

## Google_Palm_key:
Google AI Studio creates a new Google Cloud project for each new API key. You also can create an API key in an existing Google Cloud project. All projects are subject to the Google Cloud Platform. Create_key : https://makersuite.google.com/app/apikey

## Faiss Vector Database:
Vector databases are specialized storage systems designed to house high-dimensional vectors or embeddings of data, particularly text. They possess the capacity for semantic search, enabling the retrieval of similar vectors as results. These databases play a crucial role in various GenAI applications and scenarios such as similarity search and the utilization of models like RAG.

## Streamlit:
Streamlit is an open source python library/framework used to create and share webpages/front end applications, sometimes to check the actual output for the client.

### General Pipeline of PDF-Chatbot :
Fetching text from uploaded pdf/n
Creating Chunks of extracted text
Applying Embeddings on chunks and storing it in any Vector db
Taking user query from prompt
Applying same Embeddings on query question text
Searching and extracting most similar chunks from vector db using (using semantic search or cosine similariy)
Passing most similar chunk along with question as an input prompt to LLM. (RAG)
LLM will generate relevant output as per user question.
