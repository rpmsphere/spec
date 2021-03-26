Name:			fontpage
Version:		2.0
Release:		5.1
Summary:		Simple Font Viewing Utility
Source0:		http://www.pcbypaul.com/software/dl/FONTpage_src-%{version}.tar.bz2
Source1:		fontpage.desktop
Source2:		fontpage.png
URL:			http://www.pcbypaul.com/linux/FONTpage.html
Group:			Productivity/Publishing/Other
License:		GPL
Requires:		pygtk2 fontconfig
BuildArch:		noarch

%description
Fontpage Uses python-gtk to display system fonts and allows user to change
font size, color, background color, font face and the displayed text. Handy
to view fonts and styles quickly, or use to make "logo" graphics.

%prep
%setup -q -n "FONTpage_src-%{version}"

%build

%install
%__install -D -m 0755 fontpage.py "%{buildroot}%{_bindir}/fontpage"
%__install -D -m 0644 "%{SOURCE1}" "%{buildroot}%{_datadir}/applications/%{name}.desktop"
%__install -D -m 0644 "%{SOURCE2}" "%{buildroot}%{_datadir}/pixmaps/%{name}.png"

sed -i 's|/usr/bin/env python$|/usr/bin/python2|' %{buildroot}%{_bindir}/*

%files
%doc changelog COPYING README
%{_bindir}/fontpage
%{_datadir}/applications/fontpage.desktop
%{_datadir}/pixmaps/fontpage.png

%changelog
* Thu Feb 13 2014 Wei-Lun Chao <bluebat@member.fsf.org> - 2.0
- Rebuild for Fedora
* Fri Jul 21 2006 Pascal Bleser <guru@unixtech.be> 2.0-1
- removed Packager and Distribution, injected by rpmmacros
- new upstream version
* Mon Jan 23 2006 Pascal Bleser <guru@unixtech.be> 1.0-1
- new upstream version
* Fri Jan 20 2006 Pascal Bleser <guru@unixtech.be> 0.9-1
- new upstream version
* Tue Jan 17 2006 Pascal Bleser <guru@unixtech.be> 0.8-1
- new upstream version
* Mon Jan  9 2006 Pascal Bleser <guru@unixtech.be> 0.7-1
- changed Source URL
- rewrote spec file
- new upstream version
* Thu Oct 27 2005 Pascal Bleser <guru@unixtech.be> 0.6-1
- new upstream version
* Wed Oct  5 2005 Pascal Bleser <guru@unixtech.be> 0.2-1
- new package
