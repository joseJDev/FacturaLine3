# Django
from django.views.generic import View
from django.shortcuts import redirect, render
from django.utils.decorators import method_decorator
from django.views.decorators.cache import never_cache
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth import login, logout, authenticate

class LoginUserView(View):
    template_name = "login.html"
    def get(self, request, *args, **kwargs):
        print('Hola...')
        if request.user.is_authenticated:
            return redirect('factura:home')
        else:
            return render(request, self.template_name) 
    
    @method_decorator(csrf_protect)
    @method_decorator(never_cache)
    def post(self, request, *args, **kwargs):
        data = request.POST
        print(data)
        email = data.get('email', None)
        password = data.get('password', None)

        if email and password:
            user = authenticate(email=email, password=password)

            if user is not None: # None, False, ""
                login(request, user)
                return redirect('factura:home')
            else:
                print('Nel')
                return render(request, self.template_name, { "error": "Credenciales incorrectas" })
        else:
            return render(request, self.template_name, { "error": "Algo salio..." })

class LogoutUserView(View):
    def get(self, request, *args, **kwargs):
        logout(request)
        return redirect('login')