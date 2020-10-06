from tkinter import Label, Entry, Button, Tk
from joblib import load

model = load('Iris_model.joblib')
root = Tk()

def result():
    s1 = sepalLength.get()
    s2 = sepalWidth.get()
    p1 = petalLength.get()
    p2 = petalWidth.get()
    
    result = model.predict([[ float(s1),float(s2), float(p1), float(p2) ]]).argmax(axis=1)
    result = list(result)
    text = 'The flower is '
    if result[0] == 0:
        result_label = Label(root, text=text+'Iris-setosa')
    elif result[0] == 1:
        result_label = Label(root, text=text+'Iris-versicolor')
    elif result[0] == 2:
        result_label = Label(root, text=text+'Iris-virjinica')
    else:
        result_label = Label(root, text='Not found')
    result_label.grid(row=5,column=0,columnspan=2)
        
    
sepalLength_Label = Label(root, text='Sepal Length')
sepalWidth_Label = Label(root, text='Sepal Width')
petalLength_Label = Label(root, text='Petal Length')
petalWidth_Label = Label(root, text='Petal Width')

sepalLength_Label.grid(row=0,column=0)
sepalWidth_Label.grid(row=1,column=0)
petalLength_Label.grid(row=2,column=0)
petalWidth_Label.grid(row=3, column=0)

sepalLength = Entry(root, width = 50)
sepalWidth = Entry(root, width = 50)
petalLength = Entry(root, width = 50)
petalWidth = Entry(root, width = 50)

sepalLength.grid(row=0,column=1)
sepalWidth.grid(row=1,column=1)
petalLength.grid(row=2,column=1)
petalWidth.grid(row=3, column=1)

submit = Button(root, text='find folwer', command=result)
submit.grid(row=4,column=0)


root.mainloop()