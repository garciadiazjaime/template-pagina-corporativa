from django.shortcuts import render_to_response

# Inicio
def home(request):
	return render_to_response('inicio.html')