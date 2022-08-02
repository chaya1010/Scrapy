# %%
from Driver import *
import pandas as pd
from tqdm import tqdm

# %%
Link = pd.read_csv('data/link3.csv').Link.to_list()
# %%
i = 0
Cat = []
for item in Link:
    driver = createDriver(site=Link[5])
    try:
        Cat.append(driver.find_elements(By.CLASS_NAME,"breadcrumb_list"))
    except:
        Cat.append('')
        
    i = i+1
    if i >20:
        break
# %%
