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
    total_checkout = 0

    if _is_sku_illegal(skus):
        return -1




    return total_checkout

skus = "ABCDE"
print(checkout(skus))
