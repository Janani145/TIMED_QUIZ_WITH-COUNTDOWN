import time

i = None


quiz = ["What is 2 + 2?", "What is the capital of India?", "How many days are there in a week?", "Who wrote the national anthem of India?", "What is the largest ocean on Earth?"]
answers = ["4", "Delhi", "7", "Rabindranath Tagore",  "Pacific"]
score = 0
time_limit = 10
for i in range(len(quiz)):
  print(f"\nQuestion {i+1}: {quiz[i]}")
  start_time = time.time()
  user_answer = input("Answer within 10 seconds:")
  end_time = time.time()
  if end_time - start_time > time_limit:
      print(("Time's up!"))
      elif user_answer.lower() == answers[i].lower():
          print('Correct answer!')
          score += 1
      else:
          print('Wrong answer')
print(f"\nYour Final Score: {score} / {len(quiz)}")
