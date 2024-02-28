import requests

# Replace with the path to the image file you want to upload
image_file_path = 'image.png'

url = 'http://localhost:8000/process_image/'

files = {'file': open(image_file_path, 'rb')}
response = requests.post(url, files=files)

if response.status_code == 200:
    result = response.json()
    print(result)
else:
    print(f"Error: {response.status_code}")
