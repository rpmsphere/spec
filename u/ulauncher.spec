Name: ulauncher
Summary: Application launcher for Linux
Version: 5.3.0
Release: 1
Group: Applications/Productivity
License: GPL-3
URL: http://ulauncher.io
Source0: Ulauncher-%{version}.tar.gz
BuildArch: noarch
BuildRequires: desktop-file-utils
Requires: python3-Levenshtein
Requires: python3-inotify
Requires: python3-websocket-client

%description
Ulauncher is a fast application launcher for Linux. It's is written in Python, using GTK+.

%prep
%setup -q -n Ulauncher-%{version}
sed -i 's|%%VERSION%%|%{version}|' setup.py

%build
python3 setup.py build

%install
install -Dm644 build/share/applications/ulauncher.desktop %{buildroot}%{_datadir}/applications/%{name}.desktop
python3 setup.py install --skip-build --root=%{buildroot} --prefix=/usr

%files
%{_bindir}/%{name}
%{_bindir}/%{name}-toggle
%{python3_sitelib}/%{name}*
%{_datadir}/applications/%{name}.desktop
%{_datadir}/doc/%{name}
%{_datadir}/icons/breeze/apps/48/%{name}-indicator.svg
%{_datadir}/icons/elementary/scalable/apps/%{name}-indicator.svg
%{_datadir}/icons/gnome/scalable/apps/%{name}-indicator.svg
%{_datadir}/icons/gnome/scalable/apps/%{name}.svg
%{_datadir}/icons/hicolor/48x48/apps/%{name}-indicator.svg
%{_datadir}/icons/hicolor/48x48/apps/%{name}.svg
%{_datadir}/icons/hicolor/scalable/apps/%{name}-indicator.svg
%{_datadir}/icons/hicolor/scalable/apps/%{name}.svg
%{_datadir}/icons/ubuntu-mono-dark/scalable/apps/%{name}-indicator.svg
%{_datadir}/icons/ubuntu-mono-light/scalable/apps/%{name}-indicator.svg
%{_datadir}/%{name}

%changelog
* Wed Sep 25 2019 Wei-Lun Chao <bluebat@member.fsf.org> - 5.3.0
- Rebuild for Fedora
