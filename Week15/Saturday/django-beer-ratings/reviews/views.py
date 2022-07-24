from django.shortcuts import redirect, render
from .models import Beer, Reviews
from .forms import BeerForm, ReviewForm
from django.contrib.auth.models import User

def get_beer(beer_id):
    return Beer.objects.get(id=beer_id)

def get_review(review_id):
    return Reviews.objects.get(id=review_id)

def get_user(user_id):
    return User.objects.get(id=user_id)

def beer_list(request):
    beers = Beer.objects.all()
    return render(request, 'reviews/beer_list.html', {'beers': beers})

def new_beer(request):
    beer = BeerForm(request.POST or None)
    if beer.is_valid():
        beer.save()
        return redirect('beer:beer_list')
    return render(request, 'reviews/beer_form.html', {'beer': beer})

def beer_details(request, beer_id):
    beer = get_beer(beer_id)
    reviews = beer.reviews.all()
    return render(request, 'reviews/beer_details.html', {'beer': beer, 'reviews': reviews})

def update_beer(request, beer_id):
    beer = BeerForm(request.POST or None, instance=get_beer(beer_id))
    if beer.is_valid():
        beer.save()
        return redirect('beer:beer_details', beer_id)
    return render(request, 'reviews/beer_form.html', {'beer': beer})

def delete_beer(request, beer_id):
    beer = get_beer(beer_id)
    if request.method == 'POST':
        beer.delete()
        return redirect('beer:beer_list')
    return render(request, 'reviews/delete_beer.html', {'beer':beer})

def add_review(request, beer_id, user_id):
    beer = get_beer(beer_id=beer_id)
    user = get_user(user_id=user_id)
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid:
            review = form.save(commit=False)
            review.beer = beer  
            review.user = user
            review.save()
            return redirect('beer:beer_details', beer_id)
    else:
        form =ReviewForm()
        return render(request, 'reviews/review_form.html', {'form': form, 'beer':beer, 'user':user})

def update_review(request, review_id):
    review = get_review(review_id)
    form = ReviewForm(request.POST or None, instance=review)
    if form.is_valid():
        form_review = form.save(commit=False)
        form_review.beer = review.beer
        form_review.user = review.user
        form_review.save()
        return redirect('beer:beer_details', review.beer.id)
    return render(request, 'reviews/review_form.html', {'form': form})

def delete_review(request, review_id):
    review = get_review(review_id)
    beer = review.beer
    if request.method == 'POST':
        review.delete()
        return redirect('beer:beer_details', beer.id)
    return render(request, 'reviews/delete_review.html', {'review': review})