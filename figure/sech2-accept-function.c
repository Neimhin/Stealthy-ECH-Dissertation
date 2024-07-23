sech_accept_confirmation = 
  HKDF-Expand-Label(
    Secret=sech_early_secret,
    Label="sech accept",
    Context=sech_transcript_hash,
    Length=8);
