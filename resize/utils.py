from django.shortcuts import render 
from django.shortcuts import get_object_or_404


class ObjectDetailMixin:
    model = None
    template = None

    def get(self, request, pk):
        obj = get_object_or_404(self.model, pk__iexact=pk)
        return render(request, self.template, context={self.model.__name__.lower(): obj, 'detail': True})
