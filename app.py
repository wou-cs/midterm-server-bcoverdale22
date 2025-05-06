from flask import Flask, request


app = Flask(__name__)


@app.route("/api/calcs/<int:num>", methods=["GET"])
def calc(num):
    if num < 0:
        return(404)
    if type(num) != int:
        return(404)
    dec = num - 1
    hex_num = hex(num)
    print(f"dec: {dec}, hex: {hex_num}")
    return {
        "dec": dec,
        "hex": hex_num
    }

@app.route("/api/calcs/<string:num>", methods=["GET"])
def calc_string(num):
    return ({}, 400)