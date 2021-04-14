Name:           ap-utils
Version:        1.5
Release:        6.1
Summary:        Configure and monitor Wireless Access Points
Group:          Applications/Internet
License:        GPLv2
URL:            http://ap-utils.polesye.net/
Source0:        ftp://linux.zhitomir.net/%{name}/%{name}-%{version}.tar.bz2
BuildRequires:  gettext
BuildRequires:  ncurses-devel

%description
Wireless Access Point Utilities for Unix - it's a set of utilities to
configure and monitor Wireless Access Points under Unix using SNMP
and tftp protocol.

* ap-config - to config and get stats from Atmel-MIB based APs and
  devices that support IEEE 802.11 MIB and NWN DOT11EXT MIB
* ap-gl - to config and get stats from Atmel-MIB based APs with
  1.4k.2 firmware
* ap-tftp - command line utility to upgrade AP firmare over tftp
* ap-auth - command line utility to work with mac auth
* ap-mrtg - to get stat from AP and return it in MRTG parsable format
* ap-rrd - to get stat from AP and save it into RRD database
* ap-trapd - to receive, parse, and log trap messages from AP

%prep
%setup -q

%build
%configure
make %{?_smp_mflags} CFLAGS+="-Wno-format-security"
iconv -f iso8859-1 -t utf-8 README > README.conv
touch -c -r README README.conv
mv README.conv README

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT
%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%doc ABOUT-NLS AUTHORS ChangeLog COPYING NEWS README THANKS TODO
%doc Documentation/*.html Documentation/FAQ
%doc %{_mandir}/man?/ap-*.8*
%{_bindir}/ap-*
%{_sbindir}/ap-*

%changelog
* Thu Feb 09 2012 Wei-Lun Chao <bluebat@member.fsf.org> - 1.5
- Rebuilt for Fedora
* Sun Nov 02 2008 Fabian Affolter <fabian@bernewireless.net> - 1.5-1
- Initial package for Fedora
