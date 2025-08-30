def transformar_numero(texto):
    texto = texto.replace("R$", "")
    texto = texto.replace(" ", "")
    texto = texto.replace(".", "")
    texto = texto.replace(",", ".")
    valor = float(texto)
    return valor    
   
def calcular_imposto_mensal(valor_faturamento):
    iss = valor_faturamento * 0.05
    pis = valor_faturamento * 0.0065
    cofins = valor_faturamento * 0.03
    imposto_mensal = iss + pis + cofins
    return imposto_mensal

def calcular_imposto_trimestral(valor_faturamento):
    ir = valor_faturamento * 0.048
    csll = valor_faturamento * 0.0288
    ir_adicional = 0
    if valor_faturamento >= 20000:
        ir_adicional = (valor_faturamento - 20000) * 0.1        
    imposto_trimestral = ir + csll + ir_adicional    
    return imposto_trimestral

def calcular_impostos(dados_faturamento):
    """
    Função principal que calcula os impostos para cada mês do faturamento
    
    Parâmetros:
    dados_faturamento (dict): Dicionário com os valores de faturamento por mês
    
    Retorno:
    dict: Dicionário com os valores de faturamento, imposto mensal e imposto trimestral por mês
    """
    resultado = {}
    
    for mes in dados_faturamento:
        valor_faturamento = transformar_numero(dados_faturamento[mes])
        imposto_mensal = calcular_imposto_mensal(valor_faturamento)
        imposto_trimestral = calcular_imposto_trimestral(valor_faturamento)
        resultado[mes] = (valor_faturamento, imposto_mensal, imposto_trimestral)
    
    return resultado

# Exemplo de uso
if __name__ == "__main__":
    faturamento = {
        'jan': 'R$ 95.141,98',
        'fev': 'R$ 95.425,16',
        'mar': 'R$ 89.716,31',
        'abr': 'R$ 78.459,99',
        'mai': 'R$ 71.087,28',
        'jun': 'R$ 83.911,06',
        'jul': 'R$ 56.467,26',
        'ago': 'R$ 88.513,58',
        'set': 'R$ 66.552,49',
        'out': 'R$ 80.164,07',
        'nov': 'R$ 66.964,33',
        'dez': 'R$ 71.525,25',
    }
    
    resultado = calcular_impostos(faturamento)
    print(resultado)