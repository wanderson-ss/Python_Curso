segundos = input("Informe os segundos que serão convertidos: ")
total_de_segundos = int(segundos)

horas = total_de_segundos // 3600
segundos_rest = total_de_segundos % 3600
minutos = segundos_rest // 60
segundos_rest_final = segundos_rest % 60

print(horas, "horas,", minutos, "minutos e ", segundos_rest_final, "segundos." )


print("Olá")
print()
print("bom dia!")