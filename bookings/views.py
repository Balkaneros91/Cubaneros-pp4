from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from reservation_booking.models import Booking
from reservation_booking.forms import BookingForm


@login_required
def booking_list(request):
    if request.user.is_superuser:
        bookings = Booking.objects.all()
    else:
        bookings = Booking.objects.filter(user=request.user)
    context = {'bookings': bookings}
    return render(request, 'Bookings/booking_list.html', context)


@login_required
def booking_edit(request, pk):
    booking = get_object_or_404(Booking, pk=pk)

    if request.method == 'POST':
        form = BookingForm(request.POST, instance=booking)
        if form.is_valid():
            form.save()
            messages.success(request, 'Booking successfully updated!')
            return redirect('booking_list')
    else:
        form = BookingForm(instance=booking)
    context = {'form': form}
    return render(request, 'Bookings/booking_edit.html', context)


@login_required
def booking_delete(request, pk):
    booking = get_object_or_404(Booking, pk=pk)

    if request.method == 'POST':
        booking.delete()
        messages.success(request, 'Booking successfully deleted!')
        return redirect('booking_list')
    context = {'booking': booking}
    return render(request, 'Bookings/booking_delete.html', context)
