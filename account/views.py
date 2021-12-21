from django.shortcuts import render, redirect
from django.views import View
from account.foms import RegistrationForm


class RegisterView(View):
    form_class = RegistrationForm
    template_name = 'account/registration.html'
    def get(self,request,*args, **kwargs):
        form = self.form_class()
        return  render (request, self.template_name,
                        {'form': form})
    def post(self, request,*args,**kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            return redirect(...)
        return render(request, self.template_name, {'form':form})
class ActivationView(View):
    pass
#login
class LoginView(View):
    pass
# logaut
class LogoutView(View):
    pass
# smena parol
class ChangePasswordView(View):
    pass
#bosstanovlenie
class ForgotPasswordView(View):
    pass
