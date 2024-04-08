from django.shortcuts import render
from .forms import SearchForm
from faker import Faker
from time import sleep
import threading
from .models import Search

fake = Faker()


def save_search(form):
    form.save()

def search(request):
    context = {}
    form = SearchForm(request.GET or None)

    if form.is_valid():
        background_thread = threading.Thread(target=save_search, args=(form,))
        background_thread.start()

        dummy_data = fake.text()
        query = form.cleaned_data['query']
        context['dummy_data'] = f"{query} {dummy_data}"

    context['form'] = form

    context['forms_no'] = Search.objects.all()
    return render(request, 'search.html', context=context)