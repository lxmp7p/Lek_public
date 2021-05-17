from django.shortcuts import render, redirect
# Create your views here.

def ethicalStandard(request):
	return render(request, 'docs/ethical_standards.html')