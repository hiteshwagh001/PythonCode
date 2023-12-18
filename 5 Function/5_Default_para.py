def fun(a,b,c=50):
    print(a)
    print(b)
    print(c)

fun(10,20)
fun(90,100,120)


def companyInfo(CompName,EmpCount):
    print(CompName,EmpCount)

companyInfo("TechMahindra",34786)
companyInfo("FaceBook",50000)

companyInfo(EmpCount=90000,CompName="Monster")