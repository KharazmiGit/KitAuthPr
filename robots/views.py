import selenium
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from django.http import JsonResponse


def hello_world(request):
    try:
        # Start Firefox WebDriver
        driver = selenium.webdriver.Firefox(service=Service(r"C:\Users\k.foroozanfard\Desktop\geckodriver.exe"))

        # Open the login page
        driver.get("http://localhost:8080/login")

        # Wait for elements to be present
        wait = WebDriverWait(driver, 10)
        username = wait.until(EC.presence_of_element_located((By.ID, "login-username")))
        password = wait.until(EC.presence_of_element_located((By.ID, "login-password")))
        btn = wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div/div/div[2]/form/button")))

        # Enter username and password
        username.send_keys("kiarash")
        password.send_keys("kiarash")

        # Click the login button
        btn.click()

        # Wait for the user list page to load
        wait.until(EC.presence_of_element_located((By.TAG_NAME, "table")))

        # Extract users from the table
        users = []
        rows = driver.find_elements(By.CSS_SELECTOR, "tbody tr")
        for row in rows:
            cols = row.find_elements(By.TAG_NAME, "td")
            if len(cols) >= 3:  # Ensure it has enough columns
                users.append({
                    "username": cols[1].text.strip(),
                    "password": cols[2].text.strip(),  # Consider removing password for security
                    "email": cols[3].text.strip(),
                })

        # Close the browser
        driver.quit()

        return JsonResponse({"status": "success", "users": users})

    except Exception as e:
        return JsonResponse({"status": "error", "message": str(e)})
