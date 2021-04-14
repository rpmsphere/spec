Name:           arpcheck
Version:        1.8
Release:        2.1
Summary:        Ethernet Layer 2 checking tool

Group:          Applications/Internet
License:        GPLv2+
URL:            http://ge.mine.nu/arpcheck.html
Source0:        http://ge.mine.nu/code/arpcheck
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:      noarch

Requires:       samba-client
Requires:       iptables

%description
arpcheck checks /proc/net/arp for MAC/IP combinations and compares them
to a static or dynamic MAC list. If something does not fit, you'll get
an alarm which will also be logged. You can also run custom scripts.

This is useful, if you're a router with multiple interfaces (e.g. WAN, 
LAN, DMZ) and want to check if anyone from your clients is evil and does
some arpspoofing (mitm) or changes his IP.

%prep

%build

%install
rm -rf $RPM_BUILD_ROOT
install -Dp -m 0755 %{SOURCE0} $RPM_BUILD_ROOT%{_bindir}/%{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%{_bindir}/%{name}

%changelog
* Thu Feb 09 2012 Wei-Lun Chao <bluebat@member.fsf.org> - 1.8
- Rebuilt for Fedora

* Thu Jan 02 2009 Fabian Affolter <fabian@bernewireless.net> - 1.8-1
- Initial spec for Fedora
