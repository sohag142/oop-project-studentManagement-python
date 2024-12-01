from tkinter import *
from PIL import Image, ImageTk
from tkinter import ttk, messagebox
import sqlite3


class Report:
    def __init__(self, root):
        self.root = root
        self.root.title("Student Result Management System")
        self.root.geometry("1200x600+200+150")
        self.root.config(bg="white")
        self.root.focus_force()

        # Title
        title = Label(self.root, text="View Student Results", font=("goudy old style", 20, "bold"), bg="orange",
                      fg="#262626").place(x=10, y=15, width=1180, height=50)

        # Search Section
        self.var_search = StringVar()

        lbl_search = Label(self.root, text="Search By Roll No.", font=("goudy old style", 20, "bold"),
                           bg="white").place(x=280, y=100)
        txt_search = Entry(self.root, textvariable=self.var_search, font=("goudy old style", 20),
                           bg="lightyellow").place(x=520, y=100, width=150)
        btn_search = Button(self.root, text="Search", command=self.search, font=("goudy old style", 15, "bold"),
                            bg="#03a9f4", fg="white", cursor="hand2").place(x=680, y=100, width=100, height=35)
        btn_clear = Button(self.root, text="Clear", command=self.clear, font=("goudy old style", 15, "bold"), bg="gray",
                           fg="white", cursor="hand2").place(x=800, y=100, width=100, height=35)
        btn_delete = Button(self.root, text="Delete", command=self.delete, font=("goudy old style", 15, "bold"),
                            bg="red", fg="white", cursor="hand2").place(x=910, y=100, width=100, height=35)

        # Table Frame
        self.result_frame = Frame(self.root, bd=2, relief=RIDGE)
        self.result_frame.place(x=10, y=160, width=1180, height=400)

        scrolly = Scrollbar(self.result_frame, orient=VERTICAL)
        scrollx = Scrollbar(self.result_frame, orient=HORIZONTAL)

        self.result_table = ttk.Treeview(
            self.result_frame,
            columns=("rid", "roll", "name", "course", "marks_ob", "full_marks", "percentage"),
            yscrollcommand=scrolly.set,
            xscrollcommand=scrollx.set,
            style="Custom.Treeview"
        )

        scrollx.pack(side=BOTTOM, fill=X)
        scrolly.pack(side=RIGHT, fill=Y)
        scrollx.config(command=self.result_table.xview)
        scrolly.config(command=self.result_table.yview)

        self.result_table.heading("rid", text="ID")
        self.result_table.heading("roll", text="Roll No.")
        self.result_table.heading("name", text="Name")
        self.result_table.heading("course", text="Course")
        self.result_table.heading("marks_ob", text="Marks Obtained")
        self.result_table.heading("full_marks", text="Total Marks")
        self.result_table.heading("percentage", text="Percentage")
        self.result_table["show"] = "headings"

        self.result_table.column("rid", width=50)
        self.result_table.column("roll", width=100)
        self.result_table.column("name", width=150)
        self.result_table.column("course", width=150)
        self.result_table.column("marks_ob", width=150)
        self.result_table.column("full_marks", width=150)
        self.result_table.column("percentage", width=100)

        self.result_table.pack(fill=BOTH, expand=1)

        # Apply styling to make the table more attractive
        self.style = ttk.Style()
        self.style.theme_use("clam")
        self.style.configure(
            "Custom.Treeview",
            background="#f4f4f4",
            fieldbackground="#e1e1e1",
            foreground="black",
            font=("Arial", 12),
            rowheight=30,
        )
        self.style.configure("Custom.Treeview.Heading", font=("Arial", 14, "bold"), background="#003366",
                             foreground="white")
        self.style.map("Custom.Treeview", background=[("selected", "#ffcc00")])

        # Alternate row colors
        self.result_table.tag_configure('oddrow', background="white")
        self.result_table.tag_configure('evenrow', background="#f2f2f2")

    def search(self):
        con = sqlite3.connect(database="rms.db")
        cur = con.cursor()
        try:
            if self.var_search.get() == "":
                messagebox.showerror("Error", "Roll No. should be required", parent=self.root)
            else:
                cur.execute("SELECT * FROM result WHERE roll=?", (self.var_search.get(),))
                rows = cur.fetchall()
                if rows:
                    self.result_table.delete(*self.result_table.get_children())  # Clear previous results
                    for i, row in enumerate(rows):
                        tag = 'evenrow' if i % 2 == 0 else 'oddrow'
                        self.result_table.insert('', END, values=row, tags=(tag,))
                else:
                    messagebox.showerror("Error", "No record found!!!", parent=self.root)
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to: {str(ex)}")
        finally:
            con.close()

    def clear(self):
        self.var_search.set("")
        self.result_table.delete(*self.result_table.get_children())

    def delete(self):
        con = sqlite3.connect(database="rms.db")
        cur = con.cursor()
        try:
            selected_item = self.result_table.focus()
            if not selected_item:
                messagebox.showerror("Error", "Select a record to delete", parent=self.root)
                return

            item_values = self.result_table.item(selected_item, 'values')
            rid = item_values[0]  # Get the ID from the selected row

            confirm = messagebox.askyesno("Confirm", "Do you really want to delete this result?", parent=self.root)
            if confirm:
                cur.execute("DELETE FROM result WHERE rid=?", (rid,))
                con.commit()
                self.result_table.delete(selected_item)
                messagebox.showinfo("Success", "Result deleted successfully", parent=self.root)
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to: {str(ex)}")
        finally:
            con.close()


if __name__ == "__main__":
    root = Tk()
    obj = Report(root)
    root.mainloop()