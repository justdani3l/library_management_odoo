# Library Management System

The Library Management System module for Odoo is designed to help manage library operations effectively. It allows
tracking of authors, books, categories, members, and invoices, while offering features such as book availability, member
registration, borrowing/returning books, and automatic invoice generation. This module ensures a seamless library
experience for both staff and members.

# Key Features

# 1. Authors Management

- Author Profiles: Track author details like name, biography, nationality, and an optional image.
- Books Tracking: Link books written by each author to their profiles.
- Duplicate Handling: Authors' names must be unique, and a copy feature allows easy duplication of author profiles while
  maintaining name uniqueness.

# 2. Books Management

- Book Records: Track book information such as title, ISBN, publisher, production year, language, rating, and number of
  pages.
- Categories: Assign books to specific categories for easy filtering and organization.
- Copies Management: Track the number of available copies, automatically adjusting the count when books are borrowed or
  returned.
- Priority: Assign priority levels to books (Normal, Low, High, Very High).

# 3. Categories Management

- Category Records: Create and manage different categories, associating multiple books with each category.
- Uniqueness: Category names are required to be unique.

# 4. Member Management

- Member Profiles: Manage detailed profiles for library members, including name, contact information, gender, and
  membership date.
- Membership Date Validation: Ensure membership dates are valid (not in the future).
- Invoice History: Track members' borrowing history through associated invoices.
- Automatic Reference Generation: Unique member references are generated automatically during registration.

# 5. Invoice Management

- Book Borrowing: Manage book borrowing by creating invoices that track the issue date, return date, and the member
  borrowing the book.
- Dynamic Return Dates: Automatically calculate the return date based on the borrowing duration.
- Book Availability: Adjust the number of available book copies when books are borrowed or returned.
- State Management: Invoices have multiple states: Draft, Running, Delayed, and Ended. Delayed books trigger warnings,
  while returning books marks the invoice as ended.
- Automatic Sequence for Invoices: Automatically generates a reference for invoices, ensuring traceability.
- WhatsApp Integration: Notify members about the end of their borrowing period via WhatsApp messages.
- Email Notifications: Send reminders and updates to members about their invoices through email.

# SQL Constraints

- Unique Names: Both author names and book categories have constraints that enforce name uniqueness.

# Automated Updates

- Book Copies: The system automatically updates the number of available copies when invoices are created or deleted.
- Progress Tracking: Each invoice tracks its progress from creation to completion, giving the staff a quick view of the
  status of ongoing borrows.
- This module enhances the management of a library's essential operations, making it easier for the staff to handle
  day-to-day activities while ensuring members receive a seamless borrowing experience.

# Installation Guide for Library Management System Module (Odoo)

This guide walks you through the installation process of the Library Management System module for Odoo.

# Prerequisites

-
    1. Odoo: Ensure that Odoo (version 17 or compatible) is installed on your machine. You can download it from the
       official Odoo website.

-
    2. Python: Python 3.10 or higher should be installed. Verify installation by running:

`python --version`

-
    3. PostgreSQL: Odoo uses PostgreSQL as its database management system. Ensure PostgreSQL is installed and running.

-
    4. Development Tools:

    - Git (for version control)
    - IDE or Text Editor (VSCode, PyCharm, etc.)

# Step-by-Step Installation

# 1. Clone the Module Repository

- To install the Library Management System module, first, clone the module's repository into Odoo's custom add-ons
  directory.
  `cd /path/to/odoo/addons`
  `git clone https://github.com/your-repository/library_management_system.git`
  Replace `https://github.com/your-repository/library_management_system.git` with the actual repository URL.

# 2. Configure Odoo to Use the Module

-
    1. Modify Odoo Configuration File: Add the path to the `addons` folder (if not done already). Open the Odoo
       configuration file (`odoo.conf` or `odoo17.conf` located in `/etc/odoo` or `odoo/odoo-server/`), and add the path
       to the custom add-ons.
       `addons_path = /path/to/odoo/addons,/path/to/your/custom/addons`
-
    2. Restart Odoo: After editing the configuration file, restart your Odoo server
       `sudo service odoo restart`
       or if you are running Odoo from a virtual environment:
       `./odoo-bin -c /etc/odoo.conf`

# 3. Install Module Dependencies

The module may require some Python libraries that are not included by default. You can install the required libraries
using pip:
`pip install -r /path/to/odoo/addons/library_management_system/requirements.txt`
If no requirements.txt is present, ensure the following Python libraries are installed:
`pip install -r requirements.txt`

# Install the Module from Odoo UI

# 1. Login to Odoo:

Open Odoo in your browser (usually on http://localhost:8069).

# 2. Activate Developer Mode:

- Go to the Settings menu.
- Scroll down and click Activate the developer mode (usually found at the bottom of the Settings page).

# 3. Install the Module:

- Go to Apps in the main menu.
- Click on the Update Apps List button (found in the top-right corner).
- Search for Library Management System.
- Once found, click Install.

# Verify the Installation

- After installation, you will see the Library menu in the top bar of Odoo.
- From here, you can start managing books, authors, members, invoices, and categories.

# Set Up Email Integration (Optional)

To send email notifications for invoices or book returns, configure Odoo's email settings:

- Go to Settings > General Settings.
- Scroll down to the Email section and configure your outgoing mail server (SMTP).
- Once configured, test by sending an email from a member's profile.

# Conclusion

Once the module is installed, you can start using the Library Management System to manage authors, books, members, and
invoices seamlessly within your Odoo system.