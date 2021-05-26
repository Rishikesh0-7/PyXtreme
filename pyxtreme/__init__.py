"""PyAPI - The most easy to use api module"""

import requests


class Xtreme():

    def __init__(self):
        super().__init__()
        """
        Urls and json for the functions 
        """
        self.meme_url = "https://some-random-api.ml/meme"
        self.meme_json = requests.get(self.meme_url).json()

        self.df_url = "https://some-random-api.ml/facts/dog"
        self.df_json = requests.get(self.df_url).json()

        self.cf_url = "https://some-random-api.ml/facts/cat"
        self.cf_json = requests.get(self.cf_url).json()

        self.pf_url = "https://some-random-api.ml/facts/panda"
        self.pf_json = requests.get(self.pf_url).json()

        self.ff_url = "https://some-random-api.ml/facts/fox"
        self.ff_json = requests.get(self.ff_url).json()

        self.bf_url = "https://some-random-api.ml/facts/bird"
        self.bf_json = requests.get(self.bf_url).json()

        

        

        
    
    def getMeme(self):
        '''Returns a json of randome memes''' 
        return self.meme_json

    def getDogFact(self):
        """Gives a dog fact!"""
        return self.df_json['fact']

    def getPandaFact(self):
        """Gives a Panda fact!"""
        return self.pf_json['fact']

    def getCatFact(self):
        """Gives a cat fact!"""
        return self.cf_json['fact']

    def getFoxFact(self):
        """Gives a Fox fact!"""
        return self.ff_json['fact']

    def getBirdFact(self):
        """Gives a Bird fact!"""
        return self.bf_json['fact']

    def encode(self, text: str):
        """To encode the text to binary codes!"""
        bi = requests.get(f"https://some-random-api.ml/binary?text={text}").json()
        return bi['binary']

    def decode(self, text: str):
        """To encode the text to binary codes!"""
        bi = requests.get(f"https://some-random-api.ml/binary?decode={text}").json()
        return bi['text']
         