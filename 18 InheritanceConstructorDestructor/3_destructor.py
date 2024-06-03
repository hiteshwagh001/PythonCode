class demo:
    def __init__(self) :
        print("in parent constructor")

    def run(self):
        print("in parent fun")

    def __del__(self):
        print("destrctor called")


class child(demo):
    pass

obj=child()
obj.run()

del  obj

print("end of the code")
