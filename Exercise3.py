import string 
text = str(raw_input('type the text you want to convert: '))
rot_13 = string.maketrans( 
    "ABCDEFGHIJKLMabcdefghijklmNOPQRSTUVWXYZnopqrstuvwxyz", 
    "NOPQRSTUVWXYZnopqrstuvwxyzABCDEFGHIJKLMabcdefghijklm")
transtext = string.translate(text, rot_13)
print transtext