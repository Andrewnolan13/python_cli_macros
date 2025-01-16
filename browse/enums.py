import json
import os

this_dir = os.path.dirname(os.path.abspath(__file__))

class CommonUrls:
    urls = dict(
                    google  = "https://www.google.com",
                    bing    = "https://www.bing.com" ,
                    chatgpt = "https://chatgpt.com/"
                )

    # this is a static method, maybe java's not so bad after all
    def getURL(url:str)->str:
        try:
            return CommonUrls.urls[url.lower()]
        except KeyError:
            return url
    
    def saveURLName(name:str,url:str):
        if name:
            if url in CommonUrls.urls:
                raise ValueError(f"Cannot save alias as a predefined url. {url} is defined as {CommonUrls.urls[url]}")
            CommonUrls.addURL(name,url)
            CommonUrls.save()
    # makeNewURL
    def addURL(name:str,url:str):
        CommonUrls.urls[name] = url
        
    def save():
        with open(os.path.join(this_dir, 'common_urls.json'), 'w') as f:
            json.dump(CommonUrls.urls, f, indent=4)
    
    def load():
        with open(os.path.join(this_dir, 'common_urls.json'), 'r') as f:
            CommonUrls.urls.update(json.load(f))
    

