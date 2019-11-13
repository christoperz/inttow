from django.shortcuts import render
from .forms import NumberForm
from .num2worlds import say_number
"""Form view with field given number and print int in words"""

def word_rep_create_view(request):
    if request.method == "POST":
        form = NumberForm(request.POST or None)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
    else:
        form = NumberForm()
        post = form.save(commit=False)
        post.save()
    word = say_number(post.given_number)
    context = {
        'form': form,
        'object': word
    }
    return render(request, "word_rep.html", context)

