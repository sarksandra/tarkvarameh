myArr=[0,0,0,0]

def mySum(a,b):
    
    if isinstance(a, int) and isinstance(b,int):
        return a + b
    else:
        print("vale tüüp")
        
print(mySum(1,3))
        
        
def myMinus(a,b):
    
    if isinstance(a, int) and isinstance(b,int):
        return a - b
    else:
        print("vale tüüp")        
 
print(myMinus(1,3))

def myMult(a,b):
    
    if isinstance(a, int) and isinstance(b,int):
        return a * b
    else:
        print("vale tüüp")        
 
print(myMult(1,3))


def myJag(a,b):
    try:  
        if isinstance(a, int) and isinstance(b,int):
            return a / b
        else:
            print("vale tüüp")
    except ZeroDivisionError:
        print("nulliga ei saa jagada")
      
print(myJag(4,0))


def main():
    while True:
        valik = input("mida sa teha tahad")
        if valik == "1":
            a =int(input("sisesta esimene number 1:"))
            b =int(input("sisesta teine number 2:"))
            result = mySum(a,b)
            myArr[0] += 1
            print("tulemus on", result)
            
        elif valik == "2":
            a =int(input("sisesta esimene number 1:"))
            b =int(input("sisesta teine number 2:"))
            result = myJag(a,b)
            myArr[1] += 1
            print("tulemus on", result)
            
        elif valik == "3":
            a =int(input("sisesta esimene number 1:"))
            b =int(input("sisesta teine number 2:"))
            result = myMult(a,b)
            myArr[2] += 1
            print("tulemus on", result)
            
        elif valik == "4":
            a =int(input("sisesta esimene number 1:"))
            b =int(input("sisesta teine number 2:"))
            result = myMinus(a,b)
            myArr[3] += 1
            print("tulemus on", result)
            
        else:
            print("seda ei ole valikus")
        
main()

def displayInfo():
    print("kokku oli", sum(myArr))
    print("Suumerimine töötas : ", myArry[0], "Korda")
    print("lahutamine oli: ", myArry[1], "Korda")
    print("korrutamine oli: ", myArry[2], "Korda")
    print("jagamine oli: ", myArry[3], "Korda")
    


        
        

    

        
        





