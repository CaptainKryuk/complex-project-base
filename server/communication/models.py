from django.db import models


class Email(models.Model):
    text = models.TextField()
    receiver = models.ForeignKey('users.User', on_delete=models.RESTRICT)
    send_at = models.DateTimeField(auto_now_add=True)
