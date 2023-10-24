names = []
if names:
    for name in names:
        if name == "admin":
            print(f"Hello {name}, would you like to see a status report?")
        elif name != "admin":
            print(f"Hello {name}, thank you for logging in again.")
else:
    print("We need more users!")

current_users = ["kubo", "kubeiro", "kubebe", "beiro", "maca"]
new_users = ["kubo", "wishbone", "jessy", "lola", "maca"]

for new_user in new_users:
    if new_user in current_users:
        print("Please enter another username")
    else:
        print("Username available")
