import random
import time
import pandas as pd
import re
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, WebDriverException, NoSuchElementException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from bs4 import BeautifulSoup
from datetime import datetime

service = Service(r'C:\Users\marti\Documents\Facu\Beca Maestría\Scraping\Selenium\geckodriver-v0.35.0-win64\geckodriver.exe')
options = webdriver.FirefoxOptions()
profile_path = r"C:\Users\marti\AppData\Roaming\Mozilla\Firefox\Profiles\yx3gd714.Scraping"
profile = webdriver.FirefoxProfile(profile_path)
options.add_argument('-private')
def humanized_mouse_movement(driver, element):
    #"""Mueve el mouse en líneas imperfectas alrededor del elemento."""
    actions = ActionChains(driver)
    element_location = element.location
    element_size = element.size

    # Obtener dimensiones del viewport
    viewport_width = driver.execute_script("return window.innerWidth;")
    viewport_height = driver.execute_script("return window.innerHeight;")

    # Coordenadas del centro del botón
    center_x = element_location['x'] + element_size['width'] // 2
    center_y = element_location['y'] + element_size['height'] // 2

    # Iniciar en el centro del botón
    actions.move_to_element(element).perform()

    # Generar movimientos aleatorios dentro del viewport
    for _ in range(random.randint(5, 10)):  # Número de movimientos
        offset_x = random.randint(-20, 20)
        offset_y = random.randint(-20, 20)

        # Coordenadas de destino calculadas
        target_x = center_x + offset_x
        target_y = center_y + offset_y

        # Verificar que las coordenadas estén dentro del viewport
        if 0 <= target_x <= viewport_width and 0 <= target_y <= viewport_height:
            actions.move_by_offset(offset_x, offset_y).perform()
            time.sleep(random.uniform(0.1, 0.3))  # Pausa aleatoria
driver = webdriver.Firefox(service=Service(), options=options, firefox_profile=profile)

# INICIAR: Completar fecha inicio, fecha final, términos búsqueda y output_file
fecha_inicio = "2022-02-24" #aaaa-mm-dd [guerra es 24/02/22]. rusos and argentina: me falto del 1 al 3 de enero del 2022
fecha_final = "2023-12-31" #aaaa-mm-dd 
terminos_busqueda = "migrantes guerra rusia AND Argentina"
link = f"https://x.com/search?q={terminos_busqueda}%20until%3A{fecha_final}%20since%3A{fecha_inicio}&src=typed_query"
print(link)
driver.get(link)
output_file = f"código_fuente_{terminos_busqueda}_{fecha_final}_{fecha_inicio}.html" 

#Scrapeados sin hilos (primer grupo): "embarazadas rusas", "inmigrantes AND rusia AND argentina", "migrantes AND rusia AND Argentina",  #"migrantes AND rusos AND argentina", "inmigracion rusa AND argentina", 

#Scrapeados sin hilos (segundo grupo): "inmigración rusos AND argentina", #"inmigración rusas and argentina", "migraciones rusia AND argentina", "rusos en Argentina", "rusos AND Argentina"
#inmigrantes AND rusos AND Argentina -embarazadas -rusia -rusa -migrantes -inmigración -migraciones
#migración rusa AND Argentina -embarazadas -rusia -migrantes -inmigración -migraciones" "migrantes guerra rusia AND argentina"



#Login
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div/div/div[1]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[4]/label/div/div[2]/div/input')))
username_element = driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div[1]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[4]/label/div/div[2]/div/input')
humanized_mouse_movement(driver=driver,element=username_element)
time.sleep(random.uniform(1,3.5))
username_element.send_keys("_")  # Reemplaza "your_username" con tu nombre de usuario
time.sleep(random.uniform(0.5,2.23))
siguiente = driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div[1]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/button[2]/div/span/span')
humanized_mouse_movement(driver=driver,element=siguiente)
time.sleep(random.uniform(1,3.5))
siguiente.click()
try:
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "/html/body/div/div/div/div[1]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div[1]/div/h1/span/span"))
    )
    print("Pide correo:", element.text)
    campo_correo = driver.find_element(By.CSS_SELECTOR, ".r-homxoj")
    humanized_mouse_movement(driver=driver,element=campo_correo)
    time.sleep(random.uniform(1,3.5))
    campo_correo.send_keys("_")
    time.sleep(random.uniform(0.5,2.23))
    siguiente = driver.find_element(By.CSS_SELECTOR, "span.r-1inkyih > span:nth-child(1)")
    humanized_mouse_movement(driver=driver,element=siguiente)
    time.sleep(random.uniform(1,3.5))
    siguiente.click()
except Exception as e:
    print("No pide correo")
    pass

WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".r-homxoj")))
password_element = driver.find_element(By.CSS_SELECTOR, ".r-homxoj")
humanized_mouse_movement(driver=driver,element=password_element)
time.sleep(random.uniform(1,3.5))
password_element.send_keys("_") 
time.sleep(random.uniform(0.5,2.23))
WebDriverWait(driver,30).until(EC.presence_of_element_located((By.CSS_SELECTOR, "span.r-1inkyih > span:nth-child(1)")))
iniciar = driver.find_element(By.CSS_SELECTOR, "span.r-1inkyih > span:nth-child(1)")
humanized_mouse_movement(driver=driver,element=iniciar)
time.sleep(random.uniform(1,3.5))
iniciar.click()
    
while True:
    time.sleep(2)
    time.sleep(random.uniform(1,1.8))
    WebDriverWait(driver,45).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div/div/div[2]/main/div/div/div/div[1]/div/div[1]/div[1]/div[2]/nav/div/div[2]/div/div[2]/a/div/div')))
    Latest = driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div[2]/main/div/div/div/div[1]/div/div[1]/div[1]/div[2]/nav/div/div[2]/div/div[2]/a/div/div')
    humanized_mouse_movement(driver=driver,element=Latest)
    Latest.click()
    time.sleep(random.uniform(2,3))
    last_height = driver.execute_script("return document.body.scrollHeight")
    scroll_attempts = 0
    max_attempts = 5  # Número máximo de intentos si no se cargan más tweets
    
    with open(output_file, "a", encoding="utf-8") as file:
        while scroll_attempts < max_attempts:
            try:
                # Guardar el código fuente de la página
                file.write(driver.page_source)
                file.write("\n\n<!-- New Scroll -->\n\n")

                # Desplazarse hacia abajo
                driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
                humanized_mouse_movement(driver=driver,element=Latest)
                time.sleep(random.uniform(3, 5))  # Espera aleatoria para simular comportamiento humano

                # Verificar si se cargaron más tweets
                new_height = driver.execute_script("return document.body.scrollHeight")
                if new_height == last_height:
                    if scroll_attempts == 7: #no va aplicarse nunca siendo 7 por la cantidad de intentos
                        user_input = input('Insertar "y" para continuar scrolleo...')
                        if user_input == 'y':
                            print('Continuando')
                            continue               
                                               
                        else:
                            print('Scrolleo terminado. Pasando a extraer links')
                            break    
                    
                    else:
                        scroll_attempts += 1  # Incrementar intentos si no se cargó nada nuevo 
                
                else:
                    scroll_attempts = 0  # Resetear intentos si se cargo más información
                last_height = new_height
                print(f"Reintento de scrolleo: {scroll_attempts}")              
            
            
            
            
            except WebDriverException as e:
                print(f"Error: {e}")                       
                print(f"Al parecer no carga más la página")
               

        break        
                     
with open(output_file, 'r', encoding='utf-8') as file:
    content = file.read()
soup = BeautifulSoup(content, 'html.parser') # Parsear el HTML con BeautifulSoup
links = soup.find_all('a', href=True) # Encontrar todos los links
tweet_links = ['https://x.com' + link['href'] 
               for link in links 
               if '/status/' in link['href']
                and not link['href'].endswith('/analytics') 
                and not link['href'].endswith('/people')
                and not re.search(r'/photo/\d+$', link['href'])] # Filtrar los links de los tweets

# Create a DataFrame with the new links
new_df = pd.DataFrame(tweet_links, columns=['url'])
new_df = new_df.drop_duplicates()

output_path = f"C:\\Users\\marti\\Documents\\Facu\\Beca Maestría\\Scraping\\Selenium\\WebScraping Twitter\\linkstweets_{terminos_busqueda}.csv"

# Try to read the existing CSV file
try:
    existing_df = pd.read_csv(output_path)
    # Concatenate the existing DataFrame with the new DataFrame
    combined_df = pd.concat([existing_df, new_df]).drop_duplicates().reset_index(drop=True)
except FileNotFoundError:
    # If the file does not exist, use the new DataFrame as the combined DataFrame
    combined_df = new_df

# Save the combined DataFrame to the CSV file
combined_df.to_csv(output_path, index=False)
print(combined_df) # Mostrar el DataFrame
    


