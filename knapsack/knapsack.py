#!/usr/bin/python

import sys
from collections import namedtuple

Item = namedtuple('Item', ['index', 'size', 'value'])
 
thing1 = Item(index=0,size=11,value =22)
thing2 = Item(index=1,size=4,value=33)
thing3 = Item(index=2,size=5, value=40) 
thing4 = Item(3,4,55 )
stuff = []  

newStuff = []
stuff.append(thing1 )
stuff.append(thing2)
stuff.append(thing3)
stuff.append(thing4)


def divide_item(arr):
      # res= int (item.value//item.size)
      newArr = []
      for item in arr:
          eff=  item.value//item.size
          newArr.append(item.index)

          newArr.append(eff)
             
      return newArr
    
print("GWAA",divide_item(stuff)) 
   
def knapsack_solver(items, capacity):
    for i in items:
      # i.efficiency  = i.value/ i.size
      items.sort(key= lambda x: x.size , reverse=True)    
      sack= [] 
      weight= 0
      for i in items:
        weight += i.size
        if weight > capacity:
          return sack
        else:
          sack.append(i)
        
    return sack    
            
print(knapsack_solver(stuff, 25)     )
 

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
    
from itertools import combinations  
def knapsack_brute_force(weight_limit, items):
     all_combos =[]
     for i in range (1,len(items)+1):
       list_of_combos = list(combinations(items, i))
       for combo in list_of_combos:
         all_combos.append(combo)
     max_value = -1
     best_combo = None
     for combo in all_combos:
       value= 0
       weight = 0
       for item in combo:
         value += item.value
         weight += item.weight
       if weight <= weight_limit:
         if value < max_value:
           max_value = value
           best_combo = combo  
           
                
       return best_combo         
 #PROS = faster than brute force, much smarter than naive
 #CONS - may not get optimal result.
     
def knapsack_greedy(weight_limit, items):
  for i in items:
    i.efficiency = i.value/ i.weight
    
    items.sort(keys= lambda x: x.efficiency, reverse=True)    
    
    sack= [] 
    weight= 0
    for i in items:
      weight += i.weight
      if weight > weight_limit:
        return sack
      else:
        sack.append(i)
        
    return sack    