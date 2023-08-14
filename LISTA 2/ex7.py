area = int(input('Área: '))

if area/(18*3) == 0:
    latas = area/(18*3)
else:
    latas = int(area/(18*3)) + 1
preco = latas*80
print("Latas: ", latas, "\n", "Preço: ",preco )
