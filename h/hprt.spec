%undefine _debugsource_packages
%undefine _missing_build_ids_terminate_build

Name:		hprt
Summary:	CUPS Drivers for HPRT Printers
Group:		Applications/System
Version:	2022.1
Release:	1.bin
License:	Commercial, freeware
URL:		https://www.hprt.com.tw/
Source0:	HPRT.zip
Requires:	cups
Requires:       ghostscript

%description
CUPS Drivers for HPRT Printers.

%prep
%setup -q -n HPRT

%build

%install
install -d %{buildroot}/usr/lib/cups/filter
install -Dm755 filter/* %{buildroot}/usr/lib/cups/filter
install -d %{buildroot}%{_datadir}/cups/model/HPRT
install -Dm644 ppd/* %{buildroot}%{_datadir}/cups/model/HPRT

%files
%{_datadir}/cups/model/HPRT
/usr/lib/cups/filter/*

%changelog
* Sun Jan 2 2022 Wei-Lun Chao <bluebat@member.fsf.org> - 2022.1
- Initial package
