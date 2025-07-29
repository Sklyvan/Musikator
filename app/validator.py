import hashlib

def verifySignature(filepath: str, signature: str) -> bool:
    """
    Verifies the SHA-256 signature of a file against a given signature.
    :param filepath: Path to the file to verify.
    :param signature: The expected SHA-256 signature of the file.
    :return: bool: True if the file's signature matches the expected signature, False otherwise.
    :raises FileNotFoundError: If the file does not exist.
    :raises IOError: If there is an error reading the file.
    :raises Exception: For any other exceptions that may occur during the verification.
    """
    sha256 = hashlib.sha256()
    try:
        with open(filepath, "rb") as f:
            for chunk in iter(lambda: f.read(4096), b""):
                sha256.update(chunk)
        fileHash = sha256.hexdigest()
        return fileHash.lower() == signature.lower()
    except (FileNotFoundError, IOError):
        return False
    except Exception as e:
        raise Exception(f"Error verifying signature for {filepath}: {e}") from e
