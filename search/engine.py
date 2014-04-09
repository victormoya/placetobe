from django.db.models import Q

from events.models import Event


class SearchEngine(object):

    @staticmethod
    def search_method(search):

        keyword_list = search.split()
        event_list = []

        for keyword in keyword_list:

            query = ((Q(category__name__icontains=keyword) | Q(description__icontains=keyword) |
                      Q(title__icontains=keyword) | Q(publisher__username__icontains=keyword) |
                      Q(location__icontains=keyword) | Q(website__icontains=keyword)) & Q(confirmed=True))

            event_list.extend(Event.objects.filter(query))

        return sorted(set(event_list))