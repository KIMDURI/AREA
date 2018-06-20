from django.contrib import admin
from .models import Room
from board.models import Board
from quiz.models import Question, ANSWER, Result


admin.site.register(Room)
admin.site.register(Board)

admin.site.register(Question)
admin.site.register(ANSWER)


admin.site.register(Result)
