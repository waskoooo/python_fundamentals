n = int(input())
parking_lot = {}

for _ in range(n):
    command = input().split()

    if command[0] == "register":
        username, license_plate = command[1], command[2]
        if username in parking_lot:
            print(f"ERROR: already registered with plate number {parking_lot[username]}")
        else:
            parking_lot[username] = license_plate
            print(f"{username} registered {license_plate} successfully")

    elif command[0] == "unregister":
        username = command[1]
        if username not in parking_lot:
            print(f"ERROR: user {username} not found")
        else:
            print(f"{username} unregistered successfully")
            del parking_lot[username]

# Print the currently registered users and their license plates
for username, license_plate in parking_lot.items():
    print(f"{username} => {license_plate}")
