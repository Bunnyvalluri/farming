import requests

def get_real_url(google_url):
    try:
        # Use a real user agent
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        }
        res = requests.get(google_url, headers=headers, allow_redirects=True, timeout=5)
        return res.url
    except Exception as e:
        return str(e)

if __name__ == "__main__":
    test_url = "https://news.google.com/rss/articles/CBMisAFBVV95cUxNSGtlODFRR3BNZmxTRHhLclV0eHByYWNNbWlBZWU1RmZ6X3NYTThzNWlSM3RsSWdSRFk2RGpPdkpIdzQxX0tXU2tTRTNNZDJyQ1FmNWdyODN0cTBybGN6VzFHRUFtU0ZZd29UdlFwQndUSkFDbFhWbnF1QnpfMWVTR3hXck1YWG5iWTVkQTh3bTNJOU5kbl9NRTRPTEcyNVBKVnBDbENudjdNVEtNbms?oc=5"
    print("Real URL:", get_real_url(test_url))
