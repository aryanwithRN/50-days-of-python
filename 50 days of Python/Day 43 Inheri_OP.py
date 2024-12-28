# ------------------------------- OP 1 ------------------------------------------------------
# class A:
#    def __init__(self):
#      self.a=0
#    def A_data(self,a):
#      self.a=a
#      print(self.a)
# class B(A):
#     def __init__(self):
#      self.b=0
#     def B_data(self,b):
#        self.b=b
#        print(self.b)
# class C(B):
#    def __init__(self):
#      self.c=0
#    def C_data(self,c):
#      self.c=c
#      self.B_data(20)
#      print(self.c)
# #MAIN
# C1=C()
# C1.A_data(10)
# C1.C_data(30)


# ------------------------------- OP 2 ------------------------------------------------------
# class A:
#     def __init__(self):
#         self.value = 1

# class B(A):
#     def __init__(self):
#         super().__init__()
#         self.value += 10

# class C(A):
#     def __init__(self):
#         super().__init__()
#         self.value += 20

# class D(B, C):
#     def __init__(self):
#         super().__init__()

# obj = D()
# print(obj.value)

# ------------------------------- OP 3 ------------------------------------------------------

# class A:
#     def __init__(self):
#         self.x = 5

# class B(A):
#     def __init__(self):
#         super().__init__()

# class C(A):
#     def __init__(self):
#         self.y = 10

# obj_b = B()
# obj_c = C()
# print(obj_b.x + obj_c.y)



# ------------------------------- OP 4 ------------------------------------------------------

# class A:
#     def display(self):
#         print("A's display method")

# class B(A):
#     def display(self):
#         super().display()
#         print("B's display method")

# class C(B):
#     def display(self):
#         super().display()
#         print("C's display method")

# obj = C()
# obj.display()


# ------------------------------- OP 5 ------------------------------------------------------

# class A:
#     def __init__(self, x):
#         self.x = x

# class B(A):
#     def __init__(self, y):
#         super().__init__(y)

# obj = B(5)
# print(obj.x)
 
# ------------------------------- OP 6 ------------------------------------------------------

# class A:
#     def __init__(self, x):
#         self.x = x

# class B(A):
#     def __init__(self, y):
#         super().__init__(y)

# class C(A):
#     def __init__(self, z):
#         super().__init__(z)

# class D(B, C):
#     def __init__(self, w):
#         super().__init__(w)

# obj = D(20)
# print(obj.x)

# -------------------------------------------------------- Que 1 ---------------------------------------------------------------

# This scenario involves creating a recipe management system. We have a base class called Recipe representing generic recipe information, such as recipe name and ingredients.
#  The derived classes, VegetarianRecipe and NonVegetarianRecipe, specialize in vegetarian and non-vegetarian recipes, respectively.

# Base Class: Recipe
# Attributes:
# recipe_name: Represents the name of the recipe.
# ingredients: Represents the list of ingredients required for the recipe.
# servings: Represents the number of servings the recipe yields.
# prep_time: Represents the time required for preparation.

# Member Functions:
# display_recipe(): Displays details of the recipe, including its name, ingredients, servings, and prep time.
# calculate_total_calories(): Estimates the total calorie content of the recipe per serving.

# Derived Class 1: VegetarianRecipe
# Additional Attributes:
# cooking_time: Represents the time required to cook the recipe.
# difficulty_level: Represents the difficulty level of the recipe (e.g., easy, medium, hard).
# Additional Member Functions:
# adjust_spices(): Adjusts the amount of spices in the recipe based on difficulty level.
# calculate_total_protein(): Estimates the total protein content of the recipe per serving.

# Derived Class 2: NonVegetarianRecipe
# Additional Attributes:
# meat_type: Represents the type of meat used in the recipe.
# marination_time: Represents the time required for marination.
# Additional Member Functions:
# check_meat_quality(): Checks the quality of the meat based on meat type and freshness.
# calculate_total_fat(): Estimates the total fat content of the recipe per serving.

# ingredient_dict = {}
# class recipe:
#     def __init__(self):
#         self.recipe_name = ""
#         self.ingredients = 0
#         self.servings = 0
#         self.prep_time = ""
#         self.x = 0
#         self.calories = 0
#         self.protin = 0
#         self.difficulty_level= ""
        
#     def enter_(self):
#         self.recipe_name = input("ENter Recipe Name: ")
#         self.servings = int(input("Server For: "))
#         self.ingredients = int(input("ENter Number of recipe Ingredients you need: "))
#         for i in range (0, self.ingredients):
#             self.x  =  input("Enter Ingredients: ")
#             self.calories = int(input("Enter Calories"))
#             ingredient_dict [ self.x]= self.calories
        

#     def display_(self):
#         print(" = " * 40)
#         print("Recipe Name: ", self.recipe_name)
#         print("Serve For : ", self.servings)
#         print("Prep Time Est. : ", self.prep_time)
#         print("Ingredient's: ", ingredient_dict)
    
#     def calculate_total_calories(self):
#         sum_of_ingredient = sum(ingredient_dict[self.calories])
#         print("Total Calories: ", sum_of_ingredient)



# class VegetarianRecipe(recipe):
        
        
#     def enter_veg(self):
#         self.difficulty_level = input("Difficulty Level(Easy / medium / hard / tum se nhi banega -> 1 ): ").lower()
#         self.protin = input("Enter protine in gm: ")

#     def display_veg(self):
      
#         print("Difficulty level: ", self.difficulty_level)

#     def adjust_spice(self):
#         if self.difficulty_level == "easy":
#             print("Spice level Must be unpredicted as you are on easy mode ")

#         elif self.difficulty_level  == "medium":
#             print("Avg. spicey ")

#         elif self.difficulty_level == "hard ":
#             print("It taste very good and Spices are on Point")

#         elif self.difficulty_level == "1":
#             print("THE SPICES ARE ON POINT, TASTE LIKE 5 STAR HOTEL FOOD ")


#     def calculate_total_protein(self):
#         s = self.protin * self.servings
#         y = s / self.servings
#         print(f"Protine in each serve : {y}gm")
        
# class Non_veg(recipe):
#     def __init__(self):
#         super().__init__()
#         self.meat_type = ""
#         self.marination_time = ""
#         self.meat_Q = 0
#         self.fat = 0
        
#     def enter_Non (self):
#         self.meat_type = input("Enter Meat Type( Goat / Chicken ): ")
#         self.fat = input("Enter Fat in gm: ")
#         self.meat_Q = int(input("Enter Meat Quality ( 1 For Fresh / 2 For deep-Freez ): "))
#         self.marination_time = input("Enter MArination Time: ")

#     def display_non(self):
#         print("Meat Type: ", (self.meat_type).upper())
#         print("Fat in meat: ", self.fat)
#         print("Marination Time: ", self.marination_time)
#         if self.meat_Q == 1:
#             print("Fresh / Frozen : FRESH", )
#         elif self.meat_Q ==2:
#             print("Fresh / Frozen : FROZEN", )

    
    
#     def check_meat_quality(self):
#         if self.meat_Q == 1:
#             print(" The Meat is Fresh   ")

#         elif self.meat_type == 2:
#             print(" The Meat is Not Fresh and it deep-Freezed for more that 24 hr  ")

#         else:
#             print(" 404 ERROR ")

#     def calc_fat_non(self):
#         s = self.fat * self.servings
#         y = s / self.servings
#         print(f"Fat in each serve : {y}gm")


# # main
# while True:
#     print("========================== Recipe Management System ========================== ")
#     print("     1 For Vegetarian Recipe")
#     print("     2 For Non-Vegetarian Recipe")
#     print("     3 For Exit")
#     choice = int(input("Enter 1 / 2 / 3: "))
#     if choice == 1:
#             admin = VegetarianRecipe()
#             print("=================== Vegetarian Recipe ========================")
#             print("         1 For Enter Recipe Details: ")
#             print("         2 For Display Recipe Details: ")
#             print("         3 For Exit: ")
#             veg_ch = int(input("Enter 1 / 2 /  3 :"))
#             if veg_ch == 1 :
#                 print("============== Enter Recipe ================== ")
#                 admin.enter_()
#                 admin.enter_veg()
#             elif veg_ch == 2:
#                 print("========================== Display Recipe ==========================")
#                 admin.display_()
#                 admin.display_veg()
#                 admin.calculate_total_calories()
#                 admin.adjust_spice()
#                 admin.calculate_total_protein()

#             elif veg_ch == 3:
#                 break

#     elif choice == 2:
#             admin = Non_veg()
#             print("=================== Non - Vegetarian Recipe ========================")
#             print("         1 For Enter Non-Vegetarian Recipe Details: ")
#             print("         2 For Display Non-Vegetarian Recipe")
#             print("         3 For Exit: ")
#             Non_veg_ch = int(input("Enter 1 / 2 /  3 :"))
#             if Non_veg_ch == 1 :
#                 print("============== Enter Recipe ================== ")
#                 admin.enter_()
#                 admin.enter_Non()
#             elif Non_veg_ch == 2:
#                 print("========================== Display Recipe ==========================")
#                 admin.display_()
#                 admin.calculate_total_calories()
#                 admin.display_non()
#                 admin.display_()
#                 admin.calculate_total_calories()
#                 admin.calc_fat_non()

#             elif Non_veg_ch == 3:
#                 break
          
#     elif choice == 3:
#         break

# ======================================================================= Que =================================================================================

# War_of_Worlds
# characters={"char_name":{health points:,level:,char_type:(Wizard/Warrior)}}
# weapons={"weapon_name":{"level_of_warrior":points_per_hit}}
# spells={"spell_name":{"level_of_wizard":points_per_hit}}
# As the level of the character increases the points_of_hit will increase for the weapon or spells

#Functions
#game_enter()
#game_display()

# Warrior(War_pf_Worlds))
# Warrior_type=choose your character
# display all the Warrior charcters available 
# user_name=""
# choose_weapon=Choose weapon  (display all weapons to choose from for warrior)
# wh_points= health points accordig to characters
# Functions-
# attack()- whenever this function is called deduce points from opponent's health points as per points_per_hit
# special_attack()- deduce double points from the opponent's health points as per points_per_hit

# Wizard(War_of_Worlds)

# Wizard_type=choose your character
# display all the Warrior charcters available 
# user_name=""
# choose_spell=Choose spell(display all spells to choose from for warrior)
# wi_h_points= health points according to character

# Functions-
# # cast_spell()- whenever this function is called deduce points from opponent's health points as per points_per_hit
# special_spell()- deduce double points from the opponent's health points as per points_per_hit

# Now create two characters and make them fight and display who wins.

characters =  { 
    "Iron-Man" :  {
                    "Health_points" : 100 ,
                    "Level" : 7,
                    "Character Type" : "warrior",
                    "weapons":{"Level Of Warrior": 5,"Points Per Hit":20},
                    },

 
    "Goku" :  {
                    "Health_points" : 100 ,
                    "Level" : 6,
                    "Character Type" : "wizard",
                    "spell":{"Level Of Wizard": 5, "Points Per Hit":20},
 
}}


weapons = {}

# spells={"spell_name":{"level_of_wizard":points_per_hit}}

spells = {}

class War_of_Worlds:
    def __init__(self):

        # character:- 
        self.char_name = ""
        self.health_points = 0
        self.level = 0
        self.char_type = ""
        # Weapon:-
        self.weapon_name = ""
        self.level_of_warrior = 0
        self.points_per_hit_w = 0
        # spells:-
        self.spell_name = ""
        self.level_of_wizard = 0
        self.points_per_hit_s = 0

 
 
    def enter_warrior(self):
        # character:- 
        self.char_name = input("Enter Charecter Name: ")
        self.char_type = "Warrior"
        self.health_points = int(input("Enter Health Level 1-100: "))
        self.level = int(input("Enter Character level(1-10): "))
        # weapons
        self.weapon_name = input("Enter Weapon Name: ")
        self.level_of_warrior = int(input("Enter Level Of Warrior(1-10): "))
        self.points_per_hit_w = int(input("ENter Points per Hit (1-100): "))
        
        weapons[self.weapon_name] = {
                                        "Level Of Warrior" : self.level_of_warrior,
                                        "Points Per Hit" : self.points_per_hit_w,
                                        }
        
        characters[self.char_name] = {     
                                        "Health_points" : self.health_points ,
                                        "Level" : self.level,
                                        "Character Type" : self.char_type,
                                        "weapons": weapons,
                                     }
        # weapons
        

    def enter_wizard(self):
    # character:- 
        self.char_name = input("Enter Charecter Name: ")
        self.char_type = "wizard"
        self.health_points = int(input("Enter Health Level 1-100: "))
        self.level = int(input("Enter Character level(1-10): "))
    
    # spells:-
       
        self.spell_name = input("Enter Spell Name: ")
        self.level_of_wizard = int(input("Enter Level Of Wizard(1-10): "))
        self.points_per_hit_s = int(input("ENter Points per Hit (1-100): "))

        spells[self.spell_name] = {
                                    "Level Of Wizard" : self.level_of_wizard,
                                    "Points Per Hit" : self.points_per_hit_s
                                    }
        
        
        characters[self.char_name] = {     
                                        "Health_points" : self.health_points ,
                                        "Level" : self.level,
                                        "Character Type" : self.char_type,
                                        "spells": spells,
                                     }
        
        

    def display_characters(self):
     print("i'm in display function")
    for character, data in characters.items():
        print("-" * 30)
        print(f"\nCharacter: {character}")
        print(f"  Health Points: {data['Health_points']}")
        print(f"  Level: {data['Level']}")
        print(f"  Character Type: {data['Character Type']}")

        if data['Character Type'] == 'warrior':
            print("  Weapons Attack:")
            for weapon, weapon_data in data['weapons'].items():
                print(f"    Weapon Name: {weapon}")
                print(f"    Level of Warrior: {weapon_data['Level Of Warrior']}")
                print(f"    Points Per Hit: {weapon_data['Points Per Hit']}")

        elif data['Character Type'] == 'wizard':
            print("  Spells Attack:")
            for spell, spell_data in data['spells'].items():
                print(f"    Spell: {spell}")
                print(f"    Level of Wizard: {spell_data['Level Of Wizard']}")
                print(f"    Points Per Hit: {spell_data['Points Per Hit']}")


class Warrior(War_of_Worlds):
    def __init__(self):
        super().__init__()
        self.Warrior_type = ""
        self.user_name = ""
        self.select_weapon = ""
        self.wh_points = 0
        

    def enter_warrior(self):
         self.Warrior_type = input("Enter Warrior Name you want to select: ")
         self.user_name = input("Enter User Name: ")
         self.select_weapon = input("Enter Weapon Name: ")

    def Display_warrior_characters(self):
       for name, attributes in characters.items():
            if attributes['Character Type '] == 'warrior':
                print(f"Character: {name}")
                print(f"Health Points: {attributes['Health_points']}")
                print(f"Level: {attributes['Level']}")
                print(f"Character Type: {attributes['Character Type ']}")
                print("\n")
        
   
    def display_warrior_details(self): 
        print(f"Selected character: {self.Warrior_type} ")
        print(f"User Name: {self.user_name}")
        print(f"Selected Weapon: {self.select_weapon}")


    # attack
    def attack(self):
        pass
    # special_attack
    def special_attack(self):
        pass


    
class Wizard(War_of_Worlds):
    def __init__(self):
          super().__init__()
          self.Wizard_type = ""
          self.user_name = ""
          self.choose_spell = ""

    def Display_Defult_wizard(self):
        for name, attributes in characters.items():
            if attributes["Character Type "] == "wizard":
                print(f"Character: {name}")
                print(f"Health Points: {attributes['Health_points']}")
                print(f"Level: {attributes['Level']}")
                print(f"Character Type: {attributes['Character Type ']}")
                print("\n")


    def enter_wizard(self):
        self.Wizard_type = input("Enter Wizard Type For Select: ")
        self.user_name = input("Enter User Name: ")
        self.choose_spell = input("Enter Spell Word: ")

    def Display_wizard(self):
        pass
        

   
    def cast_spell(self):
        if characters[self.char_name]["Character Type "] == "wizard":
            Wizard_attack = spells[self.spell_name][self.points_per_hit_s] - characters[self.char_name][self.health_points] 
            print("Health After Wizards attack: ", Wizard_attack)
    
    def special_spell(self):
        if characters[self.char_name]["Character Type "] == "wizard":
            Wizard_attack = (spells[self.spell_name][self.points_per_hit_s] * 2) - (characters[self.char_name][self.health_points]) 
            print("Health After Double Wizards attack: ", Wizard_attack)

# main:
admin = War_of_Worlds()
while True:
    print("-------------------- Wellcome To War Of Words ------------------------ ")
    print("1 For Admin Menu")
    print("2 For User ")
    print("3 For Exit")
    choice = int(input("Enter 1 / 2 / 3 : "))


    if choice == 1:
        while True:
            print("--------------------------- Admin Screen -------------------------- ")
            print("     1 For Add Character Warrior ")
            print("     2 For Add Character Wizard ")
            print("     3 For Display Characters ")
            print("     4 For Exit")
            admin_ch = int(input("Enter Choice Number 1 / 2 / 3 / 4 : "))
            print("\n")
            if admin_ch == 1:
                admin.enter_warrior()
            if admin_ch == 2:
                admin.enter_wizard()
            if admin_ch == 3:
                admin.display_characters()
            if admin_ch == 4:
                break
        
    if choice == 2:
        while True:
            print("--------------------------- User Screen -------------------------- ")
            print("1 For Select Character Warrior ")
            print("2 For Select Character wizard ")
            print("2 For Display Selected Characters Info ")
            print("3 For Start Match")
            print("4 For Exit")
            user_ch = int(input("Enter Choice Number 1 / 2 / 3 / 4 : "))
            admin = Warrior()
            if user_ch == 1:
                print("-------------------------- Select Character Warrior --------------------------")
                admin.Display_warrior_characters()
                admin.enter_warrior()
                admin.display_characters()
            admin = Wizard()
            if user_ch == 2:
                print("-------------------------- Select Character Warrior --------------------------")
                admin.Display_Defult_wizard()
                admin.enter_wizard
                admin.Display_wizard()  
                
            if user_ch == 3:
                print("----------------------------- Selected Character --------------------------- ")

            if user_ch == 4:
                break
