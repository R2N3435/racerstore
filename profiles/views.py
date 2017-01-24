from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.db import transaction
from .forms import UserForm, ProfileForm
from django.contrib import messages
from shop.models import games, mouse, Recommend_game, Recommend_mouse
from django.core.exceptions import ObjectDoesNotExist
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
import random
# Create your views here.
def home(request):
    template = 'home.html'
    context={}
    if request.user.is_authenticated():
        i = request.user.id
        try:
            g = open(str(i)+'.txt','r')
        except:
            pass
        else:
            list_game=[]
            list_mouse=[]
            for lines in g:
                if 'game' in lines:
                    list_game.append(lines)
                elif 'mouse' in lines:
                    list_mouse.append(lines)
                else:
                    pass
            for g in range(0,len(list_game)):
                gameid = list_game[g]
                gameid = gameid[6:-1]
                list_game[g] = gameid
            for m in range(0,len(list_mouse)):
                mouseid = list_mouse[m]
                mouseid = mouseid[7:-1]
                list_mouse[m] = mouseid
            try:
                recomend = Recommend_game.objects.all()
            except ObjectDoesNotExist:
                pass
            else:
                recomend.delete()
            try:
                recomend = Recommend_mouse.objects.all()
            except ObjectDoesNotExist:
                pass
            else:
                recomend.delete()
            for gid in list_game:
                game = games.objects.get(pk=gid)
                game.recomend_game(gid)
            for mid in list_mouse:
                mouses = mouse.objects.get(pk=mid)
                mouses.recomend_mouse(mid)
            for gid in list_game:
                game = games.objects.get(pk=gid)
                try:
                    recom = Recommend_game.objects.get(recomend_game=game)
                except ObjectDoesNotExist:
                    pass
                else:
                    recom.delete()
            for mid in list_mouse:
                mouses = mouse.objects.get(pk=mid)
                try:
                    recom = Recommend_mouse.objects.get(recomend_mouse=mouses)
                except ObjectDoesNotExist:
                    pass
                else:
                    recom.delete()
            rgame = Recommend_game.objects.all()
            rmouse = Recommend_mouse.objects.all()
            paginator1 = Paginator(rgame, 5)
            page = request.GET.get('page')
            try:
                game = paginator1.page(page)
            except PageNotAnInteger:
                game = paginator1.page(1)
            except EmptyPage:
                game = paginator1.page(paginator1.num_pages)
            paginator2 = Paginator(rmouse , 5)
            page1 = request.GET.get('page1')
            try:
                mouses = paginator2.page(page1)
            except PageNotAnInteger:
                mouses = paginator2.page(1)
            except EmptyPage:
                mouses = paginator2.page(paginator2.num_pages)
            context={'rgame': game, 'rmouse': mouses, 'page': page, 'page1': page1}
    rangame = games.objects.all()
    ranmouse = mouse.objects.all()
    ragame = []
    ramouse = []
    check = []
    while len(ragame) < 5:
        i = random.randrange(0,len(rangame))
        if rangame[i] in check:
            continue
        check.append(rangame[i])
        ragame.append(rangame[i])
    while len(ramouse) < 5:
        i = random.randrange(0,len(ranmouse))
        if ranmouse[i] in check:
            continue
        check.append(ranmouse[i])
        ramouse.append(ranmouse[i])
    context['ragame'] = ragame
    context['ramouse'] = ramouse
    return render(request,template,context)

@login_required
@transaction.atomic
def buy(request):
    if request.method == 'POST':
        user_form = UserForm(request.POST, instance=request.user)
        profile_form = ProfileForm(request.POST, instance=request.user.profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, 'Your profile was successfully updated!')
            return redirect('mode_payment')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        user_form = UserForm(instance=request.user)
        profile_form = ProfileForm(instance=request.user.profile)
    context = {'user_form':user_form, 'profile_form':profile_form}
    template = 'profile.html'
    return render(request, template, context)
