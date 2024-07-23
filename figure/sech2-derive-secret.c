sech_early_secret = HKDF-Extract(Salt=0, IKM=sech2_long_term_key)
sech_session_secret = Derive-Secret(
    Salt = sech_early_secret, 
    Label = "sech2 session",
    Messages = ClientHelloOuterContext)
