#Extracts images from ameblo blog post
#Extracts all img src if given a non-ameblo url
#usage: python amebloimgcrawl.py <post url> /path/to/destination_folder

from HTMLParser import HTMLParser
import requests
import sys
import re
import os

#ameblo matching
#ameba_re = re.compile("http://stat.*\.ameba\.jp/user_images/.*")
ameblo_re = re.compile("http://ameblo.jp/*.")


imgs = []


class ParseJPG(HTMLParser):
    def handle_starttag(self, tag, attrs):
        if tag == "img":
            for attr in attrs:
                if attr[0] == 'src':
                    imgs.append(attr[1])

def download_img(url,dest_folder):
    fname = url.split('/')[-1]
    r = requests.get(url, stream=True)
    filepath = dest_folder+"/"+fname
    print(filepath)
    if not os.path.exists(dest_folder):
        print("Destination folder does not exist.")
        exit()
    with open(filepath,'wb') as f:
        for chunk in r.iter_content(chunk_size=1024):
            if chunk:
                f.write(chunk)
                f.flush()

def main(url,dest_folder):
    jparser = ParseJPG()
    try:
        req = requests.get(url)
    except requests.exceptions.MissingSchema:
        print("Not a valid url")
        exit()
    src = req.content.decode(req.encoding).replace("\n", "").replace("\r", "")
    jparser.feed(src)        
    m = re.search('http://ameblo.jp/(.+?)/entry*',url)
    user = ""
    if m:
        user = m.group(1)
    amebaimg_re = re.compile("http://stat.*\.ameba\.jp/user_images/.+/../"+user+"/../.././o.*")
    for img in imgs:
        if amebaimg_re.match(img):
            img = img.split('?')[0]
            print(img)
            download_img(img,dest_folder)
        elif not ameblo_re.match(url):
            print(img)

if __name__ == '__main__':
    if len(sys.argv) == 3:
        main(sys.argv[1],sys.argv[2])
    else:
        print("Usage: python amebloimgcrawl.py <blogpost url> path/to/destination/folder")

        
