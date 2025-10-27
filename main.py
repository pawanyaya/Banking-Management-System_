

import mysql.connector

#
def connect_database():
    try:
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="*********",
            database="Your DataBase Name"
        )
        print(" Connected to MySQL Database successfully!\n")
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
