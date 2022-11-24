#pedir un numero al usuario y que dibuje un triangulo rectangulo con asteriscos *
numero = int(input("Ingrese numero: "))
c = 0
triangulo = "*"
print("----while-----")
while (c < numero):
  print(triangulo)
  triangulo += "*"
  c += 1
print("-------for-----")
triangulo = "*"
for n in range(numero):
  print(triangulo)
  triangulo += "*"
