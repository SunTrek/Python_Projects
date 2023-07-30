============ pip3 install faker ============


from faker import Faker
fake = Faker()
name = fake.name()
address = fake.address()
phone_number = fake.phone_number()
date_of_birth = fake.date_of_birth()

print("Name:", name)
print("Address:", address)
print("Phone number:", phone_number)
print("Date of birth:", date_of_birth)
