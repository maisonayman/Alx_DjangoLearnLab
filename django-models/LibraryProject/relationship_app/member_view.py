from django.shortcuts import render
from django.contrib.auth.decorators import user_passes_test
from .access_checks import is_member

@user_passes_test(is_member, login_url='/no-access/')
def member_dashboard(request):
    return render(request, 'member_view.html')
