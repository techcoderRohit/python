import requests

def fetch_random_user_freeapi():
    url = "https://api.freeapi.app/api/v1/public/randomusers/user/random"
    response = requests.get(url)
    data = response.json()

    if data["success"] and "data" in data:
        user_data = data["data"]
        username = user_data.get("login", {}).get("username", "N/A") 
        country = user_data.get("location", {}).get("country", "N/A") 
        return username, country
    else:
        raise Exception("Failed to fetch user data")
    

def main():
    try:
       username, country = fetch_random_user_freeapi()
       print(f"Username : {username} \npyCountry: {country}")
    except Exception as e:
        print(str(e)) 

if __name__ == "__main__":
    main()