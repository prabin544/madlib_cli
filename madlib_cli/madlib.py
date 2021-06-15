import re

def welcome_message():
  text = """
  *********************************************
  **  Welcome to Mad Libs! Mad Libs is a     **
  **  fill-in-the-blank word game. Type in   **
  **  a word satisfying the request and I    **
  **  will return a funny story for you.     **
  *********************************************
  """
  print(text)

def read_template(file_to_read):
  if file_to_read:
    with open(file_to_read, 'r') as file:
      return file.read()
  else:
    raise FileNotFoundError("missing.txt")

def parse_template(string):
  text = string
  expected_parts = tuple(re.findall(r'\{(.*?)\}', text))
  expected_stripped = re.sub(r"\{(.*?)\}", "{}", text)
  return expected_stripped, expected_parts


def merge(expected_stripped,expected_parts):
  return expected_stripped.format(*expected_parts)

def game():
  welcome_message()
  story = read_template('../assets/story.txt')
  res = parse_template(story)
  question = res[1]
  for items in question:
    print(items)
 
  


if __name__ == "__main__":
  game()
  read_template("example_text.txt")
  parse_template("It was a {Adjective} and {Adjective} {Noun}.")
  merge("It was a {} and {} {}.", ("dark", "stormy", "night"))
