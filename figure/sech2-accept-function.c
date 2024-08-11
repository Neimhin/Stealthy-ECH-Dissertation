sech_accept_confirmation = 
  HKDF-Expand-Label(
    Secret=sech_session_secret,
    Label="sech 2",
    Context=sech_transcript_hash,
    Length=24);
