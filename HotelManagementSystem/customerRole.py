from roles import Role
from customerData import CustomerDao
from reservationRole import Reservation
from reservationData import ReservationDao
from billsData import BillDao
from billRole import Bill
import datetime

class Customer(Role):


    def __init__(self, id):
        #Get the customer details from database(CustomerData class). If not valid id throw exception
        #fill customer object with details
        customerDao = CustomerDao.getCustomerById(id)
        if customerDao is None:
            raise Exception("Invalid customer id")
        self.customerId = customerDao.cusId
        self.customerName = customerDao.name
        self.customerEmail = customerDao.email

    def displayActions(self):
        #Display action relevant for Customers
        print("Select one of the actions in the below list: ")
        print("1. Get my reservation details")
        print("2. Cancel my reservation")
        print("3. Pay the bill before check in")
        print("4. Check in to a room")
        print("5. Check out a room")

    def performAction(self, input):
        #Method to executed action selected
        if input == 1:
            self.getCustomerReservation()
        elif input == 2:
            self.cancelCustomerReservation()
        elif input == 3:
            self.payForReservation()
        elif input == 4:
            self.checkinRoom()
        elif input == 5:
            self.checkoutRoom()
        else:
            print("Invalid action to execute")
            return

    def getCustomerReservation(self):
        #Method to get all Reservation Details of the Customer
        try:
            reservations = ReservationDao.getReservationsByCustomerId(self.customerId)
        except:
            print("No reservation found for the given customerId {0}".format(self.customerId))
            return
        if reservations == None or reservations == []:
            print("No reservation found for the given customerId {0}".format(self.customerId))
            return
            
        customerName = CustomerDao.getCustomerById(self.customerId).name
        print("Reservation of Customer Id {0} is".format(self.customerId))
        print("Customer name is {0}".format(customerName))
        for reservation in reservations:
            print("**** Reservation ID is {0}".format(reservation.reservationId))
            print("Room Number is {0}".format(reservation.roomId))
            print("Start time is {0}".format(reservation.fromDate))
            print("End time is {0}".format(reservation.toDate))
            print("Amount for reservation is {0} USD".format(Bill(reservation.billId).amount))
            print("Payment status is {0}".format(Bill(reservation.billId).amount))
            print("Reservation status is {0}".format(reservation.status))
            print("***************************************************************")
        print("***************************************************************\n\n")

    def cancelCustomerReservation(self):
        #Method to Cancel a Reservation of Customer
        print("******************************************************")
        try:
            reservations = ReservationDao.getReservationsByCustomerId(self.customerId)
        except:
            print("No reservation found for the given customerId {0}".format(self.customerId))
            return
        if reservations == None or reservations == []:
            print("No reservation found for the given customerId {0}".format(self.customerId))
            return
        count = 1
        for reservation in reservations:
            print("{0}. Reservation ID {1}".format(count, reservation.reservationId))
            count =+ 1
        while True:
            index = input("Select a reservation from above to cancel: ")
            index =- 1
            try: reservation = reservations[index]
            except: print("Invalid selection, please try again")
            else: break
        startTimeObj = datetime.datetime.strptime(reservation.fromDate, '%Y-%m-%d')
        endTimeObj = datetime.datetime.strptime(reservation.toDate, '%Y-%m-%d')
        """if datetime.datetime.now() > (startTimeObj):
            raise Exception("The cancellation is past the check in date {0}".format(startTimeObj))"""
        if reservation.status == "CANCEL":
            print("Selected reservation is already cancelled")
        else:
            ReservationDao.updateReservationStatus(reservation.reservationId, "CANCEL")
            print("Reservation Successfully Cancelled")
        print("******************************************************")
        return reservation.reservationId

    def payForReservation(self):
        #Method to make a payment for Reservation
        print("*********************************************************")
        try:
            reservations = ReservationDao.getReservationsByCustomerId(self.customerId)
        except:
            print("No reservation found for the given customerId {0}".format(self.customerId))
            return
        if reservations == None or reservations == []:
            print("No reservation found for the given customerId {0}".format(self.customerId))
            return
        count = 1
        for reservation in reservations:
            print("{0}. Reservation ID {1}".format(count, reservation.reservationId))
            count =+ 1
        while True:
            index = input("Select a reservation from above(Press Enter for default selection of 1): ")
            index =- 1
            try: reservation = reservations[index]
            except: print("Invalid selection, please try again")
            else: break
        print("Pay for reservation {0}".format(reservation.reservationId))
        bill = Bill(reservation.billId)
        if bill.status == "PAID":
            print("Bill already paid for reservation")
            return
        print("The amount to be paid is {0} USD".format(Bill(reservation.billId).amount))
        cardNum = input("Enter payment card number ")
        BillDao.updatePaymentDetails(reservation.billId, cardNum)
        ReservationDao.updateReservationStatus(reservation.reservationId, "RESERVED")
        print("Payment is successful for amount {0} USD".format(Bill(reservation.billId).amount))
        print("*********************************************************")


    def checkinRoom(self):
        #Method to check in a Reservation by Customer
        print("*********************************************************")
        try:
            reservations = ReservationDao.getReservationsByCustomerId(self.customerId)
        except:
            print("No reservation found for the given customerId {0}".format(self.customerId))
            return
        if reservations == None or reservations == []:
            print("No reservation found for the given customerId {0}".format(self.customerId))
            return
        count = 1
        for reservation in reservations:
            print("{0}. Reservation ID {1}".format(count, reservation.reservationId))
            count =+ 1
        while True:
            index = input("Select a reservation from above(Press Enter for default selection of 1): ")
            index =- 1
            try: reservation = reservations[index]
            except: print("Invalid selection, please try again")
            else: break
        if reservation.status == "CHECK-IN":
            print("Room is already checked in")
            return
        elif reservation.status != "RESERVED":
            print("Room is not valid for check in as its status is {0}".format(reservation.status))
            return
        elif datetime.datetime.strptime(reservation.fromDate, '%Y-%m-%d').date() < datetime.datetime.now().date():
            print("Room is not valid for check in as the start date {0} is not still reached".format(reservation.fromDate))
            return
        ReservationDao.updateReservationStatus(reservation.reservationId, "CHECK-IN")
        return

    def checkoutRoom(self):
        #Method to check out a Reservation by Customer
        print("*********************************************************")
        try:
            reservations = ReservationDao.getReservationsByCustomerId(self.customerId)
        except:
            print("No reservation found for the given customerId {0}".format(self.customerId))
            return
        if reservations == None or reservations == []:
            print("No reservation found for the given customerId {0}".format(self.customerId))
            return
        count = 1
        for reservation in reservations:
            print("{0}. Reservation ID {1}".format(count, reservation.reservationId))
            count =+ 1
        while True:
            index = input("Select a reservation from above(Press Enter for default selection of 1): ")
            index =- 1
            try: reservation = reservations[index]
            except: print("Invalid selection, please try again")
            else: break
        if reservation.status != "CHECK-IN":
            print("Room is not valid for check out as its status is {0}".format(reservation.status))
            return
        elif datetime.datetime.strptime(reservation.fromDate, '%Y-%m-%d') > datetime.datetime.now():
            print("Room is not valid for check out as the end date {0} is not still reached".format(reservation.toDate))
            return
        ReservationDao.updateReservationStatus(reservation.reservationId, "CHECK-OUT")
        return

    @staticmethod
    def createNewCustomer():
        #Method create a new Customer
        print("\n\n*****************************************************************")
        while True:
            try:customerId = int(input("Enter the customer id: "))
            except: print("Invalid Value for Customer ID, please try again")
            else: break
        customerName = input("Enter the customer name: ")
        customerEmail = input("Enter the customer email: ")
        try:
            CustomerDao.addCustomer(customerId, customerName, customerEmail)
            print("New Customer {0}, {1} with email address {2} is created".format(customerId, customerName, customerEmail))
            return customerId
        except:
            print("Customer already existing with given id {0}".format(customerId))
            return 
        print("Customer with id {0} is successfully created".format(customerId))
        print("Customer name : {0}".format(customerName))
        print("Customer email : {0}".format(customerEmail))
        print("**********************************************************************\n\n")

    @staticmethod
    def updateCustomerDetails(customer):
        #Method create a update a Customer information
        print("\n\n*******************************************************************")
        print("Update details of customer id {0} ".format(customer.customerId))
        customerName = input("Enter the new customer name ({0}): ".format(customer.customerName))
        customerEmail = input("Enter the new customer email: ({0}) ".format(customer.customerEmail))
        CustomerDao.updateCustomer(customer.customerId, customerName, customerEmail)
        print("Customer updated successfully")
        print("**********************************************************************\n\n")
        return customer.customerId


