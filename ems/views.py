from django.shortcuts import render,redirect
from .forms import CreateForm,LoginForm,EditNameForm,EditPassForm
from .models import Employee
from django.contrib import messages


# Create your views here.
def index(request):
    if request.method == 'POST':
        form = request.POST
        n = form['name']
        password = form['password']
        emp = Employee.objects.filter(name=n).first()
        print(emp)
        if n=='admin' and password=='711':
            return redirect('/admin')
        elif emp and emp.password == password:
            # messages.add_message(request, messages.INFO, 'Login Successful')
            return redirect('/'+str(emp.id))
        else:
            messages.add_message(request, messages.INFO, 'Incorrect Input')
    form = LoginForm()
    context = {'form': form}
    return render(request,'index.html',context)

def create(request):
    if request.method == 'POST':
        form = request.POST
        print(form)
        emp = Employee()
        emps = Employee.objects.all()
        emp.id = len(emps)
        emp.name = form['name']
        emp.password = form['password']
        emp.mobile = form['mobile']
        emp.email = form['email']
        print(emp)
        emp1 = Employee.objects.filter(name=emp.name).values()
        print(emp1)
        if not emp1 and emp.password != '' and len(emp.mobile)==10 and emp.email!='' and emp.name!='admin':
            emp.save()
            messages.add_message(request, messages.INFO, 'User added successfully')
            return redirect('/')
        else:
            messages.add_message(request, messages.INFO, 'Incorrect Input')

    form = CreateForm()
    context = {'form': form}
    return render(request,'create.html',context)


def indi(request,id):
    user = Employee.objects.get(id=id)
    context={'usr':user,'nameform':EditNameForm(), 'passform':EditPassForm()}
    return render(request,'indi_usr.html',context)

def editname(request,id):
    user = Employee.objects.get(id=id)
    user.name = request.POST['name']
    u1 = Employee.objects.filter(name=user.name).values()
    if not u1:
        user.save()
        messages.add_message(request, messages.INFO, 'Name Changed Successfully')
    else:
        messages.add_message(request, messages.INFO, 'Name Already Exists')
    return redirect('/'+str(id))


def editpass(request,id):
    user = Employee.objects.get(id=id)
    user.password = request.POST['password']
    user.save()
    messages.add_message(request, messages.INFO, 'Password Changed Successfully')
    return redirect('/'+str(id))

def admin(request):
    users = Employee.objects.all()
    context = {'users': users,'nameform':EditNameForm()}
    return render(request, 'admin.html', context)

def edit(request,id):
    user = Employee.objects.get(id=id)
    user.name = request.POST['name']
    u1 = Employee.objects.filter(name=user.name).values()
    if not u1:
        user.save()
        messages.add_message(request, messages.INFO, 'Name Changed Successfully')
    else:
        messages.add_message(request, messages.INFO, 'Name Already Exists')
    return redirect('/admin')

def delete(request,id):
    user = Employee.objects.get(id=id)
    user.delete()
    return redirect('/admin')

def logout(request):
    return redirect('/')