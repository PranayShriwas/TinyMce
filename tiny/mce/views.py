# your_app_name/views.py
from django.shortcuts import render
from .models import YourModel

def your_model_detail(request, pk):
    your_model_instance = YourModel.objects.get(pk=pk)
    return render(request, 'your_app_name/your_model_detail.html', {'object': your_model_instance})
