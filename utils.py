def search_in_file(file_name, condition):
  with open(file_name, "r") as file:
    lines = file.readlines()
    for line in lines:
      if condition in line:
        return line
    return None


def add_to_file(file_name, data):
  with open(file_name, "w") as file:
    file.write(data)


def remove_from_file(file_name, data):
  with open(file_name) as file:
    lines = file.readlines()
    file.seek(0)
    for line in lines:
      if data not in line:
        file.write(line)
    file.truncate()


def validate_empty_input(prompt):
  while True:
    try:
      value = input(prompt)
    except ValueError:
      print("Sorry, I didn't understand that.")
      continue

    if value == '':
      print("Sorry, your response must not be empty.")
      continue
    else:
      break
  return value
