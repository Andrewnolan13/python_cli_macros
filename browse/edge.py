"""
Starts an instance of ms edge.
My company uses edge as the default browser, and it fills it up with a load of bloatware landing pages that make it extremely slow.
This jumps over the bloatware and opens a new tab with the url of your choice.
"""
import os
import sys

from selenium import webdriver
from selenium.webdriver.edge.options import Options

from .enums import CommonUrls

class Edge:
    def __init__(self,url = 'google',saveUrlName = '',alias = False):
        self.urlArgs(url,saveUrlName,alias)

        self.options = Options()
        self.config_options()

        self.driver = webdriver.Edge(options=self.options)
        self.closeStartUpTabs()
        self.get(CommonUrls.getURL(url))
        
        self.keepAlive()
    
    def config_options(self):
        self.options.add_argument("--disable-blink-features=AutomationControlled")
        self.options.add_argument("user-data-dir={LOCALAPPDATA}\\Microsoft\\Edge\\User Data".format(**os.environ))
        self.options.add_experimental_option("excludeSwitches", ["enable-automation"])

    def get(self, url):
        self.driver.get(url)
    
    def closeStartUpTabs(self):
        tabs = self.driver.window_handles
        self.driver.switch_to.window(tabs[0])
        self.driver.close()
        self.driver.switch_to.window(tabs[-1])
    
    def keepAlive(self):
        try:
            while True:
                pass
        except KeyboardInterrupt:
            sys.exit()
    
    def urlArgs(self,url,saveUrlName,alias):
        CommonUrls.load()
        CommonUrls.saveURLName(saveUrlName,url)
        if alias:
            mx = max([len(k) for k in CommonUrls.urls.keys()])
            for alias,url in CommonUrls.urls.items():
                print(f"{alias}{' '*(mx-len(alias))} : {url}")
            
if __name__ == "__main__":
    edge = Edge()

