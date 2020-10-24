from flask import Flask, jsonify, make_response

from .services.employees import get_employees
from .services.notifications import send_notifications

app = Flask(__name__)

# Mozilla provides good references for Access Control at:
# https://developer.mozilla.org/en-US/docs/Web/HTTP/CORS
# https://developer.mozilla.org/en-US/docs/Web/HTTP/Server-Side_Access_Control


@app.route('/api/employees', methods=['GET'])
def employees():
    """Return a JSON response for all employees."""
    sample_response = {
        "employees": get_employees()
    }
    # JSONify response
    response = make_response(jsonify(sample_response))

    # Add Access-Control-Allow-Origin header to allow cross-site request
    response.headers['Access-Control-Allow-Origin'] = 'http://localhost:3000'

    return response


@app.route('/api/employees/notifications', methods=['POST'])
def notifications():
    # Notifications service can be used to remind employees to fill out their timecards
    employee_emails = [employee.get('email') for employee in get_employees()]
    send_notifications(employee_emails)

    sample_response = {
        "recipients": employee_emails
    }

    # JSONify response
    response = make_response(jsonify(sample_response))

    # Add Access-Control-Allow-Origin header to allow cross-site request
    response.headers['Access-Control-Allow-Origin'] = 'http://localhost:3000'

    return response
