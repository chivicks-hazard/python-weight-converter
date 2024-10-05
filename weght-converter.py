from weights import gram, kilogram, pound, ounce, ton, ust, ukt

print("What weights do you want to convert?")
print("Gram to Kilogram: gram2kg")
print("Gram to Ton: gram2ton")
print("Gram to Pound: gram2lb")
print("Gram to Ounce: gram2oz")
print("Gram to US Ton: gram2ust")
print("Gram to UK Ton: gram2ukt")
print("Kilogram to Gram: kg2gram")
print("Kilogram to Ton: kg2ton")
print("Kilogram to Pound: kg2lb")
print("Kilogram to Ounce: kg2oz")
print("Kilogram to US Ton: kg2ust")
print("Kilogram to UK Ton: kg2ukt")
print("Pound to Gram: lb2gram")
print("Pound to Kilogram: lb2kg")
print("Pound to Ounce: lb2oz")
print("Pound to US Ton: lb2ust")
print("Pound to UK Ton: lb2ukt")
print("Ounce to Gram: oz2gram")
print("Ounce to Kilogram: oz2kg")
print("Ounce to Pound: oz2lb")
print("Ounce to US Ton: oz2ust")
print("Ounce to UK Ton: oz2ukt")
print("Ton to Gram: ton2gram")
print("Ton to Kilogram: ton2kg")
print("Ton to Pound: ton2lb")
print("Ton to Ounce: ton2oz")
print("Ton to US Ton: ton2ust")
print("Ton to UK Ton: ton2ukt")
print("US Ton to Gram: ust2gram")
print("US Ton to Kilogram: ust2kg")
print("US Ton to Pound: ust2lb")
print("US Ton to Ounce: ust2oz")
print("US Ton to Ton: ust2ton")
print("UK Ton to Gram: ukt2gram")
print("UK Ton to Kilogram: ukt2kg")
print("UK Ton to Pound: ukt2lb")
print("UK Ton to Ounce: ukt2oz")
print("UK Ton to Ton: ukt2ton")
print("UK Ton to US Ton: ukt2ust")
command = input("Enter the conversion rate: ")

def convert(command):
    while not "no" in command.lower():
        match command:
            case "gram2kg":
                weight = int(input("Enter the weight: "))
                print(f"{gram.Gram2KG(weight)}kg")
                
            case "gram2ton":
                weight = int(input("Enter the weight: "))
                print(f"{gram.Gram2Ton(weight)} ton")
                
            case "gram2lb":
                weight = int(input("Enter the weight: "))
                print(f"{gram.Gram2LB(weight)}lb")

            case "gram2oz":
                weight = int(input("Enter the weight: "))
                print(f"{gram.Gram2OZ(weight)}oz")
                
            case "gram2ust":
                weight = int(input("Enter the weight: "))
                print(f"{gram.Gram2UST(weight)}t(US)")
                
            case "gram2ukt":
                weight = int(input("Enter the weight: "))
                print(f"{gram.Gram2UKT(weight)}t(UK)")
                
            case "kg2gram":
                weight = int(input("Enter the weight: "))
                print(f"{kilogram.KG2Gram(weight)}g")
                
            case "kg2ton":
                weight = int(input("Enter the weight: "))
                print(f"{kilogram.KG2Ton(weight)} ton")
                
            case "kg2lb":
                weight = int(input("Enter the weight: "))
                print(f"{kilogram.KG2LB}lb")
                
            case "kg2oz":
                weight = int(input("Enter the weight: "))
                print(f"{kilogram.KG2OZ(weight)}oz")
                
            case "kg2ust":
                weight = int(input("Enter the weight: "))
                print(f"{kilogram.KG2UST(weight)}t(US)")
                
            case "kg2ukt":
                weight = int(input("Enter the weight: "))
                print(f"{kilogram.KG2UKT(weight)}t(UK)")
                
            case "lb2gram":
                weight = int(input("Enter the weight: "))
                print(f"{pound.LB2Gram(weight)}g")
                
            case "lb2kg":
                weight = int(input("Enter the weight: "))
                print(f"{pound.LB2KG(weight)}kg")
                
            case "lb2ton":
                weight = int(input("Enter the weight: "))
                print(f"{pound.LB2Ton(weight)} ton")
                
            case "lb2oz":
                weight = int(input("Enter the weight: "))
                print(f"{pound.LB2OZ(weight)}oz")
                
            case "lb2ust":
                weight = int(input("Enter the weight: "))
                print(f"{pound.LB2UST(weight)}t(US)")
                
            case "lb2ukt":
                weight = int(input("Enter the weight: "))
                print(f"{pound.LB2UKT(weight)}t(UK)")
                
            case "oz2gram":
                weight = int(input("Enter the weight: "))
                print(f"{ounce.OZ2Gram(weight)}g")
                
            case "oz2kg":
                weight = int(input("Enter the weight: "))
                print(f"{ounce.OZ2KG(weight)}kg")
                
            case "oz2ton":
                weight = int(input("Enter the weight: "))
                print(f"{ounce.OZ2Ton(weight)}ton")
                
            case "oz2ust":
                weight = int(input("Enter the weight: "))
                print(f"{ounce.OZ2UST(weight)}t(US)")
                
            case "oz2ukt":
                weight = int(input("Enter the weight: "))
                print(f"{ounce.OZ2UKT(weight)}t(UK)")
                
            case "ton2gram":
                weight = int(input("Enter the weight: "))
                print(f"{ton.Ton2Gram(weight)}g")
                
            case "ton2kg":
                weight = int(input("Enter the weight: "))
                print(f"{ton.Ton2KG(weight)}kg")
                
            case "ton2lb":
                weight = int(input("Enter the weight: "))
                print(f"{ton.Ton2LB(weight)}lb")
                
            case "ton2oz":
                weight = int(input("Enter the weight: "))
                print(f"{ton.Ton2OZ(weight)}oz")
                
            case "ton2ust":
                weight = int(input("Enter the weight: "))
                print(f"{ton.Ton2UST(weight)}t(US)")
                
            case "ton2ukt":
                weight = int(input("Enter the weight: "))
                print(f"{ton.Ton2UKT(weight)}t(UK)")
                
            case "ust2gram":
                weight = int(input("Enter the weight: "))
                print(f"{ust.UST2Gram(weight)}g")
                
            case "ust2kg":
                weight = int(input("Enter the weight: "))
                print(f"{ust.UST2KG}kg")
                
            case "ust2ton":
                weight = int(input("Enter the weight: "))
                print(f"{ust.UST2Ton} t")
                
            case "ust2lb":
                weight = int(input("Enter the weight: "))
                print(f"{ust.UST2LB}lb")
                
            case "ust2oz":
                weight = int(input("Enter the weight: "))
                print(f"{ust.UST2OZ}oz")
                
            case "ust2ukt":
                weight = int(input("Enter the weight: "))
                print(f"{ust.UST2UKT}t(UK)")
                
            case "ukt2gram":
                weight = int(input("Enter the weight: "))
                print(f"{ukt.UKT2Gram(weight)}g")
                
            case "ukt2kg":
                weight = int(input("Enter the weight: "))
                print(f"{ukt.UKT2KG(weight)}kg")
                
            case "ukt2ton":
                weight = int(input("Enter the weight: "))
                print(f"{ukt.UKT2Ton(weight)}ton")
                
            case "ukt2lb":
                weight = int(input("Enter the weight: "))
                print(f"{ukt.UKT2LB(weight)}lb")
                
            case "ukt2oz":
                weight = int(input("Enter the weight: "))
                print(f"{ukt.UKT2OZ(weight)}oz")
                
            case "ukt2ust":
                weight = int(input("Enter the weight: "))
                print(f"{ukt.UKT2UST(weight)}t(US)")
                
            case _:
                print("Invalid input")
                
        print("Do you still want to convert?")
        command = input("")
        if not "no" in command.lower():
            print("What weights do you want to convert?")
            print("Gram to Kilogram: gram2kg")
            print("Gram to Ton: gram2ton")
            print("Gram to Pound: gram2lb")
            print("Gram to Ounce: gram2oz")
            print("Gram to US Ton: gram2ust")
            print("Gram to UK Ton: gram2ukt")
            print("Kilogram to Gram: kg2gram")
            print("Kilogram to Ton: kg2ton")
            print("Kilogram to Pound: kg2lb")
            print("Kilogram to Ounce: kg2oz")
            print("Kilogram to US Ton: kg2ust")
            print("Kilogram to UK Ton: kg2ukt")
            print("Pound to Gram: lb2gram")
            print("Pound to Kilogram: lb2kg")
            print("Pound to Ounce: lb2oz")
            print("Pound to US Ton: lb2ust")
            print("Pound to UK Ton: lb2ukt")
            print("Ounce to Gram: oz2gram")
            print("Ounce to Kilogram: oz2kg")
            print("Ounce to Pound: oz2lb")
            print("Ounce to US Ton: oz2ust")
            print("Ounce to UK Ton: oz2ukt")
            print("Ton to Gram: ton2gram")
            print("Ton to Kilogram: ton2kg")
            print("Ton to Pound: ton2lb")
            print("Ton to Ounce: ton2oz")
            print("Ton to US Ton: ton2ust")
            print("Ton to UK Ton: ton2ukt")
            print("US Ton to Gram: ust2gram")
            print("US Ton to Kilogram: ust2kg")
            print("US Ton to Pound: ust2lb")
            print("US Ton to Ounce: ust2oz")
            print("US Ton to Ton: ust2ton")
            print("UK Ton to Gram: ukt2gram")
            print("UK Ton to Kilogram: ukt2kg")
            print("UK Ton to Pound: ukt2lb")
            print("UK Ton to Ounce: ukt2oz")
            print("UK Ton to Ton: ukt2ton")
            print("UK Ton to US Ton: ukt2ust")
            command = input("Enter the conversion rate: ")

convert(command)