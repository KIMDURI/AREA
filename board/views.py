# from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from .models import Board
from .forms import BoardForm, CreateBoardForm
from django.utils import timezone
from django.contrib.auth.models import User


def index(request):
    boards = Board.objects.all()

    # current =0;
    # if request.user == Board.user_id:
    #     current=1;

    return render(request, "board/board_index.html", {'boards' : boards})

def show_board(request, id):
    boards = Board.objects.get(id = id)
    return render(request, 'board/board_show.html', {'boards' : boards})

def create_board(request):
    form = BoardForm(request.POST or None)

    if form.is_valid():
        post = form.save(commit=False)
        post.user_id = request.user
        post.date = timezone.now()
        post.save()
        return redirect(index)

    return render(request, 'board/board_form.html', {'form' : form})

def update_board(request, id):
    boards = Board.objects.get(id = id)
    form = BoardForm(request.POST or None, instance = boards)


    if form.is_valid():
        form.save()
        return redirect(index)

    return render(request, 'board/board_form_update.html', {'form' : form, 'boards' : boards})

def delete_board(request, id):
    boards = Board.objects.get(id = id)

    if request.method == 'POST':
        boards.delete()
        return redirect(index)

    return render(request, 'board/board_delete_confirm.html', {'boards' : boards})
