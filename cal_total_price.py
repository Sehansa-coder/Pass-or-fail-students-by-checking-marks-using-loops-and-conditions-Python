
def calculate_total_price(prices,tax):
    total_price=0

    for price in prices:
        def tax_value(tax):
            nonlocal total_price
            total_price+=price+price*tax
        tax_value(0.5)
        
    return total_price
prices=[100,200,300,400]
calculate_total_price(prices,0.5)
answer=calculate_total_price(prices,0.5)
print("Total price is:", answer)