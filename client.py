import requests


url = 'http://localhost:5000/api/test'
headers = {'content-type': 'image/jpeg'}

def post_image(img_file):
  """ post image and return the response """
  img = open(img_file, 'rb').read()
  response = requests.post(url, data=img, headers=headers)
  return response

r = post_image('img.jpg')
print(r.json())

