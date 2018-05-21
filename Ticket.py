import datetime
import string
import random
import pyqrcode

class Ticket:
    '''A ticket printed from the terminal at the entrance of the parking garage'''
    def __init__(self):
        '''Initilization method'''
        self.timestamp = self.generate_ticket_timestamp()
        self.ticket_id = self.generate_ticket_id()
        self.qr_barcode = self.create_qr_barcode()
        self.hourly_parking_rate = 1.00

    def generate_ticket_timestamp(self):
        '''A method used to get the timestamp to be printed on the ticket (ie Tuesday, 5/15/2018 12:07:00 PM)'''
        ticket_timestamp = datetime.datetime.now()
        return ticket_timestamp

    def generate_ticket_id(self, size=10, chars=string.ascii_uppercase + string.digits):
        '''A method used to generate a 10 character string of numbers and letters as the ticket ID'''
        ticket_id = ''.join(random.choice(chars) for _ in range(size))
        return ticket_id

    def create_qr_barcode(self):
        '''A method to generate a QR Code, which will be printed out for the driver as they enter the garage and scanned to exit the garage'''
        qr = pyqrcode.create(self.ticket_id)
        qr.png(f"{self.ticket_id}.png", scale=6)
        return pyqrcode.create(self.ticket_id)

    def calculate_time_in_garage(self):
        '''A method to calculate time spent in the garage by taking the current time as of calling this method, less timestamp (set in __init__)'''
        enter_time = self.timestamp
        now = datetime.datetime.now()
        time_spent_in_garage = now.replace(microsecond=0) - enter_time.replace(microsecond=0)
        return time_spent_in_garage


   #def calculate_money_owed_for_parking(self):
   #     '''A method to calculate how much money is due upon exit.
   #     This takes the base rate from self.hourly_parking_rate and multiplies by hours spent in garage, rounded up.
   #     If time spent is greater than 8 hours (max) only charge for 8 hours'''
   #     if self.calculate_time_in_garage() <= datetime.timedelta(hour=1):
   #         return self.hourly_parking_rate
   #     elif self.calculate_time_in_garage() > datetime.timedelta(hours=8):
   #         return self.hourly_parking_rate * 8
   #     else: #need to calculate a rate based on hours - look up rounding timedelta objects..

   #         return #rate based on rounded timdelta



