from langchain_community.docstore.document import Document
from langchain.text_splitter import CharacterTextSplitter
from langchain_openai import OpenAI
from langchain.chains.summarize import load_summarize_chain
from langchain_community.document_loaders import UnstructuredURLLoader
from dotenv import load_dotenv
import openai
import os

load_dotenv()

def summarize(url):
    urls = [url]
    loader = UnstructuredURLLoader(urls = urls)
    data = loader.load()

    # splitting text
    chunk_size = 3000
    chunk_overlap = 200
    text_splitter = CharacterTextSplitter(
        chunk_size = chunk_size,
        chunk_overlap = chunk_overlap,
        length_function = len,
    )
    if len(data) > 0:
        texts = text_splitter.split_text(data[0].page_content)

        # converting content to document objects
        docs = [Document(page_content = t) for t in texts[:]]
        
        openai.api_key = os.getenv('OPENAI_API_KEY')
        llm = OpenAI(temperature = 0, openai_api_key = openai.api_key)

        # below step will find summary for all splitted document and will merge in one
        map_reduce_chain = load_summarize_chain(llm, chain_type = "map_reduce")
        output = map_reduce_chain.invoke(docs)['output_text']
        # print("\nsummary: ", output,end="\n")
        return output
    return "summary about a website"

