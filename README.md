# LLM-Chatbot-With-Custom-Database

### Here are the key highlights of our chatbot architecture workflow:


1.	User Input Analysis: When a user asks a question, we analyze it to identify the entities involved and their relationships.
2.	Knowledge Base Management: We maintain a knowledge base that includes synonyms for various entities, data structures, and table information.
3.	Entity Embedding: We convert this information into vector embeddings using Python libraries.
4.	Vector Database Query: We query a vector database that stores reference SQL queries and their corresponding DDL embeddings to find the closest semantic match.
5.	SQL Query Generation: Based on the user's question and the retrieved match, we generate a new SQL query (if needed) or utilize a reference SQL query (if available).
6.	Database Execution: The generated SQL query is executed on the database to retrieve the requested data.
7.	Feedback Loop: We implement a feedback loop to continuously improve our model by incorporating user feedback and analysis.


Create an environment first with these commands in the terminal window:

1. python -m venv llmchabot
2. llmchatbot\Scripts\Activate.ps1 - To activate the environment
3. pip install -r requirements.txt


After setting up the environment, you can run the code with the following command:

-> chainlit run main.py -w
