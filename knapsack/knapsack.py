#!/usr/bin/python

import sys
from collections import namedtuple

Item = namedtuple('Item', ['index', 'size', 'value'])
 
thing1 = Item(index=0,size=11,value =22)
thing2 = Item(index=1,size=4,value=33)
thing3 = Item(index=2,size=5, value=40)
thing4 = Item(3,4,55)
print("ITEM",thing4[2])
stuff = []  

newStuff = []
stuff.append(thing1 )
stuff.append(thing2)
stuff.append(thing3)
stuff.append(thing4)


def divide_item(item):
      # res= int (item.value//item.size)
      return item.value//item.size
    
Eff = divide_item( thing1)   

print("EFF",Eff) 
for i in stuff:
  res =divide_item(i)
  newStuff.append(res)
  print("STUFF", stuff)
  print("NEWSTUFF", newStuff)
   
def knapsack_solver(items, capacity):
    # Your code here
    items.sort(key = lambda x: x.value, reverse =True)

    sack = []
    best =[]
    cur_weight = 0
    i = 0
    for i in (len(items)):
      return i.value//i.weight
      # cur_weight+ items[i].weight
      # if cur_weight + items[i].weight<=capacity:
      #   sack.append(items[i])
      ##Sort by value
       
            
      
 

if __name__ == '__main__':
  if len(sys.argv) > 1:
    capacity = int(sys.argv[2])
    file_location = sys.argv[1].strip()
    file_contents = open(file_location, 'r')
    items = []

    for line in file_contents.readlines():
      data = line.rstrip().split()
      items.append(Item(int(data[0]), int(data[1]), int(data[2])))
    
    file_contents.close()
    print(knapsack_solver(items, capacity))
  else:
    print('Usage: knapsack.py [filename] [capacity]')
    


def naive_knapsack(weight_limit, items):
    items.sort(key = lambda x: x.value, reverse =True)
    
    sack = []
    sack2=[]
    cur_weight =0
    i = 0
    def divide_item(item):
      return item.value//item.weight
    for i in range(0,len(items)-1):
      divide_item(i)
      sack2.append(i)
    #while there is toom in the sack IF there is Room.
    for i in range(len(items)-1):
        if cur_weight + items[i].weight <=weight_limit:
           sack.append(items[i])
        
    return sack    
    #put the next most valuable item in it
    
     