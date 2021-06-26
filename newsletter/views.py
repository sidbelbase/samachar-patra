from django.http.response import HttpResponse
from django.shortcuts import render
from django.views.generic import View

from newsletter.models import SubscriptionEmail
from newsletter.utils import (send_already_exist_email, send_confirmation_link,
                              verify_token)

from .forms import SubscriptionForm


class SubscribeView(View):

    def get(self, request):
        form = SubscriptionForm(request.POST or None)
        return render(request, 'newsletter/subscribe.html', {'form': form})

    def post(self, request):
        form = SubscriptionForm(request.POST or None)

        if form.is_valid():
            email = form.cleaned_data.get('email')
            user_exists = SubscriptionEmail.objects.filter(
                email=email).first()

            if user_exists:
                send_already_exist_email(email)
                return HttpResponse('Please check your email!')

            # if user not in database save the email and send confirmation link
            new_user = SubscriptionEmail.objects.create(email=email)
            new_user.save()
            _ctx = {
                'scheme': request.scheme,
                'host': request.get_host()
            }
            send_confirmation_link(new_user.email, **_ctx)
            return HttpResponse('200 : OK')


class ConfirmSignup(View):

    def get(self, _, token):
        from django.shortcuts import redirect
        user = verify_token(token)
        if user is not None:
            return redirect("http://www.google.com")
        return HttpResponse("Either confirmation link expired or there is no user in our server.")
