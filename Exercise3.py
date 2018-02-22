import string 
text = str(raw_input('Plhktrologhste to keimeno sas:'))
rot_13 = string.maketrans( 
    "ABCDEFGHIJKLMabcdefghijklmNOPQRSTUVWXYZnopqrstuvwxyz", 
    "NOPQRSTUVWXYZnopqrstuvwxyzABCDEFGHIJKLMabcdefghijklm")
transtext = string.translate(text, rot_13)
print transtext