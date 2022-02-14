from django.contrib.auth import logout
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView, RedirectView, TemplateView
from django.contrib.auth.views import LoginView
from django.contrib.auth.models import User
from user.forms import SignInForm, SignUpForm
from user.models import UserProfile


class SignUpView(CreateView):
    model = User
    form_class = SignUpForm
    template_name = "user/sign-up.html"
    success_url = reverse_lazy('user:sign-in')


class SignInView(LoginView):
    form_class = SignInForm
    template_name = "user/sign-in.html"

    def get_success_url(self):
        user = self.request.user
        user_is_staff = User.objects.filter(is_staff=True).all()
        if user in user_is_staff:
            return reverse_lazy('admin:index')
        else:
            return reverse_lazy('user:profile')


class LogoutView(RedirectView):
    def get_redirect_url(self, *args, **kwargs):
        return reverse('user:sign-in')

    def get(self, request, *args, **kwargs):
        logout(request)
        return super(LogoutView, self).get(request, *args, **kwargs)


class UserProfileView(TemplateView):
    template_name = "user/profile.html"

    def get_context_data(self):
        user = self.request.user
        try:
            profile = UserProfile.objects.get(user=user)
        except UserProfile.DoesNotExist:
            profile = None
        return {"user": user, "profile": profile}
