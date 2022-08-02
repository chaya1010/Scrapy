from Driver import *
import pandas as pd
from tqdm import tqdm

def main():
    driver = createDriver('https://www.lazada.co.th/', results=False)
    menu = driver.find_elements(By.CLASS_NAME,"lzd-site-menu-grand-item")
    Link = []
    for item in tqdm(menu):
        for subitem in item.find_elements(By.TAG_NAME,'a'):
            Link.append(subitem.get_attribute("href"))
    df = pd.DataFrame({'Link': Link})
    df.dropna().drop_duplicates()
    df.to_csv('data\link4.csv')
    driver.quit()

if __name__ == '__main__':
    main()
    
    