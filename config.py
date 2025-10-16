# config_example.py — copy to config.py and fill with real values.
NEO4J_URI = "neo4j+s://f1901de6.databases.neo4j.io"
NEO4J_USER = "neo4j"
NEO4J_PASSWORD = "zGS2znwPKastJF9XWXBN4PJvkMQxCLQlaJutp_KqBgk"
OPENAI_API_KEY ="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"
PINECONE_API_KEY = "pcsk_4BEK3E_UA1LgiXyTWDArCkqmRQFiUGjaSfo7raboDgikQFS9MW2HeUARCTM8EnVkBw28Vm" # your Pinecone API key
PINECONE_ENV = "us-east-1"   # example
PINECONE_INDEX_NAME = "vietnam-travel"
PINECONE_VECTOR_DIM = 1536       # adjust to embedding model used (text-embedding-3-large ~ 3072? check your model); we assume 1536 for common OpenAI models — change if needed.
