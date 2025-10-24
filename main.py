# import numpy as np
#
# # Generate random data (100 numbers between 1 and 100)
# data = np.random.randint(1, 11, size=10)
#
# # Print the data
# print("📊 Generated Data:")
# print(data)
#
# # Calculate basic stats
# mean = np.mean(data)
# median = np.median(data)
# std_dev = np.std(data)
# max_val = np.max(data)
# min_val = np.min(data)
#
# data2d=np.random.randint(1, 100, size=(1, 2))
# print(data2d)
#
# # Print analysis results
# print("\n📈 Data Analysis Results:")
# print(f"Mean (Average): {mean:.2f}")
# print(f"Median: {median}")
# print(f"Standard Deviation: {std_dev:.2f}")
# print(f"Maximum Value: {max_val}")
# print(f"Minimum Value: {min_val}")
# print(f"Sum of the data {np.sum(data)}")
# # Sort the data
# sorted_data = np.sort(data)
# print("\n🔢 Sorted Data:")
# print(sorted_data)
#
#
# import pandas as pd
#
#
# Load the CSV file
# data = pd.read_csv("expenses.csv")
# data["Date"] = pd.to_datetime(data["Date"])
# # Display all data
# print("💰 Expense Data:")
# print(data)
# print("-" * 40)
#
# # Basic info
# total_expense = data["Amount"].sum()
# average_expense = data["Amount"].mean()
# max_expense = data["Amount"].max()
# min_expense = data["Amount"].min()
#
# print("📊 Summary:")
# print(f"Total Expense: ${total_expense:.2f}")
# print(f"Average Expense: ${average_expense:.2f}")
# print(f"Highest Expense: ${max_expense:.2f}")
# print(f"Lowest Expense: ${min_expense:.2f}")
# print("-" * 40)
#
# # Category-wise totals
# print("📂 Expense by Category:")
# # Show only Food expenses
#
#
# Non_food = data[(data["Category"]!= "Food") & (data["Amount"]>50)]
# print(Non_food)
# total_expesnes = data["Amount"].sum
# filtered = data[(data["Date"] > "2025-10-02") & (data["Date"] < "2025-10-05")]
# print(filtered)
# max_row = filtered[filtered["Amount"] == filtered["Amount"].max()]
# print(max_row)
#
# category_totals=data.groupby("Category")["Amount"].sum()
# print(category_totals)
# food_expenses = data[(data["Category"]=="Food") & (data["Amount"]<30)]
# print(food_expenses)
#
# class information:
#     def __init__ (self, name , age, sex):
#         print("YOYO Honey SIngh")
#         self.name=name
#         self.age=age
#         self.sex=sex
#     def info (self):
#         print(f"({self.name} is {self.age} years old and he is {self.sex}")
#
# a=information("Muna", 12, "Female")
# b=information("Bijay", 18, "Male")
# a.info()
# b.info()
#
# class MyClass :
#     def __init__ (self , value) :
#         self._value = value
#
#     def hello (self) :
#         print ( f"Value is {self._value}" )
#
#     @property
#     def ten_value (self) :
#         return 10 * self._value
#
#     @ten_value.setter
#     def ten_value (self , new_value) :
#         self._value = new_value / 10
# obj = MyClass ( 10 )
# obj.ten_value = 57
# print ( obj.ten_value )
# obj.hello ( )
#
# class Car:
#     def __init__(self, brand, price):
#         self.price = price
#         self.brand = brand
#     def show(self):
#             print(f"My car is {self.brand} and its price is {self.price}")
#
# mycar = Car("Toyota", "2000")
# print(mycar.brand)
# print(mycar.price)
# mycar.show()
#
#
# def greet (fx) :
#     def mfx (*args , **kwargs) :
#         print ( "Good Morning" )
#         fx ( *args , **kwargs )
#         print ( "Thank You" )
#
#     return mfx
# class toy:
#     def __init__(self, Name, Location, age):
#         self.Name=Name
#         self.Location=Location
#         self.age=age
#     @greet
#     def hello(self):
#         print(f"My Toy's name is {self.Name} and He Lives in {self.Location} and its age is{self.age}")
#
#
#
#
# Mytoy=toy("Hotwheels", "Scarborough", 12)
#
# Mytoy.hello()
#
# class data:
#     def __init__(self, Name, Age, Sex):
#         self.Name=Name
#         self.Age=Age
#         self.Sex=Sex
#
#     def info(self):
#      print(f"My name is {self.Name} and My age is {self.Age} and My Gender is {self.Sex}")
#
#
# myobj=data("pawan", 12, "Male")
# myobj.info()

# import mysql.connector
#
# # --- Connect to MySQL once at the top ---
# conn = mysql.connector.connect(
#     host="localhost",
#     user="root",
#     password="@Manutddevil7",   # your MySQL password
#     database="Data"             # your MySQL database name
# )
#
# cursor = conn.cursor()
# class Bank:
#     def __init__(self, Name, Balance):
#         self.Name=Name
#         self.Balance=Balance
#         print(f"Nice You have a account with us and You have {self.Balance}$ in your account")
#
#
#
#
#
#
#
#
#     def Deposit(self):
#         p="y"
#         while p == "y":
#             Deposit_Amount=int(input("Enter the amount You want to deposit:  "))
#             self.Balance = self.Balance + Deposit_Amount
#             print(f"Amount is added in {self.Name} Account Balance Your New Balance is {self.Balance}")
#             Again = input ( "Do you want deposit again Type Y to Proceed and N for end this Y/N: " ).lower ( )
#             if Again=="y":
#                 continue
#             elif Again=="n":
#                 print("Thank You for the deposit")
#                 break
#             else:
#                 print("You entered inavild Answer Please Choose Y or N")
#
#
#
#     def Withdrawl(self):
#             if self.Balance>0:
#                 Withdrawl_Amount=int(input("Enter The amount You want to withdraw from Your Account:  "))
#             else:
#                 print ( "You Dont Have Sufficient balance" )
#             if Withdrawl_Amount>self.Balance:
#                         print(f"Your Account has not Sufficient balance to withdraw {Withdrawl_Amount} ")
#             else:
#                         self.Balance = self.Balance - Withdrawl_Amount
#                         print(f"A Amount has been Withdrawn Form Account Name {self.Name} and Your New Balance is {self.Balance}")
#
#     def Check (self) :
#         ask = input (f"Do you want any service from us like Deposit or Withdraw or Check balance IF you want to deposit just say 'Deposit' & If you want to withdraw just say 'Withdraw' and You want to check Balance on your account just write check:  " ).lower ( )
#
#         if ask == "deposit" :
#             self.Deposit()
#         elif ask=="withdraw":
#             self.Withdrawl()
#         elif ask=="check":
#             print(f"Your account has {self.Balance}$")
#         else:
#             print("You gave a inavlid response please try again and give a valid resposne")
#
# p = "y"
# while p == "y":
#     Account_name = input(
#         "Hello Customer! This is Scotia Bank.\n"
#         "Do you have an account with us?\n"
#         "If yes, please tell me the name on the account:\n"
#         "Type 'Quit' to stop the service: "
#     ).lower()
#
#     if Account_name == "quit":
#         break
#
#     # ✅ Database query goes here (not inside the quit condition)
#     cursor.execute("SELECT Name, Balance FROM BankDatabase WHERE LOWER(Name) = %s", (Account_name,))
#     result = cursor.fetchone()
#
#     if result:
#         customer = Bank(result[0], result[1])
#         customer.Check()
#     else:
#         print("❌ Sorry, we couldn’t find an account under that name.")
#
# # ✅ Close the connection after the loop finishes
# cursor.close()
# conn.close()

import mysql.connector

#
def connect_database():
    try:
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="@Manutddevil7",
            database="BankDataBase"
        )
        print("✅ Connected to MySQL Database successfully!\n")
        return conn
    except mysql.connector.Error as err:
        print(f" Database connection failed: {err}")
        return None


class BankAnalytics:
    def __init__(self, conn):
        self.conn=conn
        self.cursor=conn.cursor()

    def fetch_all(self):
        self.cursor.execute("SELECT * FROM BankDataBase")
        return self.cursor.fetchall()

    def show_all_customer(self):
        print("\n ALL CUSTOMERS")
        self.cursor.execute("SELECT Name, Balance, Transactions, WithdrawFrequency, AccountAgeMonths, Salary, Region FROM BankDataBase")
        for Name, Balance, Transactions, WithdrawFrequency, AccountAgeMonths, Salary, Region  in self.cursor.fetchall():
            print(f"{Name} -- {Balance} -- {Transactions} -- {WithdrawFrequency} -- {AccountAgeMonths} -- {Salary} -- {Region}")
        print()

    def richest_customer(self):
        self.cursor.execute("SELECT Name, Balance FROM BankDataBase ORDER BY Balance DESC LIMIT 1")
        name , balance = self.cursor.fetchone ( )
        print ( f" Richest Customer: {name} with ${balance}" )

    def average_balance(self):
        self.cursor.execute("SELECT AVG(Balance) FROM BankDataBase")
        avg = self.cursor.fetchone()[0]
        print(f" Average Balance is ${round(avg, 2)}")

    def low_balance_alerts(self):
        print ( "\n Customers with Low Balance (< $200):" )
        self.cursor.execute("SELECT Name, Balance FROM BankDataBase WHERE Balance < 200")
        results = self.cursor.fetchall ( )
        if results :
            for name , balance in results :
                print ( f" {name} — ${balance}" )
        else :
            print ( " No customers with low balance!" )
        print ( )

    def region_summary(self):
        print ( "\n Average Balance by Region:" )
        self.cursor.execute("SELECT Region, Round(AVG(Balance), 2) FROM BankDataBase GROUP BY Region ")
        for region, avg in self.cursor.fetchall():
            print ( f"{region}: ${avg}" )
        print ( )

    def risk_detection (self) :
        print ( "\n Financial Risk Detection (AI-style rule):" )
        query = """
        SELECT Name, Balance, Salary, WithdrawFrequency
        FROM BankDatabase
        WHERE Balance < 300 AND WithdrawFrequency > 6
        """
        self.cursor.execute ( query )
        results = self.cursor.fetchall ( )
        if results :
            for name , bal , sal , freq in results :
                print ( f"️ {name} may be at financial risk: balance ${bal}, salary ${sal}, withdrawals {freq}/month" )
        else :
            print ( " No high-risk accounts detected!" )
        print ( )

    def close_cursor (self) :
        self.cursor.close ( )

class BankOperations:
    def __init__(self, conn):
        self.conn = conn
        self.cursor = conn.cursor()

    def deposit (self , name , amount) :
        self.cursor.execute ( "SELECT Balance FROM BankDatabase WHERE Name = %s" , (name ,) )
        result = self.cursor.fetchone ( )

        if result is None :
            print ( f" No account found for '{name}'. Please check the name." )
            return

        new_balance = result[ 0 ] + amount
        self.cursor.execute ( "UPDATE BankDatabase SET Balance = %s WHERE Name = %s" , (new_balance , name) )
        self.conn.commit ( )

        print ( f" Deposit successful! New balance for {name} is ${new_balance}." )

    def withdraw(self, name, amount):
        self.cursor.execute("SELECT Balance FROM BankDatabase WHERE LOWER(Name) = %s", (name.lower(),))
        result = self.cursor.fetchone()

        if not result:
            print(" Account not found.\n")
            return

        current_balance = result[0]
        if amount > current_balance:
            print(f" Insufficient funds! You only have ${current_balance}.\n")
            return

        query = "UPDATE BankDatabase SET Balance = Balance - %s WHERE LOWER(Name) = %s"
        self.cursor.execute(query, (amount, name.lower()))
        self.conn.commit()

        new_balance = current_balance - amount
        print(f" Withdrawn ${amount} successfully! New balance: ${new_balance}\n")

    def close_cursor(self):
        self.cursor.close()



def main():
    conn = connect_database()
    if not conn:
        return

    analytics = BankAnalytics(conn)
    operations = BankOperations(conn)

    while True:
        print("""
===========================
     SMART BANK SYSTEM
===========================
1. Show all customers
2. Show richest customer
3. Show average balance
4. Low balance alerts
5. Regional summary
6. Financial risk detection
7. Deposit money
8. Withdraw money
9. Exit
""")
        choice = input(" Enter your choice (1–9): ").strip()

        if choice == "1":
            analytics.show_all_customer()
        elif choice == "2":
            analytics.richest_customer()
        elif choice == "3":
            analytics.average_balance()
        elif choice == "4":
            analytics.low_balance_alerts()
        elif choice == "5":
            analytics.region_summary()
        elif choice == "6":
            analytics.risk_detection()
        elif choice == "7":
            name = input("Enter customer name: ")
            amount = int(input("Enter deposit amount: "))
            operations.deposit(name, amount)
        elif choice == "8":
            name = input("Enter customer name: ")
            amount = int(input("Enter withdraw amount: "))
            operations.withdraw(name, amount)
        elif choice == "9":
            analytics.close_cursor()
            operations.close_cursor()
            conn.close()
            print(" Database connection closed. Goodbye!")
            break
        else:
            print(" Invalid option, please try again.\n")


if __name__ == "__main__":
    main()