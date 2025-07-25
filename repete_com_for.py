#!/usr/bin/env python3

#numbers = [1, 2, 3, 4, 5, 6]
#numbers = range(1, 700, 100)
'''
numbers = range(1,11)

#Iterable
for number in numbers:
    par = number % 2 == 0
    if par:
        print(number)
    else:
        continue

    print(f'mais código com {number}')
'''

'''
dados = {}

for line in open("post.txt"):
    if line == "---\n":
        break
    key, valor = line.split(":")
    dados[key] = valor.strip()
    
print(dados)
print(dados["title"])
'''

# For loops / laço for
original = [1, 2, 3]
dobrada = []
for n in original:
    dobrada.append(n * 2)
print(dobrada)

# Funcional
# List Comprehension
dobrada = [n * 2 for n in original]
print (dobrada)

# Dict comprehension
#dados = [line for line in open("post.txt") if ":" in line]
dados = {
    #key: value
    line.split(":")[0]: line.split(":")[1].strip()
    for line in open("post.txt") 
    if ":" in line
    }

dados = {}
for line in open("post.txt"):
    if ':' in line:
        key, valor = line.split(":")
        dados[key] = valor.strip()

print(dados)