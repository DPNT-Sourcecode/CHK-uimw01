PRICE = {"A": 50,
         "B": 30,
         "C": 20,
         "D": 15,
         "E": 40}

OFFERS = [("A", 3, 130),
          ("B", 2, 45)]


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


def _get_discount_offer(basket, balance, item, num_items_offer, price_offer):
    if item in basket:
        offers_sold = basket[item]//num_items_offer
        num_items_to_retrieve = offers_sold * num_items_offer
        balance += offers_sold * price_offer
        basket[item] -= num_items_to_retrieve

    return basket, balance


def _get_free_item_offer(basket, item, num_items_offer, free_item):
    if item in basket and free_item in basket:
        offers_sold = basket[item]//num_items_offer
        basket[free_item] -= offers_sold
    return basket


# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):

    if _is_sku_illegal(skus):
        return -1

    balance = 0
    basket = _get_basket(skus)

    # get OFFER
    basket, balance = _get_discount_offer(basket, balance, "A", 5, 200)
    basket, balance = _get_discount_offer(basket, balance, "A", 3, 130)
    basket, balance = _get_discount_offer(basket, balance, "B", 2, 45)
    basket = _get_free_item_offer(basket, "E", 2, "B")

    balance += sum([PRICE[item]*quantity for item,quantity in basket.items()])

    return balance

skus = "EEB"
print(checkout(skus))
