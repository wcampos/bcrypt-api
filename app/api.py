#!/usr/bin/env python3
"""
Password Encryption Service using bcrypt.

This Flask application provides endpoints for password encryption using bcrypt.
It's designed to be a simple, secure service for password hashing.
"""

import os
from typing import Union
import logging
from flask import Flask, jsonify
import bcrypt
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

app = Flask(__name__)

@app.route('/')
def index() -> dict:
    """Root endpoint that confirms the service is running.

    Returns:
        dict: A simple message indicating the service is running.
    """
    return jsonify({"status": "running", "message": "Password Encryption Service"})

@app.route('/pwdncrypt')
def pwd_alive() -> dict:
    """Health check endpoint for the password encryption service.

    Returns:
        dict: Service status information.
    """
    return jsonify({
        "status": "alive",
        "service": "Password Encryption Service"
    })

@app.route('/pwdncrypt/<string:initpwd>', methods=['GET'])
def pwd_encrypt(initpwd: str) -> Union[dict, tuple]:
    """Encrypt a password using bcrypt.

    Args:
        initpwd (str): The password to encrypt.

    Returns:
        Union[dict, tuple]: A JSON response containing the encrypted password
        or an error message with appropriate status code.
    """
    try:
        if not initpwd:
            return jsonify({"error": "Password cannot be empty"}), 400
        
        # Convert string to bytes
        password_bytes = initpwd.encode('utf-8')
        
        # Get rounds from environment or use default
        rounds = int(os.getenv('BCRYPT_ROUNDS', '12'))
        
        # Generate salt and hash password
        hashed = bcrypt.hashpw(password_bytes, bcrypt.gensalt(rounds=rounds))
        
        logger.info("Password successfully encrypted")
        return jsonify({
            "status": "success",
            "hashed_password": hashed.decode('utf-8')
        })
        
    except ValueError as e:
        logger.error(f"Value error during encryption: {str(e)}")
        return jsonify({"error": "Invalid input provided"}), 400
    except Exception as e:
        logger.error(f"Error during encryption: {str(e)}")
        return jsonify({"error": "Internal server error"}), 500

if __name__ == '__main__':
    # In production, use gunicorn instead
    debug_mode = os.getenv('FLASK_DEBUG', 'False').lower() == 'true'
    port = int(os.getenv('PORT', 5000))
    
    app.run(
        host='0.0.0.0',
        port=port,
        debug=debug_mode
    )
