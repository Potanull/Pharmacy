from django.shortcuts import render, redirect
from .models import Client
from .forms import ClientForm
from datetime import date, timedelta
from jinja2 import Template

def client_view(request):
    client = Client.objects.order_by('surname', 'name', 'patronymic')
    return render(request, 'client/client.html', {'client': client })

def add_client_view(request):
    if request.method == 'POST':
        form = ClientForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('client')

    form = ClientForm()

    return render(request, 'client/add_client.html', {'form': form })