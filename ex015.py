dias = int(input("Quantos dias o carro foi alugado? "))
km = float(input("Quantos km o carro rodou? "))
preco = (dias * 60) + (km * 0.15)
print("O total a ser pago é de R${:.2f}".format(preco))




