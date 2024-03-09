from langchain_google_genai import GoogleGenerativeAI
from langchain_community.utilities import SQLDatabase
from langchain_experimental.sql import SQLDatabaseChain
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from langchain.prompts.prompt import PromptTemplate
from langchain.prompts import FewShotPromptTemplate
from langchain.chains.sql_database.prompt import PROMPT_SUFFIX, _mysql_prompt
from langchain.prompts import SemanticSimilarityExampleSelector
import few_shots

import os
from dotenv import load_dotenv
load_dotenv()


llm = GoogleGenerativeAI(model="models/text-bison-001", google_api_key=os.environ["GOOGLE_API_KEY"], temperature = 0.2)

db_user = "root"
db_password = "root"
db_host = "localhost"
db_name = "A2ZDigital"

db = SQLDatabase.from_uri(f"mysql+pymysql://{db_user}:{db_password}@{db_host}/{db_name}",sample_rows_in_table_info=1)

few_shot_list = []
for shot in few_shots.few_shots:
    converted_shot = f"{shot['Question']} {shot['SQLQuery']} {shot['SQLResult']} {shot['Answer']}"
    converted_shot = converted_shot.replace('\n', ' ')
    converted_shot = ' '.join(converted_shot.split())
    few_shot_list.append(converted_shot)

def sql_chain():
    embeddings = HuggingFaceEmbeddings(model_name='sentence-transformers/all-MiniLM-L6-v2')

    vectorstore = FAISS.from_texts(few_shot_list, embeddings, metadatas= few_shots.few_shots)

    example_selector = SemanticSimilarityExampleSelector(vectorstore=vectorstore, k=2,)

    example_prompt = PromptTemplate(
    input_variables=["Question", "SQLQuery", "SQLResult","Answer",],
    template="\nQuestion: {Question}\nSQLQuery: {SQLQuery}\nSQLResult: {SQLResult}\nAnswer: {Answer}",)

    few_shot_prompt = FewShotPromptTemplate(
    example_selector=example_selector,
    example_prompt=example_prompt,
    prefix=_mysql_prompt,
    suffix=PROMPT_SUFFIX,
    input_variables=["input", "table_info", "top_k"],)

    new_chain = SQLDatabaseChain.from_llm(llm, db, verbose=True, prompt=few_shot_prompt)

    return new_chain