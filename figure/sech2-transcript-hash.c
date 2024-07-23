transcript =
    ClientHelloInner ||
    *HelloRetryRequest || // optionally
    *ClientHello2 ||      // only if HRR is included
    ServerHello           // but with last 8 octets of random set to 0

sech_transcript_hash =
    Message-Digest(transcript, algorithm)
    
