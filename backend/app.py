from flask import Flask, request, jsonify
from flask_cors import CORS
import pyodbc

app = Flask(__name__)
CORS(app, origins=["http://34.138.59.169"])
# SQL Server connection details
conn_str = (
    'DRIVER={ODBC Driver 18 for SQL Server};'
    'SERVER=34.139.183.194;'
    'DATABASE=myappdb;'
    'UID=myuser;'
    'PWD=Sukhi@1374;'
    'TrustServerCertificate=yes;'
)

@app.route('/upload', methods=['POST'])
def upload_file():
    # Check if the file part is in the request
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'}), 400

    file = request.files['file']

    # Check if a file has been selected
    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400

    try:
        # Read the file data
        file_data = file.read()
        file_name = file.filename

        # Connect to SQL Server
        conn = pyodbc.connect(conn_str)
        cursor = conn.cursor()

        # Insert data into SQL Server
        cursor.execute(
            "INSERT INTO YourTable (FileName, FileData, UploadDate) VALUES (?, ?, DEFAULT)",
            (file_name, file_data)
        )
        conn.commit()

        # Close the cursor and connection
        cursor.close()
        conn.close()

        return jsonify({'message': 'File uploaded successfully'}), 200
    except pyodbc.Error as e:
        return jsonify({'error': str(e)}), 500
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
