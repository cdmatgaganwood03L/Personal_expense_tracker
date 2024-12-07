from pymongo import MongoClient
from time import strptime
from bson.objectid import ObjectId

class Expense():
    def __init__(self, description, amount, date):
        self.description = description
        self.amount = amount
        self.date = date
        
class Expense_Tracker():
    def __init__(self, dbname = "MY_PET", collectname = "Monthly_expenses"):
        self.client_link =MongoClient("mongodb+srv://myataung:5634##CC!!hell5634@cluster0.4s0eo.mongodb.net/") 
        self.db_name =self.client_link[dbname]
        self.coll =self.db_name[collectname]
        print("Successfully connected to MongoDB!")
        
        pass
    def add_expense(self, description, amount, date):
        try:
            strptime(date, '%d-%m-%Y')

            if amount <= 0:   
                raise ValueError("Your amount must be greater than Zero!")
            else:
                pass

            expenses: dict = { 
                "description" : description,
                "amount" : amount,
                "date" : date
            }
            result = self.coll.insert_one(expenses)
            print(f"Expense successfully added with ID: {result.inserted_id}")

        except ValueError:
            print("Invalid date format! Please use DD-MM-YYYY.")
        except Exception as e:
            print(f"Unexpected Error: {e}")

    def view_expense(self):
        results = self.coll.find()
        print("\nRecorded Expenses: ")
        for shown in results:
            print(f"ID: {shown['_id']}, Description: {shown['description']}, "
                    f"Amount: {shown['amount']}, Date: {shown['date']}")
                
    def total_amount(self):
        total = self.coll.aggregate([{"$group": {"_id": None, "total": {"$sum": "$amount"}}}])
        convert_into = list(total)
        if convert_into:
            print(f"Total Expenses: {convert_into[0]['total']:.2f}")
        else:
            print("No expenses are found yet.")

    def delect_expense(self, expenses_id):
        try:
            result = self.coll.delete_one({"_id": ObjectId(expenses_id)})
            if result.deleted_count > 0:
                print("Expense are deleted successfully!")
            else:
                print("No expense are found with provided ID.")
        except ValueError as er:
            print(f"Input Error: {er}")
        except Exception as e:
            print(f"An error found out: {e}")

    def exist_PET(self):
        self.client_link.close()
        print("Connection to MongoDB is closed right now!")
        

def menu():
    print("\n <<<_____Personal Expense Tracker_____>>> ",
          "\n 1. Add New Expense",
          "\n 2. View All Expenses",
          "\n 3. View Total Amount",
          "\n 4. Delect The Expense",
          "\n 5. Exit") 

def main():
    the_class = Expense_Tracker()
    while True:
        menu()
        choice: float =float(input("Enter your option: "))
        
        if choice == 1:
            des: str =input('Enter your description: ')
            if len(des) > 100:
                print("Description too long. Limit is 100 characters.")
                continue
            try:
                amt: float =float(input('Enter your amount: '))
            except ValueError:
                print("Amount must be a number!")
                continue
            date : str =input('Enter your date(DD-MM-YYYY): ')
            the_class.add_expense(des,amt,date)

        elif choice == 2:
            the_class.view_expense()
        
        elif choice == 3:
            the_class.total_amount()

        elif choice == 4:
            del_ID: str=input("Enter your ID to delect: ")
            the_class.delect_expense(del_ID)

        elif choice == 5:
            the_class.exist_PET()
            print("Exiting.......\nSee you later, Sweetheart!\n")
            break

        else:
            print("Your option is unvalid. Please select a valid option!")       

if __name__ == '__main__':
    main()