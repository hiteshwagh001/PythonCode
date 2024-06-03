can=int(input("Size of can "))
water=int(input("how much water in can " ))

class OverFlowWater(Exception):
    def __init__(self,message):
        super().__init__(message)

class check(object):
    def checkoverflow(self,can,water):
        if water>can:
            raise OverFlowWater("water is overFlow dude ")
        else:
            print("Bucket is not full!!")


obj=check()
try:
    obj.checkoverflow(can,water)
except OverFlowWater as err:
    print(err)