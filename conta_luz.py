numero_quilowatts = float(input('Digite o número de quilowatts consumidos:'))
valor_quilowatts = 0.12
valor_ICMS = 0.18 
valor_energia = numero_quilowatts * valor_quilowatts
valor_ICMS2 = valor_energia * valor_ICMS
valor_total = valor_energia + valor_ICMS2
print('valor a ser pago' , valor_total)

