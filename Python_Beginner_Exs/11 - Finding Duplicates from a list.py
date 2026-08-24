"""
Practice Problem: Write a script that takes a list containing duplicate items and returns a new list with only unique elements.

Exercise Purpose: This exercise teaches “Data De-duplication.” In real-world data science, datasets are often “messy” with repeating entries. Mastering the conversion between Lists (which allow duplicates) and Sets (which do not) is the fastest way to clean data.

Given Input: data = [1, 2, 2, 3, 4, 4, 4, 5]

Expected Output: Unique List: [1, 2, 3, 4, 5]
"""

def remove_duplicates(lista : list):
  sett = set(lista) # Permite apenas elementos unicos  
  lista_denovo = list(sett)

  return lista_denovo


print (remove_duplicates([1,1,1,1,2,2,2,2,3,3,3,4,4,4,4,5,5,5,6,7,7,7,7,9,5,5,2,1,8]))
    
