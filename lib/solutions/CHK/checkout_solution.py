PRICE = {"A":50,
        "B":30,
        "C":20,
        "D":15}


def _is_sku_illegal(skus):
    for item in skus:
        if item not in PRICE:
            return True
    return False

def _get_basket(skus):
    basket = {}
    for item in skus:
        if item not in basket:
            basket[item] = 0
        basket[item] += 1
    return basket
# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):

    if _is_sku_illegal(skus):
        return -1

    total_checkout = 0
    basket = _get_basket(skus)


    total_checkout = sum([PRICE[item]*quantity for item,quantity in basket.items()])


    print(basket)


    #total_checkout = sum([for item in ])


    return total_checkout

skus = "ABBBCD"
print(checkout(skus))
