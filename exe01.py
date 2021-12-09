USERNAME = "Jake"
CREDITS = 2.2
ITENS_IN_CART = ["Jeans", "Shoes", "Socks"]


def get_first_name(user, credits, items):
    return f"fist item: {items[0]} user: {user} credits left: {credits}"


print(get_first_name(USERNAME, CREDITS, ITENS_IN_CART))
