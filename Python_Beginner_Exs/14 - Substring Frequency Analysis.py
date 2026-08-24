"""
Practice Problem: Write a program to find how many times the substring “Emma” appears in a given string.

Exercise Purpose: Text analysis and pattern matching are core pillars of programming. This exercise introduces searching for a “needle in a haystack,” a fundamental concept for building search engines or data validation tools.

Given Input:

str_x = "Emma is good developer. Emma is a writer"
Expected Output: Emma appeared 2 times
"""

def AcharSubstringEmma(string : str):
  count = string.count("Emma") #Conta a quantidade de vezes que emma aparece (.count)
  return count

print (AcharSubstringEmma("Emma Emma Emma Em,ma Emka, Ema, teste te stes teasda"))


