from django.http import HttpResponse

from formtools.wizard.views import CookieWizardView

from .forms import ToppingMultiModelForm


class NewToppingMultimodelView(CookieWizardView):
    form_list = [('topping_multimodel_form', ToppingMultiModelForm)]

    def done(self, form_list, **kwargs):
        return HttpResponse('Your multiform just completed a wizard')
