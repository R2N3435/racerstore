from django.shortcuts import render
from django.core.mail import send_mail
from .forms import Contactform
from django.conf import settings
# Create your views here.
def contact(request):
	title = 'Contact'
	form = Contactform(request.POST or None)
	confirm_message = None
	if form.is_valid():
		name = form.cleaned_data['name']
		comment = form.cleaned_data['comment']
		subject = 'Message from Mysite'
		emailfrom = form.cleaned_data['email']
		message =  '%s. From %s %s.' %(comment, name, emailfrom)
		emailto = [settings.EMAIL_HOST_USER]
		send_mail(
	         subject,
	         message,
	         emailfrom,
	         emailto,
	         fail_silently=False,
         )
		title = "Thanks!"
		confirm_message = "We appreciate your feedback."
		form = None
	context = {'title':title, 'form':form, 'confirm_message': confirm_message}
	template = 'contact.html'
	return render(request,template,context)