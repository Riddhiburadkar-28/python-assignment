# Take input from user
prices = tuple(map(float, input("Enter prices separated by space: ").split()))

# a) Total number of items sold
print("Total items sold:", len(prices))

if len(prices) > 0:
    # b) Cheapest item
    print("Cheapest item price:", min(prices))

    # c) Costliest item
    max_price = max(prices)
    print("Costliest item price:", max_price)

    # d) Prices in ascending order
    print("Prices in ascending order:", tuple(sorted(prices)))

    # e) Number of costliest items sold
    print("Number of costliest items sold:", prices.count(max_price))
else:
    print("No items sold")