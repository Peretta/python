user = input('Cadastre um usuário: ')
senha = input('Cadastre uma senha: ')

while user == senha:
    print('A senha deve ser diferente do usuário')
    senha = input('Cadastre uma senha: ')
    
print('Cadastro feitto com sucesso')