# CustAcctMgmtProject
This project creates a Customer Account Management application for a Bank. The web application will let the user open a new account and manage an existing account. The account will have customer details and account details.
The business domain model deals with Customer Account Management and the entities are Customer, Account, Transactions.

The entities have the relationships according to the following:

A Customer Object will have one or many Account Objects (OneToMany)
An Account Object will have one or many Transaction Objects (OneToMany)
An Order Object should have one or many Order Item Objects (OneToMany)

This project develops a web application that offers the users the following functionality:

createCustomer – Creates a new Customer.
editCustomer – Updates an existing customer
add_account – Creates a new Account and links it with an existing Customer.
edit_account – Updates an existing Account.
addTransaction – Creates a new Transaction and links it with an existing Account.
view_home_list – Lists a list of all Customers.
listCustomerJSON - Returns all the Customers as a JSON list.
listAccountJSON – Returns all the Accounts as a JSON list.
updateAccountJSON - GetProducts related to an Order – Returns all the Products associated with an Order as a JSON list
listTransactionJSON - 

To run this project, you will need to do the following:
Download all these codes to your local folder and open them up in PyCharm.
If the code is compiled without any errors then you should see this URL http://127.0.0.1:8000/
You may first need to create a user/password login by: python manage.py createsuperuser or go to http://127.0.0.1:8000/admin/ to sign in with User ID: eric and password: eric. image
You then go back to the home page: http://127.0.0.1:8000/home
You then can click on the URL links on the screen or manually enter the below URLs on the browser to edit data.
