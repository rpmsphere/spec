Name:           pykaraoke
License:        LGPL
Group:          Applications/Multimedia
Version:        0.7.5
Release:        5.4
Summary:	Free karaoke player
URL:		http://www.kibosh.org/pykaraoke/
Source:         http://sourceforge.net/projects/pykaraoke/files/%name/%version/%name-%version.zip
Requires:       pygame python2-wxpython libtimidity liberation-sans-fonts
BuildRequires:  gcc python2-wxpython python2-devel pygame-devel SDL-devel desktop-file-utils atlas-devel

%description
PyKaraoke is a free karaoke player for Linux, FreeBSD, NetBSD, Windows, OSX
and GP2X. You can use this program to play your collection of CDG, MIDI and
MPEG karaoke songs. No songs are provided, you must obtain these from elsewhere.
Warning - this version uses 1251 codepage for kar files!

%prep
%setup -q

%build
python2 setup.py build

%install
rm -rf $RPM_BUILD_ROOT
python2 setup.py install --prefix=/usr --root=$RPM_BUILD_ROOT
chmod +x $RPM_BUILD_ROOT/usr/bin/cdg2mpg
chmod +x $RPM_BUILD_ROOT/usr/bin/py*

sed -i 's|/usr/bin/env python$|/usr/bin/python2|' %{buildroot}%{_bindir}/*

%post
ln -sf /usr/share/fonts/truetype/LiberationSans-Regular.ttf /usr/share/%name/fonts/DejaVuSans.ttf
ln -sf /usr/share/fonts/truetype/LiberationSans-Bold.ttf /usr/share/%name/fonts/DejaVuSansCondensed-Bold.ttf
ln -sf /usr/share/fonts/truetype/LiberationSans-Bold.ttf /usr/share/%name/fonts/DejaVuSansCondensed.ttf

%clean
rm -rf $RPM_BUILD_ROOT

%files
%doc README.txt PKG-INFO
%{_bindir}/cdg2mpg
%{_bindir}/py*
%{python_sitearch}/*
%{_datadir}/applications/*.desktop
%{_datadir}/%name

%changelog
* Sun Jul 08 2012 Wei-Lun Chao <bluebat@member.fsf.org> - 0.7.5
- Rebuild for Fedora
* Sun Dec 28 2008 Dmitry Stropaloff <helions8@gmail.com>
- initial version 0.6
