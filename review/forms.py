from django import forms


class ReviewForm(forms.Form):
    user_name = forms.CharField(max_length=100, label="Your username")
    review = forms.CharField(widget=forms.Textarea,
                             max_length=200, label="Your review")
    rating = forms.IntegerField(min_value=1, max_value=5, label="Your rating")
