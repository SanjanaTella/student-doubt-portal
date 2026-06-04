from django.db import models
from django.contrib.auth.models import User

class Doubt(models.Model):
    student = models.ForeignKey(User, on_delete=models.CASCADE)
    subject = models.CharField(max_length=100)
    doubt_text = models.TextField()
    answer = models.TextField(blank=True, null=True)
    status = models.CharField(max_length=20, default='Pending')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Student Doubt"
        verbose_name_plural = "Student Doubts"

    def save(self, *args, **kwargs):
        if self.answer:
            self.status = 'Answered'
        super().save(*args, **kwargs)

    def __str__(self):
        return self.subject


class Feedback(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    message = models.TextField()
    rating = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Student Feedback"
        verbose_name_plural = "Student Feedback"

    def __str__(self):
        return self.user.username