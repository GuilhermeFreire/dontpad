import urllib.request as request
import urllib.parse as parse
import json

main_url = "http://dontpad.com/"

def write(page, content):
	url = main_url + page
	data = parse.urlencode({"text" : content})
	data = data.encode("utf-8")
	req = request.Request(url, data)
	with request.urlopen(req) as response:
		timestamp = response.read()
	return timestamp

def read_raw(page):
	with request.urlopen(main_url + page + ".body.json?lastUpdate=0") as response:
		resp = response.read()
	return resp

def read(page):
	content = json.loads(read_raw(page).decode())
	if content["body"]:
		return content
	return ""

if __name__ == "__main__":
	print("==> POST:", write("dontpad.py", "test"))
	print(read("dontpad.py"))

