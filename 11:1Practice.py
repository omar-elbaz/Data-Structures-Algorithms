# # Calories Program


# def intro():
#     print()
#     print("Welcome!, lets breakdown your calorie intake")
#     print()

# def calculate_calories():
#     Fat = float(input("How many grams of fat do you intake in a day?     "))
#     Carbs = float(input("How many grams of carbs do you intake in a day?     "))
   
#     print()
#     print("Now lets calculate the calories")
#     print()
#     Calories_From_Fat = Fat * 9  
#     Calories_From_Carbs = Carbs * 4 
#     total_Calories = Calories_From_Fat + Calories_From_Carbs

#     print ("You have an intake of", Calories_From_Fat,"calories from fat and", Calories_From_Carbs, "calories from carbs")

# intro()
# calculate_calories()

def main():
    def intro_message():
        print()
        print("Welcome, I will help convert from feet to inches")
        print()
        
    def feet_to_inches(feet):
        print()
        print(feet*12)
        print()
        print( "The equivalent of",feet, "feet is", feet*12, "inches")
        print()
    
    intro_message()
    feet_to_inches(float(input("Enter a Number of feet: ")))
    


main()