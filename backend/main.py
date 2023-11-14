"""This module handles Firestore  operations and Flask request processing."""

import logging
from typing import Tuple
from google.cloud import firestore
from flask import jsonify, Request

# Initialize logger
logging.basicConfig(level=logging.INFO)


# pylint: disable=no-member
def get_current_number(number_ref: firestore.DocumentReference) -> int:
    """Retrieves the current visitor number from Firestore."""
    try:
        doc = number_ref.get()
        if doc.exists:
            return int(doc.to_dict().get('count', 0))
        return 0  # Return 0 if document does not exist
    except firestore.exceptions.NotFound:
        logging.error("Firestore document not found")
        return 0  # Return 0 or a suitable default value
    except firestore.exceptions.FirestoreError as e:
        logging.error("Error retrieving visitor number: %s", e)
        raise

def save_visitor_count(number_ref: firestore.DocumentReference, current_number: int) -> None:
    """Updates the visitor count in Firestore."""
    try:
        number_ref.set({'count': current_number})
    except firestore.exceptions.FirestoreError as e:
        logging.error("Error saving visitor count: %s", e)
        raise

def current_number_visitors(_: Request) -> Tuple[dict, int, dict]:
    """Handles the incoming request to get and update the current number of visitors."""
    try:
        db = firestore.Client()
        number_ref = db.collection('visitors').document('visitors_id')

        current_number = get_current_number(number_ref)
        new_number = current_number + 1
        save_visitor_count(number_ref, new_number)

        data = {'new_number': new_number}
        headers = {'Access-Control-Allow-Origin': '*'}

        return jsonify(data), 200, headers
    except firestore.exceptions.FirestoreError as e:
        logging.error("Error in current_number_visitors: %s", e)
        return jsonify({'error': 'An internal error occurred'}), 500
