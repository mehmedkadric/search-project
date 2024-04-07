from django.shortcuts import render, redirect  # Import redirect
from .forms import SearchForm
from faker import Faker
fake = Faker()


def search(request):
    if request.method == 'POST':
        form = SearchForm(request.POST)
        if form.is_valid():
            form.save()
            dummy_data = fake.text()
            query = request.POST['query']
            return render(request, 'search.html', {'form': form, 'dummy_data': dummy_data, 'query': query})
    else:
        form = SearchForm()

    return render(request, 'search.html', {'form': form})