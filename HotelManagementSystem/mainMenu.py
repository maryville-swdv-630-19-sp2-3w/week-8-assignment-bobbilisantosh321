from receptionistRole import Receptionist
from customerRole import Customer
from managerRole import Manager
from sampleData import SampleData


class Main():
    def __init__(self):
        #For creating some sample data for operations
        SampleData.createCustomerData()
        SampleData.createRoomsData()
    
    def printIntro(self):
        #Method to print intro for the System
        print("***********************************************************")
        print("                     WELCOME TO HOTEL TAJ                  ")
        print("***********************************************************")
    
    def runApplication(self):
        #Default Variable value
        person = None
        #Method to Run the Managemment Application
        while True:
            #Get Input for Role ID for relevant actions to display
            while True:
                try:
                    role = int(input("Select your appropriate role: \n 1. Receptionist \n 2. Existing Customer \n 3. Manager \n 4. Exit \n Your Role: "))
                except:
                    print("Invalid role to display menu, please try again\n")
                else: break
            
            if role == 1:
                #Role 1 - Receptionist
                #Get actions relevant to the Role
                person = Receptionist()
            
            elif role == 2:
                #Role 2 - Existing Customer
                #Get actions relevant to the Role
                while True:
                    #Get Customer ID
                    try: personId = int(input("Enter the customer Id: "))
                    except: print("ID can only a number, please try again\n")
                    else: break
                #Get actions for a Valid customer ID
                try: person = Customer(personId)
                except:
                    print("\nNo customer found for the ID {0}, role is no more valid".format(personId))
                    person = None
            elif role == 3:
                #Role 3 - Manager
                #Get actions relevant to the Role
                person = Manager()
            elif role == 4:
                #Role 4 - Exit Appication
                #Get actions relevant to the Role
                return
            else:
                #Invalid menu option selected
                print("Invalid role to display menu, please try again")
                
            if person == None:
                #No valid value selected for the menu action
                print("Invalid id for the role, please try again")
            else:
                #Display actions relevant for the Role
                person.displayActions()
                #Input action
                try: action = int(input("Select an action from above: "))
                except: print("Invalid action selected\n")
                else:
                #Perform selected action
                    person.performAction(action)                

def runMain():
    #Prints Main menu
    main = Main()
    main.printIntro()
    main.runApplication()
    
runMain()