from datetime import datetime, timedelta
from typing import Optional, Union

import jwt
from django.conf import settings
from django.http import HttpResponse

from .models import SubscriptionEmail


def generate_confirmation_token(email: str) -> str:
    payload = {
        'user_email': email,
        'exp': datetime.utcnow() + timedelta(minutes=30),
        'iat': datetime.utcnow()
    }

    # Generates a web token in json format with expiry of 30 minutes
    return jwt.encode(payload, settings.SECRET_KEY, algorithm='HS256')


def verify_token(token: str) -> Optional[Union[HttpResponse, SubscriptionEmail]]:
    try:
        # deocodes the the token generated for confirmation link
        payload = jwt.decode(
            token, settings.SECRET_KEY, algorithms=['HS256'])

    except jwt.ExpiredSignatureError:
        return HttpResponse("Link Expired!")

    # verifies the user from the decoded token
    user = SubscriptionEmail.objects.filter(
        email=payload.get('user_email')).first()

    return (user, None)


def send_confirmation_link(email: str, **kwargs) -> None:
    from django.core.mail import EmailMessage
    from django.template.loader import get_template

    token = generate_confirmation_token(email)
    template = get_template('newsletter/confirm.html')
    subject = 'Confirm Your Subscription'
    _from = 'noreply@djangonewsletter.com'
    context = {
        'email': email,
        'token': token,
        'protocol': kwargs['scheme'],
        'domain': kwargs['host']
    }

    # pass the domain and protocol context from request &
    # other required credentials while sending email
    content = template.render(context)
    msg = EmailMessage(subject, content, _from, to=[email])
    msg.send()


def send_already_exist_email(email: str) -> None:
    from django.core.mail import send_mail

    subject = 'Already Subscribed!'
    content = 'You are already our member!'
    _from = 'noreply@djangonewsletter.com'

    send_mail(subject, content, _from, [email], fail_silently=False)
