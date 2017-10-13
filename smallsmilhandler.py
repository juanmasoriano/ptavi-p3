#!/usr/bin/python3
# -*- coding: utf-8 -*-

from xml.sax import make_parser
from xml.sax.handler import ContentHandler

class SmallSMILEHandler(ContentHandler):

    def __init__ (self):
        """
        Constructor. Inicializamos las variables
        """
        self.rootlayout = {}
        self.inRootlayout = False
        self.region = {}
        self.inRegion = False
        self.img = {}
        self.inImg = False
        self.audio = {}
        self.inAudio = False
        self.textstream = {}
        self.inTextstream = False
        self.lista_total = []

    def startElement(self, name, attrs):
        """
        Método que se llama cuando se abre una etiqueta
        """
        if name == 'root-layout':
            self.inRootlayout = True
            self.rootlayout['width'] = attrs.get('width',"")
            self.rootlayout['height'] = attrs.get('height',"")
            self.rootlayout['background-color'] = attrs.get('background-color', "")
            self.lista_total.append('root-layout: ')
            self.lista_total.append(self.rootlayout)
        elif name == 'region':
            self.inRegion = True
            self.region['id'] = attrs.get('id',"")
            self.region['top'] = attrs.get('top',"")
            self.region['bottom'] = attrs.get('bottom',"")
            self.region['left'] = attrs.get('left',"")
            self.region['right'] = attrs.get('right',"")
            self.lista_total.append('region: ')
            self.lista_total.append(self.region)
        elif name == 'img':
            self.inImg = True
            self.img['src'] = attrs.get('src',"")
            self.img['region'] = attrs.get('region',"")
            self.img['begin'] = attrs.get('begin',"")
            self.img['dur'] = attrs.get('dur',"")
            self.lista_total.append('img: ')
            self.lista_total.append(self.img)
        elif name == 'audio':
            self.inAudio = True
            self.audio['sr'] = attrs.get('src',"") 
            self.audio['begin'] = attrs.get('begin',"")
            self.audio['dur'] = attrs.get('dur',"")
            self.lista_total.append('audio: ')
            self.lista_total.append(self.audio)
        elif name == 'textstream':
            self.inTextstream = True
            self.textstream['src'] = attrs.get('src',"")
            self.textstream['region'] = attrs.get('region',"")
            self.lista_total.append('textstream: ')
            self.lista_total.append(self.textstream)
            print(self.lista_total)
  
    def endElement(self, name):
        """
        Método que se llama al cerrar una etiqueta
        """
        if name == 'root-layout':
            self.rootlayout = {}
            self.inRootlayout = False
        if name == 'region':
            self.region = {}
            self.inRegion = False
        if name == 'img':
            self.img = {}
            self.inImg = False
        if name == 'audio':
            self.audio = {}
            self.inAudio = False
        if name == 'textstream':
            self.textstream = {}
            self.inTextstream = False

if __name__ == "__main__":
    """
    Programa principal
    """
    parser = make_parser()
    cHandler = SmallSMILEHandler()
    parser.setContentHandler(cHandler)
    parser.parse(open('karaoke.smil'))
