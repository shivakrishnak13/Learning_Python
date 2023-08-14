from django import forms

class DishForm(forms.Form):
    name = forms.CharField(max_length=100)
    price = forms.DecimalField(max_digits=10)
    availability = forms.ChoiceField(choices=[('Yes', 'Yes'), ('No', 'No')])


class OrderForm(forms.Form) :
    customerName = forms.CharField()
    quantity = forms.IntegerField()

class UpdateStatus(forms.Form) :
    status = forms.ChoiceField(choices=[('Pending', 'Pending'), ('On the Way', 'On the Way'),('Delivered','Delivered'),('Cancelled','Cancelled')])