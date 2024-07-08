
frase = input("Digite uma String: ").strip()
frase_sem_esp = frase.replace(" ","").replace("-","").replace("?","").replace(".","").lower()
print("-="*30)
if frase_sem_esp == frase_sem_esp[::-1]:
    print(f"A String {frase} É UM PALÍNDROMO!! ")
else:
    print(f"A String {frase} É UM PALÍNDROMO!! ")



