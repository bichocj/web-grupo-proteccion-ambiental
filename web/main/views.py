from django.shortcuts import render


def render_page(request, page_slug):
    try:
        return render(request, 'main/' + page_slug + '.html')
    except:
        return not_found(request)


def render_home(request):
    return render_page(request, 'index')


def not_found(request):
    return render(request, 'main/common/404.html', locals(), status=404)


def bad_request(request):
    return render(request, "main/common/500.html", locals(), status=500)
