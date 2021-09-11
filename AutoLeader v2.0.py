import os

#ALTERAÇÕES V1.1
#O programa tava com um bug fudendo todo o assets! Fiz uma alteração
#agora para ver se ele altera apenas os arquivos terminados em php e html.

#VERSÃO 2.0
#Suporte ao Jotform
#Remoção dos PHPs
#Remoção das variáveis relacionadas aos PHPs.

print('#############################\nBEM-VINDO AO AUTOLEADER\n#############################\n')
print('O AutoLeader substitui automaticamente os dados dos modelos de GLead e GSite, facilitando e acelerando o processo.\n')
print('Lembre-se de sempre executar o programa dentro da pasta principal de uma cópia do modelo desejado. O programa irá buscar todos\nos arquivos .html automaticamente (inclusive nas subspastas!)\n\n')
print('Sempre que um valor não se aplicar, apenas aperte [enter]. O programa ignora quando não encontra nada para substituir.\n\n')

#Fase 1: Dando nome aos bois (definindo as strings que irão substituir os placeholders): 


print('#############################')
print('DADOS DOS HTML: ')

tagmng = input('Insira a Google Tag Manager: ')
fone1 = input('Insira o Fone 1: ')
whats1 = input('Insira o Whats 1: ')
dominio_cliente = input('Insira o domínio do cliente: ')
versaocliente = input('Insira o nome da pasta do cliente (versaocliente): ')
link_whats = input('Insira o link do Whatsapp: ')
parag_1 = input('Insira o parágrafo 1: ')
parag_2 = input('Insira o parágrafo 2: ')


print('#############################')
print('CÓDIGOS DOS FORMULÁRIOS: ')
jot_index = input('Index: ')
jot_cotar = input('Cotar: ')
jot_popup = input('Popup: ')
jot_whats = input('Whats: ')

print('#############################')
print('DADOS DA PAGE POLITICA.HTML: ')

nome_politica = input('Insira o nome: ')
email_politica = input('Insira o e-mail: ')
cpf_politica = input('Insira o CPF/CNPJ: ')
fone_politica = input('Insira o fone: ')


'''
Aqui embaixo tá rolando uma iteração por todos os arquivos que terminam
com .html. Preciso agora abrir cada um deles, buscar pelas strings que quero
substituir e fazer a substituição.

para substituir: queremos abrir o arquivo ( open() ), então encontrar e substituir ( replace(velho,novo) ) - por fim, salvar e fechar.
            

Esse for vai olhar em todas as subpastas também!
'''
#Fase 3: Pegando arquivo por arquivoe mostrando ao usuário, para em seguida encontrar e substituir as strings:
for subdir, dirs, files in os.walk('.'):
    for file in files:
        #print(os.path.join(subdir, file))
        arquivo = subdir + os.sep + file  
        if arquivo.endswith(".html"):
            print('Arquivo a ser editado: ', arquivo)
input('Pressione [enter] para fazer a substituição... ')
for subdir, dirs, files in os.walk('.'):
    for file in files:
        #print(os.path.join(subdir, file))
        arquivo = subdir + os.sep + file  
        if arquivo.endswith(".html"):
            print('Alterando arquivo: ', arquivo)
            #Fase 4: Lendo e trocando:
        try:
            if arquivo.endswith(".html"):
                with open(arquivo,'r',encoding="utf-8") as pagina:
                        trocador = pagina.read().replace('GTM-XXX',tagmng).replace('dominio-cliente',dominio_cliente).replace('fone1',fone1).replace('whats1',whats1).replace('versaocliente',versaocliente).replace('link-whats',link_whats).replace('parag-1',parag_1).replace('parag-2',parag_2).replace('jot-index',jot_index).replace('jot-cotar',jot_cotar).replace('jot-popup',jot_popup).replace('jot-whats',jot_whats).replace('nome-politica',nome_politica).replace('email-politica',email_politica).replace('cpf-cnpj-politica',cpf_politica).replace('fone-politica',fone_politica)
                with open(arquivo,'w',encoding="utf-8") as pagina:
                        pagina.write(trocador)
        except:
                with open(arquivo,'r',encoding="ISO-8859-1") as pagina:
                        trocador = pagina.read().replace('GTM-XXX',tagmng).replace('dominio-cliente',dominio_cliente).replace('fone1',fone1).replace('whats1',whats1).replace('versaocliente',versaocliente).replace('link-whats',link_whats).replace('parag-1',parag_1).replace('parag-2',parag_2).replace('jot-index',jot_index).replace('jot-cotar',jot_cotar).replace('jot-popup',jot_popup).replace('jot-whats',jot_whats).replace('nome-politica',nome_politica).replace('email-politica',email_politica).replace('cpf-cnpj-politica',cpf_politica).replace('fone-politica',fone_politica)
                with open(arquivo,'w',encoding="utf-8") as pagina:
                        pagina.write(trocador)
input('Obrigado por escolher a BernaCorp©!\n Pressione [enter] para sair ;)')
