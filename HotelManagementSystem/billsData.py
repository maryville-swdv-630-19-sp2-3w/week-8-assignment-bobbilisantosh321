from sqlalchemy import Column, Integer, String
from databaseSingleTon import DataBaseSession
from databaseSingleTon import Base
import uuid

class BillDao (Base):

    def __init__(self,billId, cusId, amount, roomId, billStatus, cardNum):
        #Instantiate with billing object details
        self.billId = billId
        self.roomId = roomId
        self.cusId = cusId
        self.amount = amount
        self.billStatus = billStatus
        self.cardNum = cardNum

    __tablename__ = 'bill'
    billId = Column(String, primary_key=True)
    cusId = Column(String)
    amount = Column(String)
    roomId = Column(String)
    billStatus = Column(String)
    cardNum = Column(String)

    @staticmethod
    def createBill(roomId, cusId, amount):
        #create a bill with these details and return billId with status "NOTPAID"
        session = DataBaseSession().createSession()
        session.add(BillDao(roomId, cusId, amount, roomId, 'NOT PAID', '2341 16547 8222 2123'))
        session.commit()
        return BillDao.getBillByCustomerId(cusId).billId

    @staticmethod
    def getBillByCustomerId(cusId):
        #Method to get Bills for a Customer
        session = DataBaseSession().createSession()
        billdao = session.query(BillDao).filter_by(cusId=cusId).first()
        return billdao

    @staticmethod
    def getBillById(billId):
        #get bill details by id
        session = DataBaseSession().createSession()
        billdao = session.query(BillDao).filter_by(billId=billId).first()
        return billdao

    @staticmethod
    def updatePaymentDetails(id, cardNum):
        #update card num for the bill with given id and change status to PAID
        session = DataBaseSession().createSession()
        session.query(BillDao).filter_by(billId=id).update({BillDao.cardNum: cardNum}, synchronize_session=False)
        session.commit()
        return