from datetime import datetime

expenses = []
user_data = {'name': '', 'budget': 0.0}
CATEGORIES = ['Food', 'Transport', 'Education', 'Entertainment', 'Shopping', 'Health', 'Bills', 'Others']

def save_data():
    try:
        with open('expenses.txt', 'w') as f:
            for exp in expenses:
                f.write(f"{exp['id']}|{exp['date']}|{exp['category']}|{exp['amount']}|{exp['description']}\n")
        
        with open('user.txt', 'w') as f:
            f.write(f"{user_data['name']}|{user_data['budget']}\n")
        return True
    except Exception as e:
        print(f"Error saving: {e}")
        return False

def load_data():
    global expenses, user_data
    try:
        with open('expenses.txt', 'r') as f:
            for line in f:
                parts = line.strip().split('|')
                expenses.append({
                    'id': parts[0],
                    'date': parts[1],
                    'category': parts[2],
                    'amount': float(parts[3]),
                    'description': parts[4]
                })
        
        with open('user.txt', 'r') as f:
            line = f.readline().strip()
            parts = line.split('|')
            user_data['name'] = parts[0]
            user_data['budget'] = float(parts[1])
    except FileNotFoundError:
        pass

def add_expense(date, category, amount, description):
    expense_id = f"EXP{len(expenses)+1:04d}"
    expense = {
        'id': expense_id,
        'date': date,
        'category': category,
        'amount': amount,
        'description': description
    }
    expenses.append(expense)
    save_data()
    return expense_id

def delete_expense(expense_id):
    global expenses
    initial_count = len(expenses)
    expenses = [e for e in expenses if e['id'] != expense_id]
    if len(expenses) < initial_count:
        save_data()
        return True
    return False

def search_expenses(keyword):
    return [e for e in expenses if keyword.lower() in e['description'].lower()]

def filter_by_category(category):
    return [e for e in expenses if e['category'] == category]

def filter_by_month(month, year):
    month_str = f"{year}-{month:02d}"
    return [e for e in expenses if e['date'].startswith(month_str)]

def calculate_total(expense_list):
    return sum(e['amount'] for e in expense_list)

def get_category_breakdown():
    current = datetime.now()
    month_expenses = filter_by_month(current.month, current.year)
    
    breakdown = {}
    for exp in month_expenses:
        cat = exp['category']
        breakdown[cat] = breakdown.get(cat, 0) + exp['amount']
    return breakdown

def check_budget():
    current = datetime.now()
    month_expenses = filter_by_month(current.month, current.year)
    spent = calculate_total(month_expenses)
    remaining = user_data['budget'] - spent
    
    return {
        'budget': user_data['budget'],
        'spent': spent,
        'remaining': remaining,
        'exceeded': remaining < 0
    }

def generate_monthly_report(month, year):
    month_expenses = filter_by_month(month, year)
    total = calculate_total(month_expenses)
    
    print(f"\n{'='*70}")
    print(f"MONTHLY REPORT - {month}/{year}")
    print(f"{'='*70}")
    print(f"Total Expenses: {len(month_expenses)}")
    print(f"Total Amount: ₹{total:.2f}")
    print(f"\nCategory Breakdown:")
    
    cat_breakdown = {}
    for exp in month_expenses:
        cat = exp['category']
        cat_breakdown[cat] = cat_breakdown.get(cat, 0) + exp['amount']
    
    for cat, amt in sorted(cat_breakdown.items(), key=lambda x: x[1], reverse=True):
        percentage = (amt/total*100) if total > 0 else 0
        print(f"  {cat:15}: ₹{amt:8.2f} ({percentage:5.1f}%)")
    print("="*70)

def setup_user():
    print("\n" + "="*70)
    print("WELCOME TO STUDENT EXPENSE MANAGER")
    print("="*70)
    name = input("\nEnter your name: ")
    budget = float(input("Enter monthly budget (₹): "))
    user_data['name'] = name
    user_data['budget'] = budget
    save_data()
    print(f"\n✓ Welcome, {name}!")

def display_menu():
    print(f"\n{'='*70}")
    print(f"EXPENSE MANAGER - {user_data['name']}")
    print("="*70)
    print("1. Add Expense")
    print("2. View All Expenses")
    print("3. Search Expenses")
    print("4. Filter by Category")
    print("5. Delete Expense")
    print("6. Budget Status")
    print("7. Monthly Report")
    print("8. Update Budget")
    print("9. Exit")
    print("="*70)

def add_expense_ui():
    print("\n--- Add Expense ---")
    date = input("Date (YYYY-MM-DD) or Enter for today: ")
    if not date:
        date = datetime.now().strftime('%Y-%m-%d')
    
    print(f"Categories: {', '.join(CATEGORIES)}")
    category = input("Category: ")
    if category not in CATEGORIES:
        print("❌ Invalid category!")
        return
    
    amount = float(input("Amount (₹): "))
    description = input("Description: ")
    
    exp_id = add_expense(date, category, amount, description)
    print(f"✓ Expense added! (ID: {exp_id})")
    
    status = check_budget()
    if status['exceeded']:
        print(f"⚠️ Budget exceeded by ₹{abs(status['remaining']):.2f}!")

def view_expenses_ui():
    if not expenses:
        print("\n📝 No expenses recorded!")
        return
    
    print(f"\n{'='*90}")
    print(f"ALL EXPENSES (Total: {len(expenses)})")
    print(f"{'='*90}")
    print(f"{'ID':10} {'Date':12} {'Category':15} {'Amount':10} {'Description':30}")
    print("-"*90)
    
    for exp in expenses:
        print(f"{exp['id']:10} {exp['date']:12} {exp['category']:15} ₹{exp['amount']:8.2f} {exp['description'][:28]:30}")
    
    total = calculate_total(expenses)
    print("-"*90)
    print(f"{'TOTAL:':60} ₹{total:.2f}")
    print("="*90)

def main():
    load_data()
    
    if not user_data['name']:
        setup_user()
    
    while True:
        display_menu()
        choice = input("\nChoice (1-9): ")
        
        if choice == '1':
            add_expense_ui()
        
        elif choice == '2':
            view_expenses_ui()
        
        elif choice == '3':
            keyword = input("\nSearch keyword: ")
            results = search_expenses(keyword)
            if results:
                for exp in results:
                    print(f"{exp['id']} | {exp['date']} | {exp['category']} | ₹{exp['amount']} | {exp['description']}")
            else:
                print("No results found!")
        
        elif choice == '4':
            print(f"Categories: {', '.join(CATEGORIES)}")
            cat = input("Enter category: ")
            results = filter_by_category(cat)
            if results:
                for exp in results:
                    print(f"{exp['id']} | {exp['date']} | ₹{exp['amount']} | {exp['description']}")
                print(f"Total: ₹{calculate_total(results):.2f}")
            else:
                print("No expenses in this category!")
        
        elif choice == '5':
            exp_id = input("Enter Expense ID: ")
            if delete_expense(exp_id):
                print("✓ Deleted!")
            else:
                print("❌ Not found!")
        
        elif choice == '6':
            status = check_budget()
            print(f"\n{'='*50}")
            print("BUDGET STATUS")
            print(f"{'='*50}")
            print(f"Budget    : ₹{status['budget']:.2f}")
            print(f"Spent     : ₹{status['spent']:.2f}")
            print(f"Remaining : ₹{status['remaining']:.2f}")
            if status['exceeded']:
                print("⚠️ Budget exceeded!")
            print("="*50)
        
        elif choice == '7':
            month = int(input("Month (1-12): "))
            year = int(input("Year: "))
            generate_monthly_report(month, year)
        
        elif choice == '8':
            new_budget = float(input("New budget: ₹"))
            user_data['budget'] = new_budget
            save_data()
            print("✓ Budget updated!")
        
        elif choice == '9':
            print("\nGoodbye!")
            break
        
        else:
            print("❌ Invalid choice!")

if __name__ == "__main__":
    main()