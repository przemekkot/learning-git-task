shopping_list = {
  "piekarnia": ["chleb", "pączek", "bułki"],
  "warzywniak": ["marchew", "seler", "rukola"]
}

# print(shopping_list)

n = 0

for shop in shopping_list:
    for i in range(len(shopping_list[shop])):
        shopping_list[shop][i]=shopping_list[shop][i].capitalize()
    print(f"Idę do {shop.capitalize()} i kupuję tam {shopping_list[shop]}")
    items=len(shopping_list[shop])
    n = n + len(shopping_list[shop])
    
print(f"W sumie kupuję {n} produktów.")

print(' ')

shop = list(shopping_list.keys())

print(f"Moje sklepy do wyboru to: {shop[0].capitalize()} i {shop[1].capitalize()}.")

print(' ')

products = list(shopping_list.values())

print(f"Brakuje mi pieczywa w domu, więc idę do {shop[0].capitalize()} żeby kupić {products[0][0]} lub {products[0][2]}.")

print(' ')

print("Greetings for my Mentor - Artur :)"
