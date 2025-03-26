# CustAcctMgmtProject
This project creates a Customer Account Management application for a Bank. The web application will let the user open a new account and manage an existing account. The account will have customer details and account details.
The business domain model deals with Customer Account Management and the entities are Customer, Account, Transactions.

This application also creates RESTFul APIs using the same model objects indicated above. These APIs will allow user to list and create a Customer, an Account, and a Transaction. Be able to load a customer, an Account and update it as needed.

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

RESTFul APIs
1.	List_customers – Displays all the customers and be able to create a new customer.
2.	List_accounts – Displays all the accounts for a customer and be able to create a new account linked to that customer.
3.	Update_customer – Takes the ‘pk’ of a customer from the list and brings up the customer details and renders it for editing. Upon successful update display the updated customer.
4.	Update_Account – Takes the ‘pk’ of an account from the list and brings up the account details and renders it for editing. 
5.	List Transactions – Displays all the transactions for an Account and be able to create a new transaction on that account.

To run this project, you will need to do the following:

Download all these codes to your local folder and open them up in PyCharm.
If the code is compiled without any errors then you should see this URL http://127.0.0.1:8000/

You may first need to create a user/password login by: python manage.py createsuperuser or go to http://127.0.0.1:8000/admin/ to sign in with User ID: eric and password: eric.

To go back to the home page: http://127.0.0.1:8000/home
Click on the URL links below on the browser to edit data.
1. http://127.0.0.1:8000/createCustomer
2. http://127.0.0.1:8000/editCustomer/1/ (where 1 is a customer id)
3. http://127.0.0.1:8000/add_account/1 (where 1 is a customer id)
4. http://127.0.0.1:8000/edit_account/2 (where 2 is the account id)
5. http://127.0.0.1:8000/addTransaction/2 (where 2 is the account id)

Enter the available RESTFul APIs below on the browser to edit data.
1. http://127.0.0.1:8000/view_home_list/
2. http://127.0.0.1:8000/listCustomerJSON/
3. http://127.0.0.1:8000/listAccountJSON/1 (where 1 is a customer id)
4. http://127.0.0.1:8000/updateCustomerJSON/1 (where 1 is a customer id)
5. http://127.0.0.1:8000/updateAccountJSON/2 (where 2 is the account id)
6. http://127.0.0.1:8000/listTransactionJSON/2 (where 2 is the account id)








