from flask import Flask, render_template, jsonify
from http import HTTPStatus
from app.accesibilidad import *
from app.ocio import *
from app.transporte import *
from app.parking import *

app = Flask(__name__)


@app.route("/api/<string:ciudad1>/<string:ciudad2>")
def compararCiudades(ciudad1, ciudad2):

    ciudad1Format = ciudad1.capitalize()
    ciudad2Format = ciudad2.capitalize()

    porcentajeCiudad1 = obtenerPorcentajeCiudad(ciudad1Format)
    porcentajeCiudad2 = obtenerPorcentajeCiudad(ciudad2Format)

    porcentajeOcio1 = obtenerOcio(ciudad1Format)
    porcentajeOcio2 = obtenerOcio(ciudad2Format)

    porcentajeTransporte1 = obtenerTransporte(ciudad1Format)
    porcentajeTransporte2 = obtenerTransporte(ciudad2Format)

    porcentajeParking1 = obtenerParking(ciudad1Format)
    porcentajeParking2 = obtenerParking(ciudad2Format)

    return jsonify(
        {
            "status": "OK",
            "ciudad1": ciudad1Format,
            "porcentajeAccesibilidad1": porcentajeCiudad1,
            "porcentajeOcio1": porcentajeOcio1,
            "ciudad2": ciudad2Format,
            "porcentajeAccesibilidad2": porcentajeCiudad2,
            "porcentajeOcio2": porcentajeOcio2,
            "porcentajeTransporte1": porcentajeTransporte1,
            "porcentajeTransporte2": porcentajeTransporte2,
            "porcentajeParking1": porcentajeParking1,
            "porcentajeParking2": porcentajeParking2
        }
    ), HTTPStatus.OK
