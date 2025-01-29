from django.contrib import admin
from .models import FootballPlayers, PlayerReviews, PlayerTeams, PlayerTrophy


class PlayerReviewInline(admin.TabularInline):
    model = PlayerReviews
    extra = 2


class FootballPlayersAdmin(admin.ModelAdmin):
    list_display = ("name", "age", "type", "date_added")
    inlines = [PlayerReviewInline]


class PlayerReviewsAdmin(admin.ModelAdmin):
    list_display = (
        "players",
        "user",
        "comment",
        "rating",
        "date_added",
    )


class PlayerTeamsAdmin(admin.ModelAdmin):
    list_display = ("name", "location")
    filter_horizontal = ("players",)


class PlayerTrophyAdmin(admin.ModelAdmin):
    list_display = ("player", "trophy_name", "win_date")


# Register models with admin site
admin.site.register(FootballPlayers, FootballPlayersAdmin)
admin.site.register(PlayerReviews, PlayerReviewsAdmin)
admin.site.register(PlayerTeams, PlayerTeamsAdmin)
admin.site.register(PlayerTrophy, PlayerTrophyAdmin)
