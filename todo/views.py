from django.shortcuts import render
from django.http import HttpResponseRedirect

from .forms import UserForm

def get_name(request):
    if request.method == 'POST':
        form = NameForm(request.POST)
        if form.is_valid():
            # process the data in form.cleaned_data as required
            return

    else:
        form = NameForm()

    return render(request, 'name.html', {'form': form})
