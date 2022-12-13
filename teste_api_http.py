import http.client

conn = http.client.HTTPConnection("127.0.0.1", 5000)
payload = ''
headers = {}
conn.request("GET", "/healthcheck", payload, headers)
res = conn.getresponse()
data = res.read()
print(data.decode("utf-8"))
print(res)