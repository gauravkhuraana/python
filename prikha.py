import pandas as pd
import matplotlib.pyplot as plt
food=pd.read_csv("S:\\Automation\\python\\newfile.csv")
print(food)
while(True):
    print("\n\n\n\t\t############ MAIN MENU ###############")
    print("\n\t\t\t 1. Add Data ")
    print("\n\t\t\t 2. Search Data ")
    print("\n\t\t\t 3. Visualize Data ")
    print("\n\t\t\t 4. Exit ")
    print("\t\t###########################################")
    ch=int(input("\t\tEnter your choice 1-4: "))
    
    if (ch==1):
        while(True):
            print("Add Menu")
            print("1. Add new column")
            print("2. Add new row")
            print("3. Exit")
            ch1=int(input("Enter your choice 1-3:"))
            if (ch1==1):
                name=input("Enter the name of the new column:")
                data=input("Enter the value by which you want to initialize this column:")
                food[name]=data
                print(food)
            elif (ch1==2):
                name=input("Enter name of the Indian Food:")
                typeofdiet=input("Enter typeofdiet:")
                preparationtime=int(input("Enter preparationtime:"))
                cookingtime=int(input("Enter cookingtime:"))
                flavor=input("Enter flavour:")
                course=input("Enter course:")
                state=input("Enter state:")
                region=input("Enter region:")
                countrec=food.shape[0]
                print(food)
            else:
                break
            
    elif (ch==2):
        while(True):
            print("--------------------------------------------------------------------------")
            print("| Search Menu |")
            print("| 1. Search given food item details |")
            print("| 2. Search records of a given state (any Indian state) |")
            print("| 3. Search records of a given region: East/West/North/South |")
            print("| 4. Search records of a given course: dessert/main course/drink/snack |")
            print("| 5. Search records of a given flavor: sweet/savoury |")
            print("| 6. Search records of a given typeofdiet: vegetarian/non-vegetarian |")
            print("| 7. Exit |")
            print("--------------------------------------------------------------------------")
            ch1=int(input("Enter your choice 1-7"))
            if (ch1==1):
                data=input("Enter name of the Indian Food whose details are to be displayed")
                print(food[food.name==data])

            elif (ch1==2):
                data=input("Enter name of the state whose details are to be displayed")
                print(food[food.state==data])
            elif (ch1==3):
                data=input("Enter name of the region whose details are to be displayed")
                print(food[food.region==data])
            elif (ch1==4):
                data=input("Enter name of the course whose details are to be displayed")
                print(food[food.course==data])
            elif (ch1==5):
                data=input("Enter name of the flavour whose details are to be displayed")
                print(food[food.flavour==data])
 
            elif (ch1==6):
                data=input("Enter name of the typeofdiet whose details are to be displayed")
                print(food[food.typeofdiet==data])
            else:
                break
            
                
    elif (ch==3):
        while(True):
            print("-------------------------------------------------------------------------------")
            print("| Visualize Menu |")
            print("| 1. Visualize cooking time state wise |")
            print("| 2. Visualize cooking time region: East/West/North/South wise |")
            print("| 3. Visualize cooking time course: dessert/main course/starter/snack wise |")
            print("| 4. Visualize preparation time state wise |")
            print("| 5. Visualize preparation time region: East/West/North/South wise |")
            print("| 6. Visualize preparation time course: dessert/main course/starter/snack wise|")
            print("| 7.Exit |")
            print("-------------------------------------------------------------------------------")
            ch1=int(input("Enter your choice 1-7"))
            
            if (ch1==1):
                print(food.columns)
                ab=food.state
                cd=food.cookingtime
                plt.title("Cooking Time of Indian Dishes")
                plt.xlabel("Indian States")
                plt.ylabel("Cooking Time")
                plt.xticks(rotation=30)
                plt.grid(True)
                print("----------------------")
                print("| 1. Line Chart |")
                print("| 2. Bar Chart |")
                print("----------------------")
                print("Select the type of chart")
                type=int(input("Enter choice 1-2"))
                if (type==1):
                    plt.plot(ab,cd,label="cooking time")
                    plt.show()
                elif (type==2):
                    plt.bar(ab,cd,label="cooking time")
                    plt.show()
                else:
                    print("Invalid choice")
            elif (ch1==2):
                ab=food.region
                cd=food.cookingtime
                plt.title("Cooking Time of Indian Dishes")
                plt.xlabel("Regions")
                plt.ylabel("Cooking Time")
                plt.xticks(rotation=30)
                plt.grid(True)
                print("----------------------")
                print("| 1. Line Chart |")
                print("| 2. Bar Chart |")
                print("----------------------")
                print("Select the type of chart")
                type=int(input("Enter choice 1-2"))
                if (type==1):
                    plt.plot(ab,cd,label="cooking time")
                    plt.show()
                elif (type==2):
                    plt.bar(ab,cd,label="cooking time")
                    plt.show()
                else:
                    print("Invalid choice")
            elif (ch1==3):
                ab=food.course
                cd=food.cookingtime
                plt.title("Cooking Time of Indian dishes")
                plt.xlabel("Course")
                plt.ylabel("Cooking Time")
                plt.xticks(rotation=30)
                plt.grid(True)
                print("----------------------")
                print("| 1. Line Chart |")
                print("| 2. Bar Chart |")
                print("----------------------")
                print("Select the type of chart")
                type=int(input("Enter choice 1-2"))
                if (type==1):
                    plt.plot(ab,cd,label="cooking time")
                    plt.show()
                elif (type==2):
                    plt.bar(ab,cd,label="cooking time")
                    plt.show()
                else:
                    print("Invalid choice")
                    
            elif (ch1==4):
                ab=food.state
                cd=food.preparationtime
                plt.title("Preparation Time of Indian dishes")
                plt.xlabel("Indian States")
                plt.ylabel("Preparation Time")
                plt.xticks(rotation=30)
                plt.grid(True)
                print("----------------------")
                print("| 1. Line Chart |")
                print("| 2. Bar Chart |")
                print("----------------------")
                print("Select the type of chart")
                type=int(input("Enter choice 1-2"))
                if (type==1):
                    plt.plot(ab,cd,label="preparation time")
                    plt.show()
                elif (type==2):
                    plt.bar(ab,cd,label="preparation time")
                    plt.show()
                else:
                    print("Invalid choice")
            elif (ch1==5):
                ab=food.region
                cd=food.preparationtime
                plt.title("Preparation Time of Indian dishes")
                plt.xlabel("Regions")
                plt.ylabel("Preparation Time")
                plt.xticks(rotation=30)
                plt.grid(True)
                print("----------------------")
                print("| 1. Line Chart |")
                print("| 2. Bar Chart |")
                print("----------------------")
                print("Select the type of chart")
                type=int(input("Enter choice 1-2"))
                if (type==1):
                    plt.plot(ab,cd,label="preparation time")
                    plt.show()
                elif (type==2):
                    plt.bar(ab,cd,label="preparation time")
                    plt.show()
                else:
                    print("Invalid choice")
            elif (ch1==6):
                ab=food.course
                cd=food.preparationtime
                plt.title("Preparation Time of Indian dishes")
                plt.xlabel("Course")
                plt.ylabel("Preparation Time")
                plt.xticks(rotation=30)
                plt.grid(True)
                print("----------------------")
                print("| 1. Line Chart |")
                print("| 2. Bar Chart |")
                print("----------------------")
                print("Select the type of chart")
                type=int(input("Enter choice 1-2"))
                if (type==1):
                    plt.plot(ab,cd,label="preparation time")
                    plt.show()
                elif (type==2):
                    plt.bar(ab,cd,label="preparation time")
                    plt.show()
                else:
                    print("Invalid choice")
            else:
                break
            
    else:
        print("****")
        break
