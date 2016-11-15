from django.shortcuts import render
from django.core.mail import send_mail
from django.shortcuts import render_to_response
from books.forms import ContactForm
from django.http import HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt


# Create your views here.

@csrf_exempt
def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            #process form data
            topic = form.cleaned_data['topic']
            message = form.cleaned_data['message']
            sender = form.cleaned_data.get('sender', 'noreply@example.com')
            #send_mail('Feedback from your site, topic: %s' % topic,
            #          message, sender, ['bushuevzi@mail.ru'],'', 'bushuevzi','2CnpS1Lov4M','smtp.mail.ru')
            return HttpResponseRedirect('./thanks')
    else:
        form = ContactForm(initial={'sender':'user@example.com'})
    return render_to_response('contact.html', {'form':form})

def thanks(request):
    return render_to_response('thanks.html')