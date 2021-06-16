from django.urls import path, include
from main.api import views as api_views

urlpatterns = [
    path(
        "makaleler", api_views.MakaleListCreateAPIView.as_view(), name="makale-listesi"
    ),
    path(
        "makaleler/<int:id>",
        api_views.MakaleDetailAPIView.as_view(),
        name="makale-detail",
    ),
]


# Function based URLs
"""
urlpatterns = [
    path("makaleler", api_views.makale_list_create_api_view, name="makale-listesi"),
    path("makaleler/<int:id>", api_views.makale_detail_api_view, name="makale-detail"),
]
"""
