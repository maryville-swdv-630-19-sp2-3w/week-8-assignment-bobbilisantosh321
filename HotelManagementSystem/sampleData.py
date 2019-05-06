from customerData import CustomerDao
from reservationData import ReservationDao
from roomsData import RoomDao
from billsData import BillDao

#Class to create Test Data for the Application
class SampleData:

    @staticmethod
    def createCustomerData():
        #Mthod to create Customers details in the system
        CustomerDao.addCustomer(2, 'John', 'john@gmailcom')
        CustomerDao.addCustomer(3, 'Will', 'Will@gmailcom')
        CustomerDao.addCustomer(4, 'Good', 'Good@gmailcom')
        CustomerDao.addCustomer(5, 'James', 'James@gmailcom')
        CustomerDao.addCustomer(6, 'Jerry', 'Jerry@gmailcom')
        CustomerDao.addCustomer(7, 'Tom', 'jTomohn@gmailcom')
        CustomerDao.addCustomer(18, 'Smith', 'Smith@gmailcom')
        CustomerDao.addCustomer(19, 'Dwayne', 'Dwayne@gmailcom')
        CustomerDao.addCustomer(10, 'Samantha', 'Samantha@gmailcom')
        CustomerDao.addCustomer(11, 'Barry', 'Barry@gmailcom')
        CustomerDao.addCustomer(12, 'Sam', 'Sam@gmailcom')
        CustomerDao.addCustomer(13, 'Samuel', 'Samuel@gmailcom')
        CustomerDao.addCustomer(14, 'Darcy', 'Darcy@gmailcom')
        CustomerDao.addCustomer(15, 'Sandy', 'Sandy@gmailcom')
        CustomerDao.addCustomer(16, 'Boyer', 'Boyer@gmailcom')
        CustomerDao.addCustomer(17, 'Eric', 'Eric@gmailcom')

    @staticmethod
    def createRoomsData():
        #Method to create Invantory of Rooms
        RoomDao.createRooms("KING", "200")
        RoomDao.createRooms("QUEEN", "100")
        RoomDao.createRooms("SINGLE", "50")
        RoomDao.createRooms("QUEEN", "100")
        RoomDao.createRooms("SINGLE", "50")
        RoomDao.createRooms("KING", "200")
        RoomDao.createRooms("QUEEN", "100")
        RoomDao.createRooms("SINGLE", "50")
        RoomDao.createRooms("KING", "200")
        RoomDao.createRooms("QUEEN", "100")
        RoomDao.createRooms("SINGLE", "50")
        RoomDao.createRooms("KING", "200")
        RoomDao.createRooms("QUEEN", "100")
        RoomDao.createRooms("SINGLE", "50")
        RoomDao.createRooms("KING", "200")
        RoomDao.createRooms("QUEEN", "100")
        RoomDao.createRooms("SINGLE", "50")
        RoomDao.createRooms("QUEEN", "100")
        RoomDao.createRooms("KING", "200")
