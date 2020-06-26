import random
import string
import eel

eel.init('web')

# Generates a random password. 
# Exposes method generate_password() and allows this method to be called in javascript side.
@eel.expose
def generate_password():
  pass_index = 0
  password = ''

  while pass_index < 12:
    # Genrates a value between 0 and 1 randomly.
    pass_val = random.randint(0,2)
  
    # If value = 0 a random char will be added to the password.
    if pass_val == 0:
      new_char = random.choice(string.ascii_letters)
      password += new_char

    # If value = 1 a random int will be added to the password.
    elif pass_val == 1:
      new_int = random.randint(0, 9)
      password += str(new_int)
    
    # If value = 2 a random symbol will be added to the password.
    elif pass_val == 2:
      new_char = random.choice(string.punctuation)
      password += str(new_char)
    
    # Allows the index value to raise. Once this value is equal to 12 the while loop will break and we will have a password of the length 12.
    pass_index += 1
    
  return password


def main():
  # Starts the main.html on server 127.0.0.1:8000 with the size of the window.
  eel.start('main.html', size=(768, 850), block=False)

  # Keeps the app running after start up.
  while True:
    eel.sleep(10)

# Calls the main function if ran locally and not imported.
if __name__ == "__main__":
  main()