from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from shop.models import games, Cart, GameOrder
from django.core.exceptions import ObjectDoesNotExist



# Create your views here.

@login_required
def checkout(request):
	token = None
	if request.method == 'POST':
		token = request.POST['stripeToken']
		print token
	context = {'token':token}
	template = 'checkout.html'
	return render(request,template,context)

@login_required
def mode_payment(request):
	context = {}
	template = 'mode.html'
	return render(request,template,context)

@login_required
def end(request):
	try:
		cart = Cart.objects.get(user=request.user, active=True)
	except ObjectDoesNotExist:
		pass
	else:
		cart.delete()
	context = {}
	template = 'end.html'
	return render(request,template,context)