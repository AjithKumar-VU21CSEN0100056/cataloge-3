class Auction:
    def __init__(self, item_name, starting_bid):
        self.item_name = item_name
        self.starting_bid = starting_bid
        self.current_bid = starting_bid
        self.highest_bidder = None
        self.is_open = True

    def place_bid(self, bidder_name, bid_amount):
        if not self.is_open:
            return "Auction is closed."
        if bid_amount <= self.current_bid:
            return "Bid must be higher than the current bid."
        self.current_bid = bid_amount
        self.highest_bidder = bidder_name
        return f"New highest bid of ${bid_amount} by {bidder_name}."

    def close_auction(self):
        self.is_open = False
        if self.highest_bidder:
            return f"Auction won by {self.highest_bidder} with a bid of ${self.current_bid}."
        else:
            return "No bids were placed."


# Get input from the user to create an auction
item_name = input("Enter the name of the item for auction: ")
starting_bid = float(input("Enter the starting bid amount: "))

auction = Auction(item_name, starting_bid)

while auction.is_open:
    print("\nAuction is open for bidding.")
    bidder_name = input("Enter bidder's name (or type 'close' to end the auction): ")
    
    if bidder_name.lower() == 'close':
        print(auction.close_auction())
        break
    
    bid_amount = float(input(f"Enter the bid amount for {bidder_name}: "))
    print(auction.place_bid(bidder_name, bid_amount))

if not auction.is_open:
    print("\nThe auction has been closed.")
