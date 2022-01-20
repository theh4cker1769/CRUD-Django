import email
from django.shortcuts import render, HttpResponseRedirect
from .forms import StudentRegistration, ItemForm
from .models import User, Item

def index(request):
    if request.method == "POST":
        fm = StudentRegistration(request.POST, request.FILES)
        if fm.is_valid():
            nm = fm.cleaned_data['name']
            em = fm.cleaned_data['email']
            ph = fm.cleaned_data['phone']
            im = fm.cleaned_data['profileImg']
                
            reg = User(name=nm, email=em, phone=ph, profileImg=im)
            reg.save()
            fm = StudentRegistration()
    else:
        fm = StudentRegistration()
    stud = User.objects.all()
    return render(request, 'index.html', {'form': fm, 'stud': stud})


def test_page(request):
    if request.method == "POST":
        fmt = ItemForm(request.POST, request.FILES)
        if fmt.is_valid():
            nmt = fmt.cleaned_data['testName']
            imt = fmt.cleaned_data['testImage']
            regt = Item(testName=nmt, testImage=imt)
            regt.save()
            fmt = ItemForm()
    else:
        fmt = ItemForm()
    return render(request, 'test.html', {'form': fmt})

# Update data
def update_data(request, id):
    if request.method == "POST":
        pi = User.objects.get(pk=id)
        fm = StudentRegistration(request.POST, instance=pi)
        if fm.is_valid():
            fm.save()
    else:
        pi = User.objects.get(pk=id)
        fm = StudentRegistration(instance=pi)
    return render(request, 'updatestudent.html', {'form': fm})


# Delete data
def delete_data(request, id):
    if request.method == "POST":
        pi = User.objects.get(pk=id)
        pi.delete()
        return HttpResponseRedirect('/')

# Create your views here.
