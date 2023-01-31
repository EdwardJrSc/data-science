Numbers = "123456"

print(Numbers[1::2] )

print("01234567"[::2])

name = 'edward'

print(name.upper())

tupla = (1,2,3,4,5)

print(tupla[1], "prueba") # De esta forma se busca por el indice
print(tupla[-1])

B = ["a","b","c"]
print(B[1:])

mySet = {"Edward", "Sierra", "Lola"}
marySet = {"Mary", "Acosta", "Lola"}

print("Edward" in mySet)
print("Mary" in marySet)
print(mySet & marySet) # Interseccion
print(mySet.union(marySet)) # Union

dic = {"Edward": 23, "Mary": 18, "Lola": 3}
dic['Alberto'] = '34'
del(dic["Lola"])
print(dic)

Dict={"A":1,"B":"2","C":[3,3,3],"D":(4,4,4),'E':5,'F':6}

print(Dict["D"])

L = [1,2,3]
L.append(['a','b'])
print(L)

i = 1
print(i!=0)



x=3
y=1

while(y!=x):
  print(y)
  y=y+1


list = [7.2,2.5,3.6,4.1]

print(len(list), 'Conteo de elementos')
print(sum(list), 'Suma de todos los elementos') # Sumar los elementos de un array
print(sorted(list, reverse = True), 'Sorted') # Los ordena en order ascendente, y el uso de la bandera para cambiar
print(list.sort()) # Consultar para que sirve el sort
