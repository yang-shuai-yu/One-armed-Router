from mininet.net import Mininet
from mininet.node import Host, Switch, Controller
from mininet.link import Link, TCLink
from mininet.cli import CLI

# create topology
def main_topology():
    
    net = Mininet(link=Link)
    # add hosts
    h1 = net.addHost('h1')
    h2 = net.addHost('h2')
    h3 = net.addHost('h3')
    h4 = net.addHost('h4')

    # add bridges from hosts
    br1 = net.addHost('br1')

    # add a router
    r1 = net.addHost('r1')

    # add links
    net.addLink(h1, br1)
    net.addLink(h2, br1)
    net.addLink(h3, br1)
    net.addLink(h4, br1)
    net.addLink(br1, r1)
    net.addLink(r1, br1)

    net.build()

    h1.cmd('ifconfig h1-eth0 0')
    h2.cmd('ifconfig h2-eth0 0')
    h3.cmd('ifconfig h3-eth0 0')
    h4.cmd('ifconfig h4-eth0 0')
    br1.cmd('ifconfig br1-eth0 0')
    br1.cmd('ifconfig br1-eth1 0')
    br1.cmd('ifconfig br1-eth2 0')
    br1.cmd('ifconfig br1-eth3 0')
    br1.cmd('ifconfig br1-eth4 0')
    br1.cmd('ifconfig br1-eth5 0')
    r1.cmd('ifconfig r1-eth0 0')
    r1.cmd('ifconfig r1-eth1 0')
    
    h1.cmd('ip address add 192.168.10.1/24 brd + dev h1-eth0')
    h2.cmd('ip address add 192.168.10.2/24 brd + dev h2-eth0')
    h3.cmd('ip address add 192.168.20.1/24 brd + dev h3-eth0')
    h4.cmd('ip address add 192.168.20.2/24 brd + dev h4-eth0')
    r1.cmd('ip address add 192.168.10.254/24 brd + dev r1-eth0')
    r1.cmd('ip address add 192.168.20.254/24 brd + dev r1-eth1')


    br1.cmd('brctl addbr mybr1')
    br1.cmd('brctl addif mybr1 br1-eth0')
    br1.cmd('brctl addif mybr1 br1-eth1')
    br1.cmd('brctl addif mybr1 br1-eth4')

    br1.cmd('brctl addbr mybr2')
    br1.cmd('brctl addif mybr2 br1-eth2')
    br1.cmd('brctl addif mybr2 br1-eth3')
    br1.cmd('brctl addif mybr2 br1-eth5')

    r1.cmd('ifconfig r1-eth0 192.168.10.254/24 netmask 255.255.255.0')
    r1.cmd('ifconfig r1-eth1 192.168.20.254/24 netmask 255.255.255.0')
    r1.cmd('echo 1 > /proc/sys/net/ipv4/ip_forward')

    h1.cmd('ip route add default via 192.168.10.254')
    h2.cmd('ip route add default via 192.168.10.254')
    h3.cmd('ip route add default via 192.168.20.254')
    h4.cmd('ip route add default via 192.168.20.254')

    br1.cmd('ifconfig mybr1 up')
    br1.cmd('ifconfig mybr2 up')
    
    CLI(net)
    net.stop()

if __name__ == '__main__':
    main_topology()