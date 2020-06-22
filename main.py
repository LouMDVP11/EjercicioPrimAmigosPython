from os import system
op = int(0)
while op != 3:
  print("\n\tM E N U")
  print("1. Mostrar números primos")
  print("2. Mostrar números amigos")
  print("3. SALIR\n")
  op = int(input("Ingrese una opción: "))
  if op == 1:
    n1 = int(input("Ingrese número inicial: "))
    n2 = int(input("Ingrese número final: "))
    cont=0
    if n1>n2:
      for x in range(n2, n1+1):
        for y in range(1,x+1):
          if(x%y==0):
            cont+=1
        if(cont==2 or x==1):
          print(x,"es primo")
        cont=0
    if n2>=n1:
      for x in range(n1, n2+1):
        for y in range(1,x+1):
          if(x%y==0):
            cont+=1
        if(cont==2 or x==1):
          print(x,"es primo")
        cont=0
  elif op == 2:
    n1 = int(input("Ingrese un número: "))
    n2 = int(input("Ingrese otro número: "))
    cont=0
    for y in range(1,n1):
      if(float(n1)%float(y)==0):
        cont+=y
    if(cont==n2):
      print("\nSON AMIGOS")
    else:
      print("\nNO SON AMIGOS")
    cont=0
  elif op == 3:
      print("Vuelva pronto")
  else:
      print("Usted ingresó un número no válido")
  g = input("\nPresione una tecla para continuar...")
  system("clear")
