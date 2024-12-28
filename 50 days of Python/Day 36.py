## Dummy movie Data

movie = {
    'The Fighter': {
        'Movie Name': 'The Fighter',
        'Movie Genre': 'Action',
        'Movie Language': 'Hindi',
        'Release Year': 2019,
        'Rating': 9.1,
        'On Screen': 'Available On Netflix'
    },
    'Inception': {
        'Movie Name': 'Inception',
        'Movie Genre': 'Science Fiction',
        'Movie Language': 'English',
        'Release Year': 2010,
        'Rating': 9.5,
        'On Screen': 'Available On Amazon Prime'
    },
    'La La Land': {
        'Movie Name': 'La La Land',
        'Movie Genre': 'Musical',
        'Movie Language': 'English',
        'Release Year': 2016,
        'Rating': 8.1,
        'On Screen': 'Available On Hulu'
    }
}

class Movie:
    def __init__(self):
        self.movieName = ""
        self.movieGenre = ""
        self.movieLanguage = ""
        self.releaseYear = ""
        self.rating = 0
        self.onScreen = ""
        self.info_dict = {}

    def entry(self):
        self.movieName = input("Enter Movie Name > ")
        self.movieGenre = input("Enter movie Genre > ")
        self.movieLanguage = input("Enter Movie Language > ")
        self.releaseYear = input("Enter Release Year > ")
        self.rating = float(input("Enter Rating > "))
        self.onScreen = input("On Screen > ")

        self.info_dict = {
            'Movie Name': self.movieName,
            'Movie Genre': self.movieGenre,
            'Movie Language': self.movieLanguage,
            'Release Year': self.releaseYear,
            'Rating': self.rating,
            'On Screen': self.onScreen
        }

        movie[self.movieName] = self.info_dict

    def display(self):
        
        print("="* 45)
        print("All Movies")
        print("-"* 30)
        for movie_name, movie_info in movie.items():
            print(f"\nMovie: {movie_name}")
            for key, value in movie_info.items():
                print(f"{key}: {value}")
            print("-"* 30)
        print("="* 45)
        
    def top(self):
        
        print("="* 45)
        print("Movies with Rating >= 9:")
        print(""* 30)
        for movie_name, movie_info in movie.items():
            if movie_info["Rating"] >= 9:
                print(f"\nMovie: {movie_name}")
                for key, value in movie_info.items():
                    print(f"{key}: {value}")
                print("-"* 30)
        print("="* 45)
        
    def search(self,userInput):
    
        if userInput.isnumeric() :
            
            userInput = int(userInput)
            ## user ne integer diya hain -> Year
            for key,value in movie.items():
                if value['Release Year'] == userInput:
                    
                    print(value["Movie Name"])
                    print(value["Movie Genre"])
                    print(value["Movie Language"])
                    print(value["Release Year"])
                    print(value["Rating"])
                    print(value["On Screen"])
                   
            
            print("Testing")          
        
        elif type(userInput) == str:
            ## user ne string diya hain . means -> Genre
            for key,value in movie.items():
                if value["Movie Genre"] == userInput:
                   
                    print(value["Movie Name"])
                    print(value["Movie Genre"])
                    print(value["Movie Language"])
                    print(value["Release Year"])
                    print(value["Rating"])
                    print(value["On Screen"])
                   
        else:
            print("Search Invalid")
        

## Main    
while True:
    
    print("--- Choose One ---")
    print("1> Admin")
    print("2> User")
    print("3> Exit")

    inputt = int(input("Select 1 or 2 or (3 to Exit) > "))
   
    
    # for admin only 

    if inputt == 1:
        
        while True:
            
            admin = Movie()
    
            print("\n\n------ Choose One  ------")
            print("1> Add Movie")
            print("2> Display Movies")
            print("3> Exit")
            inputt2 = int(input("Select 1,2 > "))
    
            if inputt2 == 1:
                admin.entry()
            elif inputt2 == 2:
                admin.display()
            elif inputt2 == 3:
                print("Wrong Choice ")
                break
        
    # for user only 
    
    elif inputt == 2:    
        
        while True:
        
            user = Movie()
            print("\n\n--- Choose One  ---")
            print("1> Top Movies")
            print("2> Display Movies")
            print("3> Search By Year, Genre")
            print("4> Exit")
            inputt2 = int(input("Select 1,2,3,4 > "))
        
 
        
            if inputt2 == 1:
                user.top()
            elif inputt2 == 2:
                user.display()
                
            elif inputt2 == 3:
                ## Search krna by year or genre
                userValue  = input("Enter Year or Genre > ")
                user.search(userValue)
                            
            elif inputt2 == 4:
                print("Wrong Choice ")
                break
        
         
    ## handles exit thing 
    elif inputt == 3:
        # while loop break krdo :)
        break
