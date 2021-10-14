from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LoginView
from django.http.response import HttpResponseBadRequest, HttpResponseRedirect
from django.urls.base import reverse_lazy
from django.views.generic.base import RedirectView
from django.views.generic.edit import FormView







    
    
class LoginFormView2(FormView):
    form_class = AuthenticationForm
    template_name = 'login.html'
    success_url= reverse_lazy('core.misitio:evaluaciones_listar')
    
    def form_valid(self, form):
        login(self.request, form.get_user())
        return HttpResponseRedirect(self.success_url)
        
        
    
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return HttpResponseRedirect(self.success_url)
        return super().dispatch(request, *args, **kwargs)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context ['title']= 'Inico de Sesion'
        return context


class LogoutView(RedirectView):
    pattern_name = 'login'

    def dispatch(self, request, *args, **kwargs):
        logout(request)
        return super().dispatch(request, *args, **kwargs)    