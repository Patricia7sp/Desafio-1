#Criando um novo arquivo xml usando como base o exemplo de reporte de parcelados 
#!/usr/bin/python
#  encoding: utf-8
#   
from xml.dom.minidom import Document

doc = Document()

#<EnvioHistoricoCredito>
root = doc.createElement('EnvioHistoricoCredito')
contrato = doc.createElement('cliente') 
contrato_1 = doc.createElement('Operacao')
contrato_2 = doc.createElement('DetalheOperacao')
cnpj = doc.createElement('CNPJ')
dataRemessa = doc.createElement('DataRemessa')
nome = doc.createElement('Identificacao')
dataContratacao = doc.createElement('DadosContrato')
indicador = doc.createElement('DadosContrato')
UltimaParcela = doc.createElement('DadosContrato')
valorContrato = doc.createElement('DadosContrato')
TotalParcelas = doc.createElement('DadosContrato')
ParcelasAbertas = doc.createElement('DadosContrato')
Parcela = doc.createElement('ParcelaAnterior')
vencimento = doc.createElement('ParcelaAnterior')
ValorParcela = doc.createElement('ParcelaAnterior')
pagamento = doc.createElement('ParcelaAnterior')
valorPago = doc.createElement('ParcelaAnterior')
situacaoParcela = doc.createElement('ParcelaAnterior')
proximaParcela = doc.createElement('ParcelaFutura')
valorProximaParcela = doc.createElement('ParcelaFutura')
parcelasVencer=doc.createElement('ParcelaFutura')


#passando informações das minhas tags
root.setAttribute('nome','histórico do cadastro positivo')
cnpj.setAttribute('numero','12345678901234')
dataRemessa.setAttribute('data_envio','30/01/2019')
nome.setAttribute('nome','Maria da Silva')
dataContratacao.setAttribute('data_contratacao','10/01/2019')
indicador.setAttribute('indicador','pré-fixado')
UltimaParcela.setAttribute('data_venc_ult_parcela','10/02/2021')
valorContrato.setAttribute('valor_contrato_futuro','R$ 30.000,00')
TotalParcelas.setAttribute('qtd_total_parcelas','25')
ParcelasAbertas.setAttribute('qtd_parcelas_aberta','24')
Parcela.setAttribute('numero_parcela','01')
ValorParcela.setAttribute('valor_parcela','R$ 1.200,00')
vencimento.setAttribute('data_vencimento','10/02/2019')
pagamento.setAttribute('data_pagamento','09/02/2019')
valorPago.setAttribute('valor_pago','R$ 1.200,00')
situacaoParcela.setAttribute('situacao_parcela','total')
proximaParcela.setAttribute('data_venc_prox_parcela','10/03/2019')
valorProximaParcela.setAttribute('valor_prox_parcela','R$ 1.200,00')
parcelasVencer.setAttribute('qtd_parcelas_vencer','24')




doc.appendChild(root) # ponto de partida 
root.appendChild(contrato)
root.appendChild(contrato_1)
root.appendChild(contrato_2)
contrato.appendChild(contrato_1)
contrato_1.appendChild(contrato_2)
contrato.appendChild(cnpj)
contrato.appendChild(dataRemessa)
contrato.appendChild(nome)
contrato_1.appendChild(dataContratacao)
contrato_2.appendChild(indicador)
contrato_1.appendChild(UltimaParcela)
contrato_2.appendChild(valorContrato)
contrato_2.appendChild(TotalParcelas)
contrato_1.appendChild(ParcelasAbertas)
contrato_1.appendChild(Parcela)
contrato_1.appendChild(vencimento)
contrato_1.appendChild(ValorParcela)
contrato_1.appendChild(pagamento)
contrato_1.appendChild(valorPago)
contrato_1.appendChild(situacaoParcela)
contrato_1.appendChild(proximaParcela)
contrato_1.appendChild(valorProximaParcela)
contrato_1.appendChild(parcelasVencer)





doc.writexml(open("arquivo_xml.xml", "w"),
                    addindent='   ', #colocando espaçamento
                    newl= '\n' ) #colocando quebra de linha e identar 

#remover sujeira do arquivo
doc.unlink()
