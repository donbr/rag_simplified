# web_search.py
from langchain.utilities import GoogleSearchAPIWrapper

def search_web(query):
    search = GoogleSearchAPIWrapper()
    results = search.run(query)
    return results