"""
Practice Problem: Given a list of integers, find and print both the largest and the smallest numbers.

Exercise Purpose: This exercise explores “Aggregate Functions.” While Python has built-in tools for this, understanding how to identify extremes is critical for data normalization, where you often need to find the range of a dataset before processing it.

Given Input: nums = [45, 2, 89, 12, 7]

Expected Output: Largest: 89 Smallest: 2
"""

def minmax(list : list):
  list.sort() #.sort ordena a lista de maior para o menor
  min = list[0]
  max = list[-1]

  return (min, max)

#PODIA TER SO USADO A FUNCAO MAX() E MIN. SENDO MAX(LIST) E MIN(LIST)

print (minmax([5,1,2,3,7,4])) 