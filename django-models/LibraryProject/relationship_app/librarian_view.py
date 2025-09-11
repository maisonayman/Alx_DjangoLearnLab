from django.shortcuts import render
from django.contrib.auth.decorators import user_passes_test
from .access_checks import is_librarian

@user_passes_test(is_librarian, login_url='/no-access/')
def librarian_dashboard(request):
    return render(request, 'librarian_view.html')
