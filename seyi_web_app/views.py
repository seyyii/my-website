from django.shortcuts import render
from seyi_web_app.models import Service, Portfolio, Client, Subscribe, Mycv
from seyi_web_app.forms import ContactForm, SubscribeForm
from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.template.loader import render_to_string
from django.core.mail import send_mail
from django.conf import settings

# Create your views here.
def index(request):
    cv = Mycv.objects.all()
    srv = Service.objects.all()
    cl = Client.objects.all()
    args = {'srv':srv, 'cl':cl, 'cv':cv}
    return render(request, 'seyi_web_app/index.html', args)



          

def about(request):
    cl = Client.objects.all()
    return render(request, 'seyi_web_app/about.html', {'cl':cl})
    

def contact(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            # send email code goes here
            sender_name = form.cleaned_data['name']
            sender_email = form.cleaned_data['email']

            message = "{} with email {} has sent you a new message:\n\n{}".format(sender_name, sender_email, form.cleaned_data['message'])
            send_mail('New Enquiry', message, sender_email, ['omotoshotoheeb@gmail.com'])
            return HttpResponse('Thanks for contacting us!')
    else:
        form = ContactForm()
        
    return render(request, 'seyi_web_app/contact.html', {'form': form})

def portfolio(request):
    port = Portfolio.objects.all()
    if request.method == "POST":
        sform = SubscribeForm(request.POST)
        if sform.is_valid():
            sform.save(commit=True)
            return HttpResponse('Thanks for Subscribing!')
    else:
        sform = SubscribeForm()
        args = {'sform': sform, 'port': port}
        return render(request, 'seyi_web_app/portfolio.html', args )

def services(request):
    srv = Service.objects.all()
    cl = Client.objects.all()
    args = {'srv':srv, 'cl':cl}
    return render(request, 'seyi_web_app/services.html', args)

# def newsletter(request):
#     if request.method == "POST":
#         sform = SubscribeForm(request.POST)
#         if sform.is_valid():
#             sform.save(commit=True)
#     else:
#         sform = SubscribeForm(request.POST)
#         return render(request, 'seyi_web_app/newsletter.html', {'sform': sform}) 

# def mycv_view(request):
#     mycv = Mycv.objects.all()
#     return render(request, '')


