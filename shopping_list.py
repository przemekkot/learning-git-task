shopping_list = {
  "piekarnia": ["chleb", "pączek", "bułki"],
  "warzywniak": ["marchew", "seler", "rukola"]
}

print(shopping_list)

for shop in shopping_list:
    for i in range(len(shopping_list[shop])):
        shopping_list[shop][i]=shopping_list[shop][i].capitalize()
    print(f"Idę do {shop.capitalize()} i kupuję tam {shopping_list[shop]}")
    items=len(shopping_list[shop])