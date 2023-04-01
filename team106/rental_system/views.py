from django.shortcuts import render, redirect
from django.contrib.auth.views import PasswordResetView
from django.urls import reverse_lazy


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


from django.contrib.auth.views import PasswordResetView


class MyPasswordResetView(PasswordResetView):
    template_name = 'forgot_password.html'
    success_url = reverse_lazy('password_reset_done')


def forgot_password(request):
    if request.method == 'POST':
        # Handle form submission and send password reset link to user's email
        # ...
        return redirect('login')
    else:
        # Display forgot password form
        return MyPasswordResetView.as_view()(request)
