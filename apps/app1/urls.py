from django.urls import path
from . import views  # Import views from the current directory

urlpatterns = [
    path('', views.index, name='index'),  # landing page
    path('login/', views.login_view, name='login'),  # Login page view
    path('createteam/', views.createteam, name='createteam'),  # createteam URL
    path('manageteam/', views.manageteam, name='manageteam'),  # createteam URL
   #path('create-campaign/', views.create_campaign, name='createcampaign'),
    path('email-campaign/', views.email_campaign, name='emailcampaign'),
    path('sms-campaign/', views.sms_campaign, name='smscampaign'),
    path('campaign-details/', views.campaign_details, name='campaigndetails'),
    path('user-report/', views.user_report, name='userreport'),
    path('whatsapp-campaign/', views.whatsapp_campaign, name='whatsappcampaign'),
    path('phishing-material/', views.phishing_material, name='phishingmaterial'),
    
   #path('camp/', views.campaign_create, name='campaign_create'),
    path('groups/', views.create_group, name='group_list')
]
