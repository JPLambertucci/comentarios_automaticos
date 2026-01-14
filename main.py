from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options
import time
from dotenv import load_dotenv
from dotenv import dotenv_values
from users import usuarios

def main():
    load_dotenv("credentials.env")

    target_post = "https://www.instagram.com/p/DTMBoQDGJu5/"
    coment_text = usuarios

    driver = webdriver.Chrome()
    driver.get("https://www.instagram.com/accounts/login/")

    time.sleep(5)

    username_input = driver.find_element(By.NAME, "username")
    password_input = driver.find_element(By.NAME, "password")

    config = dotenv_values("credentials.env")

    username_input.send_keys(config.get("USERNAME"))
    time.sleep(5)
    password_input.send_keys(config.get("PASSWORD"))
    time.sleep(5)
    password_input.send_keys(Keys.RETURN)


    driver.get(target_post)
    time.sleep(5)

    for x in range(0, 100):
        for i in range(0, len(coment_text)):
            user = "@" + coment_text[i]
            try:
                if i == 0:
                    time.sleep(2)
                    comment_field = driver.find_element(By.XPATH,
                                                        '//textarea[@class="x1i0vuye xgcd1z6 x1ejq31n x18oe1m7 x1sy0etr xstzfhl x5n08af x78zum5 x1iyjqo2 x1qlqyl8 x1d6elog xlk1fp6 x1a2a7pz xexx8yu xyri2b x18d9i69 x1c1uobl xtt52l0 xnalus7 xs3hnx8 x1bq4at4 xaqnwrm"]')
                    ActionChains(driver).move_to_element(comment_field).click(comment_field).perform()
                    comment_field = driver.find_element(By.XPATH,
                                                        '//textarea[@class="x1i0vuye xgcd1z6 x1ejq31n x18oe1m7 x1sy0etr xstzfhl x5n08af x78zum5 x1iyjqo2 x1qlqyl8 x1d6elog xlk1fp6 x1a2a7pz xexx8yu xyri2b x18d9i69 x1c1uobl xtt52l0 xnalus7 xs3hnx8 x1bq4at4 xaqnwrm focus-visible"]')
                    comment_field.send_keys(user)

                else:
                    time.sleep(2)
                    comment_field = driver.find_element(By.XPATH,
                                                        '//textarea[@class="x1i0vuye xgcd1z6 x1ejq31n x18oe1m7 x1sy0etr xstzfhl x5n08af x78zum5 x1iyjqo2 x1qlqyl8 x1d6elog xlk1fp6 x1a2a7pz xexx8yu xyri2b x18d9i69 x1c1uobl xtt52l0 xnalus7 xs3hnx8 x1bq4at4 xaqnwrm focus-visible"]')
                    comment_field.send_keys(user + " ")

                publicar_button = driver.find_element(By.XPATH,
                                                      '//div[@role="button" and contains(text(), "Publicar")]')
                publicar_button.click()
                print("Comentario publicado con éxito.")
            except Exception as e:
                print(f"Error al comentar: {e}")

            print(coment_text[i])


if __name__ == "__main__":
    main()