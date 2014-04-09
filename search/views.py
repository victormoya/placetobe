from django.contrib import messages
from django.core.urlresolvers import reverse
from django.shortcuts import render, redirect
from django.views.generic import View

from search.engine import SearchEngine


class SearchResultView(View):

    template_name = 'search/result.html'

    def get(self, request):

        s = SearchEngine()

        search = request.GET.get('search', None)
        if search is None:
            messages.error(request, 'No words for search')
            return redirect(reverse('events:list'))

        event_list = s.search_method(search)

        data = {
            'event_count': len(event_list),
            'events': event_list
        }
        return render(request, self.template_name, data)