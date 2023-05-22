'''switch 实现 vlan trunk'''

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
    # add switches
    s1 = net.addHost('s1')
    s2 = net.addHost('s2')
    # make links
    net.addLink(h1, s1)
    net.addLink(h2, s1)
    net.addLink(h3, s2)
    net.addLink(h4, s2)
    net.addLink(s1, s2)

    net.build()

    h1.cmd('ip address add 10.0.10.1/24 brd + dev h1-eth0')
    h2.cmd('ip address add 10.0.10.2/24 brd + dev h2-eth0')
    h3.cmd('ip address add 10.0.10.3/24 brd + dev h3-eth0')
    h4.cmd('ip address add 10.0.10.4/24 brd + dev h4-eth0')

    # h1.cmd('ifconfig h1-eth0 10.0.10.1 netmask 255.255.255.0')
    # h2.cmd('ifconfig h2-eth0 10.0.10.2 netmask 255.255.255.0')
    # h2.cmd('ifconfig h3-eth0 10.0.10.3 netmask 255.255.255.0')
    # h2.cmd('ifconfig h4-eth0 10.0.10.4 netmask 255.255.255.0')

    s1.cmd('ifconfig s1-eth0 0')
    s1.cmd('ifconfig s1-eth1 0')
    s1.cmd('ifconfig s1-eth2 0')
    s1.cmd('vconfig add s1-eth2 10')
    s1.cmd('vconfig add s1-eth2 20')

    s2.cmd('ifconfig s2-eth0 0')
    s2.cmd('ifconfig s2-eth1 0')
    s2.cmd('ifconfig s2-eth2 0')
    s2.cmd('vconfig add s2-eth2 10')
    s2.cmd('vconfig add s2-eth2 20')

    s1.cmd('ifconfig s1-eth2.10 up')
    s1.cmd('ifconfig s1-eth2.20 up')
    s2.cmd('ifconfig s2-eth2.10 up')
    s2.cmd('ifconfig s2-eth2.20 up')

    s1.cmd('brctl addbr brvlan10')
    s1.cmd('brctl addbr brvlan20')
    s1.cmd('brctl addif brvlan10 s1-eth0')
    s1.cmd('brctl addif brvlan20 s1-eth1')
    s1.cmd('brctl addif brvlan10 s1-eth2.10')
    s1.cmd('brctl addif brvlan20 s1-eth2.20')

    s2.cmd('brctl addbr brvlan10')
    s2.cmd('brctl addbr brvlan20')
    s2.cmd('brctl addif brvlan10 s2-eth0')
    s2.cmd('brctl addif brvlan20 s2-eth1')
    s2.cmd('brctl addif brvlan10 s2-eth2.10')
    s2.cmd('brctl addif brvlan20 s2-eth2.20')

    s1.cmd('ifconfig brvlan10 up')
    s1.cmd('ifconfig brvlan20 up')
    s2.cmd('ifconfig brvlan10 up')
    s2.cmd('ifconfig brvlan20 up')

    CLI(net)
    net.stop()

if __name__ == '__main__':
    main_topology()