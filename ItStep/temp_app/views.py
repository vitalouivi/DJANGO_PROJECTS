from django.contrib.auth.decorators import user_passes_test
from django.core.paginator import Paginator
from django.forms.formsets import ORDERING_FIELD_NAME
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, DetailView, CreateView
from .models import Temp, ReverseTemp
from .forms import Temp1Form, Temp2Form, Temp3Form, Temp4Form, formset
from django.db import transaction


def commit_handler():
    print('commit successful')

@user_passes_test(lambda user: user.is_staff)
#@transaction.atomic
def change(request):
    param = []
    if request.method == 'POST':
        TempFormSet = formset(request.POST)
        if TempFormSet.is_valid():
            #with transaction.atomic():
            for form in TempFormSet:
                if form.cleaned_data:
                    sp = transaction.savepoint()
                        #with transaction.atomic():
                    try:
                        temp = form.save(commit=False)
                        temp.order = form.cleaned_data[ORDERING_FIELD_NAME]
                        temp.save()
                        transaction.savepoint(sp)
                    except:
                        transaction.savepoint_rollback(sp)
                    transaction.commit()
                    transaction.on_commit(commit_handler)
            #for temp in TempFormSet.changed_objects:
            #for temp in TempFormSet.new_objects:
            TempFormSet.save(commit=False)
            for temp in TempFormSet.deleted_objects:
                temp.delete()
            return HttpResponseRedirect('/templates')
    else:
        TempFormSet = formset()

    context = {'formset': TempFormSet}
    return render(request, 'temp_app/formset.html', context)


def edit(request, slug):
    tp = Temp.objects.get(slug=slug)
    if request.method == 'POST':
        tpf = Temp3Form(request.POST, instance=tp)
        if tpf.is_valid():
            try:
                content = tpf.cleaned_data['content']
                tpf.save()
                tp.content = content
                tp.save()
                #if content.contains(ругательства):
                #    transaction.rollback()
                #else:
                transaction.commit()
            except:
                transaction.rollback()
            return HttpResponseRedirect(reverse('temp:detail-temp', kwargs={'slug': tpf.cleaned_data['slug']}))
        else:
            context = {'form': tpf}
            html = '<h1>Incorrect form</h1><a href="<slug:slug>"><input type="submit" value="Исправить"></a>'
            html = html.replace('<slug:slug>', str(slug))
            return HttpResponse(html)
            #return render(request, 'temp_app/create.html', context)
    else:
        tpf = Temp3Form(instance=tp)
        context = {'form': tpf}
        return render(request, 'temp_app/create.html', context)



class TempCreateView(CreateView):
    form_class = Temp3Form
    template_name = "temp_app/create.html"
    success_url = '/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


def testindex(request):
    temps = Temp.objects.all()
    amount = 2
    paginator = Paginator(temps, amount)
    if 'page' in request.GET:
        page_num = request.GET['page']
    else:
        page_num = 1

    page = paginator.get_page(page_num)

    #print(paginator.count)
    #print(paginator.num_pages)
    #print(paginator.page_range)

    #print(paginator.get_page(3))
    #print(paginator.page(3))
    #print(paginator.get_page(0))
    #print(paginator.get_page(90))
    #print(paginator.page(0.3))
    #print(page.object_list)
    #print(page.number)
    #print(page.paginator)
    #print(page.has_next())
    #print(page.has_previous())
    #print(page.has_other_pages())
    #print(page.next_page_number())
    #print(page.previous_page_number())
    #print(page.start_index())
    #print(page.end_index())

    context = {'page': page, 'temps': page.object_list}
    return render(request, 'temp_app/testindex.html', context)


class TempDetail(DetailView):
    model = Temp
    context_object_name = "tmp"
    template_name = "temp_app/detail.html"


@transaction.non_atomic_requests
class TempListView(ListView):
    model = Temp
    template_name = 'temp_app/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['Tmps'] = Temp.objects.all()
        return context


def create_Temp(request):
    model = Temp
    tf = Temp4Form(request.POST)
    if tf.is_valid():
        tf.save()

    return HttpResponseRedirect(reverse_lazy("temp:detail-temp", kwargs={"slug": tf.cleaned_data['slug']}))


#css_path = 'temp_app/main.css'

#STATIC_URL+css_path --->'static/temp_app/main.css'
# Create your views here.
