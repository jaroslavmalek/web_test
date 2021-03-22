from django.shortcuts import render, reverse
from .models import Activitie, MemberActivitie
from django.views.generic import DetailView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin


def index(request):
    activities = Activitie.objects.all()
    member_activities = MemberActivitie.objects.all()
    return render(request, 'index.html', {'activities': activities, 'member_activities': member_activities})


class ActivityDetailView(LoginRequiredMixin, DetailView):
    model = Activitie


class MemberActivityCreateView(LoginRequiredMixin, CreateView):
    model = MemberActivitie
    fields = ['member_since', 'activity']

    def form_valid(self, form):
        form.instance.member = self.request.user.profile.member
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('home')





