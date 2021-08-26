list = []
i = 1
while i < 6:
    a = int(input("please enter a number:\n"))
    list.append(a)
    i+=1
list.sort()
first=0
last=len(list)-1
mid = (first+last)//2
item = int(input("enter the number to be searched\n"))
found = False
while( first<=last and not found):
    mid = (first + last)//2
    if list[mid] == item :
         print(f"found at location {mid}")
         found= True
    else:
        if item < list[mid]:
            last = mid - 1
        else:
            first = mid + 1 
   
if found == False:
    print("Number not found")