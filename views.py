from django.shortcuts import render, redirect
from .forms import ReviewForm
from .models import Review
from ..model.sentiment_analysis import predict_sentiment_and_rating

def review_create(request):
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)

            # Call the neural network model to predict sentiment and rating
            predicted_sentiment, predicted_rating = predict_sentiment_and_rating(review.comment)
            review.sentiment = predicted_sentiment
            review.rating = predicted_rating
            review.save()

            return redirect('review_thankyou')
    else:
        form = ReviewForm()
    return render(request, 'reviews/review_form.html', {'form': form})
