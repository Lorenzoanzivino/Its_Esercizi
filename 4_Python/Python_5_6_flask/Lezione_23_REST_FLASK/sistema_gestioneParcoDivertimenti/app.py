from flask import Flask, jsonify, url_for
from main import Ride, RollerCoaster, Carousel, Park

app = Flask(__name__)

park = Park()

rc = RollerCoaster("rc1", "Dragon Fury", 140, 3)
ca = Carousel("ca1", "Magic Animals", 0)

park.add(rc)
park.add(ca)


@app.route("/")
def home():

    descrizione = "Welcome to Park API"

    links = {}

    links["all_rides"] = url_for("get_all_rides")

    for ride in park.list_all():
        ride_id = ride.id

        links[f"ride_{ride_id}"] = url_for("get_ride", ride_id=ride_id)

        links[f"ride_{ride_id}_wait"] = url_for("get_wait_time", ride_id=ride_id, crowd=4.0)

    risposta = {
        "message": descrizione,
        "routes": links
    }

    return jsonify(risposta)


@app.get("/rides")
def get_all_rides():
    lista = []
    for ride in park.list_all():
        lista.append(ride.info())
    return jsonify(lista)


@app.get("/rides/<ride_id>")
def get_ride(ride_id):
    ride = park.get(ride_id)
    if ride is None:
        return jsonify({"error": "Ride not found"}), 404

    return jsonify(ride.info())


@app.get("/rides/<ride_id>/wait/<float:crowd>")
def get_wait_time(ride_id, crowd):
    ride = park.get(ride_id)
    if ride is None:
        return jsonify({"error": "Ride not found"}), 404

    return jsonify({
        "id": ride.id,
        "crowd_factor": crowd,
        "wait_time": ride.wait_time(crowd)
    })

app.run(debug=True)
