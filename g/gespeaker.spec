Name: gespeaker
Summary: GTK+ front-end for eSpeak and mbrola
Version: 0.8.6
Release: 1
Group: sound
License: Free Software
URL: http://www.muflone.com/gespeaker/
Source0: %{name}-%{version}.tar.gz
BuildArch: noarch
BuildRequires: desktop-file-utils

%description
Gespeaker is a GTK+ frontend for eSpeak and mbrola.
It allows one to play a text in many languages with settings
for voice, pitch, volume, speed and word gap.

Since version 0.6 it can use mbrola package and voices to
obtain a more realistic text reading experience.

%prep
%setup -q

%build
python2 setup.py build

%install
python2 setup.py install --root=%{buildroot} --prefix=/usr
sed -i 's|/usr/bin/env python|/usr/bin/python2|' %{buildroot}%{_datadir}/gespeaker/src/gespeaker.py

%files
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/doc/%{name}
%{_datadir}/%{name}
#{_datadir}/gtk-doc/html/%{name}
%{_datadir}/locale/*/LC_MESSAGES/%{name}.mo
%{_mandir}/man1/%{name}.1.gz
#{_datadir}/python/runtime.d/%{name}.rtupdate
/usr/lib/python2.7/site-packages/Gespeaker-%{version}-py2.7.egg-info

%changelog
* Sun Dec 12 2021 Wei-Lun Chao <bluebat@member.fsf.org> - 0.8.6
- Rebuilt for Fedora
