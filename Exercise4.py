from collections import OrderedDict

def RomanSymbols(noum):

    roman = OrderedDict()
    roman [1000] = "M"
    roman [900] = "CM"
    roman [500] = "D"
    roman [400] = "CD"
    roman [100] = "C"
    roman [90] = "XC"
    roman [50] = "L"
    roman [40] = "XL"
    roman [10] = "X"
    roman [9] = "IX"
    roman [5] = "V"
    roman [4] = "IV"
    roman [1] = "I"

    def IntToRoman(noum):
        for i in roman.keys():
            x, z = divmod(noum , i)
            yield roman[i] * x
            noum -= (i * x)
            if noum > 0:
                IntToRoman(noum)
            else:
                break

    return "".join([k for k in IntToRoman(noum)])
noum = int(input("Dwste enan akeraio arithmo:"))
print RomanSymbols(noum)
	
 
	