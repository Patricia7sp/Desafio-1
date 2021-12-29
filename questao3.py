
#importando as bibliotecas necessárias 

from bs4  import BeautifulSoup as bs
import pandas as pd

#abrindo arquivo xml com uma base de dados de exemplo
arquivo= open('arquivo_xml.xml','r')

#Fazendo a leitura dos dados
leitura= arquivo.read()

## transformando essa base de dados em um objeto, propriedade da biblioteca BeautifulSoup para trazermos os dados em 
#uma forma mais amigável(limpa)

dado = bs(leitura, 'xml')

# Criando uma tabela para receber todas as informações da base e  assim conseguir fazer uma análise melhor
tabela = pd.DataFrame(columns = ['cnpj', 'data_envio', 'nome', 'data_contratacao', 'indicador', 'data_venc_ult_parcela',
                              'valor_contrato_futuro', 'qtd_total_parcelas', 'qtd_parcelas_aberta', 'numero_parcela', 'data_venc'
                              'valor_parcela', 'data_pagamento', 'valor_pago', 'situacao_parcela', 'data_venc_prox_parcela', 'valor_prox_parcela',
                              'qtd_parcelas_vencer'])



# Loop pelos resultados do scraping e extração dos dados nas tags xmL do nosso interesse

for texto in dado:
    
    


     # cnpj
    try:
         cnpj= texto.find( "numero").text.replace('\n', '')
            
    except:
        cnpj = 'None'
    
           # data_envio
    try:
        data_envio = texto.find("DataRemessa").text.replace('\n', '')
    except:
        data_envio = 'None'


     # nome
    try:
         nome = texto.find("Identificacao", ).text.replace('\n', '')
    except:
        nome = 'None'


 

    # data_contratacao
    try:
        data_contratacao = texto.find("DadosContrato").text.replace('\n', '')
    except:
        data_contratacao = 'None'


     # indicador
    try:
        indicador = texto.find( "DadosContrato").text.replace('\n', '')
    except:
        indicador = 'None'


    # data_venc_ult_parcela
    try:
        data_venc_ult_parcela = texto.find( "DadosContrato").text.replace('\n', '')

    except:
        data_venc_ult_parcela = 'None'


     # valor_contrato_futuro
    try:
        valor_contrato_futuro = texto.find( "DadosContrato").text.replace('\n', '')

    except:
        valor_contrato_futuro = 'None'


     # qtd_total_parcelas
    try:
        qtd_total_parcelas = texto.find( "DadosContrato").text.replace('\n', '')

    except:
        qtd_total_parcelas = 'None'

        
    
       # qtd_parcelas_aberta
    try:
        qtd_parcelas_aberta = texto.find( "DadosContrato").text.replace('\n', '')

    except:
        qtd_parcelas_aberta = 'None'

        
        
        
      # numero_parcela
    try:
        numero_parcela = texto.find( "ParcelaAnterior").text.replace('\n', '')

    except:
        numero_parcela = 'None'

        
     # data_vencvalor_parcela
    try:
        data_vencvalor_parcela = texto.find( "ParcelaAnterior").text.replace('\n', '')

    except:
        data_vencvalor_parcela = 'None'
        
    
     # data_pagamento
    try:
        data_pagamento = texto.find( "ParcelaAnterior").text.replace('\n', '')

    except:
        data_pagamento = 'None'
        
        
      # valor_pago
    try:
        valor_pago = texto.find( "ParcelaAnterior").text.replace('\n', '')

    except:
        valor_pago = 'None'
        
    
       
      # situacao_parcela
    try:
        situacao_parcela = texto.find( "ParcelaAnterior").text.replace('\n', '')

    except:
        situacao_parcela = 'None'
        
    
     # data_venc_prox_parcela
    try:
        data_venc_prox_parcela = texto.find( "ParcelaFutura").text.replace('\n', '')

    except:
        data_venc_prox_parcela = 'None'
        
    
    
     # valor_prox_parcela
    try:
        valor_prox_parcela = texto.find( "ParcelaFutura").text.replace('\n', '')

    except:
        valor_prox_parcela = 'None'
        
        
     # qtd_parcelas_vencer
    try:
        qtd_parcelas_vencer = texto.find( "ParcelaFutura").text.replace('\n', '')

    except:
        qtd_parcelas_vencer = 'None'

        
   

    
    


    # Gravamos o resultado em nosso dataframe

    xml = tabela.append({

                       'cnpj':cnpj, 
                       'data_envio':data_envio,
                       'nome':nome, 
                       'data_contratacao':data_contratacao,
                       'indicador':indicador,
                       'data_venc_ult_parcela':data_venc_ult_parcela,
                       'valor_contrato_futuro':valor_contrato_futuro,
                       'qtd_total_parcelas':qtd_total_parcelas,
                       'qtd_parcelas_aberta':qtd_parcelas_aberta,
                       'numero_parcela':numero_parcela,
                       'data_vencvalor_parcela':data_vencvalor_parcela,
                       'data_pagamento':data_pagamento,
                       'valor_pago':valor_pago,
                       'situacao_parcela':situacao_parcela,
                       'data_venc_prox_parcela':data_venc_prox_parcela,
                       'valor_prox_parcela':valor_prox_parcela,
                       'qtd_parcelas_vencer':qtd_parcelas_vencer, 
                                          },
                       ignore_index = True)




#Salvando os dados em disco
arquivo.to_csv('arquivo.csv', encoding = "utf-8", index = False)
