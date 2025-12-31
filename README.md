# QR Code Generator

A Python script that generates QR codes containing authentication data (URL and secret key) and displays them both in the terminal and as image files.

## Features

- Generates QR codes with authentication data (URL and secret key)
- Displays QR code directly in the terminal
- Saves QR code as PNG image file
- Uses functional programming principles

## Requirements

- Python 3.6+
- `qrcode` library
- `qrcode-terminal` library

## Installation

1. Clone this repository:
```bash
git clone https://github.com/Egregore-ai/generate-qr-code
cd generate-qr-code
```

2. Install required packages:
```bash
pip install qrcode qrcode-terminal
```

## Usage

Run the script directly:
```bash
python main.py
```

The script will:
1. Generate a random secret key
2. Create a JSON payload with the URL and secret key
3. Display the QR code in the terminal
4. Save the QR code as `auth_qr.png` in the current directory

## Customization

You can modify the `url` and `secret_key` values in the `if __name__ == "__main__":` block to customize the authentication data.

## API

The script provides several functions for generating QR codes:

- `create_auth_qr_data(url, secret_key)`: Creates a JSON payload containing the URL and secret key
- `generate_qr_code(data)`: Generates a QR code (as PNG bytes) from input string data
- `qr_pipeline(url, secret_key)`: End-to-end pipeline that returns both JSON payload and QR image bytes
