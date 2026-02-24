import yaml
import pickle
import hashlib

# 1. Insecure YAML loading (ALWAYS flagged)
def load_config(user_input):
    return yaml.load(user_input, Loader=yaml.Loader)

# 2. Insecure deserialization (ALWAYS flagged)
def load_data(user_input):
    return pickle.loads(user_input)

# 3. Hardcoded credentials (ALWAYS flagged)
DB_PASSWORD = "SuperSecretPassword123"

# 4. Weak hashing (ALWAYS flagged)
def hash_password(pw):
    return hashlib.md5(pw.encode()).hexdigest()
