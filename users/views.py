from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.tokens import default_token_generator
from django.contrib.auth.views import PasswordResetConfirmView, PasswordResetView, LoginView, LogoutView
from django.contrib.messages.views import SuccessMessageMixin

from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import CreateView, UpdateView, TemplateView

from users.forms import UserRegisterForm, UserProfileForm, UserForgotPasswordForm, UserSetNewPasswordForm
from users.models import User
from users.utils.utils import auth_send_mail

class UserLoginView(LoginView):
    """Вход на сайт"""
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['title'] = 'Вход на сайт'
        return context


class UserLogoutView(LogoutView):
    """Выход с сайта"""
    pass


class RegisterView(CreateView):
    """Регистрация пользователя"""
    model = User
    form_class = UserRegisterForm
    template_name = 'users/register.html'
    success_url = reverse_lazy('users:login')
    success_message = 'Регистрация прошла успешно. Ссылка для активации аккаунта отправлена на почту'

    def get_context_data(self, *args, **kwargs):
        """Добавляем значение [title]"""
        context = super().get_context_data(*args, **kwargs)
        context['title'] = 'Регистрация на сайте'
        return context

    def form_valid(self, form):
        """Формируем письмо и отправляем пользователю, который только зарегился"""
        user = form.save(commit=False)
        user.is_active = False
        user.token = default_token_generator.make_token(user)
        activation_url = reverse_lazy(
            'users:confirm_email', kwargs={'token': user.token}
        )
        auth_send_mail(user.email, activation_url)
        user.save()
        return redirect('users:email_confirmation_sent')


class UserProfileView(LoginRequiredMixin, UpdateView):
    """Просмотр профиля"""
    model = User
    form_class = UserProfileForm
    success_url = reverse_lazy('users:profile')
    template_name = 'users/user_form.html'

    def get_object(self, queryset=None):
        return self.request.user

    def get_context_data(self, **kwargs):
        """Добавляем значение [title]"""
        context = super().get_context_data(**kwargs)
        context['title'] = f'{self.object.first_name} {self.object.last_name} ({self.object.email})'
        return context


class EmailConfirmationSentView(TemplateView):
    """ Отправка письмо активации"""
    template_name = 'users/email_confirmation_sent.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Письмо активации отправлено'
        return context


class UserConfirmEmailView(View):
    """Проверка ссылки и активация профиля"""
    def get(self, request, token):
        try:
            user = User.objects.get(token=token)
        except User.DoesNotExist:
            return redirect('users:email_confirmation_failed')

        user.is_active = True
        user.token = None
        user.save()
        return redirect('users:email_verified')


class EmailConfirmView(TemplateView):

    template_name = 'users/email_verified.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Ваш электронный адрес активирован'
        return context


class EmailConfirmationFailedView(TemplateView):
    template_name = 'users/email_confirmation_failed.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Ваш электронный адрес не активирован'
        return context

class UserForgotPasswordView(SuccessMessageMixin, PasswordResetView):
    """
    Представление по сбросу пароля по почте
    """
    form_class = UserForgotPasswordForm
    template_name = 'users/user_password_reset.html'
    success_url = reverse_lazy('users:password_reset_sent')
    success_message = 'Письмо с инструкцией по восстановлению пароля отправлена на ваш email'
    subject_template_name = 'users/password_subject_reset_mail.txt'
    email_template_name = 'users/password_reset_mail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Запрос на восстановление пароля'
        return context


class UserPasswordResetConfirmView(SuccessMessageMixin, PasswordResetConfirmView):
    """
    установка нового пароля
    """
    form_class = UserSetNewPasswordForm
    template_name = 'users/user_password_set_new.html'
    success_url = reverse_lazy('users:password_success_sent')
    success_message = 'Пароль успешно изменен. Можете авторизоваться на сайте.'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Установить новый пароль'
        return context


class PasswordResetSentView(TemplateView):
    template_name = 'users/password_reset_sent.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Письмо активации отправлено'
        return context


class PasswordSuccessSentView(TemplateView):
    template_name = 'users/password_success_sent.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Вы сменили пароль'
        return context

