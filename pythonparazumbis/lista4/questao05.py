print("""Seja o mesmo texto acima “splitado”. Calcule quantas palavras possuem uma das letras “python” e que tenham mais de 4 caracteres. Não se esqueça de transformar maiúsculas para minúsculas e de remover antes os caracteres especiais. """)

statement = "The Python Software Foundation and the global Python community welcome and encourage participation by everyone. Our community is based on mutual respect, tolerance, and encouragement, and we are working to help each other live up to these principles. We want our community to be more diverse: whoever you are, and whatever background, we welcome you"

palavras = statement.replace(',','').replace('.','').replace(':','').strip()
palavras = palavras.lower().split()
i = 0
qtd_palavras = 0

for palavra in palavras:
    if len(palavra) >= 4:
        for i in range(len(palavra)):
            if palavra[i] in 'python':
                qtd_palavras += 1
                break
            
print(qtd_palavras)