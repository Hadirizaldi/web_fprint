import hashlib
from datetime import datetime, timedelta

def generate_password_md5():
    time_data = datetime.now() + timedelta(hours=1)
    date = time_data.strftime("%d")
    month = time_data.strftime("%m")
    year = time_data.strftime("%y")
    password_string = f"bisacoding-{date}-{month}-{year}"
    # check for spasi
    if any(char.isspace() or char == '' for char in password_string):
        raise ValueError("String password tidak boleh mengandung spasi atau karakter kosong.")
    # make md 5
    password_md5 = hashlib.md5(password_string.encode()).hexdigest()

    return password_md5

from datetime import datetime, timedelta

def generate_username():
    time_data = datetime.now() + timedelta(hours=1)
    date = time_data.strftime("%d")
    month = time_data.strftime("%m")
    year = time_data.strftime("%y")
    hour = time_data.strftime("%H")
    username = f"tesprogrammer{date}{month}{year}C{hour}"
    # check if contain spasi
    if any(char.isspace() or char == '' for char in username):
        raise ValueError("String username tidak boleh mengandung spasi atau karakter kosong.")

    return username

# # Contoh penggunaan
# try:
#     username = generate_username()
#     print(f"Username: {username}")
# except ValueError as e:
#     print(f"Error: {e}")

# # Contoh penggunaan
# try:
#     password = generate_password_md5()
#     print(f"Password MD5: {password}")
# except ValueError as e:
#     print(f"Error: {e}")