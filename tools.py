import os
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
    """Useful for current events, latest news, and real-time updates using DuckDuckGo."""
    return search_tool.run(query)

# Export this list
tools_list = [search_wikipedia, search_web]

# Conditionally add Tavily search tool when TAVILY_API_KEY is set
if os.getenv("TAVILY_API_KEY"):
    from tavily import TavilyClient

    _tavily_client = TavilyClient()

    @tool
    def search_web_tavily(query: str) -> str:
        """Useful for current events, latest news, and real-time updates using Tavily.
        Provides high-quality, AI-optimized search results."""
        response = _tavily_client.search(query=query, max_results=5, search_depth="basic")
        results = response.get("results", [])
        if not results:
            return "No results found."
        return "\n\n".join(
            f"{r['title']}\n{r['url']}\n{r.get('content', '')}" for r in results
        )

    tools_list.append(search_web_tavily)