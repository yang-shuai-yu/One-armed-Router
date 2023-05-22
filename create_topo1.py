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

    # add bridges from hosts
    # br1 = net.addHost('br1')
    br1 = net.addHost('br1')

    # add links
    net.addLink(h1, br1)
    net.addLink(h2, br1)
    net.addLink(h3, br1)

    net.build()

    h1.cmd('ifconfig h1-eth0 0')
    h2.cmd('ifconfig h2-eth0 0')
    h3.cmd('ifconfig h3-eth0 0')
    br1.cmd('ifconfig br1-eth0 0')
    br1.cmd('ifconfig br1-eth1 0')
    br1.cmd('ifconfig br1-eth2 0')
    
    h1.cmd('ip address add 192.168.10.1/24 brd + dev h1-eth0')
    h2.cmd('ip address add 192.168.10.2/24 brd + dev h2-eth0')
    h3.cmd('ip address add 192.168.10.3/24 brd + dev h3-eth0')

    br1.cmd('brctl addbr br1')
    br1.cmd('brctl addif br1 br1-eth0')
    br1.cmd('brctl addif br1 br1-eth1')
    br1.cmd('brctl addif br1 br1-eth2')

    br1.cmd('brctl addbr mybr1')
    br1.cmd('brctl addbr mybr1 br1-eth0')
    br1.cmd('brctl addbr mybr1 br1-eth1')
    br1.cmd('brctl addbr mybr1 br1-eth2')
    br1.cmd('ifconfig br1 up')


    # ping
    # h1.cmd('ping -c h2')
    
    CLI(net)
    net.stop()

def brctl_operation(net):
    pass

def ping_operation(net):
    pass

if __name__ == '__main__':
    main_topology()

