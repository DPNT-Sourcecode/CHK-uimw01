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


def _is_sku_illegal(skus):
    """
    Check if the sku is illegal...
    """
    for item in skus:
        if item not in PRICE:
            return True
    return False


def _get_basket(skus):
    """
    Count the elements of the skus
    """
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
        num_items_to_remove = offers_sold * num_items_offer
        balance += offers_sold * price_offer
        basket[item] -= num_items_to_remove

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


def _get_group_discount_offer(basket, balance, group_items, num_items_offer, price_offer):
    """
    Update the balance and the basket for a Group discount offer.


    """
    group_items = [item for item in group_items if item in basket]
    offers_sold = sum([basket[item] for item in group_items])//num_items_offer
    sorted_group_item = [item for item in sorted(PRICE, key=PRICE.get,reverse=True) if item in group_items]

    balance += offers_sold * price_offer
    number_of_items_to_remove = offers_sold * num_items_offer

    for item in sorted_group_item:
        number_of_items = basket[item]
        if number_of_items < number_of_items_to_remove:
            basket[item] = 0
            number_of_items_to_remove -= number_of_items
        else:
            basket[item] -= number_of_items_to_remove
            break

    return basket, balance

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):

    if _is_sku_illegal(skus):
        return -1

    balance = 0
    basket = _get_basket(skus)

    # Apply OFFERs
    basket, balance  = _get_group_discount_offer(basket, balance, ['S', 'T', 'X', 'Y', 'Z'], 3, 45)
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
    basket, balance = _get_discount_offer(basket, balance, "K", 2, 120)
    basket, balance = _get_discount_offer(basket, balance, "P", 5, 200)
    basket, balance = _get_discount_offer(basket, balance, "Q", 3, 80)
    basket, balance = _get_discount_offer(basket, balance, "V", 3, 130)
    basket, balance = _get_discount_offer(basket, balance, "V", 2, 90)


    # Sum the regular items
    balance += sum([PRICE[item]*quantity for item,quantity in basket.items()])

    return balance

#### Notes
#
# _get_group_discount_offer method works for a list of items or a single item.
# For performence purpuse I advise you to use _get_discount_offer if you have a single items
#
# It would be possible the factorize all the methods into a single one but I think this is
# easier to read the code this way.
#

def _test():
    """
    I should have done that way before :)

    """
    print("Tests are running")

    assert(checkout("AAA") == 130)
    assert(checkout("RRRQQ") == 180)
    assert(checkout("XXX") == 45)
    assert(checkout("SSSZ") == 65)
    assert(checkout("ZZZS") == 65)
    assert(checkout("ZZZZ") == 66)
    assert(checkout("FFF") == 20)
    assert(checkout("FF") == 20)
    assert(checkout("AAAAAA") == 250)
    assert(checkout("AAAAAAAA") == 330)
    assert(checkout("KK") == 120)
    assert(checkout("KKK") == 190)
    assert(checkout("KKKK") == 240)

_test()
