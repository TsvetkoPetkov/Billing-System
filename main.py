from tkinter import *

# ROOT
root = Tk()

root.title("Billing System")
root.geometry('1550x725')
root.iconbitmap('images/icon.ico')

# HEADING LABEL
heading_label = Label(root, text="Billing System", font=("times new roman", 30, 'bold'),
                      bg='seashell3', fg='black', bd=10, relief=RIDGE)
heading_label.pack(fill=X, pady=10)

# CUSTOMER INFO LABEL FRAME

customer_info = LabelFrame(root, text="Customer Information", font=("times new roman", 15, 'bold'),
                           bg='seashell3', fg='black', bd=10, relief=RIDGE)
customer_info.pack(fill=X)

# NAME LABEL

name_label = Label(customer_info, text="Name", font=("times new roman", 15, 'bold'),
                   bg='seashell3', fg='black')
name_label.grid(row=0, column=0, padx=20, pady=2)

name_entry = Entry(customer_info, font=('arial', 15), bd=5, width=18)
name_entry.grid(row=0, column=1, padx=10)

# PHONE LABEL

phone_label = Label(customer_info, text="Phone Number", font=("times new roman", 15, 'bold'),
                    bg='seashell3', fg='black')
phone_label.grid(row=0, column=2, padx=20, pady=2)

phone_entry = Entry(customer_info, font=('arial', 15), bd=5, width=18)
phone_entry.grid(row=0, column=3, padx=10)

# BILL NUMBER LABEL

bill_number_label = Label(customer_info, text="Bill Number", font=("times new roman", 15, 'bold'),
                          bg='seashell3', fg='black')
bill_number_label.grid(row=0, column=4, padx=20, pady=2)

bill_number_entry = Entry(customer_info, font=('arial', 15), bd=5, width=18)
bill_number_entry.grid(row=0, column=5, padx=10)

# SEARCH BUTTON

search_button = Button(customer_info, text='SEARCH', font=('arial', 12), bd=4)
search_button.grid(row=0, column=6, padx=30, pady=8)

# PRODUCTS FRAME

products_frame = Frame(root)
products_frame.pack(pady=10)

# SALADS FRAME
salads_frame = LabelFrame(products_frame, text="Salads", font=("times new roman", 15, 'bold'),
                         bg='seashell3', fg='black', bd=10, relief=RIDGE)
salads_frame.grid(row=0, column=0)

# GARDEN AVOCADO LABEL
shopska_label = Label(salads_frame, text="Garden Avocado", font=("times new roman", 15, 'bold'),
                      bg='seashell3', fg='black')
shopska_label.grid(row=0, column=1, padx=10, pady=9, sticky="w")

shopska_entry = Entry(salads_frame, font=('arial', 15), bd=5, width=10)
shopska_entry.grid(row=0, column=2, padx=10, pady=9)

# BEET SALAD LABEL
shopska_label = Label(salads_frame, text="Beet Salad", font=("times new roman", 15, 'bold'),
                      bg='seashell3', fg='black')
shopska_label.grid(row=1, column=1, padx=10, pady=9, sticky="w")

shopska_entry = Entry(salads_frame, font=('arial', 15), bd=5, width=10)
shopska_entry.grid(row=1, column=2, padx=10, pady=9)

# CAESAR LABEL
shopska_label = Label(salads_frame, text="Caesar Salad", font=("times new roman", 15, 'bold'),
                      bg='seashell3', fg='black')
shopska_label.grid(row=2, column=1, padx=10, pady=9, sticky="w")

shopska_entry = Entry(salads_frame, font=('arial', 15), bd=5, width=10)
shopska_entry.grid(row=2, column=2, padx=10, pady=9)

# GREEK LABEL
shopska_label = Label(salads_frame, text="Greek Salad", font=("times new roman", 15, 'bold'),
                      bg='seashell3', fg='black')
shopska_label.grid(row=3, column=1, padx=10, pady=9, sticky="w")

shopska_entry = Entry(salads_frame, font=('arial', 15), bd=5, width=10)
shopska_entry.grid(row=3, column=2, padx=10, pady=9)

# ARUGULA LABEL
shopska_label = Label(salads_frame, text="Arugula Salad", font=("times new roman", 15, 'bold'),
                      bg='seashell3', fg='black')
shopska_label.grid(row=4, column=1, padx=10, pady=9, sticky="w")

shopska_entry = Entry(salads_frame, font=('arial', 15), bd=5, width=10)
shopska_entry.grid(row=4, column=2, padx=10, pady=9)

# SHOPSKA LABEL
shopska_label = Label(salads_frame, text="Shopska Salad", font=("times new roman", 15, 'bold'),
                      bg='seashell3', fg='black')
shopska_label.grid(row=5, column=1, padx=10, pady=9, sticky="w")

shopska_entry = Entry(salads_frame, font=('arial', 15), bd=5, width=10)
shopska_entry.grid(row=5, column=2, padx=10, pady=9)

# MEALS FRAME

meals_frame = LabelFrame(products_frame, text="Meals", font=("times new roman", 15, 'bold'),
                         bg='seashell3', fg='black', bd=10, relief=RIDGE)
meals_frame.grid(row=0, column=1)

# HAPPY CHICKEN LABEL
happy_chicken_label = Label(meals_frame, text="Happy Chicken", font=("times new roman", 15, 'bold'),
                            bg='seashell3', fg='black')
happy_chicken_label.grid(row=0, column=0, padx=10, pady=9, sticky="w")

happy_chicken_entry = Entry(meals_frame, font=('arial', 15), bd=5, width=10)
happy_chicken_entry.grid(row=0, column=1, padx=10, pady=9)

# CRISPY CHICKEN LABEL
beef_steaks_label = Label(meals_frame, text="Crispy Chicken", font=("times new roman", 15, 'bold'),
                          bg='seashell3', fg='black')
beef_steaks_label.grid(row=1, column=0, padx=10, pady=9, sticky="w")

beef_steaks_entry = Entry(meals_frame, font=('arial', 15), bd=5, width=10)
beef_steaks_entry.grid(row=1, column=1, padx=10, pady=9)

# BEEF STEAKS LABEL
beef_steaks_label = Label(meals_frame, text="Beef Steak", font=("times new roman", 15, 'bold'),
                          bg='seashell3', fg='black')
beef_steaks_label.grid(row=2, column=0, padx=10, pady=9, sticky="w")

beef_steaks_entry = Entry(meals_frame, font=('arial', 15), bd=5, width=10)
beef_steaks_entry.grid(row=2, column=1, padx=10, pady=9)

# ASIAN RIBS LABEL
beef_steaks_label = Label(meals_frame, text="Asian Ribs", font=("times new roman", 15, 'bold'),
                          bg='seashell3', fg='black')
beef_steaks_label.grid(row=3, column=0, padx=10, pady=9, sticky="w")

beef_steaks_entry = Entry(meals_frame, font=('arial', 15), bd=5, width=10)
beef_steaks_entry.grid(row=3, column=1, padx=10, pady=9)

# PORK MEATBALLS LABEL
beef_steaks_label = Label(meals_frame, text="Pork Meatballs", font=("times new roman", 15, 'bold'),
                          bg='seashell3', fg='black')
beef_steaks_label.grid(row=4, column=0, padx=10, pady=9, sticky="w")

beef_steaks_entry = Entry(meals_frame, font=('arial', 15), bd=5, width=10)
beef_steaks_entry.grid(row=4, column=1, padx=10, pady=9)

# BEEF STEAKS LABEL
beef_steaks_label = Label(meals_frame, text="Beef Steaks", font=("times new roman", 15, 'bold'),
                          bg='seashell3', fg='black')
beef_steaks_label.grid(row=5, column=0, padx=10, pady=9, sticky="w")

beef_steaks_entry = Entry(meals_frame, font=('arial', 15), bd=5, width=10)
beef_steaks_entry.grid(row=5, column=1, padx=10, pady=9)

# DRINKS FRAME

drinks_frame = LabelFrame(products_frame, text="Cold Drinks", font=("times new roman", 15, 'bold'),
                          bg='seashell3', fg='black', bd=10, relief=RIDGE)
drinks_frame.grid(row=0, column=2)

# COLA LABEL

cola_label = Label(drinks_frame, text="Cola", font=("times new roman", 15, 'bold'),
                   bg='seashell3', fg='black')
cola_label.grid(row=0, column=0, padx=10, pady=9, sticky="w")

cola_entry = Entry(drinks_frame, font=('arial', 15), bd=5, width=10)
cola_entry.grid(row=0, column=1, padx=10, pady=9)

# PEPSI LABEL

pepsi_label = Label(drinks_frame, text="Pepsi", font=("times new roman", 15, 'bold'),
                    bg='seashell3', fg='black')
pepsi_label.grid(row=1, column=0, padx=10, pady=9, sticky="w")

pepsi_entry = Entry(drinks_frame, font=('arial', 15), bd=5, width=10)
pepsi_entry.grid(row=1, column=1, padx=10, pady=9)

# ORANGE JUICE LABEL

orange_juice_label = Label(drinks_frame, text="Orange Juice", font=("times new roman", 15, 'bold'),
                           bg='seashell3', fg='black')
orange_juice_label.grid(row=2, column=0, padx=10, pady=9, sticky="w")

orange_juice_entry = Entry(drinks_frame, font=('arial', 15), bd=5, width=10)
orange_juice_entry.grid(row=2, column=1, padx=10, pady=9)

# APPLE JUICE LABEL

apple_juice_label = Label(drinks_frame, text="Apple Juice", font=("times new roman", 15, 'bold'),
                          bg='seashell3', fg='black')
apple_juice_label.grid(row=3, column=0, padx=10, pady=9, sticky="w")

apple_juice_entry = Entry(drinks_frame, font=('arial', 15), bd=5, width=10)
apple_juice_entry.grid(row=3, column=1, padx=10, pady=9)

# CHERRY JUICE LABEL

cherry_juice_label = Label(drinks_frame, text="Cherry Juice", font=("times new roman", 15, 'bold'),
                           bg='seashell3', fg='black')
cherry_juice_label.grid(row=4, column=0, padx=10, pady=9, sticky="w")

cherry_juice_entry = Entry(drinks_frame, font=('arial', 15), bd=5, width=10)
cherry_juice_entry.grid(row=4, column=1, padx=10, pady=9)

# LEMONADE LABEL

lemonade_label = Label(drinks_frame, text="Lemonade", font=("times new roman", 15, 'bold'),
                       bg='seashell3', fg='black')
lemonade_label.grid(row=5, column=0, padx=10, pady=9, sticky="w")

lemonade_entry = Entry(drinks_frame, font=('arial', 15), bd=5, width=10)
lemonade_entry.grid(row=5, column=1, padx=10, pady=9)


# BILL FRAME

bill_frame = Frame(products_frame, bd=10, relief=RIDGE)
bill_frame.grid(row=0, column=3)

bill_area_label = Label(bill_frame, text="Bill", font=("times new roman", 15, 'bold'), bd=7, relief=RIDGE)
bill_area_label.pack(fill=X)

scrollbar = Scrollbar(bill_frame, orient=VERTICAL)
scrollbar.pack(side=RIGHT, fill=Y)

text_area = Text(bill_frame, height=18, width=65, yscrollcommand=scrollbar.set)
text_area.pack()
scrollbar.config(command=text_area.yview)

root.mainloop()
