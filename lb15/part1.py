import pandas as pd
import matplotlib.pyplot as plt

shop_dict = {
    "shop1": ["Milk", "Apples", "Bananas","Milk"],
    "shop2": ["Cheese", "Milk", "Tomatoes"],
    "shop3": ["Bananas", "Apples", "Cheese","Tomatoes","Bananas"],
    "shop4": ["Tomatoes", "Bananas", "Milk","Cheese"],
    "shop5": ["Apples", "Cheese", "Tomatoes"]
}

data = []
for shop, products in shop_dict.items():
    for product in products:
        data.append([shop,product])
df = pd.DataFrame(data, columns=["shop", "product"])
print(f"{df}\n\n")
aggregation = (df.groupby("shop")["product"].agg([("count","count"),("unique","unique")])).reset_index()
print(aggregation)
plt.bar(aggregation['shop'], aggregation['count'], color='purple')
plt.xlabel('Shops')
plt.ylabel('Number of Products')
plt.title('Number of Products by Shop')
plt.savefig("plt2.png", dpi=300)