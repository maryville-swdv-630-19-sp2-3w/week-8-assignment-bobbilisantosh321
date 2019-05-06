from roles import Role
from roomsData import RoomDao
from reservationData import ReservationDao

class Manager(Role):
    def displayActions(self):
        #Display action relevant for Customers
        print("Select one of the actions from the list below: ")
        print("1. Display Rooms Inventory")
        print("2. Cancel Reservation")

    def performAction(self, scrnInput):
        #Method to executed action selected
        if scrnInput == 1:
            self.getInventoryStatus()
        elif scrnInput == 2:
            self.cancelCustomerReservation()
        else:
            print("Invalid action to execute")
            return

    def getInventoryStatus(self):
        #Method to get Status of all Rooms
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
    
    def cancelCustomerReservation(self):
        #Method to cancel a Reservation
        print("\n\n***********************************************************")
        try:
            customerId = int(input("Provide the customer id: "))
        except:
            print("Customer ID can be only a number")
            return
        try:
            reservations = ReservationDao.getReservationsByCustomerId(customerId)
        except:
            print("No reservations for the given customerId {0} found".format(customerId))
            return
        if reservations == None or reservations == []:
            print("No reservation found for the given customerId {0}".format(customerId))
            return
        count = 1
        for reservation in reservations:
            print("{0}. Reservation ID {1}".format(count, reservation.reservationId))
            count = count + 1
        while True:
            try:
                index = int(input("Select a reservation from above to cancel: "))
                index = index - 1
                reservation = reservations[index]
            except: print("Invalid selection, please try again")
            else: break
        if reservation.status == "CANCEL":
            print("Selected reservation is already cancelled")
        else:
            ReservationDao.updateReservationStatus(reservation.reservationId, "CANCEL")
            print("Reservation Successfully Cancelled")
        print("******************************************************")
        return reservation.reservationId

