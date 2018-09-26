PRICE = {"A": 50,
         "B": 30,
         "C": 20,
         "D": 15,
         "E": 40,
         "F": 10,
         "G": 20,
         "H": 10,
         "I": 35,
         "J": 60,
         "K": 70,
         "L": 90,
         "M": 15,
         "N": 40,
         "O": 10,
         "P": 50,
         "Q": 30,
         "R": 50,
         "S": 20,
         "T": 20,
         "U": 40,
         "V": 50,
         "W": 20,
         "X": 17,
         "Y": 20,
         "Z": 21
         }

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
    """
    Update the balance and the basket for a DISCOUNT item offer
    """
    if item in basket:
        offers_sold = basket[item]//num_items_offer
        num_items_to_retrieve = offers_sold * num_items_offer
        balance += offers_sold * price_offer
        basket[item] -= num_items_to_retrieve

    return basket, balance


def _get_free_item_offer(basket, item, num_items_offer, free_item):
    """
    Update the balance and the basket for a FREE item offer
    """
    if item in basket and free_item in basket:
        if item == free_item:
            offers_sold = basket[item]//(num_items_offer + 1)
        else:
            offers_sold = basket[item]//num_items_offer
        num_items_to_retrieve = max(0, basket[free_item] - offers_sold)
        basket[free_item] = num_items_to_retrieve
    return basket


# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):

    if _is_sku_illegal(skus):
        return -1

    balance = 0
    basket = _get_basket(skus)

    # get OFFER
    basket = _get_free_item_offer(basket, "E", 2, "B")
    basket = _get_free_item_offer(basket, "F", 2, "F")
    basket = _get_free_item_offer(basket, "R", 3, "Q")
    basket = _get_free_item_offer(basket, "U", 3, "U")
    basket = _get_free_item_offer(basket, "N", 3, "M")
    basket, balance = _get_discount_offer(basket, balance, "A", 5, 200)
    basket, balance = _get_discount_offer(basket, balance, "A", 3, 130)
    basket, balance = _get_discount_offer(basket, balance, "B", 2, 45)
    basket, balance = _get_discount_offer(basket, balance, "H", 10, 80)
    basket, balance = _get_discount_offer(basket, balance, "H", 5, 45)
    basket, balance = _get_discount_offer(basket, balance, "K", 2, 150)
    basket, balance = _get_discount_offer(basket, balance, "P", 5, 200)
    basket, balance = _get_discount_offer(basket, balance, "Q", 3, 80)
    basket, balance = _get_discount_offer(basket, balance, "V", 3, 130)
    basket, balance = _get_discount_offer(basket, balance, "V", 2, 90)


    # Sum the regular items
    balance += sum([PRICE[item]*quantity for item,quantity in basket.items()])

    return balance

skus = "VVVVV"
print(checkout(skus))
