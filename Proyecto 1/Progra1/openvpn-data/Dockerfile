FROM kylemanna/openvpn

RUN --rm openvpn ovpn_genconfig -u udp:// "falta servidor aqui"

RUN --rm openvpn ovpn_initpki

RUN sudo chown -R $(whoami): ./openvpn-data

RUN --rm openvpn easyrsa build-client-full $CLIENTENAME nopass

RUN --rm openvpn ovpn_getclient $CLIENTENAME > $CLIENTNAME.ovpn
