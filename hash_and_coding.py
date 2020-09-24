import hashlib
import  base64


def coding_str(string):
    convert_chat_id_to_bytes = string.encode("UTF-8")
    base_64_encode_bytes = base64.b64encode(convert_chat_id_to_bytes)
    convert_bytes_to_str = base_64_encode_bytes.decode("UTF-8")
    return convert_bytes_to_str


def decoding_str(string):
    decode_chat_id_in_bytes_format = base64.b64decode(string)
    decode_chat_id = decode_chat_id_in_bytes_format.decode("UTF-8")
    return decode_chat_id


def hash_str(string):
    string_to_bytes = string.encode("UTF-8")
    hash_object = hashlib.sha256(string_to_bytes)
    hex_dig = hash_object.hexdigest()
    return hex_dig


# print(hash_str('Olga'))
