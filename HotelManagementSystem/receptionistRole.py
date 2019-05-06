from roles import Role
from customerRole import Customer
from roomsData import RoomDao
from billsData import BillDao
from reservationRole import Reservation
from reservationData import ReservationDao
import datetime
from billRole import Bill
from customerData import CustomerDao

roomPrices = {"QUEEN": 200, "KING": 300, "SINGLE": 150}

class Receptionist(Role):

    def __init__(self):
        #Get the receptionist details from employee database. If not valid id throw exception
        #fill receptionist object with details
        self.receptionistId = "R001"
        self.receptionistName = "Rita"

    def displayActions(self):
        #Display action relevant for Receotionist
        print("Select one of the actions in the below list: ")
        print("1. List Available Rooms")
        print("2. Create a Reservation")
        print("3. Get status of Reservation for Customer")
        print("4. Get bill due for Customer")
        print("5. List all Customers")
        print("6. List all rooms")
        print("7. Create a New Customer")
        print("8. Update Customer Details ")

    def performAction(self, scrnInput):
        #Method to executed action selected
        if scrnInput == 1:
            self.listAvailableRooms()
        elif scrnInput == 2:
            self.createReservation()
        elif scrnInput == 3:
            self.getReservationDetails()
        elif scrnInput == 4:
            self.getCustomerDueDetails()
        elif scrnInput == 5:
            self.getAllCustomersDetails()
        elif scrnInput == 6:
            self.getAllRoomsDetails()
        elif scrnInput == 7:
             customerId = Customer.createNewCustomer()
        elif scrnInput == 8:
            personId = int(input("Enter the customerId: "))
            try:
                person = Customer(personId)
                Customer.updateCustomerDetails(person)
            except:
                print("Invalid Customer ID")            
        else:
            print("Invalid action to execute")
            return

    def listAvailableRooms(self):
        #Method to Display all the Rooms with Available status
        roomsMap = RoomDao.listAvailableRooms()

        print("\n\n********************************************************")
        print("Room Type         :        Number of Available Rooms\n")
        for room in roomsMap:
            print("{0}              :               {1}\n".format(room[0], room[1]))
        print("********************************************************\n\n")

    def createReservation(self):
        #Method to create a Reservation
        print("\n \n")
        print("***************************************************************")
        print("START A RESERVATION")
        
        while True:
            customerId = input("Provide the customer id for creating reservation: ")
            try: customer = Customer(customerId)
            except Exception as error:
                print(error, ", please try again")
            else:
                break
            
        print("Select the room type for reservation from below")
        while True:
            print("Queen \nKing \nSingle \nExit")
            roomType = input("Provide Room Type : ")
            if roomType.upper() == "EXIT":
                return
            elif not RoomDao.isRoomAvailable(roomType.upper()):
                print("Room not available of given room type")
            else:
                break
        startTimeObj = datetime.datetime.now().date()
        while True:
            while True:
                endTimeStr = input("Enter the end time of reservation (YYYY-MM-DD): ")
                try: endTimeObj = datetime.datetime.strptime(endTimeStr, '%Y-%m-%d').date()
                except:
                    print("Invalid date, please try again")
                else:
                    break
            try: amount = self.generateAmountForReservation(startTimeObj, endTimeObj, roomType.upper())
            except Exception as error:
                print(error)
            else:
                break
        roomId = RoomDao.bookRoom(roomType.upper())
        billId = BillDao.createBill(roomId, customerId, amount)
        reservationId = ReservationDao.createReservation(customerId, billId, roomId, startTimeObj, endTimeObj)
        bill = Bill(billId)

        print("---------------------------------------------------------------")
        print("Reservation is successful")
        print("Customer name is {0}".format(customer.customerName))
        print("")
        print("Room Type is {0} with reservation ID {1}".format(roomType, reservationId))
        print("Start time is {0}".format(startTimeObj))
        print("End time is {0}".format(endTimeObj))
        print("Amount for reservation is {0}".format(amount))
        print("Bill status of the reservation is {0}".format(bill.status))
        print("---------------------------------------------------------------")
        print("***************************************************************")
        return reservationId

    def generateAmountForReservation(self, startTimeObj, endTimeObj, roomType):
        #Method to  Calculate Amount for Reservation
        if endTimeObj < datetime.datetime.now().date():
            raise Exception("Invalid end date for reservation. Please enter future date")
        days = endTimeObj - startTimeObj
        return days.days * roomPrices[roomType.upper()]

    def getReservationDetails(self):
        #Method to get list of reservations by a Customer
        print("\n\n***********************************************************")
        customerId = input("Provide the customer id to get the reservation details: ")
        try:
            reservations = ReservationDao.getReservationsByCustomerId(customerId)
        except:
            print("No reservation found for the given customerId {0}".format(customerId))
            return
        if reservations == None or reservations == []:
            print("No reservation found for the given customerId {0}".format(self.customerId))
            return
        customerName = CustomerDao.getCustomerById(customerId).name
        print("Reservation of Customer Id {0} is".format(customerId))
        print("Customer name is {0}".format(customerName))
        for reservation in reservations:
            print("**** Reservation ID is {0}".format(reservation.reservationId))
            print("Room Number is {0}".format(reservation.roomId))
            print("Start time is {0}".format(reservation.fromDate))
            print("End time is {0}".format(reservation.toDate))
            print("Amount for reservation is {0} USD".format(Bill(reservation.billId).amount))
            print("Reservation status is {0}".format(reservation.status))
            print("Billing status of reservation is {0}".format(Bill(reservation.billId).status))
            print("***************************************************************")
        print("***************************************************************\n\n")
    
    def getCustomerDueDetails(self):
        #Method to get Payment due by Customer
        print("\n\n***********************************************************")
        customerId = input("Provide the customer id to get the Payment Due: ")
        try:
            reservations = ReservationDao.getReservationsByCustomerId(customerId)
        except:
            print("No reservation found for the given customerId {0}".format(customerId))
            return
        if reservations is None or reservations == []:
            print("No reservation found for the given customerId {0}".format(customerId))
            return
        dueAmount = 0
        for reservation in reservations:
            bill = Bill(reservation.billId)
            if bill.status != "PAID":
                dueAmount += int(bill.amount)
                print("Reservation ID {0}, Amount {1}".format(reservation.reservationId, bill.amount))
                
        if dueAmount == 0:
            print("Customer ID {0} currently have no payments due".format(customerId))
        else:
            print("Customer ID {0} currently have payments due of {1}".format(customerId, dueAmount))
        print("***************************************************************\n\n")
    
    def getAllCustomersDetails(self):
        #Method to get all Customer in the System
        print("\n\n***********************************************************")
        try:
            customers = CustomerDao.getAllCustomer()
        except:
            print("No Customers in the System")
            return
        if customers == None or customers == []:
            print("No Customers in the System")
            return
        
        for customer in customers:
            print("Customer ID {0} name {1} Email address {2}".format(customer.cusId, customer.name, customer.email))
        print("***************************************************************\n\n")

    def getAllRoomsDetails(self):
        #Method to get all rooms in the system with their status
        print("\n\n***********************************************************")
        try:
            rooms = RoomDao.getAllRooms()
        except:
            print("No Rooms in the System")
            return
        if rooms == None or rooms == []:
            print("No Rooms in the System")
            return

        for room in rooms:
            print("Room ID {0} Type {1} price {2} with Status {3}".format(room.roomId, room.type, room.price, room.status))
        print("***************************************************************\n\n")
        

        
        

