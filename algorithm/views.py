from django.shortcuts import render, get_object_or_404, redirect
from .models import RSA, Sezar
from .forms import RSAForm, SezarForm
from .paillier import *


def algorithm_list(request):
    return render(request, 'algorithm/algorithm_list.html', {})


def rsa_view(request):
    if request.method == "POST":
        form = RSAForm(request.POST)
        if form.is_valid():
            rsa = form.save(commit=False)
            rsa.author = request.user
            rsa.title = "RSA"
            rsa.text = "Authors of RSA: Rivest, Shamir and Adleman"
            rsa.n = int(rsa.p) * int(rsa.q)
            rsa.f = (int(rsa.p)-1) * (int(rsa.q)-1)
            rsa.d = rsa.evklid(rsa.f, int(rsa.e))
            rsa.public_key = '({0}, {1})'.format(rsa.e, rsa.n)
            rsa.private_key = '({0}, {1})'.format(rsa.d, rsa.n)
            rsa.a2 = pow(int(rsa.a1), int(rsa.e), rsa.n)
            rsa.b2 = pow(int(rsa.b1), int(rsa.e), rsa.n)
            rsa.a1b1 = int(rsa.a1)*int(rsa.b1)
            rsa.a2b2 = int(rsa.a2)*int(rsa.b2)

            rsa.save()
            return redirect('rsa_result', pk=rsa.pk)
    else:
        form = RSAForm()
    return render(request, 'algorithm/rsa.html', {'form': form})


def rsa_result(request, pk):
    rsa = get_object_or_404(RSA, pk=pk)
    return render(request, 'algorithm/rsa_result.html', {'rsa': rsa})


def sezar_view(request):
    if request.method == "POST":
        form = SezarForm(request.POST)
        if form.is_valid():
            sezar = form.save(commit=False)
            sezar.author = request.user
            sezar.title = "Sezar"

            sezar.ab = sezar.a + sezar.b
            a1 = ''
            b1 = ''
            for i in sezar.a:
                a1 += chr(ord(i) + int(sezar.k))
            for j in sezar.b:
                b1 += chr(ord(j) + int(sezar.k))

            # a2 = ''
            # b2 = ''
            # for i in a1:
            #     a2 += chr(ord(i) - c)
            # for j in b1:
            #     b2 += chr(ord(j) - c)

            sezar.a1 = a1
            sezar.b1 = b1
            sezar.a1b1 = sezar.a1 + sezar.b1
            ba = ''

            for i in sezar.a1b1:
                ba += chr(ord(i) - int(sezar.k))
            sezar.ba = ba

            sezar.save()
            return redirect('sezar_result', pk=sezar.pk)
    else:
        form = SezarForm()
    return render(request, 'algorithm/sezar.html', {'form': form})


def sezar_result(request, pk):
    sezar = get_object_or_404(Sezar, pk=pk)
    return render(request, 'algorithm/sezar_result.html', {'sezar': sezar})
