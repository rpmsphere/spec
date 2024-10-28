Name: whyteboard
Summary: A simple whiteboard and PDF annotator
Version: 0.41.1
Release: 1
License: see /usr/share/doc/whyteboard/copyright
Group: Applications/Multimedia
Source0: https://launchpadlibrarian.net/55842796/%{name}-%{version}.tar.gz
Source1: %{name}.png
Source2: %{name}-0.40.1.zh_TW.mo
URL: https://code.google.com/p/whyteboard/
BuildArch: noarch
Requires: python2-wxpython, ImageMagick

%description
A simple whiteboard and PDF annotation program. Features tabbed drawing,
text input, multiple languages and is easy to use.

%prep
%setup -q
cp -a %{SOURCE2} locale/zh_TW/LC_MESSAGES/whyteboard.mo

%build

%install
%__rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/lib/%{name}
cp -a %{name} %{name}.py %{name}-help images locale LICENSE.txt %{buildroot}/usr/lib/%{name}
mkdir -p %{buildroot}%{_datadir}/pixmaps
cp %{SOURCE1} %{buildroot}%{_datadir}/pixmaps

mkdir -p %{buildroot}%{_bindir}
cat > %{buildroot}%{_bindir}/%{name} <<EOF
#!/bin/bash
cd /usr/lib/whyteboard
./whyteboard.py --lang=\${LANG%%.*}
EOF

mkdir -p %{buildroot}%{_datadir}/applications
cat > %{buildroot}%{_datadir}/applications/%{name}.desktop <<EOF
[Desktop Entry]
Version=1.0
Encoding=UTF-8
Name=Whyteboard
Comment=A simple PDF and image annotator
Icon=whyteboard
Exec=whyteboard %f
Terminal=false
Type=Application
Categories=GNOME;GTK;Graphics
StartupNotify=false
EOF

sed -i 's|/usr/bin/env python|/usr/bin/python2|' %{buildroot}/usr/lib/%{name}/%{name}.py %{buildroot}/usr/lib/%{name}/%{name}/*.py %{buildroot}/usr/lib/%{name}/%{name}/*/*.py

%files
%doc CHANGELOG.txt DEVELOPING.txt README.txt TODO.txt
%attr(755,root,root) %{_bindir}/%{name}
/usr/lib/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/%{name}.png

%changelog
* Tue Mar 20 2018 Wei-Lun Chao <bluebat@member.fsf.org> - 0.41.1
- Rebuilt for Fedora
