#!/usr/bin/python3
def roman_to_int(roman_string):
    roman = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    a, prev = 0, 0
    if type(roman_string) == str:
        for i in reversed(roman_string):
            if i in roman:
                if roman[i] >= prev:
                    a += roman[i]
                    prev = roman[i]
                else:
                    a -= roman[i]
    return a
