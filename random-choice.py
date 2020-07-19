import random                                                                    
count = input('how many items do you want to add to list: ')

while(1):

    try:
        count=int(items)
        items=[]

        for i in range(count):

            client_item=input('enter an item: ')

            while client_item =='' :

                print('empty input cant be accepted')
                client_item=input('enter an item: ') 

            else :

                items.append(client_item)
                
        print('items to choice: \n', choices,"\n")
        final_choice=random.choice(items)
        print(final_choice)  
        break
     
    except ValueError:

        print("[!] Wrong input!")
        print("[*]Enter Number of items do you want to add to list")
        count = input('how many items do you want to add to list: ')
