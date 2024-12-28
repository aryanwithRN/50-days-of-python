# -------------------------------------------------------QUE 1 --------------------------------------------------------------------------
# Create a class shape which has attributes Dimensions and Functions enter() to enter dimensions, and display() to display them, 
# # area() and parameters() ,For calc the area of that shape , Parameter of the shape
# dimensions=[ ]
# shape=None
# no_of_dimension=0
class shape:
    def __init__ (self):
        self.shape=None
        self.NOD=0
        self.dimensions = []
    
    def Enter(self):
        self.shape =input(" Enter shape: ").lower()
        self.NOD = int(input("Enter Number of Dimensions: "))
        
        for i in range (0, self.NOD):
            x = int(input("Enter Dimensions:  "))
            self.dimensions.append(x)
        
        # Input for Area / peremeter
        input_ = input("Area(a)/peremeter(p): ").lower()
        
# Check Shapes
    # for Circle:-
        if (self.shape) == "circle":
            # for Area
            if input_ == "a":
                print("==============================")
                self.calc_area_circle()
                print("==============================")
            #  For peremeter
            elif input_ == "p":
                print("==============================")
                self.calc_paramter_circle()
                print("==============================")
               
    # For Square:-
        elif self.shape == "square":
            # For area
             if input_ == "a":
                 print("==============================")
                 self.calc_area_Square
                 print("==============================")
               
            #  For peremeter
             elif input_ == "p":
                print("==============================")
                self.calc_paramter_Square
                print("==============================")
        
    # For Rectangle :-
        elif self.shape == "rectangle":
            # For Area
            if input_ == "a":
             print("==============================")
             self.calc_area_Rectangle
             print("==============================")
    
            #  For peremeter
            elif input_ == "p":
                print("==============================")
                self.calc_peremeter_Rectangle
                print("==============================")
                
# TO Display the inputs and result
    
    def Display(self):

        print(f"The shape is:- {self.shape}")
        print(f"The Dimensions are:-  {self.NOD}")
        print("===================================")
        # print(f"{self.dimensions}")


# circle Fn For Area and Peremeter  :-
    def calc_paramter_circle(self):
        x = 2 * 3.14 * self.dimensions[0]
        print(f"The peremeter of Circle :- {x}")
    
    def calc_area_circle(self):
        x = 3.14* self.dimensions[0] **2
        print(f"The Area of Square :-  {x}")
        

# Square Fn For Area and Peremeter  :-
    def calc_paramter_Square(self):
        x = 4 * self.dimensions[0]
        print(f"The peremeter of Square :- {x}")
    def calc_area_Square(self):
        area = self.dimensions[0] * self.dimensions[0] 
        print(f"The Area of Square :-  {area}")

# Rectangle Fn For Area and Peremeter :-
    def calc_area_Rectangle(self):
        area = self.dimensions[0] * self.dimensions [1]
        print(f"The area of Rectangle :-  {area}")
    def calc_peremeter_Rectangle(self):
        x = 2 * (self.dimensions[0]+ self.dimensions[1])
        print(f"The peremeter of Rectangle :-  {x}")



# Main
user = shape()
user.Enter()
user.Display()

