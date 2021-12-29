# Algumas formas de fazer a leitura dos dados xml



#importando as bibliotecas necessárias 

from bs4  import BeautifulSoup as bs
import pandas as pd

#abrindo arquivo xml com uma base de dados de exemplo
arquivo = open('fornecedores.xml',encoding="utf8")

leitura = arquivo.read()

# transformando essa base de dados em um objeto, propriedade da biblioteca BeautifulSoup para trazermos os dados em 
#uma forma mais amigável(limpa)

dados = bs(leitura, 'xml')

for data in dados.find_all('resource'):
     print(data.text)


# carregando as informações dos dados que desejado

for data in dados.find_all(['cnpj', 'nome', 'id_municipio', 'uf', 'id_natureza_juridica']):
     print(data.text)

# Outra forma para fazer a leitura dos dados é Criando uma tabela para receber todas as informações da base e  assim conseguir fazer uma análise melhor
tabela = pd.DataFrame(columns = [ "cnpj","nome", "id_municipio", "uf", "id_natureza_juridica", "id_porte_empresa", "id_cnae", "habilitado_licitar" ])

# fazendo um loop para captar todos os dados.

for texto in dados:
    



     # cnpj
    try:
         cnpj= texto.find( "cnpj").text.replace('\n', '')
            
    except:
        cnpj = 'None'

     # nome
    try:
         nome = texto.find("nome", ).text.replace('\n', '')
    except:
        nome = 'None'


        # id_municipio
    try:
        id_municipio = texto.find("id_municipio").text.replace('\n', '')
    except:
        id_municipio = 'None'


    # uf
    try:
        uf = texto.find("uf").text.replace('\n', '')
    except:
        uf = 'None'


     # id_natureza_juridica
    try:
        id_natureza_juridica = texto.find( "id_natureza_juridica").text.replace('\n', '')
    except:
        id_natureza_juridica = 'None'


    # id_porte_empresa
    try:
        id_porte_empresa = texto.find( "id_porte_empresa").text.replace('\n', '')

    except:
        id_porte_empresa = 'None'


     # id_cnae
    try:
        id_cnae = texto.find( "id_cnae").text.replace('\n', '')

    except:
        id_cnae = 'None'


     # habilitado_licitar
    try:
        habilitado_licitar = texto.find( "habilitado_licitar").text.replace('\n', '')

    except:
        habilitado_licitar = 'None'




    # Gravamos o resultado em nosso dataframe

    fornecedores = tabela.append({

                       'cnpj':cnpj,    
                       'nome':nome, 
                       'id_municipio':id_municipio,
                       'uf':uf,
                       'id_natureza_juridica':id_natureza_juridica,
                       'id_porte_empresa':id_porte_empresa,
                       'id_cnae':id_cnae,
                       'habilitado_licitar':habilitado_licitar
                                          },
                       ignore_index = True)


#Salvando os dados em disco
fornecedores.to_csv('fornecedores.csv', encoding = "utf-8", index = False)



