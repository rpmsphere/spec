%define	fontdir	%{_datadir}/fonts/openbarcodes

Summary: Open Barcodes Fonts
Name: openbarcodes-fonts
Version: 2.0.1
Release: 2.1
License: GPL
Group: User Interface/X
Vendor: Grand Zebu
BuildArch: noarch
BuildRoot: %{_tmppath}/%{name}-%{version}-root
Source: http://grandzebu.net/informatique/codbar/openbarcodes.zip
URL: http://grandzebu.net/informatique/codbar-en/codbar.htm
Requires(post): fontconfig

%description
Here, all is under GPL - GNU license , open source and completely free.
Barcode fonts include Code39, EAN13, Code128, 2of5code, PDF417,...

%prep
%setup -q -c

%build

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{fontdir}
install -m 0644 fonts/*.ttf $RPM_BUILD_ROOT%{fontdir}

%clean
rm -rf $RPM_BUILD_ROOT

%post
[ -x /usr/bin/fc-cache ] && /usr/bin/fc-cache 2> /dev/null

%postun
[ -x /usr/bin/fc-cache ] && /usr/bin/fc-cache 2> /dev/null

%files
%defattr(-, root, root)
%doc *.txt
%{fontdir}

%changelog
* Thu Apr 14 2011 Wei-Lun Chao <bluebat@member.fsf.org> - 2.0.1
- Rebuild for Fedora
