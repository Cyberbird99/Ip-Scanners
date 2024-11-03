import socket
import time

starttime = time.time()

if __name__ == "__main__":
    target = input("Enter a host ip for scanning: ")
    t_IP = socket.gethostbyname(target)
    print("Starting scan on host: ", t_IP)

    for i in range(50, 500):
        s = socket(socket.AF_INET, socket.SOCK_STREAM)

        conn = s.connect_ex((t_IP, i))
        if conn == 0:
            print("Port %d: OPEN" % (i,))
        s.close()

print("Duration:", time.time() - starttime)
