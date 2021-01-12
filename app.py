def main():
    cont = 'Y'
    cabs =[]
    total_distance = 0
    total_fare = 0

    while cont.upper()=='Y':
        valid = False
        cabType =input("Enter cab type(Hatchback/Sedan): ")

        while valid == False:

            if (cabType.upper() =="HATCHBACK"):
                distance = eval(input("Enter the number of kilometers travelled: "))
                valid = True
            elif (cabType.upper() == "SEDAN"):
                distance = eval(input("Enter the number of kilometers travelled: "))
                valid = True
            else:
                cabType = input("That is not a car. Enter cab type(Hatchback/Sedan): ")
                continue

        if(cabType.upper()=="HATCHBACK"):
            emp = Hatchback(cabType,distance)
        else:
            emp = Sedan(cabType,distance)

        cabs.append(emp)

        cont = input("Do you want to continue (Y/N)? ")
        if(cont.upper() == "Y"):
            emp = Hatchback(cabType,distance)
        else:
            print("")
            print("-----Kilometers driven for each cab-----")
            for cab in cabs:
                print(cab.getName(), ":", cab.getDistance()," kilometers")

        if(cont.upper() == "Y"):
            emp = Hatchback(cabType,distance)
        else:
            for cab in cabs:
                total_distance += cab.getDistance()

                total_fare += cab.CalculateFare()

            dashes()
            print("Total number of kilometers driven by all Cabs: ",total_distance)
            print("Total fare earned from all cabs (in dollars): ",total_fare)

class Cab:
    def __init__(self,name ="",distance=0):
        self._name = name
        self._distance = distance

    def setName(self,name):
        self._name = name

    def getName(self):
        return self._name

    def setRate (self, distance):
        self._distance = distance

    def getDistance (self):
        return self._distance

class Sedan(Cab):
    def CalculateFare(self):
       return self._distance * 1.5

class Hatchback(Cab):
    def CalculateFare(self):
        return self._distance * 2

def dashes():
    print()
    print("-"*40)
main()
