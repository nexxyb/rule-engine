from django.urls import path

from .views import RuleCheckView

urlpatterns = [
    path("rules/check/", RuleCheckView.as_view()),
]
