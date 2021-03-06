from django.db import models
from django.contrib.auth.models import User


class Unit(models.Model):
    unit = models.CharField(max_length=100)

    def __str__(self):
        return self.unit


class Card(models.Model):
  title = models.CharField(max_length=144)
  subject = models.ForeignKey(Unit,on_delete=models.CASCADE)
  front_side = models.TextField()
  back_side = models.TextField()
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)
  user = models.ForeignKey(User, on_delete=models.CASCADE)

  def save_card(self):
    self.save()

  def delete_card(self):
    self.delete()

  @classmethod
  def search_cards(cls, title):
    return cls.objects.filter(title__icontains=title).all()

  @classmethod
  def show_cards(cls):
    cards = cls.objects.all()
    return cards

  def __str__(self):
    return self.title