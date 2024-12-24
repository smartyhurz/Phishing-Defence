import requests

GOPHISH_API_URL = "http://localhost:3333/api"
GOPHISH_API_KEY = "9ec1e2ce9ecee84b56068193735a9c9b793285a503c60d59b573f2d74a1b4e9f"  # Replace with your actual API key

def create_campaign(name, url, smtp_id, template_id, group_id):
    endpoint = f"{GOPHISH_API_URL}/campaigns/?api_key={GOPHISH_API_KEY}"
    payload = {
        "name": name,
        "email_template": template_id,
        "landing_page": page,
        "url": url,
        "smtp": smtp_id,
        
        "groups": [group_id],
        "launch_date": None,
        "send_by_date": None,
        "login": None
    }
    response = requests.post(endpoint, json=payload)
    if response.status_code == 200:
        return response.json()
    else:
        return {"error": response.text}

def get_campaigns():
    endpoint = f"{GOPHISH_API_URL}/campaigns/?api_key={GOPHISH_API_KEY}"
    response = requests.get(endpoint)
    if response.status_code == 200:
        return response.json()
    else:
        return {"error": response.text}
