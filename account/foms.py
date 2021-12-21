from django  import forms
from django.contrib.auth import  get_user_model
User = get_user_model()


class RegistrationForm(forms.ModelForm):
    password = forms.CharField(min_length=6,widget=forms.PasswordInput)
    password_confirm = forms.CharField(min_length=6, widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['email', 'name','password','password_confirm']

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email = email).exists():
            raise forms.ValidationError('Этот email занят')
        return email

    def clean(self):
        data = self.cleaned_data
        password = data.get('password')
        password2 = data.pop('password_confirm')
        if password != password2:
            return forms.ValidationError('Пароли не совпадает')
        return data

    def save(self):
        data = self.cleaned_data
        user = User.objects.create_user(**data)
        user.create_activation_code()
        # TODO:отправка на почту
        return user

class ActivationForm():
    pass

class LoginForm():
    pass
class ChangePasswordForm():
    pass

class RestorePasswordForm():
    pass