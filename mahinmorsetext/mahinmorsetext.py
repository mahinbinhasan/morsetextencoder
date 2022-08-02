"""
This module implements the main functionality of Mahinmorsetext.
Author: MAHIN BIN HASAN
YouTube: https://www.youtube.com/c/AlMahin
Github: https://github.com/mahinbinhasan
Facebook: https://facebook.com/root.mahin
"""

__author__ = "Mahin Bin Hasan"
__email__ = "allmahin149@gmail.com"
__status__ = "planning"
mrsd = {'A':'.-', 
        'B':'-...',
        'C':'-.-.',
        'D':'-..',
        'E':'.',
        'F':'..-.',
        'G':'--.',
        'H':'....',
        'I':'..',
        'J':'.---',
        'K':'-.-',
        'L':'.-..',
        'M':'--',
        'N':'-.',
        'O':'---', 
        'P':'.--.', 
        'Q':'--.-',
        'R':'.-.',
        'S':'...',
        'T':'-',
        'U':'..-', 
        'V':'...-', 
        'W':'.--',
        'X':'-..-',
        'Y':'-.--',
        'Z':'--..',
        '1':'.----',
        '2':'..---',
        '3':'...--',
        '4':'....-',
        '5':'.....',
        '6':'-....',
        '7':'--...',
        '8':'---..',
        '9':'----.',
        '0':'-----',
        ', ':'--..--',
        '.':'.-.-.-',
        '?':'..--..',
        '/':'-..-.',
        '-':'-....-',
        '(':'-.--.',
        ')':'-.--.-'}
class texttomorse:
    def gen(textin):
        text = str(textin)
        texta = []
        texta [:0] = text
        mrst = ''
        for i in texta:
            d = str(mrsd.get(i))
            print(d)
            mrst = mrst + d + ' '
        return mrst
class morsetotext:
    def gen(morsein):
        tin = str(morsein)
        text = tin.split()
        mrst = ''
        for i in text:
            if i != '/':
                for k,v in mrsd.items():
                    if v == i:
                        d = k
                        print(d)
                        mrst = mrst + d
            else:
                mrst = mrst + ' '
        return mrst