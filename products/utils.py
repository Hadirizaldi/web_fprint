import hashlib
from datetime import datetime

# for generate password format md5
def generate_password_md5() :
  today = datetime.now()
  current_date = today.strftime("%d");
  current_month = today.strftime("%m");
  current_year = today.strftime("%y")
  password_string = f"bisacoding-{current_date}-{current_month}-{current_year}"
  password_md5 = hashlib.md5(password_string.encode()).hexdigest()

  
  return password_md5


