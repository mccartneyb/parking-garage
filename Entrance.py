from Ticket import Ticket
import time

list_of_valid_tickets = []
for i in range(3):
    i = Ticket()
    time.sleep(5)
    list_of_valid_tickets.append(i)

for i in list_of_valid_tickets:
    print(i.ticket_id, i.timestamp, i.qr_barcode)
    print(i.calculate_time_in_garage())

