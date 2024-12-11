# Personal Expense Tracker (PET)

A Python console application for tracking personal expenses with a connection to MongoDB for storing and managing records. The application allows users to add, view, calculate totals, and delete expense entries efficiently.

---

## 📖 Project Description

This project provides a simple yet powerful way to manage personal expenses. Using Python and MongoDB, it offers a structured and secure system for storing expense data.  

### **Features:**
- Add new expenses with description, amount, and date.
- View all recorded expenses.
- Calculate the total amount of all expenses.
- Delete an expense by its unique ID.
- Close the MongoDB connection gracefully when exiting.

### **Technology Stack:**
- **Python**: Core programming language for the application.
- **MongoDB**: Database for storing expenses.
- **Pymongo**: MongoDB driver for Python.

### **Challenges & Future Features:**
- Ensuring valid data input (e.g., date format, non-negative amounts).
- Handling database errors gracefully.
- **Planned Enhancements**:
  - User authentication for secure access.
  - Category-wise expense tracking.
  - Exporting expense data to CSV or Excel.

---

## ⚙️ How to Install and Run the Project

Follow these steps to set up and run the Personal Expense Tracker locally:

### **Prerequisites**
- Python 3.6 or above
- MongoDB Atlas account or a local MongoDB instance
- Downloading libraries

### **Installation Steps**
1. Clone the repository:  
   ```bash
   git clone https://github.com/cdmatgaganwood03L/cdmatgaganwood03L.git
   cd Personal_expense_tracker-main

2. Install required dependencies:
   pip install pymongo
   pip install time
   pip install bson

4. Set up your MongoDB connection:
- Update the MongoClient link in the Expense_Tracker class to match your MongoDB Atlas credentials.

4. Run the application:
   python Personal_expense_tracker-main.py

📋 How to Use the Project
- Start the application.
- Use the menu to perform the following actions:
- Add New Expense: Enter description, amount, and date (DD-MM-YYYY).
- View All Expenses: Displays all stored expenses.
- View Total Amount: Calculates and displays the sum of all expenses.
- Delete Expense: Remove an expense by entering its unique ID.
- Exit: Safely close the MongoDB connection.

🤝 How to Contribute
Contributions are also welcome!

1. Fork the repository.
2. Create a new branch:
  -git checkout -b feature/<feature-name>
3. Commit your changes:
  -git commit -m "Add <description-of-changes>"
4. Push to the branch:
  -git push origin feature/<feature-name>
5. Open a pull request.



