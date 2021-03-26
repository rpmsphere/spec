%global debug_package %{nil}
Name: fontindustry
Summary: Let you convert scanned in glyph sheet into a bitmap font
Version: 0.0.10
Release: 12.1
Group: Applications/Publishing
License: GPLv3
URL: http://code.google.com/p/fontindustry/
Source0: http://fontindustry.googlecode.com/files/Fontindustry-%{version}.tar.bz2
BuildRequires: python2-devel
BuildArch: noarch
Requires: pygoocanvas

%description
Font Industry industrialize the procedure of big charset font production.
It free the big charset font creation from artists' studio to the average
John's basement. The font market will be flooded with huge amount of cheap,
low quality, big charset, hand script font in no time.

What does Font Industry really do? The program converts a scanned in grid
sheet containing a lot of glyphs into a bitmap font. The glyphs will be
automatically indexed with unicode. That's it.

%prep
%setup -q -n Fontindustry-%{version}

%build
python2 setup.py build

%install
python2 setup.py install --skip-build --root=%{buildroot} --prefix=%{_prefix}
sed -i 's|#!/bin|#!/usr/bin|' %{buildroot}%{_bindir}/*
sed -i 's|^import Image|from PIL import Image|' %{buildroot}%{python2_sitelib}/%{name}/image.py

install -d %{buildroot}%{_datadir}/applications
cat > %{buildroot}%{_datadir}/applications/%{name}.desktop <<EOF
[Desktop Entry]
Name=Font Industry
Comment=Let you convert scanned in glyph sheet into a bitmap font
Exec=%{name}
Icon=%{name}
Terminal=false
Type=Application
Categories=Application;Graphics;
Encoding=UTF-8
EOF

sed -i 's|/usr/bin/python$|/usr/bin/python2|' %{buildroot}%{_bindir}/*

%files
%doc AUTHORS HACKING ChangeLog LICENSE README TODO
%{_bindir}/*
%{_datadir}/%{name}
%{python2_sitelib}/*
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/%{name}.png

%changelog
* Sun Jun 16 2013 Wei-Lun Chao <bluebat@member.fsf.org> - 0.0.10
- Rebuild for Fedora
