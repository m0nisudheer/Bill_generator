from datetime import datetime

name=input("Enter your name:")

#LISTS of items

lists='''

rice      Rs 20/kg

sugar     Rs 30/kg

salt      Rs 20/kg

oil       Rs 80/liter

paneer    Rs 110/kg

maggi     Rs 50/kg

boost     Rs 90/each

colgate   Rs 85/each
'''
#declaration

price=0

pricelist=[]

totalprice=0

Finalfinalprice=0

ilist=[]
qlist=[]
plist=[]

#rates for items 25 

items={'rice':20,
'sugar':30,
'salt':20,
'oil':80,
'panner':110, 'maggi':50,'boost':90, 'colgate':85}
option=int(input("for list of items press 1:"))
if option==1:
    print(lists)
for i in range(len(items)):
    inpl=int(input("if you want to buy press 1 or 2 for exit:"))
    if inpl==2:
        break
    if inpl==1:
        item=input("Enter your items: ")
        quantity=int(input("Enter quantity:"))
        if item in items.keys():
            price=quantity*(items[item])
            pricelist.append((item, quantity,items,price))
            totalprice+=price
            ilist.append(item) 
            qlist.append(quantity)
            plist.append(price)
            gst=(totalprice*5)/100
            finalamount=gst+totalprice
        else:
            print("sorry you entered item is not available")
    else:
        print("you entered wrong number")

    inp=input("can i bill the items yes or no:")
    if inp=='yes':
        pass
        if finalamount!=0:
            print (25*"=","Sudheer supermarket",28*"=")
            print(31*" ","Bapatla")
            print("Name:",name, 30*" ","Date:",datetime.now())
            print (75*"=")
            print("sno",8*" ",'items',8*" ",'Quantity',8*' ','price')
            for i in range(len(pricelist)):
                  print(i,4*' ',5*' ',ilist[i],10*' ',qlist[i],14*" ",plist[i])
            print(75*"-")
            print (50*" ",'TotalAmount:','Rs',totalprice)
            print("gst amount",40*" ",'Rs',gst)
            print (75*"-")
            print(50*" ",'finalAmount:','Rs',finalamount)
            print (75*"-")
            print(20*" ","Thanks for visting")
            print (75*"-")
