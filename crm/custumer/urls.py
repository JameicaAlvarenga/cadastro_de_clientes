from django.urls import path

from .views import CustumerListView

app_name = "custumer"

urlpatterns = [
    path("list/", CustumerListView.as_view(), name="custumer-list")
]
