from django.urls import path


from .views import GetQualificationView, CreateInvestorView, AddQualificationView, RulesView


urlpatterns = [
    path('investor/', CreateInvestorView.as_view()),
    path('investor/rules', RulesView.as_view()),
    path('investor/qualification', AddQualificationView.as_view()),
    path('investor/<int:investorId>/qualification', GetQualificationView.as_view()),
]
