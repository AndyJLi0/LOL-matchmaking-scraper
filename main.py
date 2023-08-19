from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def main(name):
    PATH = "C:\\Program Files (x86)\\chromedriver.exe"
    driver = webdriver.Chrome(PATH)
    driver.get(f'https://www.op.gg/summoners/na/{name}/ingame')
    driver.implicitly_wait(5)
    # Locate the table
    table = driver.find_element(By.XPATH, '//*[@id="content-container"]/div/table[1]/tbody')

    # Get all rows of the table
    rows = table.find_elements(By.TAG_NAME, "tr")

    # Iterate through rows to extract summoner names
    summoner_names = []
    for row in rows:
        # Get columns for the current row
        columns = row.find_elements(By.TAG_NAME, "td")

        # Assuming summoner name is in the first column (adjust index as needed)
        summoner_name = columns[3].text
        summoner_rank = columns[5].text
        summoner_names.append(summoner_name)
        summoner_names.append(summoner_rank)

    formatted_data = [names.replace('\n', ', ') for names in summoner_names]
    for i in range(0, len(formatted_data), 2):
        print(f'| {formatted_data[i]} --> {formatted_data[i+1]} |')
        print("----------------------------------------------")


main("nerner")