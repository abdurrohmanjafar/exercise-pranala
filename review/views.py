from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from .forms import ReviewForm
from .models import Review


def review(request):
    if request.method == "POST":
        form = ReviewForm(request.POST)
        if form.is_valid():
            new_review = Review(
                user_name=form.cleaned_data["user_name"], review=form.cleaned_data["review"], rating=form.cleaned_data["rating"])
            new_review.save()
            return HttpResponseRedirect(reverse('review-page'))

    else:
        form = ReviewForm()
    all_reviews = Review.objects.all()
    return render(request, "review/review.html", {"form": form, "reviews": all_reviews})
