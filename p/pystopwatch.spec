Name: pystopwatch
Version: 2.6
Release: 9.1
Summary: A stopwatch written in python
Group: Utility
License: GPL2
URL: https://xyne.archlinux.ca/projects/pystopwatch/
Source0: https://xyne.archlinux.ca/projects/pystopwatch/src/pystopwatch-2012.12.24.1.tar.xz
Source1: xyne.png
BuildArch: noarch

%description
A stopwatch with a timer and two countdown functions that can minimize
to the tray.

%prep
%setup -q -n %{name}-2012.12.24.1

%install
install -Dm755 %{name} %{buildroot}%{_bindir}/%{name}
install -Dm644 man/%{name}.1.gz %{buildroot}%{_mandir}/man1/%{name}.1.gz
install -Dm644 %{SOURCE1} %{buildroot}%{_datadir}/pixmaps/xyne.png

mkdir -p %{buildroot}%{_datadir}/applications
cat > %{buildroot}%{_datadir}/applications/%{name}.desktop << EOF
[Desktop Entry]
Name=pyStopwatch
Comment=A stopwatch with a timer and two countdown functions
Exec=%{name}
Icon=xyne
Terminal=false
Type=Application
Categories=Utility;
EOF

%files
%doc COPYING
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_mandir}/man1/%{name}.1.gz
%{_datadir}/pixmaps/xyne.png

%changelog
* Fri Feb 20 2015 Wei-Lun Chao <bluebat@member.fsf.org> - 2.6
- Rebuilt for Fedora
* Tue Oct 25 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 2.0-alt1.1.1
- Rebuild with Python-2.7
* Fri Nov 20 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.0-alt1.1
- Rebuilt with python 2.6
* Thu May 21 2009 Vitaly Lipatov <lav@altlinux.ru> 2.0-alt1
- initial build for ALT Linux Sisyphus
