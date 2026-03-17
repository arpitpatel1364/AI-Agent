from langchain_community.tools import WikipediaQueryRun
from langchain_community.tools.ddg_search.tool import DuckDuckGoSearchRun
from langchain_community.utilities import WikipediaAPIWrapper
from langchain_core.tools import tool

# Setup Wikipedia
wiki_wrapper = WikipediaAPIWrapper(top_k_results=1, doc_content_chars_max=1000)
wikipedia_tool = WikipediaQueryRun(api_wrapper=wiki_wrapper)

# Setup Search
search_tool = DuckDuckGoSearchRun()

@tool
def search_wikipedia(query: str) -> str:
    """Useful for factual, historical, or biographical information."""
    return wikipedia_tool.run(query)

@tool
def search_web(query: str) -> str:
    """Useful for current events, latest news, and real-time updates."""
    return search_tool.run(query)

# Export this list
tools_list = [search_wikipedia, search_web]