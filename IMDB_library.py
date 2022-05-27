# %% [markdown]
# # Import packages

# %%
#Import time package
from datetime import datetime
from dbm.ndbm import library
from pickle import TRUE
import time


#Import Interface builder package
from tkinter import *  
from tkinter import ttk 
from tkinter.ttk import * 

# %% [markdown]
# # Import movie text file and create dictionary

# %%
#Import movie text file and create dictionary
movies_dict = {}
with open("movies.txt") as file:
  for line in file:
    line = line.strip()
    movie_info = line.split(", ")
    for i in range(1, len(movie_info)):
      if movie_info[i] in movies_dict.keys():
        movies_dict[movie_info[i]].add(movie_info[0])
      else:
        movies_dict[movie_info[i]]=set()
        movies_dict[movie_info[i]].add(movie_info[0])
  
  # Print dictionary as a test
  print(movies_dict)

# %% [markdown]
# # Create List of movies

# %%
# create a list of all movies by looping through the movies_dict dictionary
movies_list = []
for movie, actors in movies_dict.items():
    movies_list.append(movie)

# Print list as a test
print(movies_list)

# %% [markdown]
# # Create list of actors

# %%
# creating a sinlge list of all unique actors by looping thorugh the movies_dict dictionary
actors_list = []
for movie, actors in movies_dict.items():
    actors_list.append(actors)
actors_list = list(set([item for sublist in actors_list for item in sublist]))

# Print list as a test 
print(actors_list)

# %% [markdown]
# # Create functions

# %%

#################################################      Function 1      ################################################# 

def FUNCTION():

  # Determine input source. Inputs are taken from interface tickboxes and dropdown menues described in the interface section
  Selection_1 = var1.get()
  Selection_2 = var2.get()
  Selection_3 = var3.get()
  Movie_1 = movie_1.get()
  Movie_2 = movie_2.get()
  actors_1 = movies_dict[Movie_1]
  actors_2 = movies_dict[Movie_2]

  if Selection_1 == 1:

    # Return all actors that played in the selected movies
    all_list = [actors_1, actors_2]
    all_list = [item for sublist in all_list for item in sublist]
    union_list = sorted(list(set(all_list)))
    
    # Return the results in the following format
    label_5.config(text = "Actors who played in the movies " + str(Movie_1) + " & " + str(Movie_2) + " are:\n" + "\n".join(union_list))


  elif Selection_2 == 1:

    # Return actors that starred in both selected movies 
     intersection_list = actors_1.intersection(actors_2)
     intersection_list = sorted(list(set(intersection_list)))

     # Return the results in the following format
     label_6.config(text = "Actors who played in both " + str(Movie_1) + " & " + str(Movie_2) + " are:\n" + "\n".join(intersection_list))


  elif Selection_3 == 1:

      # Return actors that starred in one movie but not the other
       difference_list = (actors_1.difference(actors_2), actors_2.difference(actors_1))
       difference_list = [item for sublist in difference_list for item in sublist]
       difference_list = sorted(list(set(difference_list)))

       # Return the results in the following format
       label_7.config(text = "Actors who played in " +  str(Movie_1) + " but not in " + str(Movie_2) + " and vice versa are:\n" + "\n".join(difference_list))



#################################################      Function 2      ################################################# 

def FUNCTION_2():
  actor_input = actor_1.get()
  movies = []

  # creating an empty list for coactors of the actor
  coactors = []

  # looping through each movie and the corresponding actors within the movie-
  # dictionary and adding all movies to the movies-list that the actor played in

  for movie, actors in movies_dict.items():
    if actor_input in actors:
      movies.append(movie)

  # looping through the movie-list and adding all respective actors as denoted 
  # in the movies-dictionary to the coactors-list

  coactors = [movies_dict[b] for b in movies]

  # reducing the coactors-list of lists to a simple list  

  coactors = [item for sublist in coactors for item in sublist]
  # removing all the dublicates in the coactors-list

  coactors = list(set(coactors))

  # removing the inputed actor from the coactor list

  coactors.remove(actor_input)
  
  # printing the inputed actor name, all the movies he played in as a list and 
  # all his coactors 
  #print(actor_input, "played in", movies, "with the following coactors:")
  #print(*coactors, sep = "\n")

  label_9.config(text = str(actor_input) + " played in " + str(movies) + " with the following coactors:\n" + "\n".join(coactors))
  



# %% [markdown]
# # Greet user

# %%
# Greet the user with different greetings dependent on time of day as test for final use in interface
# Notify the user to use the interface to execute tasks

currentTime = datetime.now()
currentTime.hour

if currentTime.hour < 12:
    print('\033[1;32;40m Good morning! Bom dia! Guten Morgen! Buenos Dias! Bonjour! 早上好!')
elif 12 <= currentTime.hour < 18:
    print('\033[1;32;40m Good afternoon! Boa tarde! Guten Nachmittag! Buenas tardes! Bonjour! 下午好!')
else:
    print('\033[1;32;40m Good evening! Boa noite! Guten Abend! Buenas noches! Bon soir! 晚上好!')
print('Weclome to the IMDB library - Please use interface')

# %% [markdown]
# # Interface

# %%

# Create greeting dependent on time of day

def menu_IF():
    if currentTime.hour < 12:
        return('Good morning!')
    elif 12 <= currentTime.hour < 18:
        return('Good afternoon!')
    else:
        return('Good evening!')

 
# Create interface and name it window
 
window = Tk()

# Create interface size - both vertical and horizontal dimension

window.geometry('800x800')

#Create interface title - IMDB library

window.title("IMDB library")

# Create time entry in hours & minuted format

now_string = time.strftime('%H:%M') 

# Place time label at the top of the interface

label_1 = Label(window, text = now_string)  
label_1.pack(side = TOP, pady = 5)

# Raise the time label to create 3D effect

label_1.configure(relief=RAISED)

# Place time label with greeting to the user dependent on time of day as configured in 

label_2 = Label(window, text=menu_IF())
label_2.pack(side = TOP)

# Create separating line 

sep_1 = ttk.Separator(window,orient='horizontal')
sep_1.pack(fill='x')

# Create label for section 1: selection of movies and return of actor "union/intersection/difference" - title: "list of movies"

label_4 = Label(window, text = "list of movies",)
label_4.pack(side = TOP, pady = 10)

# Create tickbox (1) to select "union" option which returns all actors that starred in the selected selected movies

var1 = IntVar()  
check = Checkbutton(window, text = "Union", variable=var1) 
check.pack(pady = 10) 

# Create tickbox (2) to select "intersection" option which returns actors that starred in both selected movies 

var2 = IntVar()  
check = Checkbutton(window, text = "Intersection", variable=var2) 
check.pack(pady = 10) 

# Create tickbox (3) to select "difference" option which returns actors that starred in one of the selected movies but not the other

var3 = IntVar()  
check = Checkbutton(window, text = "Difference", variable=var3) 
check.pack(pady = 10) 

# Create dropdown menu which lets the user choose from all movies in the selected .txt file

movie_1 = StringVar(window) 
movie_1.set("Select")
h = ttk.Combobox(window, textvariable=movie_1, values=[*movies_list])
h.pack()

# Create second dropdown menu which lets the user choose from all movies in the selected .txt file

movie_2 = StringVar(window) 
movie_2.set("Select")
h = ttk.Combobox(window, textvariable=movie_2, values=[*movies_list])
h.pack()

# Create an execution button which returns a result based onn the selected inputs in the tickboxes and dropdown menus

btn = Button(window, text ="Find", command=FUNCTION) 
btn.pack(pady = 10) 
options_h = StringVar(window)

# Return result in case tickbox (1) was selected

label_5 = Label(window, text = "")
label_5.pack(side = TOP, pady = 2)

# Return result in case tickbox (2) was selected

label_6 = Label(window, text = "")
label_6.pack(side = TOP, pady = 2)

# Return result in case tickbox (3) was selected

label_7 = Label(window, text = "")
label_7.pack(side = TOP, pady = 2)

# Create separating line 

sep_1 = ttk.Separator(window,orient='horizontal')
sep_1.pack(fill='x')

#Create label for section 2: selection of actor to return the movies he starred in along with the costars of these movies - title: "list of actors"

label_8 = Label(window, text = "list of actors")
label_8.pack(side = TOP, pady = 10)

# Create dropdown menu which lets the user choose from all actors in the selected .txt file

actor_1 = StringVar(window) 
actor_1.set("Select")
h = ttk.Combobox(window, textvariable=actor_1, values=[*actors_list])
h.pack()

# Create an execution button which returns a result based onn the selected inputs in the dropdown menu

btn_2 = Button(window, text ="Find", command=FUNCTION_2) 
btn_2.pack(pady = 10) 
options_h = StringVar(window)

# Returnn result

label_9 = Label(window, text = "")
label_9.pack(side = TOP, pady = 10)

# Execute application (lets Tkinter to start running the application). As the name implies it will loop forever until the user exits the window or waits for any events from the user. The mainloop automatically receives events from the window system and delivers them to the application widgets

window.mainloop()


