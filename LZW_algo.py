# -*- coding: utf-8 -*-
"""
Created on Thu Aug  3 17:19:07 2017

@author: Ashish Kumar Jayant
@reference : geeksforgeeks.org , rosettacode.org
@title: LZW Compression Algorithm

"""
from io import StringIO
 
 ##--------compression---LZW------------------------
 
def compress(uncompressed):
    dict_size = 256
    dictionary = dict((chr(i), i) for i in range(dict_size))
    w = ""
    result = []
    for c in uncompressed:
        wc = w + c
        if wc in dictionary:
            w = wc
        else:
            result.append(dictionary[w])
            dictionary[wc] = dict_size
            dict_size += 1
            w = c
    if w:
        result.append(dictionary[w])
    return result

##-------------DECOMPRESS----------------------------

def decompress(compressed):
    dict_size = 256
    dictionary = dict((i, chr(i)) for i in range(dict_size))
    result = StringIO()
    w = chr(compressed.pop(0))
    result.write(w)
    for k in compressed:
        if k in dictionary:
            entry = dictionary[k]
        elif k == dict_size:
            entry = w + w[0]
        else:
            raise ValueError('Bad compressed k: %s' % k)
        result.write(entry)
        dictionary[dict_size] = w + entry[0]
        dict_size += 1
        w = entry
    return result.getvalue()

###--------------------------------------------------------------------------

print(compress("Troy was last loser"))
print(decompress(compress("Troy was last loser")))