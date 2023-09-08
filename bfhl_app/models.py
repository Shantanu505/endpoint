from django.db import models
import json

class User(models.Model):
    user_id = models.CharField(max_length=255)
    college_email_id = models.EmailField()
    college_roll_number = models.CharField(max_length=20)

class UserInput(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    numbers = models.TextField()
    alphabets = models.TextField()

    def get_numbers_as_list(self):
        return json.loads(self.numbers)

    def get_alphabets_as_list(self):
        return json.loads(self.alphabets)

    def set_numbers(self, numbers_list):
        self.numbers = json.dumps(numbers_list)

    def set_alphabets(self, alphabets_list):
        self.alphabets = json.dumps(alphabets_list)
