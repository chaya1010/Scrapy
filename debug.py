# %%
from unittest import result
from Driver import *
import pandas as pd
from tqdm import tqdm

# %%
Link = pd.read_csv('data/link3.csv').Link.to_list()
# %%
i = 0
Cat = []
checkLink = []
for item in Link:
    driver = createDriver(site=item,results=True)
    checkLink.append(item)
    try:
        Cat.append(driver.find_elements(By.CLASS_NAME,"breadcrumb_list").text)  
    except:
        Cat.append('')

    driver.quit()
    i = i+1
    if i > 10:
        break

df = pd.DataFrame({'Link': checkLink, 'Cats': Cat})
df.to_csv("Test.csv")
