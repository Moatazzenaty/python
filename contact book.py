# Create a dictionary called contacts
contacts = { "mostafa": "01022483819"}
contacts["moataz"]="01000102248"
contacts["omar"]= "01000102247"

print("contact in the contact book")
for name in contacts :
    print(name)
# Allow the user to search for a contact by name
search_name = input("\nEnter the name of the person you're looking for: ")

# Search for the contact and print the associated phone number
if search_name in contacts:
    print(f"{search_name}'s phone number is: {contacts[search_name]}")
else:
    print(f"Sorry, {search_name} is not in the contact book.")