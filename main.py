import os
import tkinter
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip


class PasswordManager():

    def __init__(self):
        self.reps = 0
        self.window = None
        self.canvas = None
        self.pw_image = None
        self.web_entry = None
        self.email_entry = None
        self.pw_entry = None
        self.gen_button = None
        self.add_button = None
        self.current_dir = os.path.dirname(os.path.abspath(__file__))
        self.setup_ui()

    # ---------------------------- UI SETUP ------------------------------- #

    def setup_ui(self):
        """ Setup the User Interface. """
        self._setup_window()
        self._setup_canvas()
        self._setup_labels()
        self._setup_user_inputs()
        self._setup_buttons()

    def _setup_window(self):
        """ Setup the window. """
        self.window = tkinter.Tk()
        self.window.title("Password Manager")
        self.window.config(padx=50, pady=50, bg="white")

    def _setup_canvas(self):
        """ Setup Canvas with password manager image and also the timer text. """
        self.canvas = tkinter.Canvas(width=200, height=200, bg="white", highlightthickness=0)
        image_path = os.path.join(self.current_dir, "logo.png")
        self.pw_image = tkinter.PhotoImage(file=image_path)
        self.canvas.create_image(100, 100, image=self.pw_image)
        self.canvas.grid(column=1, row=0)

    def _setup_labels(self):
        """ Setup Website, username and password labels. """
        font_name = "Space Grotesk"
        website_label = tkinter.Label(text="Website:", bg="white", font=(font_name, 11))
        website_label.grid(row=1, column=0)
        email_label = tkinter.Label(text="Email/Username:", bg="white", font=(font_name, 11))
        email_label.grid(row=2, column=0)
        pw_label = tkinter.Label(text="Password:", bg="white", font=(font_name, 11))
        pw_label.grid(row=3, column=0)

    def _setup_user_inputs(self):
        """ Setup Input boxes from user for Website, username and password. """
        self.web_entry = tkinter.Entry(width=51)
        self.web_entry.grid(row=1, column=1, columnspan=2)
        # Set the cursor at website entry
        self.web_entry.focus()
        self.email_entry = tkinter.Entry(width=51)
        self.email_entry.grid(row=2, column=1, columnspan=2)
        # Set the default value
        self.email_entry.insert(0, "user@email.com")
        self.pw_entry = tkinter.Entry(width=33)
        self.pw_entry.grid(row=3, column=1)

    def _setup_buttons(self):
        """ Setup 'Generate Password' and 'Add' Buttons. """
        self.gen_button = tkinter.Button(text="Generate Password", width=14,
                                         command=self.generate_password)
        self.gen_button.grid(row=3, column=2)
        self.add_button = tkinter.Button(text="Add", width=43, command=self.save_data)
        self.add_button.grid(row=4, column=1, columnspan=2)

    # ---------------------------- PASSWORD GENERATOR ------------------------------- #

    def generate_password(self):
        """ Generates a password that includes 8-10 letters, 2-4 numbers and 2-4 symbols
        or special characters. Clear the password input box and insert the generated
        password. Also, copy the pasword to clipboard using pyperclip library.
        This method is used when 'Generate Password' button is clicked.  """
        #Password Generator Project
        letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
                   'n','o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
                   'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
                   'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
        numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

        pwd_letters =  [choice(letters) for _ in range(randint(8, 10))]
        pwd_numbers =  [choice(numbers) for _ in range(randint(2, 4))]
        pwd_symbols =  [choice(symbols) for _ in range(randint(2, 4))]
        password_list = pwd_letters + pwd_numbers + pwd_symbols
        shuffle(password_list)
        password = ''.join(password_list)

        self.pw_entry.delete(0, tkinter.END)
        self.pw_entry.insert(0, password)
        pyperclip.copy(password)

    # ---------------------------- SAVE PASSWORD ------------------------------- #

    def save_data(self):
        """ If all the users inputs are valid, saves the data (website, email/username
        and password) to 'data.txt' file and clears the entries or the user inputs.
        This method is used when 'Add' button is clicked. """
        # Concatenate user inputs separated by ' | ' and by adding a new line at the end
        website = self.web_entry.get()
        email = self.email_entry.get()
        pw = self.pw_entry.get()
        data = ' | '.join([website, email, pw]) + '\n'

        if website and email and pw:
            msg = f"These are the details entered:\nE-mail: {email}\nPassword: {pw}\n\nIs it OK to save?"
            is_ok = messagebox.askokcancel(title=website, message=msg)
            if is_ok:
                # Store data in the file
                data_file_path = os.path.join(self.current_dir, "data.txt")
                with open(data_file_path, "a") as file:
                    file.write(data)

                # Clear website and password user inputs
                self.web_entry.delete(0, tkinter.END)
                self.pw_entry.delete(0, tkinter.END)
                # messagebox.showinfo(title="Add", message="OK")
        else:
            messagebox.showinfo(title="Oops", message="Please don't leave any field empty.")


# ---------------------------- Main Method ------------------------------- #


def main():
    """ Main method to execute Pomodoro app. """
    pw_manager = PasswordManager()
    pw_manager.window.mainloop()


if __name__ == "__main__":
    main()
