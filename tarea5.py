print("Elija una opcion:  servidor1  3servidor")
print("_servidor1")
print("3servidor")
elegir = input()
letra = ''
timer = 0
guion = '_'
def opcion_palabra():
    if int(elegir) == 1:
        return '_servidor1'
    elif int(elegir) == 2:
        return '3servidor'
    else:
        print("Escoge una opcion valida")
        opcion_palabra()

def estado0(palabra,timer):
    if palabra[timer] == '_':
        timer += 1
        estado1(palabra,timer)
    else:
        print("Eror de sintaxis")

def estado1(palabra,timer):
    try:
        n = int(palabra[timer])
        estado3(n,timer)
    except:
        if palabra[timer] == '_':
            timer += 1
            estado1(palabra,timer)
        elif type(palabra[timer]) == str:
            timer += 1
            estado1(palabra,timer)

def estado3(palabra,timer):
    if type(palabra) == int:
        print("La cadena es correcta")
    else:
        print("Incorrecto")


letra = opcion_palabra()
entrada = estado0(letra,timer)
