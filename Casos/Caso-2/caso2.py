#!/usr/bin/python

from mininet.net import Mininet
from mininet.node import Controller, RemoteController, OVSController
from mininet.node import CPULimitedHost, Host, Node
from mininet.node import OVSKernelSwitch, UserSwitch
from mininet.node import IVSSwitch
from mininet.cli import CLI
from mininet.log import setLogLevel, info
from mininet.link import TCLink, Intf
from subprocess import call

def myNetwork():

    net = Mininet( topo=None,
                   build=False,
                   ipBase='10.0.0.0/8')

    info( '*** Adding controller\n' )
    info( '*** Add switches\n')
    s4 = net.addSwitch('s4', cls=OVSKernelSwitch, failMode='standalone')
    s14 = net.addSwitch('s14', cls=OVSKernelSwitch, failMode='standalone')
    s2 = net.addSwitch('s2', cls=OVSKernelSwitch, failMode='standalone')
    s7 = net.addSwitch('s7', cls=OVSKernelSwitch, failMode='standalone')
    r18 = net.addHost('r18', cls=Node, ip='')
    r18.cmd('sysctl -w net.ipv4.ip_forward=1')
    r3 = net.addHost('r3', cls=Node, ip='')
    r3.cmd('sysctl -w net.ipv4.ip_forward=1')
    s11 = net.addSwitch('s11', cls=OVSKernelSwitch, failMode='standalone')
    s19 = net.addSwitch('s19', cls=OVSKernelSwitch, failMode='standalone')
    r15 = net.addHost('r15', cls=Node, ip='')
    r15.cmd('sysctl -w net.ipv4.ip_forward=1')
    r12 = net.addHost('r12', cls=Node, ip='')
    r12.cmd('sysctl -w net.ipv4.ip_forward=1')
    s8 = net.addSwitch('s8', cls=OVSKernelSwitch, failMode='standalone')
    s5 = net.addSwitch('s5', cls=OVSKernelSwitch, failMode='standalone')
    s16 = net.addSwitch('s16', cls=OVSKernelSwitch, failMode='standalone')
    r9 = net.addHost('r9', cls=Node, ip='')
    r9.cmd('sysctl -w net.ipv4.ip_forward=1')
    r1 = net.addHost('r1', cls=Node, ip='')
    r1.cmd('sysctl -w net.ipv4.ip_forward=1')
    s13 = net.addSwitch('s13', cls=OVSKernelSwitch, failMode='standalone')
    r6 = net.addHost('r6', cls=Node, ip='')
    r6.cmd('sysctl -w net.ipv4.ip_forward=1')
    s10 = net.addSwitch('s10', cls=OVSKernelSwitch, failMode='standalone')
    s17 = net.addSwitch('s17', cls=OVSKernelSwitch, failMode='standalone')

    info( '*** Add hosts\n')
    h3 = net.addHost('h3', cls=Host, ip='10.0.3.254/24', defaultRoute='via 10.0.3.1')
    h2 = net.addHost('h2', cls=Host, ip='10.0.2.254/24', defaultRoute='via 10.0.2.1')
    h1 = net.addHost('h1', cls=Host, ip='10.0.1.254/24', defaultRoute='via 10.0.1.1')
    h6 = net.addHost('h6', cls=Host, ip='10.0.6.254/24', defaultRoute='via 10.0.6.1')
    h4 = net.addHost('h4', cls=Host, ip='10.0.4.254/24', defaultRoute='via 10.0.4.1')
    h5 = net.addHost('h5', cls=Host, ip='10.0.5.254/24', defaultRoute='via 10.0.5.1')

    info( '*** Add links\n')
    net.addLink(r1, s2,intfName2='r1-eth0',params2={ 'ip' : '192.168.100.6/29'})
    net.addLink(r1, s5,intfName2='r1-eth1',params2={ 'ip' : '192.168.100.14/29'})
    net.addLink(r3, s2,intfName2='r3-eth0',params2={ 'ip' : '192.168.100.1/29'})
    net.addLink(r3, s4,intfName2='r3-eth1',params2={ 'ip' : '10.0.1.1/24'})
    net.addLink(r6, s5,intfName2='r6-eth0',params2={ 'ip' : '192.168.100.9/29'})
    net.addLink(r6, s7,intfName2='r6-eth1',params2={ 'ip' : '10.0.2.1/24'})
    net.addLink(s4, h1)
    net.addLink(s7, h2)
    net.addLink(r1, s8,intfName2='r1-eth3',params2={ 'ip' : '192.168.100.22/29'})
    net.addLink(r9, s8,intfName2='r9-eth0',params2={ 'ip' : '192.168.100.17/29'})
    net.addLink(r9, s10,intfName2='r9-eth1',params2={ 'ip' : '10.0.3.1/24'})
    net.addLink(s10, h3)
    net.addLink(r1, s11,intfName2='r1-eth4',params2={ 'ip' : '192.168.100.30/29'})
    net.addLink(r12, s11,intfName2='r12-eth0',params2={ 'ip' : '192.168.100.26/29'})
    net.addLink(r12, s13,intfName2='r12-eth1',params2={ 'ip' : '10.0.4.1/24'})
    net.addLink(s13, h4)
    net.addLink(r1, s14,intfName2='r1-eth5',params2={ 'ip' : '192.168.100.38/29'})
    net.addLink(r15, s14,intfName2='r15-eth0',params2={ 'ip' : '192.168.100.33/29'})
    net.addLink(r15, s16,intfName2='r15-eth1',params2={ 'ip' : '10.0.5.1/24'})
    net.addLink(s16, h5)
    net.addLink(r1, s17,intfName2='r1-eth6',params2={ 'ip' : '192.168.100.46/29'})
    net.addLink(r18, s17,intfName2='r18-eth0',params2={ 'ip' : '192.168.100.40/29'})
    net.addLink(r18, s19,intfName2='r18-eth1',params2={ 'ip' : '10.0.6.1/24'})
    net.addLink(s19, h6)

    info( '*** Starting network\n')
    net.build()
    info( '*** Starting controllers\n')
    for controller in net.controllers:
        controller.start()

    info( '*** Starting switches\n')
    net.get('s4').start([])
    net.get('s14').start([])
    net.get('s2').start([])
    net.get('s7').start([])
    net.get('s11').start([])
    net.get('s19').start([])
    net.get('s8').start([])
    net.get('s5').start([])
    net.get('s16').start([])
    net.get('s13').start([])
    net.get('s10').start([])
    net.get('s17').start([])

    info( '*** Post configure switches and hosts\n')

    net['r1'].cmd('ip route add 10.0.1.0/24 via 192.168.100.1')
    net['r1'].cmd('ip route add 10.0.2.0/24 via 192.168.100.9')
    net['r1'].cmd('ip route add 10.0.3.0/24 via 192.168.100.17')
    net['r1'].cmd('ip route add 10.0.4.0/24 via 192.168.100.26')
    net['r1'].cmd('ip route add 10.0.5.0/24 via 192.168.100.33')
    net['r1'].cmd('ip route add 10.0.6.0/24 via 192.168.100.40')
    net['r3'].cmd('ip route add 10.0.0.0/21 via 192.168.100.6')
    net['r6'].cmd('ip route add 10.0.0.0/21 via 192.168.100.14')
    net['r9'].cmd('ip route add 10.0.0.0/21 via 192.168.100.22')
    net['r12'].cmd('ip route add 10.0.0.0/21 via 192.168.100.30')
    net['r15'].cmd('ip route add 10.0.0.0/21 via 192.168.100.38')
    net['r18'].cmd('ip route add 10.0.0.0/21 via 192.168.100.46')

    CLI(net)
    net.stop()

if __name__ == '__main__':
    setLogLevel( 'info' )
    myNetwork()

