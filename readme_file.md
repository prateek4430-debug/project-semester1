# Student Expense Manager

A comprehensive expense tracking application designed specifically for students to manage their finances, track spending, and maintain budget discipline.

## 📋 Overview

The Student Expense Manager is a command-line application that helps students record daily expenses, categorize spending, monitor budgets, and generate insightful reports. Built using Python, it provides an intuitive interface for financial management without requiring any external dependencies.

## ✨ Features

### Core Features
- **User Profile Management**: Create and manage user profile with monthly budget settings
- **Expense Recording**: Add expenses with date, category, amount, and description
- **Expense Management**: View, search, filter, and delete expense records
- **Budget Tracking**: Real-time budget monitoring with alerts for overspending
- **Category-wise Analysis**: Track spending across 8 predefined categories
- **Monthly Reports**: Generate detailed monthly expense summaries
- **Data Persistence**: Automatic saving and loading of data using text files
- **Search & Filter**: Find expenses by keyword or filter by category

### Supported Categories
- Food
- Transport
- Education
- Entertainment
- Shopping
- Health
- Bills
- Others

## 🛠️ Technologies/Tools Used

- **Programming Language**: Python 3.x
- **Data Storage**: Text files (pipe-delimited format)
- **Built-in Libraries**: 
  - `datetime` - Date and time operations
  - Standard file I/O operations

## 📦 Installation & Setup

### Prerequisites
- Python 3.6 or higher installed on your system

### Steps to Install

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/student-expense-manager.git
   cd student-expense-manager
   ```

2. **No additional dependencies required**
   The project uses only Python standard library

3. **Run the application**
   ```bash
   python expense_manager.py
   ```

## 🚀 How to Run

1. Navigate to the project directory
2. Run the main program:
   ```bash
   python expense_manager.py
   ```
3. On first run, you'll be prompted to set up your profile
4. Follow the on-screen menu to manage your expenses

## 📖 Usage Instructions

### First Time Setup
- Enter your name
- Set your monthly budget
- System creates your profile automatically

### Adding an Expense
1. Select option 1 from main menu
2. Enter date (or press Enter for today)
3. Choose category from the list
4. Enter amount
5. Provide description
6. System saves automatically and checks budget status

### Viewing Expenses
- Select option 2 to view all expenses in a formatted table
- Shows expense ID, date, category, amount, and description

### Searching Expenses
- Select option 3
- Enter keyword to search in descriptions
- View matching results

### Filtering by Category
- Select option 4
- Choose category
- View all expenses in that category with total

### Budget Status
- Select option 6
- View current budget, amount spent, and remaining budget
- Get warnings if budget exceeded

### Monthly Report
- Select option 7
- Enter month and year
- View detailed breakdown by category with percentages

## 🧪 Testing

### Manual Testing Steps

1. **Test Adding Expense**
   - Add expense with valid data
   - Try adding with invalid category
   - Try adding with negative amount

2. **Test Search Function**
   - Add multiple expenses
   - Search with existing keyword
   - Search with non-existing keyword

3. **Test Budget Monitoring**
   - Set budget to low amount
   - Add expenses exceeding budget
   - Verify warning message appears

4. **Test Data Persistence**
   - Add expenses
   - Close application
   - Reopen and verify data is loaded

5. **Test Report Generation**
   - Add expenses for current month
   - Generate monthly report
   - Verify category breakdown is correct

## 📁 Project Structure

```
student-expense-manager/
│
├── expense_manager.py      # Main application file
├── README.md               # Project documentation
├── statement.md            # Problem statement
├── expenses.txt            # Data file (auto-generated)
├── user.txt               # User data file (auto-generated)
│
└── docs/                   # Documentation folder
    ├── diagrams/
    └── report.pdf
```

## 📸 Screenshots

### Main Menu
```
======================================================================
EXPENSE MANAGER - John Doe
======================================================================
1. Add Expense
2. View All Expenses
3. Search Expenses
4. Filter by Category
5. Delete Expense
6. Budget Status
7. Monthly Report
8. Update Budget
9. Exit
======================================================================
```

### Budget Status Display
```
==================================================
BUDGET STATUS
==================================================
Budget    : ₹5000.00
Spent     : ₹3250.50
Remaining : ₹1749.50
==================================================
```

## 🔒 Data Storage Format

### User Data (user.txt)
```
UserName|MonthlyBudget
```

### Expense Data (expenses.txt)
```
ExpenseID|Date|Category|Amount|Description
```

## 🤝 Contributing

This is an academic project. For suggestions or improvements, please contact the author.

## 👨‍💻 Author

**[Your Name]**
- Roll Number: [Your Roll Number]
- Course: Introduction to Computer Problem Solving
- Semester: 1st Year, 1st Semester
- Institution: [Your College Name]

## 📄 License

This project is created for academic purposes as part of the VITyarthi course evaluation.

## 🙏 Acknowledgments

- Course Instructor: [Instructor Name]
- VIT Bhopal University
- Python Documentation

## 📞 Contact

For queries or support:
- Email: [your.email@example.com]
- GitHub: [yourusername]

---

**Note**: This project is part of the academic curriculum and demonstrates the application of fundamental programming concepts including data structures, file handling, functions, control flow, and modular programming.