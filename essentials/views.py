# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.views import generic
from django.shortcuts import render


class IndexView(generic.TemplateView):
    """ TemplateView does not require a model queryset """
    template_name = 'essentials/index.html'

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)

        context.update({
                'days': [1, 2, 3],
            })

        return context


class _IndexView(generic.ListView):
    template_name = 'essentials/index.html'
    context_object_name = 'latest_question_list'

#    def get_queryset(self):
#        """Return the last five published questions."""
#        return Question.objects.order_by('-pub_date')[:5]

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)

        context.update({
                'days': [1, 2, 3],
            })

        return context

    def get_queryset(self):
		return None


