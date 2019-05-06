from sqlalchemy import Column, Integer, String
from sqlalchemy import func
from databaseSingleTon import DataBaseSession
from databaseSingleTon import Base
import uuid

class RoomDao (Base):

    def __init__(self, Id, type, price, status):
        #Instantiate with Room object details
        self.roomId = Id
        self.type = type
        self.price = price
        self.status = status


    __tablename__ = 'rooms'
    roomId = Column(String, primary_key=True)
    type = Column(String)
    price = Column(String)
    status = Column(String)


    @staticmethod
    def createRooms(type, price):
        #Method to create  entry of Room
        session = DataBaseSession().createSession()
        session.add(RoomDao(uuid.uuid4().hex, type, price, "AVAILABLE"))
        session.commit()

    @staticmethod
    def isRoomAvailable(type):
        #Check if a room is available of given type
        session = DataBaseSession().createSession()
        roomDaoList = session.query(RoomDao).filter_by(type=type).filter_by(status="AVAILABLE").all()
        return len(roomDaoList) > 0

    @staticmethod
    def bookRoom(type):
        #Change status of first vacant room of given type to Occupied and return room id
        session = DataBaseSession().createSession()
        roomDao = session.query(RoomDao).filter_by(type=type).first()
        session.query(RoomDao).filter_by(roomId=roomDao.roomId).update({RoomDao.status: "OCCUPIED"}, synchronize_session=False)
        session.commit()
        return roomDao.roomId

    @staticmethod
    def listAvailableRooms():
        #return a map with numb er of available rooms {"Queen" : 20, "King": 40, "Single": 30}
        session = DataBaseSession().createSession()
        roomsList = session.query(RoomDao.type, func.count(RoomDao.roomId)).filter_by(status="AVAILABLE").group_by(RoomDao.type).all()
        return roomsList

    @staticmethod
    def getRoomById(id):
        #return room details else excewption
        session = DataBaseSession().createSession()
        roomDao = session.query(RoomDao).filter_by(roomId=id).first()
        return roomDao
    
    @staticmethod
    def getAllRooms():
        #return all rooms details else excewption
        session = DataBaseSession().createSession()
        roomsDao = session.query(RoomDao).filter_by().all()
        return roomsDao
