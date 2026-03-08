import subprocess

username = "donald"
password = "secret1234"

# Checks if the user already exists, and if not, creates it
response = subprocess.run(["id", username])

if response.returncode == 0:
    print("User exists")
else:
    subprocess.run(["sudo", "useradd", "-m", username])
    # add default password
    subprocess.run(
        ["sudo", "chpasswd"],
        input=f"{username}:{password}".encode(),
        check=True,
    )
    print(f"user with username: {username} is created.")

# Ensures the user has a home directory (/home/username)
result = subprocess.run(["test", "-d", f"/home/{username}"])

if result.returncode == 0:
    print(f"Home directory for {username} exists")
else:
    print(f"Home directory for {username} does not exist, creating it...")
    subprocess.run(["sudo", "mkdir", "-p", f"/home/{username}"])

# Sets correct ownership and permissions for the home directory
subprocess.run(["sudo", "chown", f"{username}:{username}", f"/home/{username}"])

print(f"Home directory for {username} is ready with correct permissions.")
