# Calculate the cost of items in a shopping cart
# cart = [
#       {"name":"Apple","price":0.5,"quantity":4},
#       {"name":"Banana","price":0.3,"quantity":6},
#       {"name":"Orange","price":0.7,"quantity":3}
#        ]
def shopping_cart(cart):
    #price_per_item = []
    price_per_item = [item['price'] * item['quantity'] for item in cart]
    # for item in cart:
    #     price_per_item.append(item['price'] * item['quantity'])
    return sum(price_per_item)

cart = [
       {"name":"Apple","price":0.5,"quantity":4},
       {"name":"Banana","price":0.3,"quantity":6},
       {"name":"Orange","price":0.7,"quantity":3}
        ]
print(shopping_cart(cart))