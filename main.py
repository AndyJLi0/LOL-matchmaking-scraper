from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By


def main(name, region):

    path = "C:\\Program Files (x86)\\chromedriver.exe"
    driver = webdriver.Chrome(path)
    driver.get(f'https://www.op.gg/summoners/{region}/{name}/ingame')
    driver.implicitly_wait(5)

    blue_side_info = []
    red_side_info = []
    try:
        blue_table = driver.find_element(By.XPATH, '//*[@id="content-container"]/div/table[1]/tbody')
        blue_rows = blue_table.find_elements(By.TAG_NAME, "tr")

        red_table = driver.find_element(By.XPATH, '//*[@id="content-container"]/div/table[2]/tbody')
        red_rows = red_table.find_elements(By.TAG_NAME, "tr")

        for row in blue_rows:
            blue_columns = row.find_elements(By.TAG_NAME, "td")

            summoner_name = blue_columns[3].text
            summoner_rank = blue_columns[5].text
            blue_side_info.append(summoner_name)
            blue_side_info.append(summoner_rank)

        for row in red_rows:
            red_columns = row.find_elements(By.TAG_NAME, "td")

            summoner_name = red_columns[3].text
            summoner_rank = red_columns[5].text
            red_side_info.append(summoner_name)
            red_side_info.append(summoner_rank)

        blue_formatted_data = [names.replace('\n', ', ') for names in blue_side_info]
        red_formatted_data = [names.replace('\n', ', ') for names in red_side_info]

        # Format and print table
        title = "GAME INFO"
        title = title.rjust(59)
        print(f'{title}')
        print('-' * 108)
        for i in range(0, len(blue_formatted_data), 2):
            left = blue_formatted_data[i] + " " + blue_formatted_data[i + 1]
            left = left.ljust(50)
            right = red_formatted_data[i] + " " + red_formatted_data[i + 1]
            right = right.rjust(50)
            print(f"| {left} || {right} |")
            print('-' * 108)

    except NoSuchElementException:
        print("ERROR: the user is not currently in a game!")
        driver.close()


# Run this with your summoner name and region when in loading screen
main("tfw two smart", "NA")
