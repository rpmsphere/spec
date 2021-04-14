Name:           sunflower
Version:        0.3.61
Release:        8.1
Summary:        Graphic twin panel file manager
Group:          System/X11/Utilities
License:        GPL-3.0
URL:            http://sunflower-fm.org/
Source0:        https://codeload.github.com/MeanEYE/Sunflower/tar.gz/0.3-61#/Sunflower-0.3-61.tar.gz
Source1:        sunflower.sh
BuildArch:      noarch
BuildRequires:  python2-devel
BuildRequires:  desktop-file-utils
Requires:       pygtk2
Requires:       notify-python
Requires:       vte

%description
Is a small and highly customizable twin-panel file manager for Linux with
support for plugins.

%prep
%setup -q -n Sunflower-0.3-61

%build
rm -f translations/*/LC_MESSAGES/sunflower.po
rm -f translations/sunflower.pot

%install
%__install -D -m 644 images/sunflower.svg %{buildroot}%{_datadir}/pixmaps/%{name}.svg

%__install -d -m 755 %{buildroot}%{_datadir}/sunflower
cp -r * %{buildroot}%{_datadir}/sunflower

%__install -D -m 755 Sunflower.py %{buildroot}%{_datadir}/sunflower/Sunflower.py
%__install -D -m 755 %{SOURCE1} %{buildroot}%{_bindir}/sunflower
mkdir -p %{buildroot}%{_datadir}/applications/
mv %{buildroot}%{_datadir}/sunflower/Sunflower.desktop %{buildroot}%{_datadir}/applications/Sunflower.desktop
ln -s %{_datadir}/sunflower/images/sunflower.png %{buildroot}%{_datadir}/pixmaps/sunflower.png

sed -i 's|/usr/bin/env python$|/usr/bin/python2|' %{buildroot}%{_datadir}/%{name}/*.py

%files
%{_bindir}/sunflower
%{_datadir}/applications/Sunflower.desktop
%{_datadir}/pixmaps/%{name}.*
%{_datadir}/sunflower

%changelog
* Tue Mar 13 2018 Wei-Lun Chao <bluebat@member.fsf.org> - 0.3.61
- Rebuilt for Fedora
* Sun Feb  5 2012 nekolayer@yandex.ru
- initial package
