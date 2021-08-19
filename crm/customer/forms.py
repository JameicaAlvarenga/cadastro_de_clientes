from django import forms
from .models import Customer


class CustomerForm(forms.ModelForm):
    frist_name = forms.CharField()
    last_name = forms.CharField()
    email = forms.EmailField()
    brith_date = forms.DateField()
    area_code = forms.CharField()
    phone_number = forms.CharField()
    country = forms.CharField()
    state = forms.CharField()
    city = forms.CharField()

    class Meta:
        model = Customer
        fields = {
            "frist_name",
            "last_name",
            "email",
            "brith_date",
            "area_code",
            "phone_number",
            "country",
            "state",
            "city",

        }