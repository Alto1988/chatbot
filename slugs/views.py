from django.shortcuts import render
from django.views.generic.list import ListView

from .models import Groups


class ManageGroupsListView(ListView):
    model = Groups
    template_name = 'slugs/manage/group/list.html'

    def get_queryset(self):
        query_set = super().get_queryset()
        return query_set.filter(owner=self.request.user)
