print("lista zakupów")


lista_zakupow = {
    "piekarnia": ["chleb", "bułki", "pączek"],
    "warzywniak": ["marchew","seler","rukola"]
}

#print(lista_zakupow.keys())
sump = 0

for k, v in lista_zakupow.items():
   print(f"Idę do {k.capitalize()}, kupuję tu następujące rzeczy: ", end ="")
   sump += len(v)
   for i in range (len(v)):
        if i != len(v)-1:
            print(f" {lista_zakupow[k][i].capitalize()}" , end = ",") 
        else:
            print(f" {lista_zakupow[k][i].capitalize()}")     
print(f"W sumie kupuję {sump} produktów")

print("Pozdrowienia dla Patryka 19:29 2023-01-02")

