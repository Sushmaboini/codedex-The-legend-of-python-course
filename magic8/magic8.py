
import random
question = input('question:')
random_number = random.randint(1,9)

if random_number == 1:
  answer = "Yes-definitely"
elif random_number == 2:
  answer = "It is decidedly so"
elif random_number == 3:
   answer = "without a doubt"
elif random_number == 4:
   answer = "Reply hazy, try again"
elif random_number == 5:
   answer = "Ask again later"
elif random_number == 6:
   answer = "better not tell you now"
elif random_number == 7:
   answer = "My sources says no"
elif random_number == 8:
  answer = "Outlook not so good"
elif random_number == 9:
   answer = "very doubtful"
else:
  answer = "error"
print('Magic 8 Ball:  ' + answer)
