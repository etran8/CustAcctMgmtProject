# CustAcctMgmtProject
This project creates a Customer Account Management application for a Bank. The web application will let the user open a new account and manage an existing account. The account will have customer details and account details.
The business domain model deals with Customer Account Management and the entities are Customer, Account, Transactions.

The entities have the relationships according to the following:

1. A Customer Object will have one or many Account Objects (OneToMany)
2. An Account Object will have one or many Transaction Objects (OneToMany)
3. An Order Object should have one or many Order Item Objects (OneToMany)

This project develops a web application that offers the users the following functionality:

1. createCustomer – Creates a new Customer.
2. editCustomer – Updates an existing customer
3. add_account – Creates a new Account and links it with an existing Customer.
4. edit_account – Updates an existing Account.
5. addTransaction – Creates a new Transaction and links it with an existing Account.

To run this project, you will need to do the following:

Download all these codes to your local folder and open them up in PyCharm.
If the code is compiled without any errors then you should see this URL http://127.0.0.1:8000/
You may first need to create a user/password login by: python manage.py createsuperuser or go to http://127.0.0.1:8000/admin/ to sign in with User ID: eric and password: eric. image
You then go back to the home page: http://127.0.0.1:8000/home
You then can click on the URL links on the screen or manually enter the below URLs on the browser to edit data.
1. http://127.0.0.1:8000/createCustomer
2. http://127.0.0.1:8000/editCustomer/1/ (where 1 is a customer id)
3. http://127.0.0.1:8000/add_account/1 (where 1 is a customer id)
4. http://127.0.0.1:8000/edit_account/2 (where 2 is the account id)
5. http://127.0.0.1:8000/addTransaction/2 (where 2 is the account id)

