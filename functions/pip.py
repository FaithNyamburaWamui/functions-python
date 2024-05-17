class LanguageLearning:
    def __init__(self, target_language, proficiency_level):
        self.target_language = target_language
        self.proficiency_level = proficiency_level
        self.exercises = {}
        self.quizzes = {}
        self.progress = 0 
        self.resources = {
            "Beginner": ["Textbook: Beginner's Guide to " + target_language, "Online course: Introduction to " + target_language],
            "Intermediate": ["Intermediate " + target_language + " Grammar Workbook", "Conversation Practice: " + target_language],
            "Advanced": ["Comprehension passages" + target_language + " Read and anwser the set question to perfect" + target_language]
        }

    def add_exercise(self, topic, exercise):
        if topic not in self.exercises:
            self.exercises[topic] = []
        else:
            self.exercises[topic].append(exercise)

    def add_quiz(self, topic, quiz):
        if topic not in self.quizzes:
            self.quizzes[topic] = []
        else:
            self.quizzes[topic].append(quiz)

    def track_progress(self):
        self.progress += 1

    def recommend_resources(self):

        if self.proficiency_level == "Beginner" and self.progress < 3:
            return self.resources["Beginner"]
        elif self.proficiency_level == "Intermediate" and self.progress < 6:
            return self.resources["Intermediate"]
        elif self.proficiency_level == "Advanced" and self.progress < 10:
            return self.resources["Advanced"]
        else:
            return []

    def take_exercise(self, topic):
        self.track_progress()
        print("You completed the exercise on", topic)

    def take_quiz(self, topic):
        self.track_progress()
        print("You completed the quiz on", topic)

    def upgrade_proficiency_level(self):
        if self.progress >= 6:
            if self.proficiency_level == "Beginner":
                self.proficiency_level = "Intermediate"
                print("Congratulations! You have been upgraded to Intermediate level.")
            else:
                print("You are already at the highest proficiency level.")

# Example

learner1 = LanguageLearning("French", "Beginner")

learner1.add_exercise("Vocabulary", "Match the French words with their meanings.")
learner1.add_quiz("Grammar", "Conjugation quiz for regular French verbs.")

learner1.take_exercise("Vocabulary")
learner1.take_quiz("Grammar")
print("Recommended resources:", learner1.recommend_resources())

learner1.upgrade_proficiency_level() 
print("Current proficiency level:", learner1.proficiency_level)


learner2= LanguageLearning("English", "Intermediate")

learner2.add_quiz("Vocabulary", "Multiple-choice quiz on common French words.")
learner2.add_quiz("Grammar", "Conjugation quiz for regular French verbs.")
learner2.take_exercise("Vocabulary")
learner2.take_quiz("Grammar")
print("Recommended resources:", learner2.recommend_resources())

learner2.upgrade_proficiency_level()
print("Current proficiency level:", learner2.proficiency_level)





# class Languages:
#     def __init__ (self):
#         self.beginner_english = [{"question":"choose what's correct:\n 1.an apple\n 2. a apple","answer":1},{"question":"choose the correct answer:\n1.daughter\n2.duaghter","answer":1}]
#         self.intermediate_english = []
#         self.advanced_english = []
#         self.beginner_kinyarwanda = []
#         self.intermediate_kinyarwanda = []
#         self.advanced_kinyarwanda = []
#         self.beginner_level_english_marks = 0

#     def user_preferred_language(self,language,proficiency_level):

     

#         if language == "english" and proficiency_level == "beginner":


#             for question in self.beginner_english:

#                 answer = input(question['question'])

#                 if answer == question['answer']:
#                     self.beginner_level_english_marks += 1
#                     print(f"marks currently: {self.beginner_level_english_marks}")

#             # if self.beginner_level_english_marks >= 1:
#             #     print(f"congratulation, you have upgraded to the next level {self.beginner_level_english_marks}")
#             # else:
#             #     print(f"Keep trying, practice makes perfect {self.beginner_level_english_marks}")

# learner = Languages()

# learner.user_preferred_language("english","beginner")
# learner.user_preferred_language("english","intermediate")



# You are require to build a system to assist language learners in improving on their vocubularies and grammary.
# Your system should allow learners to input their target language and their level of proficiency.
# The system must give learners tailored language, track leaners' progress and give them access to additional resources.

# Task: write a simple python code for the above program, the code must be easily understood by and entry level software developer