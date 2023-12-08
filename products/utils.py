import hashlib
from datetime import datetime, timedelta

# for generate password format md5
def generate_password_md5() :
  time_data = datetime.now() + timedelta(hours=1)
  date = time_data.strftime("%d")
  month = time_data.strftime("%m")
  year = time_data.strftime("%y")
  password_string = f"bisacoding-{date}-{month}-{year}"
  password_md5 = hashlib.md5(password_string.encode()).hexdigest()

  return password_md5

def generate_username():
  time_data = datetime.now() + timedelta(hours=1)
  date = time_data.strftime("%d")
  month = time_data.strftime("%m")
  year = time_data.strftime("%y")
  hour = time_data.strftime("%H")
  username = f"testprogrammer{date}{month}{year}C{hour}"

  return username

