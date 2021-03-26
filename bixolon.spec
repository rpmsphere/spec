%global debug_package %{nil}
%undefine _missing_build_ids_terminate_build

Name:		bixolon
Summary:	CUPS Drivers for Bixolon printers
Group:		Applications/System
Version:	1.3.4.2
Release:	1.bin
License:	Commercial, freeware
URL:		http://www.bixolon.com/
Source0:	http://www.bixolon.com/upload/download/software_%{name}cupsdrv_linux_v%{version}_x64.tgz
Source1:	http://www.bixolon.com/upload/download/software_%{name}cupsdrv_linux_v%{version}_x84.tgz
Requires:	cups
Requires:       ghostscript

%description
The printer driver was developed to add printing support for BIXOLON Thermal
printer under Linux operating systems, using the widely available and popular
CUPS (Common UNIX Printing System) printing system.

The driver was written using the C programming language, and utilizes various
CUPS API (application programming interface) calls. This driver will enable
users of BIXOLON printers to print their receipt under the Linux operating
systems.

%prep
%ifarch x86_64
%setup -q -n Software_BixolonCupsDrv_Linux_v%{version}_x64
%else
%setup -q -T -b 1 -n Software_BixolonCupsDrv_Linux_v%{version}_x84
%endif

%build

%install
install -Dm755 rastertoBixolon_v%{version} %{buildroot}/usr/lib/cups/filter/rastertoBixolon
install -d %{buildroot}%{_datadir}/cups/model
cp -a Bixolon %{buildroot}%{_datadir}/cups/model

%files
%doc SoftwareLicense.txt
%{_datadir}/cups/model/Bixolon
/usr/lib/cups/filter/rastertoBixolon

%changelog
* Tue Mar 15 2016 Wei-Lun Chao <bluebat@member.fsf.org> - 1.3.4.2
- Initial package
