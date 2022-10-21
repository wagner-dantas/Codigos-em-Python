'''

Welcome to GDB Online.
GDB online is an online compiler and debugger tool for C, C++, Python, Java, PHP, Ruby, Perl,
C#, OCaml, VB, Swift, Pascal, Fortran, Haskell, Objective-C, Assembly, HTML, CSS, JS, SQLite, Prolog.
Code, Compile, Run and Debug online from anywhere in world.

'''
n1 = float(input("Digite o primeiro numero:\n"))
n2 = float(input("Digite o segundo numero:\n"))
op = input("Digite a operação + - * /:\n")
if op == "+":
  print("O resultado da operação é: ",n1 + n2)
elif op == "-":
  print("O resultado da operação é: ",n1 - n2)
elif op == "*":
  print("O resultado da operação é: ",n1 * n2)
elif op == "/":
  print("O resultado da operação é: ",n1 / n2)
else:
  print("Operação invalida")