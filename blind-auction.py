#blind auction program

#importing the logo and clear funcion from the art module
from art import logo,clear 
print('\nWelcome to the Py Blind Auction.')
print(logo) #display the logo

blind_auction = {} #empty dict to store the name as key and bid as value
largest_bid = 0 #setting the largest bid to zero
highest_bidder = '' #empty string to store the hightest bidder
continue_bidding = True #to continue bidding

#while loop to continue the bidding 
while continue_bidding:
    #first we need to get the user's name and bid
    #then store it in a dictionary
    name = input('What is your name? ') #get the users name
    bid = int(input('what is your bid? $')) #get the user bid

    new_blind_auction = {name:bid} #a dict to store the name and bid
    #add the new blind auction dict to the empty dict outside the while loop
    blind_auction.update(new_blind_auction)
    #then we ask if the are other bidders 
    other_bidders = input('Are there any other bidders? ').lower()
    #if yes then we clear the terminal
    if other_bidders == 'yes':
        clear()
    
    #if no then we find the highest bidder and end the bidding.
    elif other_bidders == 'no':
        #looping through the keys in the blind auction dictionary
        for name in blind_auction:
            bids = blind_auction[name] #getting the values which are the bids
            #check the bids to get the highest one
            if bids > largest_bid:
                largest_bid = bids #set the largest bid to the bids
                highest_bidder = name #set the highest bidder to name

        #display the highest bidder and their bid
        print(f'{highest_bidder} got the highest bid with ${largest_bid}')

        continue_bidding = False #end the blind auction program
