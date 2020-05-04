from templates import app
import binascii
import os



# Load this config object for development mode
app.config.from_object("configurations.DevelopmentConfig")
# Generate a random key for signing the session:
app.secret_key = binascii.hexlify(os.urandom(16))

app.run()
