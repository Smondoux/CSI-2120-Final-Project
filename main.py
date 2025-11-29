import tkinter as tk #import gui toolkit
import tkinter.ttk as ttk #additional gui elements
from tkinter import * #needed for frames(?) not entirely sure why its not included
from course import Course # getting the Course object class

window = tk.Tk() #create a new window
window.geometry("1500x750") #window width x height
window.title("Build your Schedule") #window title displayed at top

#Implementation Note: I'm going to leave the frames colored for the time being to make communication easier. We can (and should) remove
#the coloring before final but I figured it'd be easier to see where the gui is being effected if it was colored. -DS

#creating grid
#columnconfigure(index, how it grows with pane proportionally (higher weight gets more space))
window.columnconfigure(0, weight=1)
window.rowconfigure(0, weight=1)
window.columnconfigure(1, weight=0)
window.rowconfigure(1,weight=0)

outerFrame = Frame(window, bg="light green", width = 1400, height=600) #sorting container // outer most one, others contained
outerFrame.grid(row=0,column=0, sticky="nsew") #formats the grid and makes it so it stretches with the container
outerFrame.rowconfigure(0,weight =1) #top row for schedule pane
outerFrame.rowconfigure(1, weight = 0) #bottom row for bottom pane
outerFrame.columnconfigure(0,weight=1) #left side of the pane, the size that grows
outerFrame.columnconfigure(1, weight=0) #right column
outerFrame.grid_propagate(False) #prevents it from shrinking to fit the smallest itme in it


#innerMainFrame is top left, used for the schedule display
innerMainFrame = Frame(outerFrame, bg="red", width=1000, height=450, padx=20, pady=20)
innerMainFrame.grid(row=0, column=0, sticky="nsew")
innerMainFrame.grid_propagate(False)

#rightVerticalFrame is the right column, used for displaying available classes
rightVerticalFrame = Frame(outerFrame, bg="purple", width = 500, height= 600, borderwidth=1, relief="solid")
rightVerticalFrame.grid(row=0,column=1,rowspan=2, sticky="ns")
rightVerticalFrame.grid_propagate(False)

#bottomHorizontalFrame is the bottom row, used for displaying selected classes
bottomHorizontalFrame= Frame(outerFrame, bg="blue", width=1000, height=300)
bottomHorizontalFrame.grid(row=1, column=0, sticky="ew")
bottomHorizontalFrame.grid_propagate(False)
bottomHorizontalFrame.pack_propagate(False)


# add time labels at the top
for col in range(13):
    label = tk.Label(innerMainFrame, text=f"{8+col}:00", borderwidth=1, relief="solid", width=9)
    label.grid(row=0, column=col+1)

timeCells = {} #array to hold positions of cells on the time table, use this to display what time blocks a class occupies

# storing container section where classes will be displayed
for row in range(6):  # class 1 to 6
    for col in range(13):  # 8am to 8pm
        cell = tk.Label(innerMainFrame, text="", borderwidth=1, relief="solid", width=9, height=4)
        cell.grid(row=row+1, column=col+1)
        timeCells[(row,col)] = cell


#Space holding space in top left corner, otherwise it loses its shape
topLCorner = tk.Label(innerMainFrame, borderwidth=1, relief="solid", width=9)
topLCorner.grid(row=0,column=0,sticky="nsew")
for row in range(6):
    label = tk.Label(innerMainFrame, text="DAY", borderwidth=1, relief="solid", width=9, height=4)
    label.grid(row=row+1, column=0, sticky="nsew")


#change the background color of the label to highlight it
timeCells[(3,5)].configure(bg = "yellow")
timeCells[(3,6)].configure(bg = "yellow")


#Sample Classes
courses = [
    Course("English", "ENG101", days= ["Mon", "Wed"], times=["9:00", "14:00"]),
    Course("Math", "MTH101", days= ["Mon", "Thur"], times=["10:00", "17:00"]),
    Course("Programming", "CSI101", days= ["Wed", "Fri"], times=["11:00", "14:00"]),
    Course("Science", "SCI101", days= ["Tue", "Thur"], times=["13:00", "18:00"])
]

#Display Classes
def display_courses(frame, course_list):
    # Clear existing widgets (Widgets are the elements from tkinter) in the right panel
    for widget in frame.winfo_children():
        widget.destroy()
    
    # Create a label for each course
    for i, course in enumerate(course_list): #enumerate returns index and the Course Object, allows each label to be put in its own row
        label_text = (f"{course.getName()} ({course.getCourseId()})\n" f"Days: {', '.join(course.getDays())}\n" f"Times: {', '.join(course.getTimes())}") #prints data of object
        label = tk.Label(frame, text=label_text, borderwidth=1, relief="solid", justify="left", anchor="w", padx=5, pady=5)
        label.grid(row=i, column=0, sticky="ew", padx=5, pady=5)
        label.bind("<Button-1>", lambda e, c=course: select_Course(c))

    # Make column stretch if frame resizes
    frame.columnconfigure(0, weight=1)

display_courses(rightVerticalFrame, courses)


#On select- Labels for Classes
def select_Course(course):
    print("SELECT WORKS")
    # Clear previous selection in bottom frame
    for widget in bottomHorizontalFrame.winfo_children():
        widget.destroy()
    # Create a label for the selected course
    label_text = (f"{course.getName()} ({course.getCourseId()})\n" f"Days: {', '.join(course.getDays())}\n" f"Times: {', '.join(course.getTimes())}")
    label = tk.Label(bottomHorizontalFrame, text=label_text, borderwidth=1, relief="solid", justify="left", anchor="w", padx=5, pady=5)
    label.pack(side="left", padx=5, pady=5, fill="x", expand=True)
    

window.mainloop() #activates gui event loop
