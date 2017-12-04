from django.shortcuts import render

def render_page(request, page_slug):
	return render(request, 'main/'+page_slug+'.html' )