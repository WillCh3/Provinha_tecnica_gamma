"""Elabore um programa que leia um número que o usuário digitar. Dependendo do
número informado, das frases abaixo, o sistema imprimirá somente as que forem
verdadeiras.
○ O número é menor que 10.
○ O número é par.
○ O número está entre 8 e 16.
○ O número é 51 ou 80.
Por exemplo, se o usuário digitar o número “12”, o programa irá imprimir:
O número é par.
O número está entre 8 e 16.
Se o usuário digitar o número “51”, então será impresso:
O número é 51 ou 80.
Ou, se o usuário digitar “101”, então o programa não imprime nada."""


sair = "C"
while sair == 'C':
   print('\n')
   num = int(input("Digite um numero: "))
   if num < 10:
      print('O número é menor que 10.')
   if num % 2 == 0:
      print('O número é par.')
   if num >= 8 and num <= 16 :
      print('O número está entre 8 e 16.')
   if num == 51 or num == 80:
      print('O número é 51 ou 80.')

   sair = input('\n\nDigite: \nS para sair\nC para continuar: ').upper()