def make_pizza(size, *toppings):
    print(f'\nMaking a {size}-inch with toppings')
    for topping in toppings:
        print(f'- {topping}')