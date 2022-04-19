# A-Social-Browser-Extension-
CSE573 Group28

This is the api to get keyword from a website
## Installment
```
flask
BeautifulSoup
requests
```
## Example
endpoint: `http://127.0.0.1:5000/url?url=XXX`
- XXX is where you input the url\n
e.g. Get keyword from website: https://www.investopedia.com/terms/c/cryptocurrency.asp

### Format
Command: `curl "127.0.0.1:5000/url?url=https://www.investopedia.com/terms/c/cryptocurrency.asp"`
### Return value
JSON file:
```json
{
  "description": "A cryptocurrency is a digital or virtual currency that uses cryptography and is difficult to counterfeit.",
  "h1_tag": null,
  "title": "What Is Cryptocurrency?",
  "url": "https://www.investopedia.com/terms/c/cryptocurrency.asp"
}
```
