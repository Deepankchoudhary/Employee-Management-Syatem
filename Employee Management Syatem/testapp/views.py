
from django.shortcuts import render, redirect
from .forms import *
from django.urls import reverse_lazy
from django.views import generic


def Employeelist(request):
    emp = EmployeeDetail.objects.filter(added_by=request.user)
    return render(request,'List.html',{'employee':emp})


def add(request):
    if request.method == "POST":
        form = Userdetail(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.added_by = request.user
            post.save()
            return redirect('testapp:list')
        else:
            context = {
                'form': form
            }
            return render(request, 'Add.html', context)
    context = {
        'form': Userdetail(),
    }

    return render(request, 'Add.html', context)





class UpdateView(generic.UpdateView):
    model = EmployeeDetail
    template_name = 'Edit.html'
    context_object_name = 'update'
    success_url = reverse_lazy('testapp:list')
    fields = ['name', 'email']

class DeleteView(generic.DeleteView):
    model = EmployeeDetail
    template_name = 'Delete.html'
    context_object_name = 'delete'
    success_url = reverse_lazy('testapp:list')


def edit(request):
        if request.method == "POST":
            emp_email = request.POST.get('email', '')
            fri_list = EmployeeDetail.objects.values('name', 'email', )
            for item in fri_list:
                if (item["email"] == emp_email):
                    name = request.POST.get('name', '')
                    emp = EmployeeDetail(name=name)
                    emp.save()

        return render(request, "Edit.html")

def delete(request):
        if request.method == "POST":
            emp_email = request.POST.get('email', '')
            EmployeeDetail.objects.get(email=emp_email).delete()

        return render(request, "Delete.html")