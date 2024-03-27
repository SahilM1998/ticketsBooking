import requests
from bs4 import BeautifulSoup

def check_ticket_availability():
    url = 'https://in.bookmyshow.com/explore/sports-mumbai'  # URL of the event page on BookMyShow
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Safari/537.36 Edge/12.246'}  # Add your user agent

    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')

    # Locate the relevant HTML elements to determine ticket availability
    # Modify this according to the structure of the BookMyShow website
    available_tickets = soup.find('div', class_='style__StyledText-sc-7o7nez-0 dxpBCo').text.strip()
    print(available_tickets);

    return available_tickets

if __name__ == "__main__":
    availability = check_ticket_availability()
    if "Tickets Available" in availability:
        print("Tickets are available!")
        # You could send an email, SMS, or any other notification method here
    else:
        print("Tickets are not available.")
