import socket


def send_msg(udp_socket):
    """send"""
    msg = input("\nEnter message:")
    dest_ip = input("\nEnter recipient's ip:")
    dest_port = int(input("\nEnter recipient's port:"))
    udp_socket.sendto(msg.encode("utf-8"), (dest_ip, dest_port))


def recv_msg(udp_socket):
    """receive and view"""
    recv_msg = udp_socket.recvfrom(1024)
    recv_ip = recv_msg[1]
    recv_msg = recv_msg[0].decode("utf-8")
    print(">>>%s:%s" % (str(recv_ip), recv_msg))


def main():
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    udp_socket.bind(("", 7890))
    while True:
        print("="*30)
        print("1:send")
        print("2:receive")
        print("="*30)
        op_num = input("Enter operation number:")

        if op_num == "1":
            send_msg(udp_socket)
        elif op_num == "2":
            recv_msg(udp_socket)
        else:
            print("Incorrect. Enter again...")

if __name__ == "__main__":
    main()
