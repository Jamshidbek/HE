from django.shortcuts import render, get_object_or_404, redirect
# from .models import RSA
# from .forms import PostForm


def algorithm_list(request):
    # algorithms = Al.objects.all()
    return render(request, 'algorithm/algorithm_list.html', {})
