from pyhpke import AEADId, CipherSuite, KDFId, KEMId, KEMKey
from collections import Counter
import math
import random
def new_enc():
    # The sender side:
    suite_s = CipherSuite.new(
        KEMId.DHKEM_P256_HKDF_SHA256, KDFId.HKDF_SHA256, AEADId.AES128_GCM
    )
    pkr = KEMKey.from_jwk(  # from_pem is also available.
        {
            "kid": "01",
            "kty": "EC",
            "crv": "P-256",
            "x": "Ze2loSV3wrroKUN_4zhwGhCqo3Xhu1td4QjeQ5wIVR0",
            "y": "HlLtdXARY_f55A3fnzQbPcm6hgr34Mp8p-nuzQCE0Zw",
        }
    )
    enc, sender = suite_s.create_sender_context(pkr)
    return enc

def generate_encs(n=1000):
    for i in range(n):
        yield new_enc()
def generate_uniform(n=1000):
    for i in range(n):
        yield random.choice([b'\xFF', b'\x00'])

def calculate_entropy(generator):
    # Initialize counters for first bit occurrences
    bit_counter = Counter()

    total = 0
    for byte_str in generator:
        if len(byte_str) > 0:
            # Extract the first bit from the first byte
            first_bit = (byte_str[0] & 0b10000000) >> 7
            bit_counter[first_bit] += 1
            total += 1

    if total == 0:
        return 0.0  # No data to calculate entropy
    
    # Calculate probabilities
    p0 = bit_counter[0] / total
    p1 = bit_counter[1] / total

    # Calculate Shannon entropy
    entropy = 0.0
    if p0 > 0:
        entropy -= p0 * math.log2(p0)
    if p1 > 0:
        entropy -= p1 * math.log2(p1)

    return entropy

enc = new_enc()
print(len(enc))
exit()
print(calculate_entropy(generate_uniform()))
print(calculate_entropy(generate_encs()))
