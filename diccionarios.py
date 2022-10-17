
#-------------
# diccionario = {'c1' :'valor1', 'c2':'valor2'}
#consultar lo que hay en las claves
#resultado = diccionario['c1']
#print(resultado)
#--------------------------------------------------
#cliente = {'nombre' :'Juan', 'apellido':'Pino', 'peso': '50', 'talla':'1.80'}
#consulta = (cliente['apellido'])
#print(consulta)
#--------------------------------------------------
#diccionarios dentro de otro diccionario
#dic = {'c1':'55','c2':[10,20,30],'c3':{'s1':100,'s2' :200}}
#print(dic['c2'][1]) #solo imprime de la clave 2 el indice 1 = 20
#--------------------------------------------------
#Ejercicio para imprimir la letra E
#dic = {'c1':['a', 'b', 'c'], 'c2':['d','e','f']}
#print(dic['c2'][1].upper()) #Upper es para imprimirla en mayuscula
#--------------------------------------------------
#Para modificar la lista sin necesidad de modificar las variables
#aqui se agraga la variable 3:c
dic = {1:'a', 2:'b'}
print(dic)
dic[3] = 'c'
print(dic)
dic[2] = 'B' #Aqui se sobre escribe el valor anterior de 2 por lo tanto se imprime en mayuscula
print(dic)
print(dic.keys()) #Para imprimir solo las claves : 1,2,3
print(dic.values()) #Para imprimir solo los valores: a,B,c
print(dic.items()) #Para imprimir valores y claves : 1a,2B,3c
 
