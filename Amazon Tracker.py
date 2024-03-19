import lxml
import requests
import smtplib
from bs4 import BeautifulSoup
URL = "https://www.amazon.in/Pigeon-single-Aluminium-Electric-cooker/dp/B01N7WZ675/ref=sr_1_2_sspa?crid=1B4UBGQB10Y4H&dib=eyJ2IjoiMSJ9.ALEjbR9LN70bEcwsqQmP6ZSmYZciezlp3tnxbbOpmUc46yKKRJKtN7Ee7p6tHXguBKMZLWjsZ4CdvcUajJlzcK4V1N0_3cUZ7IcWnXlrK_B5of5TnTgxDBGM6U-1d8kseqJrV34MTvUJHfAlNeYOx34tiI67BCwNbgkVBos9aU20x2lUaLLKG8rH60UWCVzmJ-pNOVxRKgeEnm64JXdluBAKJSusUGzLZG967ltjQLKQHcHye05kirKZA56oa5moOYl07iEUhGKGzyRmrgTsaIWbc4yjtLXtO7HaFVgkecU.cYfVCX3wtT_Vx_ZIuEr4_pPHRcfMhV9EHVOPNbM28hc&dib_tag=se&keywords=rice+cooker&qid=1710353681&s=appliances&sprefix=rice+cooker%2Cappliances%2C708&sr=1-2-spons&sp_csd=d2lkZ2V0TmFtZT1zcF9hdGY&psc=1"
request_header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,/;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "Accept-Language": "en-US,en;q=0.9"
}
my_email = "bimoboti33@gmail.com"
password = "gopw xydg maka evon"
response = requests.get(URL, headers=request_header)
html_text = response.text
#print(html_text)
soup = BeautifulSoup(html_text, "lxml")
price=soup.find(name="span",class_="a-price-whole")
actual_price=price.getText().split(".")[0]
value_with_comma = f"{actual_price}"
value_without_comma = value_with_comma.replace(',', '')
float_value = float(value_without_comma)
print(float_value)
if float(float_value)<1700:
    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email,
                            to_addrs=my_email,
                            msg=f"Subject:Amazon Prime Alert\n\nPigeon by Stovekraft Joy 1.8 Liter Electric Rice Cooker 700 Watt, White{actual_price}\n{URL}".encode("utf-8"))
