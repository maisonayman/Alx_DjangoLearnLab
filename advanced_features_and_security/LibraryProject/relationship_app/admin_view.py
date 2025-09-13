from django.shortcuts import render
from django.contrib.auth.decorators import user_passes_test
from .access_checks import is_admin  # استدعاء الشرط

@user_passes_test(is_admin, login_url='/no-access/')
def admin_dashboard(request):
    return render(request, 'admin_view.html')
