from django.views.generic import ListView
from .models import Custumer


class CustumerListView(ListView):
    template_name = "custumer/custumer_list.html"
    model = Custumer
    queryset = Custumer.objects.all()

