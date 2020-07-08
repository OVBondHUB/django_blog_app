from django.shortcuts import render, get_list_or_404, get_object_or_404


class ObjectDetailMixin:
    model = None
    template = None

    def get(self, request, slug):
        obj = get_object_or_404(self.model, slug__iexact=slug)
        return render(request, self.template, context={self.model.__name__.lower(): obj})


class ObjectListMixin:
    model = None
    template = None
    context_list_name = None

    def get(self, request):
        obj_list = get_list_or_404(self.model)
        return render(request, self.template, context={self.context_list_name: obj_list})
