from sqlalchemy import Column, Integer, String
from databaseSingleTon import DataBaseSession
from databaseSingleTon import Base


# This class is responsible to perform all the CRUD operations with Customer Database

class CustomerDao(Base):

    def __init__(self, cusId, name, email):
        #Instantiate with Customer object details
        self.cusId = cusId
        self.name = name
        self.email = email

    __tablename__ = 'customer'
    cusId = Column(Integer, primary_key=True)
    name = Column(String)
    email = Column(String)

    def __repr__(self):
        #Customer Object Details
        return "Customer(cusId = {0}, name={1}, email={2})".format(self.cusId, self.name, self.email)

    @staticmethod
    def addCustomer(cusId, name, email):
        #Method to add a new customer 
        session = DataBaseSession().createSession()
        session.add(CustomerDao(cusId, name, email))
        session.commit()

    @staticmethod
    def getCustomerById(cusId):
        #Method to get customer object
        session = DataBaseSession().createSession()
        customerdao = session.query(CustomerDao).filter_by(cusId=cusId).first()
        return customerdao

    @staticmethod
    def getAllCustomer():
        #Method to get all customers
        session = DataBaseSession().createSession()
        customersdao = session.query(CustomerDao).filter_by().all()
        return customersdao

    @staticmethod
    def updateCustomer(id, name, email):
        #Mthod to update details of a customer
        session = DataBaseSession().createSession()
        session.query(CustomerDao).filter_by(cusId=id).update({CustomerDao.name: name, CustomerDao.email: email}, synchronize_session=False)
        return id



