#this program chescks if a lost item in the lost and found list
lost_items = ["phone", "wallet", "keys", "glasses", "watch", "earphones", "bag", "laptop", "jacket", "umbrella"]

def check_lost_item(item):
    for li in lost_items:
        if li == item:
            print(item + " is in the lost and found list")
            return
    print(item + " is not in the lost and found list") 

#applies how many they wish to check
howmanylooking = input("how many do you want to look for? ")
for i in range(int(howmanylooking)):
    item = input("Enter the item you want to check: ").lower()
    check_lost_item(item)

#allows to add new items to the lost and found list
addnewitwm = input("Do you want to add a new item to the lost and found list? (yes/no): ").lower()
if addnewitwm == "yes":
    newitem = input("Enter the new item: ").lower()
    lost_items.append(newitem)
    print(newitem + " has been added to the lost and found list")
    print(lost_items)
else:
    print("Thank you for using our service")
    


