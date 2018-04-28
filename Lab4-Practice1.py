city_list=[]
city=input("Enter name of city or stop >")
city_list.append(city)
    
while city!='stop':
    city=input("Enter name of city or stop >")
    city_list.append(city)

for city in city_list:
    if city[0]=='C':
        print(city)