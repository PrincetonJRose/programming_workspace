# Written by Princeton Rose on 9/30/2018
import sys
import math

SERVICE_CHARGE = 2
TICKET_PRICE = 10

tickets_remaining = 100  

# Function to calculate the price
def calculate_price(number_of_tickets):
	if number_of_tickets == 0:
		return 0
	else:
		return (number_of_tickets * TICKET_PRICE) + SERVICE_CHARGE

# Run code continuously until tickets run out
while tickets_remaining > 0:

	# Print remaining ticket count
	print("\nThere are {} tickets remianing.\nTickets cost ${} each with an additionl one-time processing fee of ${}.\n".format(tickets_remaining,TICKET_PRICE, SERVICE_CHARGE))
	
	# Get user's name
	name = input("Please enter your name:  ")
	
	# Display user name and ask how many tickets they would like to purchase
	print("\nHello {}!  ".format(name))
	
	# While loop to make sure the user enters a valid number
	purchase = None
	def how_many(purchase):
		while True:
			try:
				purchase = int(input("How many tickets would you like to purchase?\n(Or enter 0 to cancel): "))
			except ValueError:
				print("Please enter a valid number.")
				continue
			if purchase > tickets_remaining:
				print("\nSorry, there is not enough tickets for you to purchase that many.\nThere are currently {} tickets left.".format(tickets_remaining))
				continue
			elif purchase == 0:
				break
			elif purchase < 0:
				print("Please enter a valid number.")
				continue
			else:
				return purchase
				break
		return purchase
	
	num_tickets = how_many(purchase)

	# Display how many tickets they want to purchase along with the total cost
	amount_due = calculate_price(num_tickets)
	print("For {} tickets, the total will be ${}.".format(num_tickets, amount_due))
	
	# Prompting the user if they want to continue
	confirm = None
	def want_to_buy(confirm, num_tickets1 = num_tickets):
		while True:
			confirm1 = input("Are you sure? (Y=Yes  N=No): ")
			if confirm1.lower() == 'n' or confirm1.lower() == 'no':
				confirm = 0
				num_tickets1 = how_many(purchase)
				if num_tickets1 != num_tickets:
					amount_due = calculate_price(num_tickets1)
					print("Current tickets {} and total ${}.".format(num_tickets1, amount_due))
				continue
			elif confirm1.lower() == 'y' or confirm1.lower() == 'yes':
				confirm = 1
				return confirm, num_tickets1
				break
			else:
				print("Please enter the correct response.")
				continue
	
	# Get confirmation that they want to proceed
	# I used a tuple here, and it worked!  ^_^
	confirmation, num_tickets = want_to_buy(confirm)
	
	if confirmation == 1 and num_tickets != 0:
		# Print "Sold!" to confirm purchase
		print("Sold! We look forward to seeing you at the show!  ^_^")
		# then subtract the tickets purchased from the tickets_remaining
		tickets_remaining -= num_tickets
		
	# Otherwise...
	if num_tickets == 0:
		# Thank them by name
		print("No charges have been made. Thank you {}.\n".format(name))

# Notify users when tickets are sold out
print("Sorry, tickets are all sold out.  =(")