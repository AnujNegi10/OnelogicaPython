
again = False
auction = {}
maxbidder = ""
while(not again):
    maxvalue = 0
    name = input("enter your name ")
    bid = int(input("enter the bid you want to make :$"))

    auction[name] = bid 

    bidmore = input("Anymore bidders : type yes or no ")

    if bidmore=="yes":
        again = False
    elif bidmore=="no":
        for keys in auction:
            if auction[keys]>maxvalue:
                maxvalue = auction[keys]
                maxbidder = keys
        print(f"the max bid is ${maxvalue} by the bidder {maxbidder}")
        break

    # using built in function to get the key which has the max value

    # ! maxi = max(auction , key=auction.get)

    # same way we can get max values
    # ! auction[maxi] => max value

    else:
        print("invalid")
        


    



