seg = int(input('Por favor, entre com o número de segundos que deseja converter: '))
dia = seg // 86400
s_resto = seg % 86400
hora = s_resto // 3600
s_resto = s_resto % 3600
minutos = s_resto // 60
seg = s_resto % 60

print(f'{dia} dias, {hora} horas, {minutos} minutos e {seg} segundos.')