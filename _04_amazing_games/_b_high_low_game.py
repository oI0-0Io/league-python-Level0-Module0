from tkinter import messagebox, simpledialog, Tk
import sys
import random

if __name__ == '__main__':
    window = Tk()
    window.withdraw()

    # 1. Change this line to give you a random number between 1 - 100.
    random_num = random.randint(1, 100)

    # 2. Print out the random variable that you made in step #1
    print(random_num)
    # 3. Code a for loop to run steps 4-10, 10 times
    for i in range (10):

        # 4. Ask the user for a guess using a pop-up window, and save their response
        var = simpledialog.askinteger(title='number?', prompt='guess a number from 1 to 100')
        # 5. If the guess is correct
        if var==random_num:
            # 6. Win. Use 'sys.exit(0)' to end the program
            sys.exit(0)

        # 7. if the guess is high
        if var > random_num:
            messagebox.showinfo(message="The number you guessed is too high!")
            # 8. Tell them it's too high
        if var < random_num:
            messagebox.showinfo(message="The number you guessed is too low!")
        # 9. Else if the guess is low
            # 10. Tell them it's too low

    #11. Outside of the loop, tell the user they lost
    messagebox.showinfo(message="You lost")

    window.mainloop()
