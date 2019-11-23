from flask import Flask, request, jsonify, render_template
from locFuncs import LocationHandler
import vision

global loc
global app


def create_app():
    app = Flask(__name__, template_folder='FrontEnd')
    loc = LocationHandler()

    @app.route("/")
    def main():
        return render_template("MainHTML.html")

    # Returns true if user is nearing an intersection
    @app.route('/get-location-info')
    def getLocationInfo():
        crossingIncoming = loc.do_locationing()
        response = {"crossing": crossingIncoming}
        return jsonify(response)

    @app.route('/get-image-data', methods=["POST"])
    def getImageData():
        req_data = request.get_json()
        if req_data is not None:
            data = req_data.replace("data:image/webp;base64,", "")
            response = vision.analyze_picture(data)
        else:
            response = {"Received": False}

        return jsonify(response)
    return app

app = create_app()

if __name__ == "__main__":
    app.run()
