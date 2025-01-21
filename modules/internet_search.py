from firecrawl import Firecrawler

def search_web(query):
    crawler = Firecrawler()
    results = crawler.search(query)
    return results
