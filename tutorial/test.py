import test_pb2, sys

# Create Person
def CreatePerson():
    person = test_pb2.Person()
    person.id = 1234
    person.name = "John Doe"
    person.email = "jdoe@example.com"
    phone = person.phones.add()
    phone.number = "555-4321"
    phone.type = test_pb2.Person.HOME
    print(person)

# Writing a Message
# Allow user to create Person Message based on input
def PromptForAddress(person):
    person.id = int(raw_input("Enter person ID number: "))
    person.name = raw_input("Enter name: ")

    email = raw_input("Enter email address (blank for none): ")
    if email != "":
        person.email = email

    while True:
        number = raw_input("Enter a phone number (or leave blank to finish): ")
        if number == "":
          break

        phone_number = person.phones.add()
        phone_number.number = number
        phone_type = raw_input("Is this a mobile, home, or work phone")
        if phone_type == "mobile":
            phone_number.type = test_pb2.Person.MOBILE
        elif phone_type == "home":
            phone_number.type = test_pb2.Person.HOME
        elif phone_type == "work":
            phone_number.type = test_pb2.Person.WORK
        else:
            print("Unknown Phone Type")

if len(sys.argv) != 2:
    print("Usage: ", sys.argv[0])
    sys.exit(-1)

address_book = test_pb2.AddressBook()

try:
    f = open(sys.argv[1], "rb")
    address_book.ParseFromString(f.read())
    f.close()
except IORError:
    print(sys.argv[1] + ": Could not open file, creating new one.")

PromptForAddress(address_book.people.add())

f = open(sys.argv[1], "wb")
f.write(address_book.SerializeToString())
f.close()
