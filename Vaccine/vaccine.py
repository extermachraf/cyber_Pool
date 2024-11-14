import requests
import json
import argparse
import colorama
from utils.payloads import injections_payloads , register_payloads
import time

class vaccine:
    def __init__(self):
        self.url = None
        self.methode = None
        self.outputfile = None
    
    def parse_args(self):
        """
        Parse the command line arguments.
        """
        parser = argparse.ArgumentParser(description='SQL Injection Attack Tool')
        parser.add_argument('-o', '--output', type=str, default='storage.txt', help='The file to store the results')
        parser.add_argument('-X', '--request', type=str, choices=['GET', 'POST'], default='GET', help='The type of request to use')
        parser.add_argument('url', type=str, help='The URL of the website to test')
        args = parser.parse_args()
        
        self.url = args.url
        self.methode = args.request
        self.outputfile = args.output
    
    def send_request(self, data=None):
        """
        Send a request to the given URL with GET or POST method.
        """
        try:
            if self.methode == 'GET':
                for payload in injections_payloads:
                    url = self.url + payload
                    response = requests.get(self.url)
                    if response.status_code == 200:
                        self.store_payloads(payload, response)
            elif self.methode == 'POST':
                for payload in register_payloads:
                    response = requests.post(self.url, json=payload)
                    if response.status_code == 200:
                        self.store_payloads(payload)
        except Exception as e:
            print('\033[31m' + f"request can be send to {self.url} because of {e}")
            exit()
    def write_inside_file(self, text):
        with open(self.outputfile, 'a') as f:
            f.write(text + '\n')
          
    def store_payloads(self, payload, response=None):
        """
        Store the payloads in a file.
        """
        if self.methode == 'POST':
            self.write_inside_file(text=fr'request can be send with : "{payload}"')
        elif self.methode == 'GET':
            if not response.headers.get('Content-Type', '').startswith('text/html'):
                self.write_inside_file(text=fr'request can be send with : "{payload}"')
                self.write_inside_file(f" ===> [INFO] Non-HTML response found: {response.text[:100]}...")

    def lunch_vaccine(self):
        self.parse_args()
        self.send_request()
        
        
def main():
    v = vaccine()
    v.lunch_vaccine()
    
if __name__ == '__main__':
    main()

