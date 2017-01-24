from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.db import models
import random

# Create your models here.
class games(models.Model):
    game_name = models.CharField(max_length=100)
    game_description = models.TextField(max_length=10000)
    game_logo = models.FileField()
    game_developers = models.CharField(max_length=100)
    price = models.IntegerField()
    game_image1 = models.FileField()
    game_image2 = models.FileField()
    game_image3 = models.FileField()
    simulator = models.BooleanField()
    car = models.BooleanField()
    arcade = models.BooleanField()
    bike = models.BooleanField()
    truck = models.BooleanField()
    dirt = models.BooleanField()
    road = models.BooleanField()

    def __unicode__(self):
        return self.game_name

    def recomend_game(self, game_id):
        recom=[]
        game = games.objects.get(pk=game_id)
        if game.simulator == True:
            sim = games.objects.filter(simulator=True)
            recom.append(sim)
        if game.car == True:
            car = games.objects.filter(car=True)
            recom.append(car)
        if game.arcade == True:
            arcade = games.objects.filter(arcade=True)
            recom.append(arcade)
        if game.dirt == True:
            dirt = games.objects.filter(dirt=True)
            recom.append(dirt)
        if game.road == True:
            road = games.objects.filter(road=True)
            recom.append(road)
        if game.truck == True:
            truck = games.objects.filter(truck=True)
            recom.append(truck)
        if game.bike == True:
            bike = games.objects.filter(bike=True)
            recom.append(bike)
        result = set(recom[0])
        for r in recom[1:]:
            result.intersection_update(r)
        results=[]
        for r in result:
            results.append(r)
        results.remove(game)
        key=[]
        if len(results) < 4:
            k = random.randrange(0,len(recom))
            result = set(recom[k])
            key=[]
            for i in range(1):
                r = random.randrange(0,len(recom))
                if r in key or r == k:
                    while r in key or r == k:
                        r = random.randrange(0,len(recom))
                key.append(r)
                result.intersection_update(recom[r])
            results=[]
            for r in result:
                results.append(r)
            results.remove(game)
            key=[]
            if len(results) > 4:
                for i in range(4):
                    r = random.randrange(0,len(results))
                    if r in key:
                        while r in key:
                            r = random.randrange(0,len(results))
                    key.append(r)
                    try:
                        recommend = Recommend_game.objects.get(recomend_game=results[r])
                    except Recommend_game.DoesNotExist:
                        Recommend_game.objects.create(recomend_game=results[r])
            else:
                for r in results:
                    try:
                        recommend = Recommend_game.objects.get(recomend_game=r)
                    except Recommend_game.DoesNotExist:
                        Recommend_game.objects.create(recomend_game=r)
        else:
            for r in results:
                try:
                    recommend = Recommend_game.objects.get(recomend_game=r)
                except Recommend_game.DoesNotExist:
                    Recommend_game.objects.create(recomend_game=r)

class mouse(models.Model):
    mouse_name = models.CharField(max_length=100)
    mouse_description = models.TextField(max_length=10000)
    mouse_logo = models.FileField()
    mouse_company = models.CharField(max_length=100)
    price = models.IntegerField()
    laser = models.BooleanField()
    custom_weight = models.BooleanField()
    extra_keys = models.BooleanField()
    custom_dpi = models.BooleanField()
    wireless = models.BooleanField(default=False)

    def __unicode__(self):
        return self.mouse_name

    def recomend_mouse(self, mouse_id):
        recom=[]
        mouses = mouse.objects.get(pk=mouse_id)
        if mouses.laser == True:
            laser = mouse.objects.filter(laser=True)
            recom.append(laser)
        if mouses.custom_weight == True:
            custom_weight = mouse.objects.filter(custom_weight=True)
            recom.append(custom_weight)
        if mouses.custom_dpi == True:
            custom_dpi = mouse.objects.filter(custom_dpi=True)
            recom.append(custom_dpi)
        if mouses.extra_keys == True:
            extra_keys = mouse.objects.filter(extra_keys=True)
            recom.append(extra_keys)
        if mouses.wireless == True:
            wireless = mouse.objects.filter(extra_keys=True)
            recom.append(wireless)
        result = set(recom[0])
        for r in recom[1:]:
            result.intersection_update(r)
        results=[]
        for r in result:
            results.append(r)
        results.remove(mouses)
        key=[]
        if len(results) < 4:
            k = random.randrange(0,len(recom))
            result = set(recom[k])
            key=[]
            for i in range(0):
                r = random.randrange(0,len(recom))
                if r in key or r == k:
                    while r in key or r == k:
                        r = random.randrange(0,len(recom))
                key.append(r)
                result.intersection_update(recom[r])
            results=[]
            for r in result:
                results.append(r)
            results.remove(mouses)
            key=[]
            if len(results) > 4:
                for i in range(4):
                    r = random.randrange(0,len(results))
                    if r in key:
                        while r in key:
                            r = random.randrange(0,len(results))
                    key.append(r)
                    try:
                        recommend = Recommend_mouse.objects.get(recomend_mouse=results[r])
                    except Recommend.DoesNotExist:
                        Recommend_mouse.objects.create(recomend_mouse=results[r])
            else:
                for r in results:
                    try:
                        recommend = Recommend_mouse.objects.get(recomend_mouse=r)
                    except Recommend_mouse.DoesNotExist:
                        Recommend_mouse.objects.create(recomend_mouse=r)
        else:
            for r in results:
                try:
                    recommend = Recommend_mouse.objects.get(recomend_mouse=r)
                except Recommend_mouse.DoesNotExist:
                    Recommend_mouse.objects.create(recomend_mouse=r)  

class Cart(models.Model):
    user = models.ForeignKey(User)
    active = models.BooleanField(default=True)

    def add_to_cart(self, game_id):
        game = games.objects.get(pk=game_id)
        try:
            preexisting_order = GameOrder.objects.get(game=game, cart=self)
            preexisting_order.quantity += 1
            preexisting_order.save()
        except GameOrder.DoesNotExist:
            new_order = GameOrder.objects.create(
                game=game,
                cart=self,
                quantity=1
            )
            new_order.save()

    def remove_from_cart(self, game_id):
        game = games.objects.get(pk=game_id)
        try:
            preexisting_order = GameOrder.objects.get(game=game, cart=self)
            if preexisting_order.quantity > 1:
                preexisting_order.quantity -= 1
                preexisting_order.save()
            else:
                preexisting_order.delete()
        except GameOrder.DoesNotExist:
            pass

    def add_to_cart1(self, mouse_id):
        mouses = mouse.objects.get(pk=mouse_id)
        try:
            preexisting_order = MouseOrder.objects.get(mouse=mouses, cart=self)
            preexisting_order.quantity += 1
            preexisting_order.save()
        except MouseOrder.DoesNotExist:
            new_order = MouseOrder.objects.create(
                mouse=mouses,
                cart=self,
                quantity=1
            )
            new_order.save()

    def remove_from_cart1(self, mouse_id):
        mouses = mouse.objects.get(pk=mouse_id)
        try:
            preexisting_order = MouseOrder.objects.get(mouse=mouses, cart=self)
            if preexisting_order.quantity > 1:
                preexisting_order.quantity -= 1
                preexisting_order.save()
            else:
                preexisting_order.delete()
        except MouseOrder.DoesNotExist:
            pass

    def clear_all(self):
        try:
            order1 = GameOrder.objects.all()
            order1.delete()
        except GameOrder.DoesNotExist:
            pass
        try:
            order2 = MouseOrder.objects.all()
            order2.delete()
        except MouseOrder.DoesNotExist:
            pass

class GameOrder(models.Model):
    game = models.ForeignKey(games, on_delete=models.CASCADE)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    quantity = models.IntegerField()

class MouseOrder(models.Model):
    mouse = models.ForeignKey(mouse, on_delete=models.CASCADE)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    quantity = models.IntegerField()

class Recommend_game(models.Model):
    recomend_game = models.ForeignKey(games, on_delete=models.CASCADE)

class Recommend_mouse(models.Model):
    recomend_mouse = models.ForeignKey(mouse, on_delete=models.CASCADE)