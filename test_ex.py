import unittest

def change_char(str1):
    ending = 'ing' 
    if len(str1) > 3 and str1[-3:] == ending:
         str1 = str1.replace('ing', 'ly')
    else:
        str1 += 'ing'
    return str1

print change_char('kot') 


def test_change_char():
    assert (change_char('koting') == "kotly")

def test_change_char2():
    assert (change_char('kot') == "kotjh")
    
