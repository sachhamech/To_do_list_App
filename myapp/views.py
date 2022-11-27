from django.shortcuts import render
from django.http import HttpResponse
# from webbrowser import get
from django.shortcuts import render,get_object_or_404,redirect
from .models import To_do
from .forms import TodoForm
# Create your views here.

def Todo_new(request):
    if request.method=='POST':
        form_data=TodoForm(request.POST)  #capturing the form data
        if form_data.is_valid():
            post_data=form_data.save()
            return redirect('Todolist')  #redirect to our Todo_list url
    else:
        form_data=TodoForm()
    # return HttpResponse("welcome")    
    return render(request,'myapp/index.html',{'form_data':form_data})  

def Todo_list(request):
    response_Data=To_do.objects.all().order_by('-id')
    return render(request,'myapp/todolist.html',{'Data':response_Data})  
    
def Todo_delete(request,pk):
    todo=get_object_or_404(To_do,pk=pk)
    todo.delete()
    return redirect('Todolist')        

def Todo_update(request,pk):
    Todo=get_object_or_404(To_do,pk=pk) 
    Todo.Status='complete'    
    Todo.save()
    return redirect('Todolist')   
