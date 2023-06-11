dias = int(input())

anos = dias // 365 
dias = dias - 365 * anos
meses = dias // 30
dias = dias - 30 * meses

print(str(anos) + ' ano (s)')
print(str(meses) + ' mes (es)')
print(str(dias) + ' dia (s)')
