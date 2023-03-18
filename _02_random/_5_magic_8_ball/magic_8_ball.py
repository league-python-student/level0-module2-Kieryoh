import random
from tkinter import messagebox, Tk, simpledialog

if __name__ == '__main__':
    window = Tk()
    window.withdraw()

    # TODO Get the user to enter a question for the 8 ball to answer
    simpledialog.askstring(title='t', prompt='What is your question?')

    # Make a variable and initialize it to a random number between 0 and 3
    random_num = random.randint(0, 3)

    # If the random number is 0
    if random_num == 0:
        messagebox.showinfo(message='Yes.')
    elif random_num == 1:
        messagebox.showinfo(message='No.')
    elif random_num == 2:
        messagebox.showinfo(message='Maybe you should ask Google?')
    elif random_num == 3:
        messagebox.showinfo(message="I don't know.")

        # tell the user "Yes"

    # If the random number is 1

        # tell the user "No"

    # If the random number is 2

        # tell the user "Maybe you should ask Google?"

    # If the random number is 3

        # write your own answer
