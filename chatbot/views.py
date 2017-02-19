from django.views.generic.base import TemplateView


class ChatBotAppView(TemplateView):
    template_name = "app.html"

