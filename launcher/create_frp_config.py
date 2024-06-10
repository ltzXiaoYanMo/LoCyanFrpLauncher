import os
import sys


def get_launch_conf_no_http(ip, port, user, type1, lip, lp, rp, proxyname):
    dirname, filename = os.path.split(os.path.abspath(sys.argv[0]))

    old_no_http = """[common]
server_addr = [serverip]
server_port = [serverport]
tcp_mux = true
protocol = tcp
user = [user]
token = LoCyanToken
dns_server = 114.114.114.114

[[proxyname]]
privilege_mode = true
type = [type]
local_ip = [lip]
local_port = [lp]
remote_port = [rp]
use_encryption = true
use_compression = true
    """

    new_nohttp = old_no_http.replace("[serverip]", ip)
    new_nohttp = new_nohttp.replace("[serverport]", port)
    new_nohttp = new_nohttp.replace("[user]", user)
    new_nohttp = new_nohttp.replace("[lip]", lip)
    new_nohttp = new_nohttp.replace("[lp]", lp)
    new_nohttp = new_nohttp.replace("[type]", type1)
    new_nohttp = new_nohttp.replace("[rp]", rp)
    new_nohttp = new_nohttp.replace("[proxyname]", proxyname)
    print(new_nohttp)
    with open(dirname + "\\frpc.ini", mode="w") as f:
        f.write(new_nohttp)
        f.close()
