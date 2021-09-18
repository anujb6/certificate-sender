# importing libraries
import pandas as pd
from PIL import Image, ImageDraw, ImageFont
import os
# reading csv
data = pd.read_excel(r'demo.xlsx', engine='openpyxl')
# remove null values
data.dropna(inplace=True,axis=1)
# dropping dupicate rows
data.drop_duplicates(subset=['Email'], keep='last', inplace=True)
# convert to list
names = data['Name'].to_list()
emails = data['Email'].to_list()
# checking if the directory exists
if os.path.exists('certificates'):
    print("Folder already exists")
else:
    os.mkdir('certificates')
# opening log file and writing ceritifcates
with open("logs.txt", 'a') as f:
    for (name, email) in zip(names, emails):
      
            file_path = 'ss1.png'
            image = Image.open(file_path)
            draw = ImageDraw.Draw(image)

            (x, y) = (447, 390)
            color = 'rgb(255,255,255)'
            name = name
            font = ImageFont.truetype('arial.ttf', size=60)
            draw.text((x, y), name, fill=color, font=font)

            cert_dir = 'certificates/'
            cert_path = cert_dir+email+'.pdf'
            image.save(cert_path)
            print(str(email) + " Success")
            f.write(str(email) + " Success")
            f.write("\n")
    
    f.close()



























































#- `git clone https://github.com/saadhaxxan/Certificate-Generator-Sender.git`
# - `cd Certificate-Generator-Sender`
# - Add `base_file.png` as your certificate file
# - Replace `demo.csv` with you own csv file that must have 2 columns of `Names` and `Emails`
# - Open up `generator.py` and add your own custom text for the certificate
# - Run command `python generator.py`
# - Open up `sender.py` and add your email credentials
# - Verify the certificates folder and then replace the subject and body of email with your own data
# - Run command `python sender.py`