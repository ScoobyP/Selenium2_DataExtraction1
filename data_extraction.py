from bs4 import BeautifulSoup
import numpy as np
import pandas as pd

# Opening the whole html file and reading it
with open('flipkart_laptops.html', 'r', encoding='utf-8') as f:
    laptop_html = f.read()
soup = BeautifulSoup(laptop_html, 'html.parser')
container = soup.find_all('div', {'class': '_2kHMtA'})

# Running a FOR loop and creating lists to store various data elements
name = []
price = []
rating = []
no_of_ratings_nd_reviews = []
core = []
rom = []
os = []
ram = []
display = []
waranty_period = []
for i in container:
    # Name column
    try:
        title = i.find('div', {'class': '_4rR01T'})
        name.append(title.text)
    except:
        name.append(np.nan)
    # Price column
    try:
        kimat = i.find('div', {'class': '_30jeq3 _1_WHN1'})
        price.append(kimat.text)
    except:
        price.append(np.nan)

    # Stars column
    try:
        stars = i.find('div', {'class': '_3LWZlK'})
        rating.append(stars.text)
    except:
        rating.append(np.nan)

    # No. of ratings and reviews column
    try:
        ratings_nd_reviews = i.find('span', {'class': '_2_R_DZ'})
        no_of_ratings_nd_reviews.append(ratings_nd_reviews.find('span').text)
    except:
        no_of_ratings_nd_reviews.append(np.nan)

    x = i.find('ul', {'class': '_1xgFaf'}).find_all('li')  # For detailed specs

    # Core column
    try:
        core.append(x[0].text)
    except:
        core.append(np.nan)

    # ROM column
    try:
        rom.append(x[1].text)
    except:
        rom.append(np.nan)

    # OS column
    try:
        os.append(x[2].text)
    except:
        os.append(np.nan)

    # RAM column
    try:
        ram.append(x[3].text)
    except:
        ram.append(np.nan)

    # Display column
    try:
        display.append(x[4].text)
    except:
        display.append(np.nan)

    # Warranty period
    try:
        waranty_period.append(x[5].text)
    except:
        waranty_period.append(np.nan)

# Creating a dictionary and putting it in a variable
data_to_add = {'Name': name, 'Price': price, 'Stars': rating, 'Total ratings and reviews': no_of_ratings_nd_reviews,
               'Core': core, 'Read Only Memory (ROM)': rom, 'Operating System': os, 'Random Access Memory (RAM)': ram,
               'Display': display,
               'Warranty Period': waranty_period}

# Appending the dictionary into a DataFrame
df = pd.DataFrame(data_to_add)

# Setting the index right
df.index +=1

print(df)

# Exporting the created DataFrame to a CSV file
df.to_csv('flipkart_laptops_february.csv')
