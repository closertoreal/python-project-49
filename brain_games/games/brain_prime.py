from random import randint

QUESTION = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_prime(expression):
  if expression < 2:
      return True
  for i in range(2, int(expression ** 0.5) + 1):
      if expression % i == 0:
          return False
  return True


def create_round_data():
    expression = randint(1, 100)
    if is_prime(expression):
        right_answer = 'yes'
    else:
        right_answer = 'no'
    expression = str(expression)
    return expression, right_answer
