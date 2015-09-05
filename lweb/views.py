from django.http import HttpResponse
from django.template import Context, loader
from django.shortcuts import render
from django.http import Http404
from django.shortcuts import render_to_response



from lweb.models import Categoria, Temas

def index(request):
    # return HttpResponse("Hola, bienvenidos a la pagina de Banquetes LATOSO.")
    lista_categorias = Categoria.objects.all().order_by('-pub_date')[:5]

    tms = Temas.objects.all().order_by('?')[:3]
    tms2 = Temas.objects.all().order_by('?')[:5]
    
        
    context = {'lista_categorias': lista_categorias, 'lstms': tms, 'lstms2': tms2}
    
    return render(request, 'index/index.html', context)

#detalle de categorias 
def detail(request, cat_id):
    try:
        lista_categorias = Categoria.objects.all().order_by('-pub_date')[:5]
        p = Categoria.objects.get(pk=cat_id)
        
        tms = Temas.objects.filter(catid=cat_id)
        
        
        tmsk = Temas.objects.all().order_by('?')[:3]
        tms2 = Temas.objects.all().order_by('?')[:5]
        
        
    except Categoria.DoesNotExist:
        raise Http404
    return render(request, 'categos/index.html', {'cat': p, 'lista_categorias': lista_categorias, 'lista_temas': tms, 'lstms': tmsk, 'lstms2': tms2 })

#detalle de tema
def tipo(request, tema_id):
    try:
        lista_categorias = Categoria.objects.all().order_by('-pub_date')[:5]        
        tms = Temas.objects.get(pk=tema_id)
        
        tmsk = Temas.objects.all().order_by('?')[:3]
        tms2 = Temas.objects.all().order_by('?')[:5]
        
        
    except Categoria.DoesNotExist:
        raise Http404
    return render(request, 'temas/index.html', {'lista_categorias': lista_categorias, 'tmdt': tms, 'lstms': tmsk, 'lstms2': tms2 })