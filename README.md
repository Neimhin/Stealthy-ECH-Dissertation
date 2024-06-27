

# Mitigating cut-and-paste attacks
```latex
\subsubsection{Mitigating cut-and-paste attacks}
Here we examine the mechanism used in the current draft of ECH to mitigate cut-and-paste attacks.
A cut-and-paste attack against a servername encryption protocol
could be used by an attacker to unveil the intended backend server of a connection
as described in Section 3.1 of \cite{rfc8744-issues}.
The following description of how a cut-and-paste attack could leak a cut-and-paste attack is after \cite{rfc8744-issues}.
\begin{enumerate}
    \item A benign client sends a ClientHello with an encrypted SNI included.
    \item An attacker copies the encrypted SNI into a new ClientHello.
    \item The client-facing/backend servers have no mitigation against the replay
    of the encrypted SNI and establish a connection between the attacker and backend server.
    \item In the handshake with the attacker the backend server sends \var{Certificate} and \var{CertificateVerify} messages,
    revealing the identity of the backend server that the benign client intended to reach. 
\end{enumerate}
\cite{esni} note in Section 10.10.1 that a cut-and-paste attack is not possible against ECH because a server either processes a \var{ClientHelloOuter} or \var{ClientHelloInner} and \var{ClientHelloInner.random} is encrypted. Since \var{ClientHelloInner.random} is encrypted using a public key from an ECHConfig, only the client (who encrypted it) and the possessor of the corresponding private key can view \var{ClientHelloInner.random}. Therefore, if a malicious client tries to replay an \var{encrypted_client_hello} extension, it will contain an encrypted \var{ClientHelloInner.random} value that has already been used.
```
