from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def booking(request):
    return render(request, 'booking.html')

def login(request):
    return render(request, 'login.html')

def signup(request):
    return render(request, 'signup.html')

def profile(request):
    rentals = Rental.objects.filter(user=request.user)
    bookings = Booking.objects.filter(user=request.user)
    context = {
        'user': request.user,
        'rentals': rentals,
        'bookings': bookings,
    }
    return render(request, 'profile.html', context)
