from django.shortcuts import render

from .models import ExampleForm, ExampleModel

# Create your views here.
def example(request):
    if request.method == 'POST':
        form = ExampleForm(request.POST)
        form.save()
    example_model = ExampleModel.objects.all()
    return render(request, 'example/example.html', {'example_model': example_model})
