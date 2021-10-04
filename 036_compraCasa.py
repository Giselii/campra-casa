# Escreva um programa para aprovar o empréstimo bancário
# para a compra de uma casa. Pergunte o valor da casa,
# o salário do comprador e em quantos anos ele vai pagar.
# A prestação mensal não pode exceder 30% do salário ou então
# o empréstimo será negado.
valorcasa = float(input('Qual o valor da casa a ser comprada:R$ '))
valorsal = float(input('Qual o seu salário:R$ '))
anos = int(input('Em quantos anos deseja pagar o financiamento: '))
meses = anos * 12
valorlimite = (valorsal*30) / 100
print(meses)
if valorcasa / meses > valorlimite:
    print('Emprestimo NEGADO')
else:
    print('Empréstimo ACEITO!!')
