from .packet_direction import PacketDirection

def get_packet_flow_key(packet, direction) -> tuple:
    """ Membuat signature key untuk paket sehingga dapat ditetapkan ke aliran """

    if "TCP" in packet:
        protocol = "TCP"
    elif "UDP" in packet:
        protocol = "UDP"
    else:
        raise Exception("Only TCP protocols are supported.")

    if direction == PacketDirection.FORWARD:
        dest_ip = packet["IP"].dst
        src_ip = packet["IP"].src
        src_port = packet[protocol].sport
        dest_port = packet[protocol].dport
    else:
        dest_ip = packet["IP"].src
        src_ip = packet["IP"].dst
        src_port = packet[protocol].dport
        dest_port = packet[protocol].sport

    return dest_ip, src_ip, src_port, dest_port
