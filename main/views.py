from time import sleep
import threading
from django.shortcuts import render
from .forms import SearchForm
from faker import Faker
from .models import Search


fake = Faker()


def save_search(form):
    sleep(3) # This is just to make this task long-running
    form.save()


def search(request):
    context = {}
    form = SearchForm(request.GET or None)

    if form.is_valid():

        # Option 1 - Create a thread to save the query in the background
        background_thread = threading.Thread(target=save_search, args=(form,))
        background_thread.start()

        # Option 2 - Save the query synchronously
        # save_search(form)

        dummy_data = fake.text()
        query = form.cleaned_data['query']
        context['dummy_data'] = f"{query} {dummy_data}"

    context['form'] = form

    context['forms_no'] = Search.objects.all()
    return render(request, 'search.html', context=context)
