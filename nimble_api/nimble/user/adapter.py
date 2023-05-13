from allauth.socialaccount.adapter import DefaultSocialAccountAdapter
from allauth.account.adapter import DefaultAccountAdapter
from .models import User


class SocialAccountAdapter(DefaultSocialAccountAdapter):
    def pre_social_login(self, request, sociallogin):
        user = sociallogin.user
        if user.id:
            return
        try:
            user = User.objects.get(email=user.email)
            sociallogin.connect(request, user)
        except User.DoesNotExist:
            pass


class DefaultAccountAdapterCustom(DefaultAccountAdapter):
    def send_mail(self, template_prefix, email, context):
        context['activate_url'] = 'https://app.nimble.com/verification/' + context['key']
        msg = self.render_mail(template_prefix, email, context)
        msg.send()
