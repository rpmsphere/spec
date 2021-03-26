Name:			reportdhcp
Summary:		Displays statistics and lease entries for DHCPD
Version:		2.1
Release:		9.1
Source:			%{name}-%{version}.tar.gz
URL:			http://www.omar.org/opensource/reportdhcp/
License:		GPL
Group:			Productivity/Networking/Diagnostic
BuildArch:		noarch
Requires:		httpd
Requires:		dhcp-server
Requires:		perl
Patch0:			%{name}-%{version}.pl.patch

%description
Reportdhcp.pl is a CGI script that displays statistics and lease
entries for ISC DHCPD by parsing the dhcpd.conf and dhcpd.leases
files. It currently supports version 3.0p1 and above of the ISC
DHCP distribution.

%prep
%setup -q
%patch0

%install
rm -rf $RPM_BUILD_ROOT
install -D -m755 %{name}.pl $RPM_BUILD_ROOT/var/www/cgi-bin/%{name}.pl

%files
/var/www/cgi-bin/%{name}.pl
%doc README CHANGELOG

%clean
rm -rf $RPM_BUILD_ROOT

%changelog
* Sun Aug 05 2012 Wei-Lun Chao <bluebat@member.fsf.org> - 2.1
- Rebuild for Fedora
