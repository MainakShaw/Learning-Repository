# Create a program capable of displaying questions to the user like KBC. 
# Use List data type to store the questions and their correct answers. 
# Display the final amount the person is taking home after playing the game.

import random

questions = [
  "Among whom of the following does the Indian Constitution permit to take part in the proceedings of Parliament?",
  "Who, in 1978, became the first person to be born in the continent of Antarctica?",
  "Which colonial power ended its involvement in India by selling the rights of the Nicobar Islands to the British on October 18, 1868?",
  "Who is the first woman to successfully climb K2, the world’s second highest mountain peak?",
  "Which poet in the court of Mughal Ruler Bahadur Shah Zafar wrote the ‘Dastan-e-Ghadar’, a personal account of the 1857 revolt?",
  "The historic Indo-Pak talks of 1972 between Indira Gandhi and Zulfikar Ali Bhutto were held at which place in Shimla?",
  "Where in Singapore did Netaji Subhash Chandra Bose make the first proclamation of an Azad Hind government?",
  "Milinda-Panha is a dialogue between King Menander or Milinda and which Buddhist monk?",
  "What was the title of the thesis that Dr. B. R. Ambedkar submitted to the London School of Economics for which he was awarded his doctorate in 1923?",
  "Which was the first mountain peak above 8,000 metres in height to be summited by humans?",
  "According to the Padma Purana, which king had to live as a tiger for a hundred years due to a deer's curse?",
  "Leena Gade, a person of Indian origin, is the first female race engineer to win which of the following races?"
]
options = [
  [
    "Solicitor General", "Attorney General", "Cabinet Secretary",
    "Chief Justice"
  ], ["Emilio Palma", "James Weddell", "Nathaniel Palmer", "Charles Wilkes"],
  ["Belgium", "Italy", "Denmark", "France"],
  ["Junko Tabei", "Wanda Rutkiewicz", "Tamae Watanabe", "Chantal Mauduit"],
  [
    "Mir Taqi Mir", "Mohammad Ibrahim Zauq", "Zahir Dehlvi",
    "Abul-Qasim Ferdowsi"
  ], ["Viceregal Lodge", "Gorton Castle", "Barnes Court", "Cecil Hotel"],
  [
    "Cathay Cinema Hall", "Fort Canning Park",
    "National University of Singapore", "National Gallery of Singapore"
  ], ["Asanga", "Nagasena", "Mahadharmarakshita", "Dharmaraksita"],
  [
    "The Want and Means of India", "The Problem of the Rupee",
    "National Dividend of India", "The Law and Lawyers"
  ], ["Annapurna", "Lhotse", "Kanchenjunga", "Makalu"],
  ["Kshemadhurti", "Dharmadatta", "Mitadhvaja", "Prabhanjana"],
  [
    "Indianapolis 500", "24 Hours of Le Mans", "12 Hours of Sebring",
    "Monaco Grand Prix"
  ]
]
correct_answers = [
  "Attorney General", "Emilio Palma", "Denmark", "Wanda Rutkiewicz",
  "Zahir Dehlvi", "Barnes Court", "Cathay Cinema Hall", "Nagasena",
  "The Problem of the Rupee", "Annapurna", "Prabhanjana", "24 Hours of Le Mans"
]
correct_answers_money = [
  5000.0, 10000.0, 20000.0, 40000.0, 80000.0, 160000.0, 320000.0, 640000.0,
  1250000.0, 2500000.0, 5000000.0, 10000000.0
]


def randomzied_question_selector():
  question_options_answer_group = []
  random_number = random.randint(0, len(questions) - 1)
  question_options_answer_group.append(questions.pop(random_number))
  question_options_answer_group.extend(
    random.sample(options.pop(random_number), k=4))
  question_options_answer_group.append(correct_answers.pop(random_number))
  return question_options_answer_group


def user_answer_checker(question_options_answer_group, user_answer):
  if (
    (user_answer == "A"
     and question_options_answer_group[1] == question_options_answer_group[5])
      or
    (user_answer == "B"
     and question_options_answer_group[2] == question_options_answer_group[5])
      or
    (user_answer == "C"
     and question_options_answer_group[3] == question_options_answer_group[5])
      or (user_answer == "D" and question_options_answer_group[4]
          == question_options_answer_group[5])):
    return True
  else:
    return False


def take_valid_input():
  user_input = input("Pick an option of your choice: ")
  while (True):
    if user_input.upper() in ["A", "B", "C", "D"]:
      return user_input.upper()
    else:
      print("\nInvalid Input!")
      user_input = input("Please pick an valid option of your choice:")


def kbc_loop():
  previous_answer_correct = True
  question_number = 1
  total_amount = 0.0
  user_answer = ''
  while (True):
    question_options_answer_group = randomzied_question_selector()
    print("Question", question_number, ": ", question_options_answer_group[0])
    print("\nYour options are:-\n")
    print("A. " + question_options_answer_group[1] + "\t\tB. " +
          question_options_answer_group[2])
    print("C. " + question_options_answer_group[3] + "\t\tD. " +
          question_options_answer_group[4])
    user_answer = take_valid_input()
    previous_answer_correct = user_answer_checker(
      question_options_answer_group, user_answer)
    if (previous_answer_correct == True):
      total_amount += correct_answers_money[question_number - 1]
      print("\nCorrect Answer! ₹", correct_answers_money[question_number - 1],
            " awarded.\n")
      if (question_number == 12):
        print("\nCongratulations! You became a CrorePati.\n")
        break
      question_number += 1
    else:
      print("\nOh no! Wrong Answer. Better Luck Next Time.\n")
      break
  return total_amount


print("WELCOME TO KAUN BANEGA CROREPATI")
print("--------------------------------\n")
print("\nYou won ₹ ", kbc_loop(), "in total. Great job!")
