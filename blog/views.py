from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.utils import timezone
from django.shortcuts import render,redirect
from django.views.generic import ListView, DetailView
from blog.models import Module, Instructor, Content_Type, ModuleInstance 
from .forms import ModuleForm, InstructorForm
# Create your views here.


def index(request):
    """View function for home page of site."""

    # Generate counts of some of the main objects
    num_modules = Module.objects.all().count()   
    num_instructors = Instructor.objects.count()
    # Number of visits to this view, as counted in the session variable.
    num_visits = request.session.get('num_visits', 0)
    request.session['num_visits'] = num_visits + 1

    context = {
        'num_modules': num_modules,
        'num_instructors': num_instructors,
        'num_visits': num_visits,
    }


# Render the HTML template index.html
    return render(request, 'blog/index.html', context=context)

class ModuleListView(ListView):
    """Generic class-based list view for module"""
    #model= Module
    queryset = Module.objects.all()
    paginate_by = 4


class ModuleDetailView(DetailView):
    model = Module
    template_name = 'blog/module_detail.html'
    def get(self, request, *args, **kwargs):
        module = get_object_or_404(Module, pk=kwargs['pk'])
        context = {'module': module}
        return render(request, 'blog/module_detail.html', context)
    
    

class InstructorListView(ListView):
    """Generic class-based list view for a list of instructors."""
    model = Instructor
    paginate_by = 10


class InstructorDetailView(DetailView):
    """Generic class-based detail view for an instructor."""
    model = Instructor
    template_name = 'blog/instructor_detail.html'

def new_module(request):
    """ Add a new module """
    if request.method != 'POST':
        #No data submitted; creat a blank form.
        form = ModuleForm()
    else:
        # POST data submitted; process data
        form = ModuleForm(data= request.POST)
        if form.is_valid():
            form.save()
            return redirect ('blog:modules')

    # Display a blank or invalid form.
    context = {'form': form}
    return render (request, 'blog/new_module.html', context)

    def new_instructor(request):
        """ Add a new instructor for module"""
        module = Module.objects.get(pk=pk)

        if request.method != 'POST':
        #No data submitted; creat a blank form.
        form = InstructorForm()
        else:
            # POST data submitted; process data
            form = InstructorForm(data= request.POST)
            if form.is_valid():
            form.save()
            return redirect ('blog:modules', pk=pk)
        
        # Display a blank or invalid form.
    context = {'form': form}
    return render (request, 'blog/new_instructor.html', context)

        

        

        

    

