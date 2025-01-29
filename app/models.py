from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class FootballPlayers(models.Model):
    FOOTBALL_PLAYERS = [
        ("GK", "Goalkeeper"),
        ("DF", "Defender"),
        ("MF", "Midfielder"),
        ("FW", "Forward"),
    ]
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    image = models.ImageField(upload_to="football/")
    date_added = models.DateTimeField(default=timezone.now)
    type = models.CharField(max_length=2, choices=FOOTBALL_PLAYERS)
    detail = models.TextField(default="")

    class Meta:
        verbose_name = "Football Player"
        verbose_name_plural = "Football Players"

    def __str__(self):
        return self.name


class PlayerReviews(models.Model):
    players = models.ForeignKey(
        FootballPlayers, on_delete=models.CASCADE, related_name="reviews"
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.IntegerField()
    comment = models.TextField(max_length=100)
    date_added = models.DateTimeField(default=timezone.now)

    class Meta:
        verbose_name = "Player Review"
        verbose_name_plural = "Player Reviews"

    def __str__(self):
        return f"{self.user.username} review for {self.players.name}"


class PlayerTeams(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    players = models.ManyToManyField(FootballPlayers, related_name="teams")

    class Meta:
        verbose_name = "Player Team"
        verbose_name_plural = "Player Teams"

    def __str__(self):
        return self.name


class PlayerTrophy(models.Model):
    player = models.OneToOneField(
        FootballPlayers, on_delete=models.CASCADE, related_name="trophy"
    )
    trophy_name = models.CharField(max_length=100)
    win_date = models.DateTimeField(default=timezone.now)

    class Meta:
        verbose_name = "Player Trophy"
        verbose_name_plural = "Player Trophies"

    def __str__(self):
        return f"Trophy won by {self.player.name}"
