PRICE = {"A":50,
        "B":30,
        "C":20,
        "D":15}


def _is_sku_illegal(skus):
    for item in skus:
        if item not in PRICE:
            return True
    return False


# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):

    if _is_sku_illegal(skus):
        return -1

    total_checkout = 0
    basket = {}

    for item in skus:
        if item not in basket:
            basket[item] = 1
        else:
            basket[item] += 1

    print(basket)


    #total_checkout = sum([for item in ])


    return total_checkout

skus = "ABBBCD"
print(checkout(skus))
