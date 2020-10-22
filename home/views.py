from django.shortcuts import render, HttpResponse
from home.models import Contact
from django.contrib import messages

def index(request):
    return render(request, 'index.html')
 #   return HttpResponse("this is index page")

def about(request):
    return render(request, 'about.html')

def contact(request):
    if request.method == "POST":
        fname = request.POST.get("fname")
        lname = request.POST.get("lname")
        areacode = request.POST.get("areacode")
        telnum = request.POST.get("telnum")
        email = request.POST.get("email")
        feedback = request.POST.get("feedback")
        contact=Contact(fname = fname , lname = lname , areacode = areacode,telnum = telnum , email= email , feedback = feedback  )
        contact.save()
        messages.success(request, 'Feedback Sent Successfully!')
    return render(request, 'contact.html')
  #  return HttpResponse("this is contact page")

