import concurrent.futures
import requests

formula_pics_urls = [
    "https://images.unsplash.com/photo-1527757780101-05985993b2e7",
    "https://images.unsplash.com/photo-1633865817989-9688e100731b",
    "https://images.unsplash.com/photo-1574785525103-c35dd9b6bb91",
    "https://images.unsplash.com/photo-1574786351749-2c2b5984a541",
    "https://images.unsplash.com/photo-1624383784228-36505c940b3f",
    "https://images.unsplash.com/photo-1537402792645-b6d9a3ac3fad",

]

def download_Img(url):
    img_bytes = requests.get(url).content
    img_name = url.split("/")[3]
    img_name = img_name + ".jpg"

    with open(img_name, "wb") as img_file:
        img_file.write(img_bytes)
        print(f"{img_name} has been downloaded...")

with concurrent.futures.ThreadPoolExecutor() as executor:
    executor.map(download_Img, formula_pics_urls)