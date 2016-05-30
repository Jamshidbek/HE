from django.shortcuts import render, get_object_or_404, redirect
from .models import RSA
from .forms import RSAForm


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
