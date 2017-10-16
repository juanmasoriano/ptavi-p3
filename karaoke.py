#!/usr/bin/python3
# -*- coding: utf-8 -*-

from xml.sax import make_parser
from xml.sax.handler import ContentHandler
from smallsmilhandler import SmallSMILEHandler
import sys

class SmallSMILEHandler(ContentHandler):

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



    def startElement(self, name, attrs):

        if name == 'root-layout':
            self.inRootlayout = True
            self.root = ('root_layout')

            if attrs.get('width',"") != "" :
                self.width = ('\twidth=' + attrs.get('width'))
            if attrs.get('height',"") != "":
                self.height = ('\theight=' + attrs.get('height'))    
            if attrs.get('background-color',"") != "":
                self.bck_gr = ('\tbackground-color=' + attrs.get('background-color'))
            print(self.root + self.width + self.height + self.bck_gr)

        elif name == 'region':
            self.inRegion = True
            self.reg = ('region')

            if attrs.get('id',"") != "":
                self.id = ('\tid=' + attrs.get('id'))
            if attrs.get('top',"") != "":
                self.top = ('\ttop=' + attrs.get('top'))
            if attrs.get('bottom',"") != "":
                self.bot = ('\tbottom=' + attrs.get('bottom'))
            if attrs.get('left',"") != "":
                self.left = ('\tleft=' + attrs.get('left'))
            if attrs.get('right',"") != "":
                self.right = ('\tright=' + attrs.get('right'))
            print(self.reg + self.id + self.top + self.bot + self.left + self.right)

        elif name == 'img':
            self.inImg = True
            self.img = ('img')

            if attrs.get('src',"") != "":
                self.src = ('\tsrc=' + attrs.get('src'))
            if attrs.get('region',"") != "":
                self.region = ('\tregion=' + attrs.get('region'))
            if attrs.get('begin',"") != "":
                self.beg = ('\tbegin=' + attrs.get('begin'))
            if attrs.get('dur',"") != "":
                self.dur = ('\tdur=' + attrs.get('dur'))
            print(self.img + self.src + self.region + self.beg + self.dur)

        elif name == 'audio':
            self.inAudio = True
            self.audio = ('audio')

            if attrs.get('src',"") != "":
                self.sr = ('\tsrc=' + attrs.get('src'))
            if attrs.get('begin',"") != "":
                self.beg1 = ('\tbegin=' + attrs.get('begin'))
            if attrs.get('dur',"") != "":
                self.dur1 = ('\tdur=' + attrs.get('dur'))
            print(self.audio + self.sr + self.beg1 + self.dur1)

        elif name == 'textstream':
            self.inTextstream = True
            self.text = ('textstream')

            if attrs.get('src',"") != "":
                self.sr1 = ('\tsrc=' + attrs.get('src'))
            if attrs.get('region',"") != "":
                self.region1 = ('\tregion=' + attrs.get('region'))
            print(self.text + self.sr1 + self.region1)

  
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
    try:    
        fichero = sys.argv[1]
        parser = make_parser()
        cHandler = SmallSMILEHandler()
        parser.setContentHandler(cHandler)
        parser.parse(open(fichero))
    except IndexError:
        sys.exit('Usage:python3 karaoke.py file.smil.')
    except FileNotFoundError:
        sys.exit('Usage:python3 karaoke.py file.smil.')
