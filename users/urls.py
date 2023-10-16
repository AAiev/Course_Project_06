from django.urls import path

from users.apps import UsersConfig
from users.views import RegisterView, UserProfileView, EmailConfirmationSentView, UserConfirmEmailView, \
    EmailConfirmView, EmailConfirmationFailedView, UserForgotPasswordView, UserPasswordResetConfirmView, \
    PasswordResetSentView, PasswordSuccessSentView, UserLoginView, UserLogoutView

app_name = UsersConfig.name


urlpatterns = [
    path('', UserLoginView.as_view(template_name='users/login.html'), name='login'),    # вход
    path('logout/', UserLogoutView.as_view(), name='logout'),   # выход
    path('register/', RegisterView.as_view(), name='register'), # регистрация
    path('profile/', UserProfileView.as_view(), name='profile'),    # профиль
    path('email_confirmation_sent/', EmailConfirmationSentView.as_view(), name='email_confirmation_sent'),  # письмо активации отправлено
    path('confirm_email/<str:token>/', UserConfirmEmailView.as_view()),   # проверка токена
    path('email_confirmed/', EmailConfirmView.as_view(), name='email_verified'), # проверка почты прошла успешно
    path('confirm_email_failed/', EmailConfirmationFailedView.as_view(), name='email_confirmation_failed'), # проверка почты не прошла, ссылка неверная
    path('password-reset/', UserForgotPasswordView.as_view(), name='password_reset'),
    path('set-new-password/<uidb64>/<token>/', UserPasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('password_reset_sent/', PasswordResetSentView.as_view(), name='password_reset_sent'),
    path('password_success_sent/', PasswordSuccessSentView.as_view(), name='password_success_sent'),
]
