# TODO-1: Ask the user for input
# TODO-2: Save data into dictionary {name: price}
# TODO-3: Whether if new bids need to be added
# TODO-4: Compare bids in dictionary
price = {}
val = 0

while(val==0):
    name = input("What is your name?: ")

    bid = int(input("What is your bid?: $ "))

    price[name] = bid

    decision= input("Are there any other bidders? Type 'yes' or 'no'. \n")

    if(decision=='yes'):
        print("\n"*20)
        val = 0
    elif(decision=='no'):
        val = 1
        highest = 0
        winner = ""
        for data in price:
            if price[data] > highest:
                highest = price[data]
                winner = data
        print(f"Winner of auction is {winner} with a bid of {highest}")
        break







