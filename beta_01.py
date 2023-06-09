''' 3.2 switching beta_01'''
from mininet.net import Mininet
from mininet.node import Controller, RemoteController, OVSKernelSwitch, UserSwitch, OVSSwitch
from mininet.cli import CLI
from mininet.link import Link, TCLink

# create topology
def main_topology():
    net = Mininet(link=Link)

    # add hosts
    h0 = net.addHost('h0')
    h1 = net.addHost('h1')
    h21 = net.addHost('h21')
    h22 = net.addHost('h22')
    h23 = net.addHost('h23')
    h3 = net.addHost('h3')

    # add switches
    s0 = net.addHost('s0')
    s1 = net.addHost('s1')
    s2 = net.addHost('s2')
    s3 = net.addHost('s3')

    # add routers
    r1 = net.addHost('r1')
    r2 = net.addHost('r2')
    r3 = net.addHost('r3')

    #make links & build network
    net.addLink(h0, s0)
    net.addLink(r1, s0)
    net.addLink(r2, s0)
    net.addLink(r3, s0)
    net.addLink(r1, s1)
    net.addLink(s1, h1)
    net.addLink(r2, s2)
    net.addLink(s2, h21)
    net.addLink(s2, h22)
    net.addLink(s2, h23)
    net.addLink(r3, s3)
    net.addLink(s3, h3)

    net.build()

    # add controllers
    # h0.cmd('ip address add 10.0.10.1/24 brd + dev h0-eth0')
    # h1.cmd('ip address add 10.0.10.2/24 brd + dev h0-eth0')
    # h3.cmd('ip address add 10.0.10.3/24 brd + dev h0-eth0')
    # h21.cmd('ip address add 10.0.10.4/24 brd + dev h0-eth0')
    # h22.cmd('ip address add 10.0.10.5/24 brd + dev h0-eth0')
    # h23.cmd('ip address add 10.0.10.6/24 brd + dev h0-eth0')

    s0.cmd('ifconfig s0-th0 0')
    s0.cmd('ifconfig s0-th1 0')
    s0.cmd('ifconfig s0-th2 0')
    s0.cmd('ifconfig s0-th3 0')

    s1.cmd('ifconfig s1-th0 0')
    s1.cmd('ifconfig s1-th1 0')

    s2.cmd('ifconfig s2-th0 0')
    s2.cmd('ifconfig s2-th1 0')
    s2.cmd('ifconfig s2-th2 0')
    s2.cmd('ifconfig s2-th3 0')

    s3.cmd('ifconfig s3-th0 0')
    s3.cmd('ifconfig s3-th1 0')

    r1.cmd('ifconfig r1-eth0 0')
    r1.cmd('ifconfig r1-eth1 0')
    r2.cmd('ifconfig r2-eth0 0')
    r2.cmd('ifconfig r2-eth1 0')
    r3.cmd('ifconfig r3-eth0 0')
    r3.cmd('ifconfig r3-eth1 0')

    s2.cmd("vconfig add s2-eth0 10")
    s2.cmd("vconfig add s2-eth0 20")
    s2.cmd("vconfig add s2-eth0 30")
    s2.cmd("vconfig add s2-eth0 99")
    s2.cmd("vconfig add s2-eth0 100")
    s2.cmd("vconfig add s2-eth1 20")
    s2.cmd("vconfig add s2-eth1 99")
    s2.cmd("vconfig add s2-eth1 100")
    s2.cmd("vconfig add s2-eth2 20")
    s2.cmd("vconfig add s2-eth2 99")
    s2.cmd("vconfig add s2-eth2 100")
    s2.cmd("vconfig add s2-eth3 10")
    s2.cmd("vconfig add s2-eth3 20")
    s2.cmd("vconfig add s2-eth3 30")
    s2.cmd("vconfig add s2-eth3 99")
    s2.cmd("vconfig add s2-eth3 100")

    s1.cmd("vconfig add s1-eth0 10")
    s1.cmd("vconfig add s1-eth0 99")
    s1.cmd("vconfig add s1-eth0 100")
    s1.cmd("vconfig add s1-eth1 10")
    s1.cmd("vconfig add s1-eth1 99")
    s1.cmd("vconfig add s1-eth1 100")

    s3.cmd("vconfig add s3-eth0 30")
    s3.cmd("vconfig add s3-eth0 99")
    s3.cmd("vconfig add s3-eth0 100")
    s3.cmd("vconfig add s3-eth1 30")
    s3.cmd("vconfig add s3-eth1 99")
    s3.cmd("vconfig add s3-eth1 100")

    r1.cmd("vconfig add r1-eth0 10")
    r1.cmd("vconfig add r1-eth0 99")
    r1.cmd("vconfig add r1-eth0 100")
    r1.cmd("vconfig add r1-eth1 10")
    r1.cmd("vconfig add r1-eth1 99")
    r1.cmd("vconfig add r1-eth1 100")

    r2.cmd("vconfig add r2-eth0 10")
    r2.cmd("vconfig add r2-eth0 20")
    r2.cmd("vconfig add r2-eth0 30")
    r2.cmd("vconfig add r2-eth0 99")
    r2.cmd("vconfig add r2-eth0 100")
    r2.cmd("vconfig add r2-eth1 10")
    r2.cmd("vconfig add r2-eth1 20")
    r2.cmd("vconfig add r2-eth1 30")
    r2.cmd("vconfig add r2-eth1 99")
    r2.cmd("vconfig add r2-eth1 100")

    r3.cmd("vconfig add r3-eth0 30")
    r3.cmd("vconfig add r3-eth0 99")
    r3.cmd("vconfig add r3-eth0 100")
    r3.cmd("vconfig add r3-eth1 30")
    r3.cmd("vconfig add r3-eth1 99")
    r3.cmd("vconfig add r3-eth1 100")

    s2.cmd("ifconfig s2-eth0.10 up")
    s2.cmd("ifconfig s2-eth0.20 up")
    s2.cmd("ifconfig s2-eth0.30 up")
    s2.cmd("ifconfig s2-eth0.99 up")
    s2.cmd("ifconfig s2-eth0.100 up")
    s2.cmd("ifconfig s2-eth1.20 up")
    s2.cmd("ifconfig s2-eth1.99 up")
    s2.cmd("ifconfig s2-eth1.100 up")
    s2.cmd("ifconfig s2-eth2.20 up")
    s2.cmd("ifconfig s2-eth2.99 up")
    s2.cmd("ifconfig s2-eth2.100 up")
    s2.cmd("ifconfig s2-eth3.10 up")
    s2.cmd("ifconfig s2-eth3.20 up")
    s2.cmd("ifconfig s2-eth3.30 up")
    s2.cmd("ifconfig s2-eth3.99 up")
    s2.cmd("ifconfig s2-eth3.100 up")

    s1.cmd("ifconfig s1-eth0.10 up")
    s1.cmd("ifconfig s1-eth0.99 up")
    s1.cmd("ifconfig s1-eth0.100 up")
    s1.cmd("ifconfig s1-eth1.10 up")
    s1.cmd("ifconfig s1-eth1.99 up")
    s1.cmd("ifconfig s1-eth1.100 up")

    s3.cmd("ifconfig s3-eth0.30 up")
    s3.cmd("ifconfig s3-eth0.99 up")
    s3.cmd("ifconfig s3-eth0.100 up")
    s3.cmd("ifconfig s3-eth1.30 up")
    s3.cmd("ifconfig s3-eth1.99 up")
    s3.cmd("ifconfig s3-eth1.100 up")

    r1.cmd("ifconfig r1-eth0.10 up")
    r1.cmd("ifconfig r1-eth0.99 up")
    r1.cmd("ifconfig r1-eth0.100 up")
    r1.cmd("ifconfig r1-eth1.10 up")
    r1.cmd("ifconfig r1-eth1.99 up")
    r1.cmd("ifconfig r1-eth1.100 up")

    r2.cmd("ifconfig r2-eth0.10 up")
    r2.cmd("ifconfig r2-eth0.20 up")
    r2.cmd("ifconfig r2-eth0.30 up")
    r2.cmd("ifconfig r2-eth0.99 up")
    r2.cmd("ifconfig r2-eth0.100 up")
    r2.cmd("ifconfig r2-eth1.10 up")
    r2.cmd("ifconfig r2-eth1.20 up")
    r2.cmd("ifconfig r2-eth1.30 up")
    r2.cmd("ifconfig r2-eth1.99 up")
    r2.cmd("ifconfig r2-eth1.100 up")

    r3.cmd("ifconfig r3-eth0.30 up")
    r3.cmd("ifconfig r3-eth0.99 up")
    r3.cmd("ifconfig r3-eth0.100 up")
    r3.cmd("ifconfig r3-eth1.30 up")
    r3.cmd("ifconfig r3-eth1.99 up")
    r3.cmd("ifconfig r3-eth1.100 up")

    # 分配子网
    s1.cmd("brctl addbr brvlan10")
    s1.cmd("brctl addbr brvlan99")
    s1.cmd("brctl addbr brvlan100")
    s1.cmd("brctl addif brvlan10 s1-eth0.10")
    s1.cmd("brctl addif brvlan99 s1-eth0.99")
    s1.cmd("brctl addif brvlan100 s1-eth0.100")
    s1.cmd("ifconfig brvlan10 s1-eth1.10")
    s1.cmd("ifconfig brvlan99 s1-eth1.99")
    s1.cmd("ifconfig brvlan100 s1-eth1.100")
    s1.cmd("ifconfig brvlan10 up")
    s1.cmd("ifconfig brvlan99 up")
    s1.cmd("ifconfig brvlan100 up")

    s2.cmd("brctl addbr brvlan10")
    s2.cmd("brctl addbr brvlan20")
    s2.cmd("brctl addbr brvlan30")
    s2.cmd("brctl addbr brvlan99")
    s2.cmd("brctl addbr brvlan100")
    s2.cmd("brctl addif brvlan10 s2-eth0.10")
    s2.cmd("brctl addif brvlan20 s2-eth0.20")
    s2.cmd("brctl addif brvlan30 s2-eth0.30")
    s2.cmd("brctl addif brvlan99 s2-eth0.99")
    s2.cmd("brctl addif brvlan100 s2-eth0.100")
    s2.cmd("brctl addif brvlan20 s2-eth1.20")
    s2.cmd("brctl addif brvlan99 s2-eth1.99")
    s2.cmd("brctl addif brvlan100 s2-eth1.100")
    s2.cmd("brctl addif brvlan20 s2-eth2.20")
    s2.cmd("brctl addif brvlan99 s2-eth2.99")
    s2.cmd("brctl addif brvlan100 s2-eth2.100")
    s2.cmd("brctl addif brvlan10 s2-eth3.10")
    s2.cmd("brctl addif brvlan20 s2-eth3.20")
    s2.cmd("brctl addif brvlan30 s2-eth3.30")
    s2.cmd("brctl addif brvlan99 s2-eth3.99")
    s2.cmd("brctl addif brvlan100 s2-eth3.100")
    s2.cmd("ifconfig brvlan10 up")
    s2.cmd("ifconfig brvlan20 up")
    s2.cmd("ifconfig brvlan30 up")
    s2.cmd("ifconfig brvlan99 up")
    s2.cmd("ifconfig brvlan100 up")

    s3.cmd("brctl addbr brvlan30")
    s3.cmd("brctl addbr brvlan99")
    s3.cmd("brctl addbr brvlan100")
    s3.cmd("brctl addif brvlan30 s3-eth0.30")
    s3.cmd("brctl addif brvlan99 s3-eth0.99")
    s3.cmd("brctl addif brvlan100 s3-eth0.100")
    s3.cmd("ifconfig brvlan30 s3-eth1.30")
    s3.cmd("ifconfig brvlan99 s3-eth1.99")
    s3.cmd("ifconfig brvlan100 s3-eth1.100")
    s3.cmd("ifconfig brvlan30 up")

    r1.cmd('ifconfig r1-eth0.10 192.168.10.254 netmask 255.255.255.0')
    r1.cmd('ifconfig r1-eth0.99 192.168.99.254 netmask 255.255.255.0')
    r1.cmd('ifconfig r1-eth0.100 192.168.100.254 netmask 255.255.255.0')
    r1.cmd('ifconfig r1-eth1.10 192.168.10.254 netmask 255.255.255.0')
    r1.cmd('ifconfig r1-eth1.99 192.168.99.254 netmask 255.255.255.0')
    r1.cmd('ifconfig r1-eth1.100 192.168.100.254 netmask 255.255.255.0')
    r1.cmd('echo 1 > /proc/sys/net/ipv4/ip_forward')

    r2.cmd('ifconfig r2-eth0.10 192.168.10.254 netmask 255.255.255.0')
    r2.cmd('ifconfig r2-eth0.20 192.168.20.254 netmask 255.255.255.0')
    r2.cmd('ifconfig r2-eth0.30 192.168.30.254 netmask 255.255.255.0')
    r2.cmd('ifconfig r2-eth0.99 192.168.99.254 netmask 255.255.255.0')
    r2.cmd('ifconfig r2-eth0.100 192.168.100.254 netmask 255.255.255.0')
    r2.cmd('ifconfig r2-eth1.10 192.168.10.254 netmask 255.255.255.0')
    r2.cmd('ifconfig r2-eth1.20 192.168.20.254 netmask 255.255.255.0')
    r2.cmd('ifconfig r2-eth1.30 192.168.30.254 netmask 255.255.255.0')
    r2.cmd('ifconfig r2-eth1.99 192.168.99.254 netmask 255.255.255.0')
    r2.cmd('ifconfig r2-eth1.100 192.168.100.254 netmask 255.255.255.0')
    r2.cmd('echo 1 > /proc/sys/net/ipv4/ip_forward')
    
    r3.cmd('ifconfig r3-eth0.30 192.168.30.254 netmask 255.255.255.0')
    r3.cmd('ifconfig r3-eth0.99 192.168.99.254 netmask 255.255.255.0')
    r3.cmd('ifconfig r3-eth0.100 192.168.100.254 netmask 255.255.255.0')
    r3.cmd('ifconfig r3-eth1.30 192.168.30.254 netmask 255.255.255.0')
    r3.cmd('ifconfig r3-eth1.99 192.168.99.254 netmask 255.255.255.0')
    r3.cmd('ifconfig r3-eth1.100 192.168.100.254 netmask 255.255.255.0')
    r3.cmd('echo 1 > /proc/sys/net/ipv4/ip_forward')

    h1.cmd('ifconfig h1-eth0 192.168.10.1')
    h1.cmd('ip route add default via 192.168.10.254')
    h21.cmd('ifconfig h21-eth0 192.168.20.1')
    h21.cmd('ip route add default via 192.168.20.254')
    h22.cmd('ifconfig h22-eth0 192.168.20.2')
    h22.cmd('ip route add default via 192.168.20.254')
    h23.cmd('ifconfig h23-eth0 192.168.99.2')
    h23.cmd('ip route add default via 192.168.99.254')
    h3.cmd('ifconfig h3-eth0 192.168.30.1')
    h3.cmd('ip route add default via 192.168.30.254')
    h0.cmd('ifconfig h0-eth0 192.168.100.1')
    h0.cmd('ip route add default via 192.168.100.254')

    CLI(net)
    net.stop()

if __name__ == '__main__':
    main_topology()


