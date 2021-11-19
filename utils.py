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
