import getpass

my_pass = input("Enter you password: ")

my_pass_with_getpass = getpass.getpass()
print(my_pass_with_getpass)

# Using Prompt with get pass
my_pass_with_getpass = getpass.getpass(prompt="Enter your Password: ")

print(getpass.getuser())
