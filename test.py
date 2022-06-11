from urllib.request import urlopen
from urllib.request import urlretrieve
import cgi

url = "https://zero.sci-hub.se/3331/c684de98e25a9b2652b0939db4441336/binh2014.pdf?download=true"
remotefile = urlopen(url)
blah = remotefile.info()['Content-Disposition']
value, params = cgi.parse_header(blah)
urlretrieve(url, "minh.pdf")