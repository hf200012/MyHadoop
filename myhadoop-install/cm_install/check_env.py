# -*- coding=utf-8 -*-

"""
    Check the env for the Cloudera manager install
"""

import os, sys
import re
from cm_conf.confs import *
from utils import *

def root_check():
    """
    check root user or has root permission
    @return:
    """
    if os.getuid() != 0:
        logInfo("You are not the root user, Install Myhadoop must be the root user, %s" % EXIT_MSG )
        sys.exit(-1)
    else:
        logInfo("Check root permission passed..........")

def root_ssh_check():
    """
    check the all server if can do ssh as root user
    @return:
    """
    hosts  = read_host_file()
    err_host = []
    for h in hosts:
        try:
            ssh = ssh_connect(h, ssh_port, username, root_pass)
            ssh.close()
        except Exception, ex:
            logInfo("root ssh to %s have exception: %s, Please check if root can ssh to %s or check the network. "
                % (h, ex, h))
            err_host.append(h)

    if len(err_host) != 0:
        logInfo("Check root ssh to %s servers failed, root user can't ssh to %s servers, Please Check that, %s"
            % (err_host, err_host, EXIT_MSG))
        sys.exit(-1)

    logInfo("Check root ssh to %s servers passed........ " % hosts)

def check_yum():
    """
    Check the yum can install software or not. There in all server to install the ntpdate.
    @return:
    """
    hosts = read_host_file()
    err_hosts = []
    for h in hosts:
        try:
            ssh = ssh_connect(h, ssh_port, username, root_pass)
            stdin, stdout, stderr = ssh_exc_cmd(ssh, 'yum -y install ntpdate')
            err = stderr.readlines()
            if len(err) != 0:
                err_hosts.append(h)
                logInfo("The server %s yum can't install ntpdate, maybe the yum in %s can't work, Please the yum"
                        " in %s. The info is:   " % (h, h, h,))
                for s in err:
                    logInfo(s)

        except Exception, ex:
            pass
    if len(err_hosts) != 0:
        logInfo("Check yum failed, in %s servers yum can't work %s " % (err_hosts, EXIT_MSG,))
        sys.exit(-1)
    else:
        logInfo("Yum work well, check passed.........")

def syn_sys_time():
    """
    synchronization system time for all server
    @return:
    """
    hosts  = read_host_file()
    err_hosts = []
    for h in hosts:
        try:
            ssh = ssh_connect(h, ssh_port, username, root_pass)
            stdin, stdout, stderr = ssh_exc_cmd(ssh, 'ntpdate cn.pool.ntp.org')
            err = stderr.readlines()
            if len(err) != 0:
                err_hosts.append(h)
                logInfo("Synchronize %s server failed. The info is: " % (h))
                for s in err:
                    logInfo(s)
        except Exception, ex:
            pass
    if len(err_hosts) != 0:
        logInfo("Synchronize %s servers failed. %s " % (err_hosts, EXIT_MSG,))
        sys.exit(-1)
    else:
        logInfo("Synchronize time passed.........")

def selinux_check():
    hosts  = read_host_file()
    err_hosts = []
    for h in hosts:
        try:
            ssh = ssh_connect(h, ssh_port, username, root_pass)
            stdin, stdout, stderr = ssh_exc_cmd(ssh, 'getenforce')

            if stdout.readline().strip() != "Disabled":
                err_hosts.append(h)
                logInfo("The server %s selinux is not closed, Please closed it first and reinstall. ")
        except Exception, ex:
            pass
    if len(err_hosts) != 0:
        logInfo("Check selinux status and %s servers have not close the selinux. Install the Myhadoop please "
                "close the selinux first. %s " % (err_hosts, EXIT_MSG,))
        sys.exit(-1)
    else:
        logInfo("Selinux have been closed. Check selinux status passed.........")

def iptables_check():
    hosts  = read_host_file()
    err_hosts = []
    for h in hosts:
        try:
            ssh = ssh_connect(h, ssh_port, username, root_pass)
            stdin, stdout, stderr = ssh_exc_cmd(ssh, '/etc/init.d/iptables status')

            if not stdout.readline().strip().endswith("not running."):
                err_hosts.append(h)
                logInfo("The server %s iptables is running, Please closed it first and reinstall. ")
        except Exception, ex:
            pass
    if len(err_hosts) != 0:
        logInfo("Check iptables status and %s servers have not stop the iptables. Install the Myhadoop please "
                "stop the iptables first. %s " % (err_hosts, EXIT_MSG,))
        sys.exit(-1)
    else:
        logInfo("Iptables have been stoped. Check iptables status passed.........")

def hosts_check():
    hosts  = read_host_file()
    err_hosts = []
    for h in hosts:
        try:
            ssh = ssh_connect(h, ssh_port, username, root_pass)
            # check hostname is set right
            stdin, stdout, stderr = ssh_exc_cmd(ssh, "cat /etc/sysconfig/network | grep HOSTNAME  | awk -F '=' '{print $2}'")
            hostname1 = stdout.readline().strip()
            stdin, stdout, stderr = ssh_exc_cmd(ssh, "hostname")
            hostname2 = stdout.readline().strip()
            if hostname1 != hostname2:
                err_hosts.append(h)
                logInfo("The server %s hostname not set correct, Please set it right first. ")
            # hostname can't have underscore
            if hostname2.find('_') > -1:
                if h not in err_hosts:
                    err_hosts.append(h)
                logInfo("The server %s hostname contains underscore is not allowed to install Myhadoop. Please "
                        "correct it first.")

            # check hosts file if correct
            stdin, stdout, stderr = ssh_exc_cmd(ssh, "cat /etc/hosts")
            hosts_content = stdout.readlines()
            ip = ''
            for l in hosts_content:
                if l.find(h) > -1:
                    ip = re.search("\d+\.\d+\.\d+\.\d+", l).group()
                    break

            # if ip have multiple hostname and this ip we use should be in the first
            for l in hosts_content:
                if l.find(ip) > -1:
                    if l.find(h) < 0:
                        if h not in err_hosts:
                            err_hosts.append(h)
                        logInfo("The server %s /etc/hosts not set correct %s have multiple hostname. if host have "
                                "multiple hostname and %s should be in first." % (ip, h, h))
        except Exception, ex:
            pass
    if len(err_hosts) != 0:
        logInfo("Check hostname and /etc/hosts conf and %s servers not set correctly . Install the "
                "Myhadoop please reset the hostname. %s " % (err_hosts, EXIT_MSG,))
        sys.exit(-1)
    else:
        logInfo("hostname and hosts set correctly. Check passed.........")

def check_env():
    root_check()
    root_ssh_check()
    check_yum()
    syn_sys_time()
    selinux_check()
    iptables_check()
    hosts_check()
    check_env()