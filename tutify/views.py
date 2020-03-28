from django.shortcuts import render

def homepage_view(request):
    return render(request, 'tutify/index.html')

def faq_view(request):
	return render(request, 'tutify/faq.html')

def contact_view(request):
	return render(request, 'tutify/contact.html')