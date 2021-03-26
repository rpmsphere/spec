%global debug_package %{nil}
%undefine _missing_build_ids_terminate_build

Name:		pos80
Summary:	CUPS Drivers for Xprinter POS-80
Group:		Applications/System
Version:	7.77
Release:	1.bin
License:	Commercial, freeware
URL:		http://www.xprinter.net/
Source0:	POS-80.zip
Requires:	cups
Requires:       ghostscript

%description
CUPS Drivers for Xprinter POS-80.

%prep
%setup -q -n POS-80

%build

%install
%ifarch x86_64
install -Dm755 pos_64 %{buildroot}/usr/lib/cups/filter/pos
%else
install -Dm755 pos_32 %{buildroot}/usr/lib/cups/filter/pos
%endif
install -Dm644 POS-80.ppd %{buildroot}%{_datadir}/cups/model/POS/POS-80.ppd

%files
%{_datadir}/cups/model/POS/POS-80.ppd
/usr/lib/cups/filter/pos

%changelog
* Wed Aug 10 2016 Wei-Lun Chao <bluebat@member.fsf.org> - 7.77
- Initial package
