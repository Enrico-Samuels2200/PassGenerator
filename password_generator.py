import random
import string
# Generates a random password. 
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
    else:
      new_sym = random.choice(string.punctuation)
      password += str(new_sym)

    # Allows the index value to raise. Once this value is equal to 12 the while loop will break and we will have a password of the length 12.
    pass_index += 1
    
  return password

def main():
  new_password = generate_password()
  print(new_password)

# Calls the main function if ran locally and not imported.
if __name__ == "__main__":
  main()