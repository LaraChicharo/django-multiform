from django.conf.urls import url
import views


urlpatterns = [
    url(
        r'^new-topping/$',
        views.NewToppingMultimodelView.as_view(),
        name='new_topping',
    ),
]
