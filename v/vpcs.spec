%undefine _debugsource_packages

Name:       vpcs
Version:	0.4b2
Release:	4.1
License:	BSD
Summary:	Virtual PC Simulator
URL:		http://www.freecode.com.cn/doku.php?id=wiki:vpcs
Group:      System/Emulators/Other
Source0:	%{name}-%{version}.tar.bz2
Requires:	dynamips

%description
The VPCS can simulate up to 9 PCs. You can ping/traceroute them, or ping/traceroute
the other hosts/routers from the virtual PCs when you study the Cisco routers in
the Dynamips. VPCS is not the traditional PC, it is just a program running on the
Linux or Windows, and only few network commands can be used in it. But VPCS can
give you a big hand when you study the Cisco devices in the Dynamips. VPCS can
replace the routers or VMware boxes which are used as PCs in the Dynamips network.

Try VPCS, it can save your CPU/Memory. It is very small. Now, VPCS can be run in
udp or ether mode. In the udp mode, VPCS sends or receives the packets via udp.
In the ether mode, via /dev/tap, not support on the Windows.

%prep
%setup -q
sed -i 's|-lpthread|-lpthread -Wl,--allow-multiple-definition|' src/Makefile.linux

%build
cd src
make -f Makefile.linux CPUTYPE=%_target_cpu

%install
install -Dm755 src/vpcs %buildroot/%_bindir/%{name}
install -Dm644 man/vpcs.1 %buildroot/%_mandir/man1/%{name}.1

%clean
%__rm -rf %{buildroot}

%files
%doc readme.txt COPYING
%_bindir/vpcs
%_mandir/man1/*

%changelog
* Sat Apr 20 2013 Wei-Lun Chao <bluebat@member.fsf.org> - 0.4b2
- Rebuilt for Fedora
* Mon Jan  7 2013 andrea@opensuse.org
- new upstream version 0.4b2
  * support DNS
  * support 'dump' packets
  * add 'rlogin' command to connect the remote host
  * support daemon mode
  * more at http://blog.chinaunix.net/space.php?uid=20020608&do=blog&id=3274792
- removed man page now in upstream code
* Thu Jan 12 2012 andrea@opensuse.org
- New upstream version 0.3
  * vpcs is now opensource (BSD)
* Tue Apr 19 2011 andrea@opensuse.org
- New package
