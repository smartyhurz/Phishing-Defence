from django.shortcuts import render

# Create your views here.

# View for the homepage
def index(request):
    return render(request, 'pages/index.html')  # Ensure this template exists

# View for login (if you want a custom login view instead of using Django's built-in)
def login_view(request):
    return render(request, 'accounts/login.html')  # Renders 'login.html' from the 'accounts/' directory

def createteam(request):
    return render(request, 'pages/createteam.html')  

def email_campaign(request):
    return render(request, 'pages/emailcampaign.html')  

def sms_campaign(request):
    return render(request, 'pages/smscampaign.html')  

def campaign_details(request):
    return render(request, 'pages/campaigndetails.html')  

def user_report(request):
    return render(request, 'pages/userreport.html')  

def whatsapp_campaign(request):
    return render(request, 'pages/whatsappcampaign.html') 

def phishing_material(request):
    return render(request, 'pages/phishingmaterial.html')
     
# This view returns the content for the modal on Page 1
#def create_campaign(request):
 #   return render(request, 'pages/createcampaign.html')

def manageteam(request):
    return render(request, 'pages/manageteam.html')  








'''from django.shortcuts import render, redirect
from .gophish_api import create_campaign,get_campaigns

def campaign_list(request):
    campaigns = get_campaigns()
    return render(request, "campaign_list.html", {"campaigns": campaigns})

def campaign_create(request):
    if request.method == "POST":
        name = request.POST.get("name")
        url = request.POST.get("url")
        smtp_id = request.POST.get("smtp_id")
        template_id = request.POST.get("template_id")
        group_id = request.POST.get("group_id")
        

        response = create_campaign(name, url, smtp_id, template_id, group_id)
        if "error" in response:
            return render(request, "pages/campaign_create.html", {"error": response["error"]})
        return redirect("pages/campaign_create.html")
    
    return render(request, "pages/campaign_create.html")'''









'''
from datetime import datetime
from django.shortcuts import render, redirect  # Replace with your API logic
import requests

# Replace with your GoPhish API key and URL
GOPHISH_API_KEY = "9ec1e2ce9ecee84b56068193735a9c9b793285a503c60d59b573f2d74a1b4e9f"
GOPHISH_BASE_URL = "http://localhost:3333/api"

def fetch_gophish_data(endpoint):
    """Fetch data from GoPhish API."""
    url = f"{GOPHISH_BASE_URL}/{endpoint}"
    headers = {"Authorization": f"Bearer {GOPHISH_API_KEY}"}
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.json()
    return []

def campaign_create(request):
    if request.method == "POST":
        # Get data from the form
        name = request.POST.get("name")
        url = request.POST.get("url")
        smtp_id = int(request.POST.get("smtp_id"))
        template_id = int(request.POST.get("template_id"))
        group_ids = [int(group_id) for group_id in request.POST.getlist("group_ids")]
        launch_date = request.POST.get("launch_date")
        send_by_date = request.POST.get("send_by_date")

        # Convert dates to ISO 8601 format
        formatted_launch_date = (
            datetime.strptime(launch_date, "%Y-%m-%dT%H:%M").isoformat() if launch_date else None
        )
        formatted_send_by_date = (
            datetime.strptime(send_by_date, "%Y-%m-%dT%H:%M").isoformat() if send_by_date else None
        )

        # Prepare API payload
        payload = {
            "name": name,
            "url": url,
            "smtp_id": smtp_id,
            "template_id": template_id,
            "groups": group_ids,
            "launch_date": formatted_launch_date,
            "send_by_date": formatted_send_by_date,
        }

        # Send request to GoPhish API
        response = requests.post(
            f"{GOPHISH_BASE_URL}/campaigns",
            json=payload,
            headers={"Authorization": f"Bearer {GOPHISH_API_KEY}"},
        )
        
        if response.status_code == 201:
            return redirect("campaign_success")  # Redirect on success
        else:
            return render(
                request,
                "pages/campaign_create.html",
                {"error": response.json().get("message", "An error occurred")},
            )

    # Fetch data for the form dropdowns
    smtp_profiles = fetch_gophish_data("smtp")
    email_templates = fetch_gophish_data("templates")
    groups = fetch_gophish_data("groups")

    return render(
        request,
        "pages/campaign_create.html",
        {
            "smtp_profiles": smtp_profiles,
            "email_templates": email_templates,
            "groups": groups,
        },
    )'''







# views.py
'''import requests
from django.shortcuts import render, redirect
from django.http import HttpResponse


# Gophish API URL and API Key (replace with actual values)
GOPHISH_API_URL = 'http://localhost:3333/api/groups'
API_KEY = '9ec1e2ce9ecee84b56068193735a9c9b793285a503c60d59b573f2d74a1b4e9f'


def create_group(request):
    if request.method == 'POST':
        group_name = request.POST.get('group_name')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        position = request.POST.get('position')

        # Prepare data to send to Gophish API
        data = {
    "name": group_name,
    "users": [
        {
            "email": email,
            "first_name": first_name,
            "last_name": last_name,
            "position": position
        }
    ]
}
        # Send the data to Gophish API using a POST request
        headers = {
            "Authorization": f"Bearer {API_KEY}",
            "Content-Type": "application/json"
        }

        try:
            # Make the API request
            response = requests.post(GOPHISH_API_URL, json=data, headers=headers)

            # Handle the API response
            if response.status_code == 201:  # Gophish typically uses 201 for created resources
                return redirect('group_list')  # Redirect to group list or success page
            else:
                # Log and return error response for debugging
                error_message = f"Error: {response.status_code} - {response.text}"
                return HttpResponse(error_message, status=response.status_code)

        except requests.exceptions.RequestException as e:
            # Handle network or connection errors
            return HttpResponse(f"Connection error: {str(e)}", status=500)

    return render(request, 'pages/group_list.html')'''


import json
import requests
from django.shortcuts import render, redirect
from django.http import HttpResponse

# Gophish API URL and API Key
GOPHISH_API_URL = 'http://localhost:3333/api/groups/'
API_KEY = '9ec1e2ce9ecee84b56068193735a9c9b793285a503c60d59b573f2d74a1b4e9f'

def create_group(request):
    if request.method == 'POST':
        print("POST Data:", request.POST)
        group_name = request.POST.get('group_name')
        users = []

        # # Parse the user details submitted in the form
        # user_details = zip(
        #     request.POST.getlist('first_name'),
        #     request.POST.getlist('last_name'),
        #     request.POST.getlist('email'),
        #     request.POST.getlist('position')
        # )

        # for first_name, last_name, email, position in user_details:
        if not group_name:
            return HttpResponse("Error: Group name is required.", status=400)

        # Parse and validate user details
        first_names = request.POST.getlist('first_name')
        last_names = request.POST.getlist('last_name')
        emails = request.POST.getlist('email')
        positions = request.POST.getlist('position')

        if not (first_names and last_names and emails and positions):
            return HttpResponse("Error: User details are incomplete.", status=400)

        for first_name, last_name, email, position in zip(first_names, last_names, emails, positions):
            # Ensure all fields for each user are provided
            if not all([first_name, last_name, email, position]):
                return HttpResponse("Error: All user fields must be filled.", status=400)
 
         
            users.append({
                "first_name": first_name,
                "last_name": last_name,
                "email": email,
                "position": position
            })

        # Prepare data for Gophish API
        data = {
            "name": group_name,
            "targets": users
        }

        # Send the data to Gophish API using POST request
        headers = {
            "Authorization": f"Bearer {API_KEY}",
            "Content-Type": "application/json"
        }

    #     response = requests.post(GOPHISH_API_URL, json=data, headers=headers)

    #     # Check if the request was successful
    #     if response.status_code == 201:
    #         return redirect('group_list')  # Redirect to group list or success page
    #     else:
    #         return HttpResponse(f"Error: {response.status_code} - {response.text}", status=400)

    # return render(request, 'pages/group_list.html')  # Render your group creation form


        try:
            response = requests.post(GOPHISH_API_URL, json=data, headers=headers)

            # Check if the request was successful
            if response.status_code == 201:
                return redirect('group_list')  # Redirect to group list or success page
            else:
                return HttpResponse(
                    f"Error: Gophish API returned status {response.status_code} - {response.text}",
                    status=400
                )
        except requests.RequestException as e:
            return HttpResponse(f"Error: Could not connect to Gophish API - {e}", status=500)

    return render(request, 'pages/createteam.html')