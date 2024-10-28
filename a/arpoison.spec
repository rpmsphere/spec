%undefine _debugsource_packages

Name:         arpoison
Summary:      ARP Request/Reply Utility
URL:          https://arpoison.sourceforge.net/
Group:        Mapping
License:      GPL
Version:      0.6
Release:      20080105.1
Source0:      https://arpoison.sourceforge.net/%{name}-%{version}.tar.gz
BuildRequires: libnet-devel

%description
Arpoison constructs ARP REQUEST or ARP REPLY packets using specified
hardware and protocol addresses and sends it out on a specified
Ethernet interface. Since ARP is a stateless protocol, this can
be used to update the ARP cache on most platforms with whatever
information is send in the hand-crafted packets.

%prep
%setup -q -n arpoison

%build
make

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p -m 755 \
    $RPM_BUILD_ROOT%{_sbindir} \
    $RPM_BUILD_ROOT%{_mandir}/man8
install -m 755 \
    arpoison $RPM_BUILD_ROOT%{_sbindir}
install -m 644 \
    arpoison.8 $RPM_BUILD_ROOT%{_mandir}/man8

%files
%doc LICENSE README TODO
%{_sbindir}/%{name}
%{_mandir}/man8//%{name}.8.*

%changelog
* Wed Sep 25 2013 Wei-Lun Chao <bluebat@member.fsf.org> - 0.6
- Rebuilt for Fedora
