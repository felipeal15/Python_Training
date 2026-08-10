"""
Practice Problem: Display only those characters which are present at an even index number in given string.

Exercise Purpose: Understand how data is stored in memory using zero-based indexing. 
In most languages, the first character is at position 0, the second at 1, and so on. Mastering indexing is vital for data parsing.

Given Input: String: "pynative"

Expected Output:

Original String is  pynative
Printing only even index chars
p
n
t
v
"""

def even_char(string : str):
  print (f"String original: {string}")
  print (f"Printando apenas agora os caracteres com o index impar ")
  for i in range(len(string)):
    if i % 2 == 0:
      print (string[i])

#nao precisa necessariamente ter return!

even_char("teste")

#Tem como fazer tambem, utilizando SLICING:

# caracteres_impares = string[0::2]
# for caracter in caracteres_impares:
#  print (caracter)
