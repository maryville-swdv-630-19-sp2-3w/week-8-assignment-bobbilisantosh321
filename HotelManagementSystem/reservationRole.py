from reservationData import ReservationDao
from billRole import Bill
from customerData import CustomerDao


class Reservation:
    def __init__(self, customerId):
        #Instance of a Reservation Document
        self.__reservationDao = ReservationDao.getReservationByCustomerId(customerId)
        if self.__reservationDao is None:
            raise Exception("Reservation not found for customer id")
        self.id = self.__reservationDao.reservationId
        self.startTime = self.__reservationDao.fromDate
        self.endTime = self.__reservationDao.toDate
        self.status = self.__reservationDao.status
        self.customerName = CustomerDao.getCustomerById(customerId).name
        self.amount = Bill(self.__reservationDao.billId).amount
        self.billId = self.__reservationDao.billId
        self.status = self.__reservationDao.status
        self.billStatus = Bill(self.__reservationDao.billId).status
        self.roomId = self.__reservationDao.roomId
