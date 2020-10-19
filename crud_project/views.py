from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, JsonResponse
from django.template.loader import render_to_string
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Izdano
from .forms import IzdanoForm
from django.views.generic import ListView, DetailView
from django.db.models import Q

# Create your views here.
class IndexView(ListView):
    model = Izdano
    template_name = 'index.html'
    context_object_name = 'izdano_list'
    paginate_by = 5
    queryset = Izdano.objects.all().order_by('-redni_br')

def filter_view(request):
    qs = Izdano.objects.all()
    search_bar_query = request.GET.get('search_bar')
    if search_bar_query != '' and search_bar_query is not None:
        qs = qs.filter(Q(preuzeo__icontains=search_bar_query) | Q(naziv_imovine__icontains=search_bar_query) | Q(status__icontains=search_bar_query))
    else:
        return redirect('index')
    context = {
    'queryset':qs
    }
    return render(request, 'search_res.html', context)


def izdano_create(request, form, template_name):
    data = dict()
    paginate_by = 5

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            data['form_is_valid'] = True
            izdano_list = Izdano.objects.all().order_by('-redni_br')
            page = request.GET.get('page',1)
            paginator = Paginator(izdano_list, 5)
            try:
                izdano_list = paginator.page(page)
            except PageNotAnInteger:
                izdano_list = paginator.page(1)
            except EmptyPage:
                izdano_list = paginator.page(num_pages)
            data['html_izdano_list'] = render_to_string('partial_index_list.html', {'izdano_list': izdano_list})

        else:
            data['form_is_valid'] = False

    context = {'form':form}
    data['html_form'] = render_to_string(template_name, context, request=request)
    return JsonResponse(data)


def izdano_create_edit(request):
    if request.method == 'POST':
        form = IzdanoForm(request.POST)
    else:
        form = IzdanoForm()
    return izdano_create(request, form, 'partial_izdano_create.html')


def izdano_edit(request, pk):
    izdano = get_object_or_404(Izdano, pk=pk)
    if request.method == 'POST':
        form = IzdanoForm(request.POST, instance = izdano)
    else:
        form = IzdanoForm(instance=izdano)
    return izdano_create(request, form, 'partial_izdano_edit.html')


def izdano_delete(request, pk):
    izdano = get_object_or_404(Izdano, pk=pk)
    data = dict()
    paginate_by = 5

    if request.method == 'POST':
        izdano.delete()
        data['form_is_valid'] = True  # This is just to play along with the existing code
        izdano_list = Izdano.objects.all().order_by('-redni_br')
        page = request.GET.get('page',1)
        paginator = Paginator(izdano_list, 5)
        try:
            izdano_list = paginator.page(page)
        except PageNotAnInteger:
            izdano_list = paginator.page(1)
        except EmptyPage:
            izdano_list = paginator.page(num_pages)
        data['html_izdano_list'] = render_to_string('partial_index_list.html', {'izdano_list': izdano_list})
    else:
        context = {'izdano': izdano}
        data['html_form'] = render_to_string('partial_izdano_delete.html', context, request=request)
    return JsonResponse(data)

# def create(request):
#     if request.method == 'POST':
#         form = IzdanoForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('index')
#     form = IzdanoForm()
#
#     return render(request,'create.html',{'form': form})


# def edit(request, pk, template_name='edit.html'):
#     izdano = get_object_or_404(Izdano, pk=pk)
#     form = IzdanoForm(request.POST or None, instance = izdano)
#     if form.is_valid():
#         form.save()
#         return redirect('index')
#     return render(request, template_name, {'form':form})
#
# def delete(request, pk, template_name='confirm_delete.html'):
#     izdano = get_object_or_404(Izdano, pk=pk)
#     if request.method=='POST':
#         izdano.delete()
#         return redirect('index')
#     return render(request, template_name, {'object':izdano})


def status(request):
    #stat = get_object_or_404(Izdano, pk=pk)
    #stat.status = 'vraćeno' if stat.status == 'izdano' else 'izdano'
    #stat.save(update_fields=['status'])
    #return redirect('index')
    id = request.GET.get('id', None)
    stat = get_object_or_404(Izdano, pk=id)
    stat.status = 'vraćeno' if stat.status == 'izdano' else 'izdano'
    stat.save(update_fields=['status'])

    data = {
        'id': True,
    }
    #stat.status = 'vraćeno' if stat.status == 'izdano' else 'izdano'
    #stat.save(update_fields=['status'])
    #data = {'radi': stat.save(update_fields=['status'])}
    #try:
        #return JsonResponse({"success": True})
    #except Exception as e:
        #return JsonResponse({"success": False})
    return JsonResponse(data)
