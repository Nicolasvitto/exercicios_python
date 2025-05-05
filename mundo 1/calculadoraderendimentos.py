investir = float(input('Valor a ser investido R$ '))
cdianual = float(input('Digite o CDI anual (em %): ')) / 100  # Converter para decimal

cdimensal = cdianual / 12  # CDI mensal em decimal
rendimento = investir * cdimensal  # Rendimento bruto mensal

print('Valor líquido mensal sem o IR será de R${:.2f} com um rendimento de {:.2f}% ao mês.'.format(rendimento, cdimensal * 100))
