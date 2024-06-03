def outer(flag):
    def inner():
        return "This is true:"if flag else"This is flase"
    return inner

if __name__=='__main__':
    true_fun=outer(True)
    false_fun=outer(False)
    
    print(true_fun())
    print(false_fun())