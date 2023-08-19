texto = input("Ingrese un texto: ")
texto = texto.lower()
contador_s = 0
    
for letra in texto:
    if letra == 's':
        contador_s += 1
    continue         
print(f"El carácter 's' aparece {contador_s} veces en el texto.")
