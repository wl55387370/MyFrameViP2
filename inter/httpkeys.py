#coding=utf8
import requests

class HTTP():
    def __init__(self):
        self.session = requests.session()