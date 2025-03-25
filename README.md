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

To run this project, you will need to do the following:

Download all these codes to your local folder and open them up in PyCharm.
If the code is compiled without any errors then you should see this URL http://127.0.0.1:8000/
You may first need to create a user/password login by: python manage.py createsuperuser or go to http://127.0.0.1:8000/admin/ to sign in with User ID: eric and password: eric. image
You then go back to the home page: http://127.0.0.1:8000/home
You then can click on the URL links on the screen or manually enter the below URLs on the browser to edit data.
http://127.0.0.1:8000/createCustomer

http://127.0.0.1:8000/editCustomer/1/ (where 1 is a customer id)

http://127.0.0.1:8000/add_account/1 (where 1 is a customer id)

http://127.0.0.1:8000/edit_account/2 (where 2 is the account id)

http://127.0.0.1:8000/addTransaction/2 (where 3 is the order id)

=============

This project implement a RESTFul Web Service that consumes and produces ‘JSON’ data. The business domain model deals with Order Management and the entities are Customer, Address, Order, and Order Items.

The entities have the relationships according to the following:

A Customer Object should have one or many Address Objects (OneToMany)
A Customer Object should have one or many Order Objects (OneToMany)
An Order Object should have one or many Order Item Objects (OneToMany)
This project develops a RESTFul Web Service that publishes the following API:

AddCustomer – Creates a new Customer.
GetCustomers – Returns all the customers it has in the database. Returns the objects as JSON list
UpdateCustomer – Updates an existing customer
AddAddress – Creates a new Address and links it with an existing Customer.
UpdateAddress – Updates an existing address
GetAddresses related to a Customer – Returns all the Addresses associated with a customer as a JSON list
AddOrder – Creates a new Order and links it with an existing Customer
UpdateOrder – Updates an existing Order
GetOrders related to a Customer – Returns all the Orders associated with a customer as a JSON list
AddProduct – Creates a new Product and associates it with an Order
GetProducts related to an Order – Returns all the Products associated with an Order as a JSON list
