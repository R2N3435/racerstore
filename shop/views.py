from django.shortcuts import render, get_object_or_404, redirect, render_to_response
from django.core.exceptions import ObjectDoesNotExist
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import games, Cart, GameOrder, Recommend_game, mouse, Recommend_mouse, MouseOrder
from django.http import HttpResponse
from django.template import RequestContext
from .forms import SearchForm
import os

# Create your views here.
def shop(request):
	post = games.objects.all()
	paginator = Paginator(post, 8)
	page = request.GET.get('page')
	try:
		game = paginator.page(page)
	except PageNotAnInteger:
		game = paginator.page(1)
	except EmptyPage:
		game = paginator.page(paginator.num_pages)
	context = {'game':game, 'page': page}
	template = 'shop.html'
	return render(request,template,context)

def mouses(request):
	post = mouse.objects.all()
	paginator = Paginator(post, 8)
	page = request.GET.get('page')
	try:
		mouses = paginator.page(page)
	except PageNotAnInteger:
		mouses = paginator.page(1)
	except EmptyPage:
		mouses = paginator.page(paginator.num_pages)
	context = {'mouse':mouses}
	template = 'mouse.html'
	return render(request,template,context)

def detail(request, games_id):
	game = get_object_or_404(games, pk=games_id)
	try:
		recomend = Recommend_game.objects.all()
	except ObjectDoesNotExist:
		pass
	else:
		recomend.delete()
	game.recomend_game(games_id)
	recomend = Recommend_game.objects.all()
	if request.user.is_authenticated():
		i = request.user.id
		g = game.id
		f = open(str(i)+'.txt', 'a')
		f.close()
		if os.stat(str(i)+".txt").st_size == 0:
			f=open(str(i)+'.txt','r+')
			f.write('game= ' + str(g)+'\n')
			f.close()
		k = 0
		with open(str(i)+'.txt','r+') as f:
			lines = f.readlines()
			s = 'game= '+str(g)+'\n'
			if len(lines) > 5:
				for j in range(0,len(lines)):
					if s == lines[j]:
						k = 1
						break
				if k==0:
					lists=[]
					g=open(str(i)+'.txt','r+')
					for line in g:
						lists.append(line)
					g.close()
					lists.remove(lists[0])
					lists.append(s)
					k=2
			if len(lines) <= 5:
				for j in range(0,len(lines)):
					if s in lines[j]:
						k = 1
						break
				if k==0:
					f.write("game= "+str(g)+'\n')
		if k==2:
			g=open(str(i)+'.txt','w')
			for n in lists:
				g.write(n)
			g.close()
	paginator = Paginator(recomend, 4)
	page = request.GET.get('page')
	try:
		rgame = paginator.page(page)
	except PageNotAnInteger:
		rgame = paginator.page(1)
	except EmptyPage:
		rgame = paginator.page(paginator.num_pages)
	context = {'game':game, 'rgame':rgame, 'page':page}
	template = 'detail.html'
	return render(request, template, context)

def detail_mouse(request, mouse_id):
	mouses = get_object_or_404(mouse, pk=mouse_id)
	try:
		recomend = Recommend_mouse.objects.all()
	except ObjectDoesNotExist:
		pass
	else:
		recomend.delete()
	mouses.recomend_mouse(mouse_id)
	recomend = Recommend_mouse.objects.all()
	if request.user.is_authenticated():
		i = request.user.id
		g = mouses.id
		f = open(str(i)+'.txt', 'a')
		f.close()
		if os.stat(str(i)+".txt").st_size == 0:
			f=open(str(i)+'.txt','r+')
			f.write('mouse= ' + str(g)+'\n')
			f.close()
		k = 0
		with open(str(i)+'.txt','r+') as f:
			lines = f.readlines()
			s = 'mouse= '+str(g)+'\n'
			if len(lines) > 5:
				for j in range(0,len(lines)):
					if s == lines[j]:
						k = 1
						break
				if k==0:
					lists=[]
					g=open(str(i)+'.txt','r+')
					for line in g:
						lists.append(line)
					g.close()
					lists.remove(lists[0])
					lists.append(s)
					k=2
			if len(lines) <= 5:
				for j in range(0,len(lines)):
					if s in lines[j]:
						k = 1
						break
				if k==0:
					f.write("mouse= "+str(g)+'\n')
		if k==2:
			g=open(str(i)+'.txt','w')
			for n in lists:
				g.write(n)
			g.close()
	paginator = Paginator(recomend, 4)
	page = request.GET.get('page')
	try:
		rmouse = paginator.page(page)
	except PageNotAnInteger:
		rmouse = paginator.page(1)
	except EmptyPage:
		rmouse = paginator.page(paginator.num_pages)
	context = {'mouse':mouses, 'rmouse':rmouse, 'page':page}
	template = 'detail_mouse.html'
	return render(request, template, context)

def add_to_cart(request, game_id):
	if request.user.is_authenticated():
		try:
			game = games.objects.get(pk=game_id)
		except ObjectDoesNotExist:
			pass
		else:
			try:
				cart = Cart.objects.get(user=request.user, active=True)
			except ObjectDoesNotExist:
				cart = Cart.objects.create(
					user=request.user
				)
				cart.save()
			cart.add_to_cart(game_id)
			i = request.user.id
			g = game.id
			f = open(str(i)+'.txt', 'a')
			f.close()
			if os.stat(str(i)+".txt").st_size == 0:
				f=open(str(i)+'.txt','r+')
				f.write('game= ' + str(g)+'\n')
				f.close()
			k = 0
			with open(str(i)+'.txt','r+') as f:
				lines = f.readlines()
				s = 'game= '+str(g)+'\n'
				if len(lines) > 5:
					for j in range(0,len(lines)):
						if s == lines[j]:
							k = 1
							break
					if k==0:
						lists=[]
						g=open(str(i)+'.txt','r+')
						for line in g:
							lists.append(line)
						g.close()
						lists.remove(lists[0])
						lists.append(s)
						k=2
				if len(lines) <= 5:
					for j in range(0,len(lines)):
						if s in lines[j]:
							k = 1
							break
					if k==0:
						f.write("game= "+str(g)+'\n')
			if k==2:
				g=open(str(i)+'.txt','w')
				for n in lists:
					g.write(n)
				g.close()
		return redirect('cart')
	else:
		return redirect('/accounts/login/')

def add_to_cart_mouse(request, mouse_id):
	if request.user.is_authenticated():
		try:
			mouses = mouse.objects.get(pk=mouse_id)
		except ObjectDoesNotExist:
			pass
		else:
			try:
				cart = Cart.objects.get(user=request.user, active=True)
			except ObjectDoesNotExist:
				cart = Cart.objects.create(
					user=request.user
				)
				cart.save()
			cart.add_to_cart1(mouse_id)
			i = request.user.id
			g = mouses.id
			f = open(str(i)+'.txt', 'a')
			f.close()
			if os.stat(str(i)+".txt").st_size == 0:
				f=open(str(i)+'.txt','r+')
				f.write('mouse= ' + str(g)+'\n')
				f.close()
			k = 0
			with open(str(i)+'.txt','r+') as f:
				lines = f.readlines()
				s = 'mouse= '+str(g)+'\n'
				if len(lines) > 5:
					for j in range(0,len(lines)):
						if s == lines[j]:
							k = 1
							break
					if k==0:
						lists=[]
						g=open(str(i)+'.txt','r+')
						for line in g:
							lists.append(line)
						g.close()
						lists.remove(lists[0])
						lists.append(s)
						k=2
				if len(lines) <= 5:
					for j in range(0,len(lines)):
						if s in lines[j]:
							k = 1
							break
					if k==0:
						f.write("mouse= "+str(g)+'\n')
			if k==2:
				g=open(str(i)+'.txt','w')
				for n in lists:
					g.write(n)
				g.close()
		return redirect('cart')
	else:
		return redirect('/accounts/login/')

def remove_from_cart(request, game_id):
	if request.user.is_authenticated():
		try:
			game = games.objects.get(pk=game_id)
		except ObjectDoesNotExist:
			pass
		else:
			cart = Cart.objects.get(user=request.user, active=True)
			cart.remove_from_cart(game_id)
		return redirect('cart')
	else:
		return redirect('/accounts/login/')

def remove_from_cart_mouse(request, mouse_id):
	if request.user.is_authenticated():
		try:
			mouses = mouse.objects.get(pk=mouse_id)
		except ObjectDoesNotExist:
			pass
		else:
			cart = Cart.objects.get(user=request.user, active=True)
			cart.remove_from_cart1(mouse_id)
		return redirect('cart')
	else:
		return redirect('/accounts/login/')

def clear(request):
	if request.user.is_authenticated():
		try:
			cart = Cart.objects.get(user=request.user, active=True)
		except ObjectDoesNotExist:
			pass
		else:
			cart.clear_all()
		return redirect('cart')
	else:
		return redirect('/accounts/login/')

def cart(request):
	if request.user.is_authenticated():
		cart = Cart.objects.filter(user=request.user.id, active=True)
		orders1 = GameOrder.objects.filter(cart=cart)
		orders2 = MouseOrder.objects.filter(cart=cart)
		total = 0
		count = 0
		for order in orders1:
			total += (order.game.price * order.quantity)
			count += order.quantity
		for order in orders2:
			total += (order.mouse.price * order.quantity)
			count += order.quantity
		context = {
			'cart_game': orders1,
			'cart_mouse': orders2,
			'total': total,
			'count': count
		}
		template = 'cart.html'
		return render(request,template,context)
	else:
		return('/accounts/login/')

def search_titles(request):
	if request.method == 'POST':
		search_text = request.POST.get('search', False)
	else:
		search_text = ''
	post1 = games.objects.filter(game_name__contains=search_text)
	post2 = mouse.objects.filter(mouse_name__contains=search_text)
	paginator1 = Paginator(post1, 4)
	page = request.GET.get('page')
	try:
		game = paginator1.page(page)
	except PageNotAnInteger:
		game = paginator1.page(1)
	except EmptyPage:
		game = paginator1.page(paginator1.num_pages)
	paginator2 = Paginator(post2 , 4)
	page1 = request.GET.get('page1')
	try:
		mouses = paginator2.page(page1)
	except PageNotAnInteger:
		mouses = paginator2.page(1)
	except EmptyPage:
		mouses = paginator2.page(paginator2.num_pages)
	context = {'game': game, 'mouse': mouses, 'page':page, 'page1':page1}
	return render(request, 'search.html', context)
	print(search_text)