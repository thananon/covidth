from flask import Flask, jsonify, make_response
import requests


data_url = "https://data.go.th/dataset/9f6d900f-f648-451f-8df4-89c676fce1c4/resource/0092046c-db85-4608-b519-ce8af099315e/download/"
app = Flask(__name__)


@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def api(path):
    response = requests.get(data_url)
    i = 0
    records = []
    for line in response.text.splitlines():
        if i > 0:
            col = line.split(",")
            try:
                date_split = col[0].split("/")
                day = f"{int(date_split[0]):02d}"
                month = f"{int(date_split[1]):02d}"
                year = date_split[2]
                convert_date = f"{year}-{month}-{day} 00:00:00"
            except Exception:
                convert_date = col[0]
            record = {
                "_id": i,
                "Date": convert_date,
                "Pos": int(col[1]),
                "Total": int(col[2])
            }
            records.append(record)
        i += 1
    response = {
        "result": {
            "records": records
        }
    }
    resp = make_response(jsonify(response))
    resp.headers['s-maxage'] = "86400"
    return resp
