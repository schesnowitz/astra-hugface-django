from django.shortcuts import render, redirect
from django.views.decorators.http import require_POST
from .models import DataSet, Data
def index(request):
    context = {}
    return render(request=request, template_name='data_sets/index.html', context=context)




def create(request):
    context = {}
    return render(request=request, template_name='data_sets/create.html', context=context)

@require_POST
def create_data_set(request):
    dataset = DataSet.objects.create(name=request.POST['dataset'],)
    
    return redirect('data_set:show', pk=dataset.pk)
    

def show(request, pk):
    context = {}
    return render(request=request, template_name='data_sets/show.html', context=context)
