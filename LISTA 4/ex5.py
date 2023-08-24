#Seja o mesmo texto acima “splitado”. Calcule quantas palavras possuem uma das letras “python” e que tenham mais de 4 caracteres. Não se esqueça de transformar maiúsculas para minúsculas e de remover antes os caracteres especiais

import string

texto = "The Python Software Foundation and the global Python community welcome and encourage participation by everyone. Our community is based on mutual respect, tolerance, and encouragement, and we are working to help each other live up to these principles. We want our community to be more diverse: whoever you are, and whatever your background, we welcome you".lower()

palavras = texto.split()

def PalavraAchada(x):
  for c in x:
    if c in 'python':
      return True
  return False

resp = [p for p in palavras
        if PalavraAchada(p) and len(p) > 4]
print (resp)
print (len(resp))