# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.views import generic

# Create your views here.


class IndexView(generic.ListView):
    template_name = 'article/index.html'
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
        #return Article.objects.all()
        return None

