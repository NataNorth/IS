from nltk.parse.corenlp import CoreNLPServer
import os

STANFORD = "stanford-corenlp-4.2.0"

# Create the server
server = CoreNLPServer(
   os.path.join(STANFORD, "stanford-corenlp-4.2.0.jar"),
   os.path.join(STANFORD, "stanford-corenlp-4.2.0-models.jar"),
)

# Start the server in the background
server.start()