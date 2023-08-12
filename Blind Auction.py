import os

logo = '''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''

print(logo)
print("Welcome to the blind auction.")

end_of_loop = False
bidding = {}

while end_of_loop == False:
  name = input('What is your name?\n')
  bid_amount = int(input('What is your bid?\n$'))
  bidding[name] = bid_amount
  keep_going = input("Are there any other bidders? Type 'yes' or 'no'").lower()
  os.system('clear')
  if keep_going == 'no':
    end_of_loop = True

highest_bidder = ''
highest_bid = 0

for key in bidding:
  if bidding[key] > highest_bid:
    highest_bidder = key
    highest_bid = bidding[key]

print(f"The winner is {highest_bidder} with a bid of ${highest_bid}.")