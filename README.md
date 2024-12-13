# Invoice Management System

## Project Overview
The Invoice Management System is a web application designed to manage invoices, payments, customers, and items efficiently. It provides CRUD functionalities for the backend and uses Django as the framework.

---

## Features
- Manage **Invoices**: Create, read, update, and delete invoice records.
- Manage **Payments**: Record and track payment transactions.
- Manage **Customers**: Store and manage customer information.
- Manage **Items**: Maintain an inventory of items related to invoices.

---

## SQL Tables
This project utilizes the following database tables:

### 1. `invoices`
- Fields: `invoice_id`, `cust_id`, `invoice_date`,`due_date`,`pay_id`,`total_amount`, `status`
- Relationships: Links to `customers` and includes invoice details.

### 2. `payments`
- Fields: `pay_id`, `bank_name`, `account_no`, `isfc`
- Relationships: Links to `invoices` to track payments.

### 3. `customers`
- Fields: `id`, `name`, `email`, `phone`, `address`
- Stores customer details.

### 4. `items`
- Fields: `invoice_id`, `item_name`, `item_price`, `id`
- Maintains item inventory and pricing information.

---

## Tech Stack
The Invoice Management System is built using the following technologies:

- **Backend Framework**: Django (Python-based web framework)
- **Database**: SQLite (default Django database)
- **Frontend**: HTML/CSS (for basic templates and forms)
- **Version Control**: Git
- **Branch**: Master branch

---

## Setup Instructions
Follow these steps to set up the project on your local machine:

1. Clone the repository:
   ```bash
   git clone https://github.com/Bhuvankambley2003/invoice_management_system/
   cd invoice_management_system
   ```

2. Create a virtual environment and activate it:
   ```bash
   python -m venv env
   source env/bin/activate   # On Windows: env\Scripts\activate
   ```

3. Install the required dependencies:
   ```bash
   pip install django db-sqlite3 Python-Rest-Framework
   ```

4. Apply migrations to set up the database:
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

5. Run the development server:
   ```bash
   python manage.py runserver
   ```

6. Access the application in your browser at:
   ```
   http://127.0.0.1:3306/
   ```


## Contributions
Feel free to fork the repository and submit pull requests. Ensure to follow coding standards and document your changes properly.

---

## License
This project is open-source and available under the [MIT License](LICENSE).

---

## Author
- **bhuvan kambley**  
  Developer of the Invoice Management System

---

Thank you for using the Invoice Management System!
