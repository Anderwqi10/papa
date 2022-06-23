
'''Solicitud de datos y variables globales'''
texto = input('Ingrese un texto por favor:\n')
letras = input('Ingrese 3 letras de su preferencia con un espacio entre ellas\n')

'''Parte 1 - Listo''' 
texto_minusculas = texto.lower()
letras_minusculas = letras.lower().split()
'''print(texto_minusculas)
print(letras_minusculas)'''
print(f"""1.- Repeción de letras:
La letra '{letras_minusculas[0].upper()}' se repite {texto_minusculas.count(letras_minusculas[0])} veces.
La letra '{letras_minusculas[1].upper()}' se repite {texto_minusculas.count(letras_minusculas[1])} veces.
La letra '{letras_minusculas[2].upper()}' se repite {texto_minusculas.count(letras_minusculas[2])} veces.\n""")


'''Parte 2 - Listo'''
texto_lista = texto_minusculas.split()
print(f'''2.- Total de palabras:
En total son {len(texto_lista)} palabras en el texto.\n''')


'''Parte 3 - Listo'''
al_reves = texto[::-1]
print(f'''3.- Primera y última letra del texto
La primera letra es "{texto[0].upper()}" y la última letra es "{al_reves[0].upper()}" .\n''')


'''Parte 4 - Listo'''
texto_al_reves = " ".join(texto_lista[::-1])
print(f'''4.- Palabras en orden inverso:
{texto_al_reves[0].upper()+texto_al_reves[1::]}.\n''')


'''Parte 5'''
esta = {
    'True': 'La palabra Python sí se encuentra en su texto',
    'False': 'La palabra Python no se encuentra en su texto'
}

booleano = str('python' in texto_minusculas)

print(f'''5.- ¿Aparece python?
{esta[booleano]}''')
