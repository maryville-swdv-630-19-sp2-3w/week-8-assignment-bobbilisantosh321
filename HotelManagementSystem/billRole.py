from billsData import BillDao
class Bill:
    def __init__(self, id):
        #Instance of a Bill Document
        self._billDao = BillDao.getBillById(id)
        self.roomId = self._billDao.roomId
        self.customerId = self._billDao.cusId
        self.amount = self._billDao.amount
        self.paymentCardNum = self._billDao.cardNum
        self.status = self._billDao.billStatus