import tkinter
from tkinter import*

root=Tk()
root.title("Grade Calculator")
root.geometry("500x400")

def marks_calculate():
    maths= int(maths_value.get())
    science= int(science_value.get())
    language= int(language_value.get())
    computer= int(computer_value.get())
    final = (maths+science+language+computer)
    Label(text=f"{final}", font="arial 20 bold").place(x=250, y=220)
    average= int(final/4)
    Label(text=f"{average}", font="arial 20 bold").place(x=250, y=270)

    if (average>50):
        grade_scored="Pass"
    else:
        grade_scored="Fail"

        Label(text=f"{grade_scored}", font="arial 20 bold").place(x=250, y=320)

sub_1=Label(root, text="Maths", font="arial 20")
sub_1.place(x=50,y=20)
sub_2=Label(root, text="Science", font="arial 20")
sub_2.place(x=50,y=70)
sub_3=Label(root, text="Language", font="arial 20")
sub_3.place(x=50,y=120)
sub_4=Label(root, text="Computer", font="arial 20")
sub_4.place(x=50,y=170)
total_marks= Label(root, text="Total", font="arial 20")
total_marks.place(x=50,y=220)
average_marks= Label(root, text="Average", font="arial 20")
average_marks.place(x=50,y=270)
grade_scored= Label(root, text="Grades", font="arial 20")
grade_scored.place(x=50,y=320)

maths_marks = StringVar()
science_marks = StringVar()
language_marks = StringVar()
computer_marks = StringVar()

maths_value=Entry(root, textvariable= maths_marks, font="arial 20", width=15)
maths_value.place(x=250, y=20)
science_value=Entry(root, textvariable= science_marks, font="arial 20", width=15)
science_value.place(x=250, y=70)
language_value=Entry(root, textvariable= language_marks, font="arial 20", width=15)
language_value.place(x=250, y=120)
computer_value=Entry(root, textvariable= computer_marks, font="arial 20", width=15)
computer_value.place(x=250, y=170)

Button(text="Calculate", font="arial 15", bg="green", bd=5, command=marks_calculate).place(x=50, y=330)
Button(text="Exit", font="arial 15", bg="red", bd=5, width=8, command=lambda: exit()).place(x=350, y=330)

root.mainloop()