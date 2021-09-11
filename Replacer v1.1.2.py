import os

#Funcionamento será semelhante ao AutoLeader:
#
# 1 - Receber input do dado a ser trocado;
# 2 - Procurar dentro da pasta pelos arquivos HTML/PHP;
# 3 - Abrir os arquivos encontrados;
# 4 - Iterar nos arquivos html/php atrás do dado inserido;
#
# - Se a string for encontrada:
#  5 - Mostrar em qual arquivo foi encontrada
#  6 - Substituí-la.
#  7 - Após a substituição, salvar e fechar.
#
# - Se ela não for encontrada:
#   - Avisar o usuário.

#v1.1 - Adicionei pergunta para mais trocas.
#v1.1.2 - Adicionei suporte a arquivos CSS.


print('#'*24)
print('REPLACER!')
print('O replacer aceita qualquer valor que você quiser trocar nas páginas HTML, PHP ou CSS. Facilita sua vida!')

while True:
    # Recebendo o input:
    replaced = input('Insira o valor a ser substituído: ')
    replacer = input('Agora insira o valor que você quer colocar no lugar: ')

    # Procurando dentro da pasta onde estamos ('.'):

    print(f'Pesquisaremos dentro dos seguintes arquivos pelo valor {replaced}:')

    for subdir, dirs, files in os.walk('.'):
        for file in files:
            arquivo = subdir + os.sep + file        
            if arquivo.endswith('.html') or arquivo.endswith('.php') or arquivo.endswith('.css'):
                print(arquivo)

    input('Pressione [enter] para fazer a substituição...')

    for subdir, dirs, files in os.walk('.'):
        for file in files:
            arquivo = subdir + os.sep + file            
            if arquivo.endswith('.html') or arquivo.endswith('.php') or arquivo.endswith('.css'): 
                try:
                    with open(arquivo,'r',encoding="utf-8") as pagina:
                        trocador = pagina.read().replace(replaced,replacer)
                    with open(arquivo,'w',encoding="utf-8") as pagina:
                        pagina.write(trocador)
                    print(f'Substituindo no arquivo: {arquivo}')
                except:
                    with open(arquivo,'r',encoding="ISO-8859-1") as pagina:
                        trocador = pagina.read().replace(replaced,replacer)
                    with open(arquivo,'w',encoding="utf-8") as pagina:
                        pagina.write(trocador)
                    print(f'Substituindo no arquivo: {arquivo}')
                    
    print('Feito!')
    
    question = input('Deseja fazer mais uma troca? (s/n)')
    if question == 's':
        continue
    elif question == 'n':
        input('bye bye! :)')
        break
    
                
                

