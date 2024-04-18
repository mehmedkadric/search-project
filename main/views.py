from django.shortcuts import render
from .forms import SearchForm, UploadDataForm
from faker import Faker
import threading
from .models import Data
import pandas as pd
import io
from django.db import transaction
from django.contrib import messages

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
    return render(request, 'search.html', context=context)


def process_data(file_contents, filename): 
    df = None
    try:
        file_buffer = io.BytesIO(file_contents)
        
        if filename.endswith('.xls') or filename.endswith('.xlsx'):  
            df = pd.read_excel(file_buffer, engine='openpyxl')
        elif filename.endswith('.csv'): 
            df = pd.read_csv(file_buffer)

        if df is not None and 'city' in df.columns and 'state_name' in df.columns:
            data_objects = []
            for index, row in df.iterrows():
                city = row['city']
                state_name = row['state_name']
                data_objects.append(Data(city=city, state_name=state_name))

            with transaction.atomic():
                Data.objects.bulk_create(data_objects)
    except Exception as e:
        print("An error occurred while processing the file:", str(e))

def upload_data(request):
    context = {}
    if request.method == 'POST':
        form = UploadDataForm(request.POST, request.FILES)
        if form.is_valid(): 
            file = request.FILES['data_file']
            filename = file.name  
            file_contents = file.read() 
            messages.success(request, 'Data uploaded successfully')
            data_processing_thread = threading.Thread(target=process_data, args=(file_contents, filename))  
            data_processing_thread.start()
    else:
         form = UploadDataForm()

    context['form'] = form
    return render(request, 'upload_data.html', context=context)
