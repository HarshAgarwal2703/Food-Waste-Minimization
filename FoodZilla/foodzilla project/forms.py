from django import forms

class EntryForm(forms.Form):
    bought = forms.IntegerField(
    label='Enter tomatoes bought today: '
    )
class StatsForm(forms.Form):
    months = forms.IntegerField(
    label='Predict estimated order how many months ahead?'
    )
