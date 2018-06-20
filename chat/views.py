from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from .models import Room
from .form import RoomForm

@login_required
def index(request):
    """
    Root page view. This is essentially a single-page app, if you ignore the
    login and admin parts.
    """
    # Get a list of rooms, ordered alphabetically
    rooms = Room.objects.order_by("title")

    # Render that in the index template
    return render(request, "chat/chat_index.html", {
        "rooms": rooms,
    })

@login_required
def newroom(request):

    form = RoomForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('chat')

    return render(request, "chat/createRoomForm.html", {"form" : form})

