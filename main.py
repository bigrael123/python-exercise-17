number_of_clients = 0
money_received = 0
clients_age = 0

while True:
    age = int(input("Type your age. 0 ends the program: "))
    if(age<0):
        print("Type a valid number.")
    if(age ==0):
        break
    if(age > 0 and  age<=3):
        print("Tickets for children from 1 to 3 years of age are free.")
        accepted = int(input("Type 1 to get the ticked o 0 to go back to the beginning: "))
        if(accepted == 1):
            number_of_clients+=1
            clients_age +=age
    if(age > 3 and age <= 12):
        print("Tickets for children from 3 to 12 years of age are 15 dollars.")
        accepted = int(input("Type 1 to get the ticked o 0 to go back to the beginning: "))
        if(accepted == 1):
            clients_age+= age
            money_received+=15
            number_of_clients+=1
    if(age>12):
        print("Tickets for people over 12 years of age are 30 dollars.")
        accepted = int(input("Type 1 to get the ticked o 0 to go back to the beginning: "))
        if(accepted == 1):
            clients_age+=age
            money_received+=30
            number_of_clients+=1
if(number_of_clients>0):
    print(f"Today we had {number_of_clients} clients, earned {money_received} dollars and the average age on the cinema was {clients_age/number_of_clients}")
print("Closing...")