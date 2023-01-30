# Password-Authentication-using-Python
Password Authentication is the process of checking the identity of a user. Almost every online platform today makes sure that they only give access to the real user which can be only possible by asking for a password while a user wants to log in to the account.

# What is a Password Authentication System?
A password authentication system is a system that is used for the identification of a user. Think of it like a login screen that you see while logging in to your Facebook account. It asks for your email or a username and then it asks for your password. If you have entered the correct password then it verifies you as the real user.

Creating a logic-based password authentication system is also a popular question in the coding interviews. So, in the section below, I will take you through how to create a password authentication system using Python.

# Password Authentication using Python
To create a password authentication system using Python you have to follow the steps mentioned below:

1.Store username and password in a dictionary called database

2.Input a username and store it in a variable called username

3.Input a password and store it in a variable called password

4.Loop through the keys of the database dictionary

5.Check if the input username matches a key in the database dictionary

.If a match is found, repeatedly prompt for password input until it matches the password in the database for the matching key
.If a match is not found, continue to the next iteration of the loop
.If the loop completes and no match was found, print a message indicating that the username and password are not verified
.If the loop breaks because the password was correct, print a message indicating that the username and password are verified.

