import requests
from bs4 import BeautifulSoup
from scrape_wiki import search_wiki
# batch_url = ['https://www.investopedia.com/terms/c/cryptocurrency.asp', 'https://en.wikipedia.org/wiki/Lionel_Messi', 'https://en.wikipedia.org/wiki/Elon_Musk', 'https://en.wikipedia.org/wiki/Barack_Obama', 'https://en.wikipedia.org/wiki/Ukraine', 'https://en.wikipedia.org/wiki/Pacific_Ocean']
def get_keyword_multiple(urls):
    urls = urls.split(",")
    result = []
    for i in urls:
        keyword = get_keyword(i.replace("'", ""))
        result.append(keyword)
    return result
def get_keyword(url):
    # Check if wiki
    if "wikipedia" in url:
        wiki_result = search_wiki(url) if search_wiki(url) else "Wiki error"
        return wiki_result
    # Check the schema
    if "https://" not in url and "http://" not in url:
        url = "https://" + url
    # Start the request
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')
    result = ""
    # result = {"url":"", "title":"", "description":"", "h1_tag":""}
    # Get the meta data
    # title = soup.find("meta", property="og:title")
    # url = soup.find("meta", property="og:url")
    description = soup.find("meta", property="og:description")
    # title = title["content"] if title else "No meta title given"
    # url = url["content"] if url else "No meta url given"
    description = description["content"] if description else "No meta url given"
    # Get the p tag
    h1_tag = soup.find("h1")
    h1_tag = h1_tag.text
    # Construct result
    # result["url"] = url
    # result["title"] = title
    # if not description:
    #     result["h1_tag"] = h1_tag
    #     result["description"] = None
    #     return result
    # result["h1_tag"] = None
    # result["description"] = description
    result = description if description else h1_tag
    return result
        
if __name__ == "__main__":
    get_keyword(url)
    # get_keyword_multiple(batch_url)

