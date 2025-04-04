import pandas as pd
from bs4 import BeautifulSoup
import re

file_path = r"c:\Users\marti\Documents\Facu\Beca Maestría\Scraping\código_fuenteinmigracion rusa AND argentina.html"
with open(file_path, 'r', encoding='utf-8') as file:
    content = file.read()
soup = BeautifulSoup(content, 'html.parser') # Parsear el HTML con BeautifulSoup
links = soup.find_all('a', href=True) # Encontrar todos los links
tweet_links = ['https://x.com' + link['href'] 
               for link in links 
               if '/status/' in link['href']
                and not link['href'].endswith('/analytics') 
                and not link['href'].endswith('/people')
                and not re.search(r'/photo/\d+$', link['href'])] # Filtrar los links de los tweets

df = pd.DataFrame(tweet_links, columns=['url']) # Crear un DataFrame de pandas con los links formateados

print(df) # Mostrar el DataFrame
df = df.drop_duplicates() # Eliminar duplicados
# Guardar los links en un archivo CSV
output_path = 'C:\\Users\\marti\\Documents\\Facu\\Beca Maestría\\Scraping\\Selenium\\linkstweets_inmigracion{terminos_busqueda}.csv'
df.to_csv(output_path, index=False)