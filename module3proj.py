restaurant_menu = {
    "Starters": {"Soup": 5.99, "Bruschetta": 6.50},
    "Main Course": {"Steak": 15.99, "Salmon": 13.99},
    "Desserts": {"Cake": 4.99, "Ice Cream": 3.99}
}
new_menu = {"beverages": {"sprite": 1.99, "Coke": 1.89}}
restaurant_menu.update(new_menu)

new_steak = {"Main Course": {"Steak": 17.99, "Salmon": 13.99}}
restaurant_menu.update(new_steak)

removing_Bruschetta = {"Starters": {"Soup": 5.99}}
restaurant_menu.update(removing_Bruschetta)
print(restaurant_menu)

import copy
service_tickets = {
    "Ticket001": {"Customer": "Alice", "Issue": "Login problem", "Status": "open"},
    "Ticket002": {"Customer": "Bob", "Issue": "Payment issue", "Status": "closed"}
    }








def opening_new_service_ticket(ticket_ID, customer_name, issue, status):
    new_ticket = {f"Ticket{ticket_ID}": {f"Customer": {customer_name}, "Issue": {issue}, "Status": {status}}}
    service_tickets.update(new_ticket)
    print(service_tickets)
        
opening_new_service_ticket("003", "John", "none", "closed")






def updating_status_of_ticket(ticket_ID, Status):

#search for the ticket that has the ticket ID for ticket that we want to update in our ticket list
    # ticket_to_update = service_tickets[f"Ticket{ticket_ID}"]

       #once ticket is found, update the status to the status of the user data
    # ticket_to_update["Status"] = Status

    service_tickets[f"Ticket{ticket_ID}"]["Status"] = Status


updating_status_of_ticket("003", "open")


def displaying_tickets():
    for item, particicpant in service_tickets.items():
        print(f"ticket:{item} For - {particicpant}")
        


displaying_tickets()









"""Tracks customer service tickets, each with a unique ID, customer name, issue description, and status (open/closed).
Implement functions to:
Open a new service ticket.
Update the status of an existing ticket.
Display all tickets or filter by status.
Initialize with some sample tickets and include functionality for additional ticket entry."""