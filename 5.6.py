def converter(hora, minuto):
    fuso=''
    if hora> 12:
        fuso = 'PM'
        novahora=hora - 12
    else:
        fuso = "AM"
        novahora = hora
    return str(str(novahora)+':'+str(minuto)+fuso)

horainicio = 21
minutoinicio = 45

print(converter(horainicio, minutoinicio))