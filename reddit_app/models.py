from django.db import models


class Subreddit(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    creation = models.DateTimeField(auto_now_add=True)

    def current_count(self):
        pass

    def today_count(self):
        pass

    def daily_average(self):
        pass

    def __str__(self):
        return self.name
