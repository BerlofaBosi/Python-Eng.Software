entrada = 1000000

Dias = entrada // 86400
restoDias = entrada % 86400

Horas = restoDias // 3600
restoHoras = restoDias % 3600

Minutos = restoHoras // 60
Segundos = restoHoras % 60

print('Dias: ', Dias)
print('Horas: ', Horas)
print('Minutos: ', Minutos)
print('Segundos: ', Segundos)
