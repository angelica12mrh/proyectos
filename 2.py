import random
def palabra()->str:
  palabras=["cangrejo", "zorro", "elefante","leon","tigre","perro","gato","loro","aguila"]
  numero=random.randint(0, len(palabras)-1)
  return palabras[numero]
a=palabra()
b=[]
for i in range(0,len(a)):
  b.append("_")
print(a)
print("Que empiecen los juegos: tematica animal")
print("No tener encuenta caracteres especiales")

error=0
vida=4
while True:
  z=0
  letra=str(input("Digite letra: "))
  letra=letra.casefold()
  for x in range(0,(len(a))):
    if(a[x]==letra):
      b[x]=letra  
      z+=1
  if(z==0):
        vida=vida-1
        error=error+1
        print("Tienes ",vida," vidas")
        
  if(vida==0):
     print("GAME OVER")
     break

  print("".join(b))  
  x="".join(b)
  if(x==a):
    print("GANASTE")
    break  
print("Gracias por participar")