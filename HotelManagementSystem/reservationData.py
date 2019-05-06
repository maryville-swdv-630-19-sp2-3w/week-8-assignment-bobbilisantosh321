from sqlalchemy import Column, Integer, String
from databaseSingleTon import DataBaseSession
from databaseSingleTon import Base
import uuid

class ReservationDao (Base):

    def __init__(self,reservationId,  cusId, billId, roomId, fromDate, toDate, status):
        #Instantiate with Reservation object details
        self.reservationId = reservationId
        self.cusId = cusId
        self.billId = billId
        self.roomId = roomId
        self.fromDate = fromDate
        self.toDate = toDate
        self.status = status

    __tablename__ = 'reservation'
    reservationId = Column(String, primary_key=True)
    cusId = Column(String)
    roomId = Column(String)
    fromDate = Column(String)
    toDate = Column(String)
    billId = Column(String)
    status = Column(String)

    def __repr__(self):
        #Reservation object 
        return "Reservation(cusId = {0}, roomId={1}, fromDate={2}, toDate={3}, billId={4}, status={5})".format(self.cusId, self.roomId, self.fromDate, self.toDate, self.billId, self.status)


    @staticmethod
    def createReservation(customerId, billId, roomId, fromDate, toDate):
        #create reservation with details and status as reserved, return reservationId
        session = DataBaseSession().createSession()
        session.add(ReservationDao(uuid.uuid4().hex, customerId, billId, roomId, fromDate, toDate, 'WAITING FOR PAYMENT'))
        session.commit()
        return ReservationDao.getReservationByCustomerId(customerId).reservationId

    @staticmethod
    def getReservationByCustomerId(cusId):
        #return reservation of customer else throw exception
        session = DataBaseSession().createSession()
        reservationdao = session.query(ReservationDao).filter_by(cusId=cusId).first()
        return reservationdao
    
    def getReservationsByCustomerId(cusId):
        #return reservation of customer else throw exception
        session = DataBaseSession().createSession()
        reservationsdao = session.query(ReservationDao).filter_by(cusId=cusId).all()
        return reservationsdao

    @staticmethod
    def updateReservationStatus(id, status):
        #change the reservation of the given id to given status
        session = DataBaseSession().createSession()
        session.query(ReservationDao).filter_by(reservationId=id).update({ReservationDao.status: status}, synchronize_session=False)
        session.commit()
        print("Reservation status is {0}".format(session.query(ReservationDao).filter_by(reservationId=id).first().status))
        return


