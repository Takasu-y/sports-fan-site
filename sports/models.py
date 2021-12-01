from django.db import models
from django.db.models.base import Model

# Create your models here.

class Sports(models.Model):
    name = models.CharField("スポーツ名", max_length=30)
    cover = models.ImageField("カバー写真", upload_to='sports/images', null=True, blank=True)
    rule = models.TextField("ルール")


    class Meta:
        verbose_name = "Sports"
        verbose_name_plural = "Sports"

    def __str__(self):
        return self.name


class Player(models.Model):
    name = models.CharField("選手名", max_length=30)
    picture = models.ImageField("プロフィール写真", upload_to='sports/images/profile', null=True, blank=True)
    description = models.TextField("選手説明")
    sports = models.ForeignKey(Sports, verbose_name="スポーツ名", on_delete=models.CASCADE)


    class Meta:
        verbose_name = 'Player'
        verbose_name_plural = 'Players'

    def __str__(self):
        return self.name

class Link(models.Model):
    title = models.CharField("タイトル", max_length=50, null=True)
    sports = models.ForeignKey(Sports, verbose_name="スポーツ", on_delete=models.CASCADE)
    link = models.URLField("関連記事", max_length=200)

    def __str__(self):
        return self.title
