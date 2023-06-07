from itertools import chain

from django.contrib.auth import logout, login
from django.contrib.auth.views import LoginView
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.db.models import Q
from django.http import HttpResponse, Http404
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import CreateView, ListView

from .models import *
from .forms import *
from .utils import *


def index(request):
    medallions = Medallion.objects.all()
    earring = Earrings.objects.all()
    rings = Ring.objects.all()
    cats = Category.objects.all()
    context = {
        'medallion': medallions,
        'earrings': earring,
        'cats': cats,
        'ring': rings,
        'cat_selected': 0,
        'title': 'Главная страница'
    }
    return render(request, 'shop/index.html', context=context)


def medallion(request):
    medallions = Medallion.objects.all()
    cats = Category.objects.all()

    context = {
        'medallion': medallions,
        'cats': cats,
        'title': 'Медальоны',
        'cat_selected': 0,
    }
    return render(request, 'shop/medallions.html', context=context)


def earrings(request):
    earring = Earrings.objects.all()
    cats = Category.objects.all()

    context = {
        'earrings': earring,
        'cats': cats,
        'title': 'Серьги',
        'cat_selected': 0,
    }
    return render(request, 'shop/earrings.html', context=context)


def ring(request):
    rings = Ring.objects.all()
    cats = Category.objects.all()

    context = {
        'ring': rings,
        'cats': cats,
        'title': 'Кольца',
        'cat_selected': 0,
    }
    return render(request, 'shop/rings.html', context=context)


def show_post_earring(request, earrings_id):
    earring = get_object_or_404(Medallion, pk=earrings_id)
    context = {
        'earrings': earring,
        'title': earring.titleEarrings,
        'cat_selected': earring.cat_id,
    }
    session_key = request.session.session_key
    if not session_key:
        request.session.cycle_key()

    print(request.session.session_key)
    return render(request, 'shop/post_earring.html', context=context)


def show_post_medallion(request, medallion_id):
    medallions = get_object_or_404(Medallion, pk=medallion_id)
    context = {
        'medallion': medallions,
        'title': medallions.titleMedallion,
        'cat_selected': medallions.cat_id,
    }
    session_key = request.session.session_key
    if not session_key:
        request.session.cycle_key()

    print(request.session.session_key)
    return render(request, 'shop/post_medallion.html', context=context)


def show_post_ring(request, ring_id):
    rings = get_object_or_404(Ring, pk=ring_id)
    context = {
        'ring': rings,
        'title': rings.titleRing,
        'cat_selected': rings.cat_id,
    }
    session_key = request.session.session_key
    if not session_key:
        request.session.cycle_key()

    print(request.session.session_key)
    return render(request, 'shop/post_ring.html', context=context)


def show_category(request, cat_id):
    medallions = Medallion.objects.filter(cat_id=cat_id)
    rings = Ring.objects.filter(cat_id=cat_id)
    earring = Earrings.objects.filter(cat_id=cat_id)
    cats = Category.objects.all()

    if len(rings) == 0 and len(medallions) == 0 and len(earring) == 0:
        raise Http404()

    context = {
        'medallion': medallions,
        'ring': rings,
        'earrings': earring,
        'cats': cats,
        'title': 'Отображение по событиям',
        'cat_selected': cat_id,
    }

    return render(request, 'shop/index.html', context=context)


class RegisterUser(DataMixin, CreateView):
    form_class = RegisterUserForm
    template_name = 'shop/register.html'
    success_url = reverse_lazy('login')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Регистрация")
        return dict(list(context.items()) + list(c_def.items()))

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('home')


class LoginUser(DataMixin, LoginView):
    form_class = LoginUserForm
    template_name = 'shop/login.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Авторизация")
        return dict(list(context.items()) + list(c_def.items()))

    def get_success_url(self):
        return reverse_lazy('home')


def logout_user(request):
    logout(request)
    return redirect('login')


class SearchResultsView(ListView):
    model = [Medallion, Ring, Earrings]
    template_name = 'search_results.html'

    def get_queryset(self):  #
        query = self.request.GET.get('q')

        object_list1 = Ring.objects.filter(Q(titleRing__icontains=query) | Q(metalRing__icontains=query))
        object_list2 = Medallion.objects.filter(Q(ttitleMedallion__icontains=query) | Q(mmetalMedallion__icontains=query))
        object_list3 = Earrings.objects.filter(Q(titleEarrings__icontains=query) | Q(metalEarrings__icontains=query))
        return object_list1, object_list2, object_list3
