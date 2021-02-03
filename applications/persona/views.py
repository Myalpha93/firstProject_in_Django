from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    TemplateView,
    UpdateView,
    DeleteView,
    )
#Models
from .models import Empleado
from .forms import EmpleadoForm
# Create your views here.
#1. Lista de todos los empleados
#2. Listar todos los empleados que pertenezcan a una de la empresa
#3. Listar empleados por trabajo
#4. Listar los empleados por palabra clave
#5 Listar habilidades de un empleado


class InicioView(TemplateView):
    template_name = "inicio.html"


class ListAllempleadosListView(ListView):
    template_name = "persona/ListaEmpleados.html"
    paginate_by = 4
    ordering = 'first_name'

    def get_queryset(self):
        palabra_clave = self.request.GET.get("kword",'')
        lista= Empleado.objects.filter(
        first_name__icontains=palabra_clave
        )
        return lista 

class ListbyAreaEmpleadosListView(ListView):
    """ Lista empleados por area """
    template_name = "persona/ListbyArea.html"
    context_object_name= 'empleados'

    def get_queryset(self):
        area = self.kwargs['shorname']
        lista= Empleado.objects.filter(
        departamento__shor_name=area
    )
        return lista

class ListbyAreaEmpleadosAdmin(ListView):
    """ Lista empleados por area """
    template_name = "persona/lista-empleado-admin.html"
    context_object_name= 'empleados'
    paginate_by = 10
    ordering = 'first_name'
    model = Empleado

class ListEmpleadoByKwordListView(ListView):
    """ Lista empleados por palabra clave"""
    template_name = "persona/by_kword.html"
    context_object_name = "empleados"
    
    def get_queryset(self):
        print('*********************************')
        palabra_clave = self.request.GET.get("kword",'')
        lista= Empleado.objects.filter(
        first_name=palabra_clave
        )
        return lista 
    

class ListHabilidadesListView(ListView):
    template_name = "persona/lista_habilidades.html"
    context_object_name = "habilidades"

    def get_queryset(self):
        empleado= Empleado.objects.get(id=1)
        print(empleado.habilidades.all())
        return empleado.habilidades.all()


class EmpleadoDetailView(DetailView):
    model = Empleado
    template_name = "persona/detalle_empleado.html"

    def get_context_data(self, **kwargs):
        context = super(EmpleadoDetailView, self).get_context_data(**kwargs)
        context['titulo']= 'Empleado del mes'
        return context


class SuccessView(TemplateView):
    template_name = "persona/success.html"
    

class EmpleadoCreateView(CreateView):
    model = Empleado
    template_name = "persona/crearEmpleado.html"
    form_class= EmpleadoForm
    # fields = ('__all__')
    success_url = reverse_lazy('persona_app:lista_empleados_admin')
    #aqui reedirecciona si todo se guardo correctamente

    def form_valid(self,form):
        #logica del proceso
        empleado = form.save(commit=False)
        empleado.full_name = empleado.first_name + ' ' + empleado.last_name
        empleado.save()
        print(empleado)
        return super(EmpleadoCreateView, self).form_valid(form)


class EmpleadoUpdateView(UpdateView):
    model = Empleado
    template_name = "persona/UpdateEmpleado.html"
    fields = [
        'first_name',
        'last_name',
        'job',
        'departamento',
        'habilidades',
        'avatar',
        ]
    success_url = reverse_lazy('persona_app:lista_empleados_admin')

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        print('************METODO POST****************')
        print(request.POST)
        print(request.POST['last_name'])
        return super().post(request, *args, **kwargs)

    def form_valid(self,form):
        #logica del proceso
        
        print('************METODO FORM VALUE****************')
        return super(EmpleadoUpdateView, self).form_valid(form)


class EmpleadoDeleteView(DeleteView):
    model = Empleado
    template_name = "persona/delete_empleado.html"
    success_url = reverse_lazy('persona_app:lista_empleados_admin')
