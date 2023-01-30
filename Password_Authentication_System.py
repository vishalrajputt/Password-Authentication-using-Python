# A dictionary to store username and password
database = {'VishalR':'Vishal&123','RvishalS':'Singh123@'}

# Input for username
username = input("Enter Your Username : ")

# Input for password
password = input("Enter Your Password : ")

# Loop through the dictionary keys
for i in database.keys():
    # Check if the input username matches a key in the dictionary
    if username == i:
        # Continuously prompt for password input until it matches the password in the dictionary
        while password != database.get(i):
            password = input("Enter Your Password Again : ")
        # Break out of the loop when the password is correct
        break

# Print message if username and password match
print("Verified")
