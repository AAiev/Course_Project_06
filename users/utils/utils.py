from django.conf import settings
from django.core.mail import send_mail


def auth_send_mail(user_email, activ_url):
    send_mail(
        subject='Подтверждение почты при регистрации',
        message=f'Вы успешно зарегистрировались.\n'
                f'Для завершения регистрации пройдите по ссылке: \n'
                f'http://127.0.0.1:8000{activ_url}',
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=[user_email],
        fail_silently=False
    )