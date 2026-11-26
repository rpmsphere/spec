%undefine _debugsource_packages

Name:		hprtpos-cups-drivers
Summary:	CUPS Drivers for HPRT POS Printers
Group:		Applications/System
Version:	1.2.22
Release:	1.bin
License:	Commercial, freeware
URL:		https://www.hprt.com.tw/
Source0:	https://www.hprt.com.tw/Product/POS-Printers/TP805/hprt_pos_printer_linux_driver_v%{version}.zip
Requires:	cups
Requires:       ghostscript

%description
CUPS Drivers for HPRT POS Printers.

%prep
%setup -q -n hprt_pos_printer_linux_driver_v%{version}

%build

%install
install -d %{buildroot}/usr/lib/cups/filter
install -Dm755 filter/x64/* %{buildroot}/usr/lib/cups/filter
install -d %{buildroot}%{_datadir}/cups/model/HPRTPOS
install -Dm644 ppd/* %{buildroot}%{_datadir}/cups/model/HPRTPOS

%files
%{_datadir}/cups/model/HPRTPOS
/usr/lib/cups/filter/*

%changelog
* Sun Aug 3 2025 Wei-Lun Chao <bluebat@member.fsf.org> - 1.2.22
- Rebuilt for Fedora
