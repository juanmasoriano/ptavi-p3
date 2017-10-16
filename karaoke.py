#!/usr/bin/python3
# -*- coding: utf-8 -*-

from xml.sax import make_parser
from xml.sax.handler import ContentHandler
from smallsmilhandler import SmallSMILEHandler
import sys
import json
import urllib.request


class KaraokeLocal(ContentHandler):

    def __init__ (self):
        """
        Constructor. Inicializamos las variables
        """
        self.inRootlayout = False
        self.root = ''
        self.width = ''
        self.height = ''
        self.bck_gr = ''
        self.frase = ''

        self.inRegion = False
        self.reg = ''
        self.id = ''
        self.top = ''
        self.bot = ''
        self.left = ''
        self.right = ''

        self.inImg = False
        self.img = ''
        self.src = ''
        self.region = ''
        self.beg = ''
        self.dur = ''

        self.inAudio = False
        self.audio = ''
        self.sr = ''
        self.beg1 = ''
        self.dur1 = ''

        self.inTextstream = False
        self.text = ''
        self.sr1 = ''
        self.region1 = ''

        self.el1 = ''
        self.el2 = ''
        self.el3 = ''
        self.el4 = ''
        self.el5 = ''

        self.jsonroot = {}
        self.jsonregion = {}
        self.jsonimg = {}
        self.jsonaudio = {}
        self.jsontext = {}


    def startElement(self, name, attrs):

        if name == 'root-layout':
            self.inRootlayout = True
            self.root = ('root_layout')

            if attrs.get('width',"") != "" :
                self.width = ('\twidth=' + attrs.get('width'))
                self.jsonroot['width'] = attrs.get('width')
            if attrs.get('height',"") != "":
                self.height = ('\theight=' + attrs.get('height'))
                self.jsonroot['height'] = attrs.get('height')    
            if attrs.get('background-color',"") != "":
                self.bck_gr = ('\tbackground-color=' + attrs.get('background-color'))
                self.jsonroot['background_color'] = attrs.get('background-color')
            self.el1 = (self.root + self.width + self.height + self.bck_gr + '\n')
        elif name == 'region':
            self.inRegion = True
            self.reg = ('region')

            if attrs.get('id',"") != "":
                self.id = ('\tid=' + attrs.get('id'))
                self.jsonregion['id'] = attrs.get('id')
            if attrs.get('top',"") != "":
                self.top = ('\ttop=' + attrs.get('top'))
                self.jsonregion['top'] = attrs.get('top')
            if attrs.get('bottom',"") != "":
                self.bot = ('\tbottom=' + attrs.get('bottom'))
                self.jsonregion['bottom'] = attrs.get('bottom')
            if attrs.get('left',"") != "":
                self.left = ('\tleft=' + attrs.get('left'))
                self.jsonregion['left'] = attrs.get('left')
            if attrs.get('right',"") != "":
                self.right = ('\tright=' + attrs.get('right'))
                self.jsonregion['right'] = attrs.get('right')
            self.el2 = (self.reg + self.id + self.top + self.bot + self.left + self.right + '\n')

        elif name == 'img':
            self.inImg = True
            self.img = ('img')

            if attrs.get('src',"") != "":
                tupla = attrs.get('src').partition("http://")
                if tupla[1] == 'http://':
                    urllib.request.urlretrieve(attrs.get('src',""),'img.jpg')
                    tupla1 = attrs.get('src').split("/")
                    self.src = ('\tsrc=' + tupla1[-1])
                    self.jsonimg['src'] = tupla1[-1]
                else:
                    self.src = ('\tsrc=' + attrs.get('src'))
                    self.jsonimg['src'] = attrs.get('src')
            if attrs.get('region',"") != "":
                self.region = ('\tregion=' + attrs.get('region'))
                self.jsonimg['region'] = attrs.get('region')
            if attrs.get('begin',"") != "":
                self.beg = ('\tbegin=' + attrs.get('begin'))
                self.jsonimg['begin'] = attrs.get('begin')
            if attrs.get('dur',"") != "":
                self.dur = ('\tdur=' + attrs.get('dur'))
                self.jsonimg['dur'] = attrs.get('dur')
            self.el3 = (self.img + self.src + self.region + self.beg + self.dur + '\n')

        elif name == 'audio':
            self.inAudio = True
            self.audio = ('audio')

            if attrs.get('src',"") != "":
                tupla = attrs.get('src').partition("http://")
                if tupla[1] == 'http://':
                    urllib.request.urlretrieve(attrs.get('src',""),'img.wav')
                    tupla1 = attrs.get('src').split("/")
                    self.sr = ('\tsrc=' + tupla1[-1])
                    self.jsonaudio['src'] = tupla1[-1]
                else:
                    self.sr = ('\tsrc=' + attrs.get('src'))
                    self.jsonaudio['src'] = attrs.get('src')
            if attrs.get('begin',"") != "":
                self.beg1 = ('\tbegin=' + attrs.get('begin'))
                self.jsonaudio['begin'] = attrs.get('begin')
            if attrs.get('dur',"") != "":
                self.dur1 = ('\tdur=' + attrs.get('dur'))
                self.jsonaudio['dur'] = attrs.get('dur')
            self.el4 = (self.audio + self.sr + self.beg1 + self.dur1 + '\n')

        elif name == 'textstream':
            self.inTextstream = True
            self.text = ('textstream')

            if attrs.get('src',"") != "":
                tupla = attrs.get('src').partition("http://")
                if tupla[1] == 'http://':
                    urllib.request.urlretrieve(attrs.get('src',""),'img.rt')
                    tupla1 = attrs.get('src').split("/")
                    self.sr1 = ('\tsrc=' + tupla1[-1])
                    self.jsontext['src'] = tupla1[-1]
                else:
                    self.sr1 = ('\tsrc=' + attrs.get('src'))
                    self.jsontext['src'] = attrs.get('src')
            if attrs.get('region',"") != "":
                self.region1 = ('\tregion=' + attrs.get('region'))
                self.jsontext['region'] = attrs.get('region')
            self.el5 = (self.text + self.sr1 + self.region1)

            print(self.el1 + self.el2 + self.el3 + self.el4 + self.el5)

            karaoke['root_layout'] = [self.jsonroot]
            karaoke['region'] = [self.jsonregion]
            karaoke['img'] = [self.jsonimg]
            karaoke['audio'] = [self.jsonaudio]
            karaoke['textstream'] = [self.jsontext]

            with open('karaoke.json', 'w') as file:
                json.dump(karaoke, file)

  
    def endElement(self, name):
        """
        Método que se llama al cerrar una etiqueta
        """
        if name == 'root-layout':
            self.inRootlayout = False
        if name == 'region':
            self.inRegion = False
        if name == 'img':
            self.inImg = False
        if name == 'audio':
            self.inAudio = False
        if name == 'textstream':
            self.inTextstream = False


if __name__ == "__main__":
    """
    Programa principal
    """
    karaoke = {}

    try:    
        fichero = sys.argv[1]
        parser = make_parser()
        cHandler = KaraokeLocal()
        parser.setContentHandler(cHandler)
        parser.parse(open(fichero))
    except IndexError:
        sys.exit('Usage:python3 karaoke.py file.smil.')
    except FileNotFoundError:
        sys.exit('Usage:python3 karaoke.py file.smil.')
