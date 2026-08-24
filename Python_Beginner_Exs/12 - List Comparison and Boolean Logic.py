"""
Practice Problem: Write a function to return True if the first and last number of a given list is the same. If the numbers are different, return False.

Exercise Purpose: This exercise introduces “Collection Indexing” and “Boolean Flags.” Comparing data structure boundaries is common in pattern matching and data integrity checks.

Given Input:

numbers_x = [10, 20, 30, 40, 10]
numbers_y = [75, 65, 35, 75, 30]
"""

def VerificaPariedade_Primeiro_Ultimo(lista : list):
  if lista[0] == lista[-1]:
    return True
  else:
    return False
