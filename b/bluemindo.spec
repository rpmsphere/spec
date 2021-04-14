Name:           bluemindo
Summary:        Simple audio player in Python/PyGTK, using GStreamer
Version:        0.3
Release:        6.1
Source0:        http://codingteam.net/project/bluemindo/download/file/%{name}-%{version}.tar.gz
Patch0:		bluemindo-0.3-makefile.patch
URL:            http://codingteam.net/project/bluemindo
License:	GPLv3
Group:          Sound
Requires:	pygtk2 
Requires:	pygtk2-libglade
Requires:	python2-gstreamer
Requires:	python-tag
Requires:	dbus-python
Requires:	gnome-python2-extras
Requires:	notify-python
Requires:	python-xmpp
BuildArch:	noarch

%description
Bluemindo aims to provide a very simple audio player under
GNU systems in PyGTK, without any GNOME dependencies.

%prep
%setup -q 
%patch0 -p1 -b .orig

%build
make

%install
rm -rf %{buildroot}
make install DESTDIR=%{buildroot}
%find_lang %{name}

sed -i 's|/usr/bin/env python|/usr/bin/python2|' %{buildroot}%{_datadir}/%{name}/src/%{name}.py

%clean 
rm -rf %{buildroot} 

%files -f %{name}.lang
%doc AUTHORS CHANGELOG COPYING README THANKS 
%{_bindir}/%{name}
%{_datadir}/%{name}
%{_datadir}/applications/Bluemindo.desktop
%{_datadir}/pixmaps/%{name}.png
%{_mandir}/man1/%{name}.*

%changelog
* Sat Aug 03 2013 Wei-Lun Chao <bluebat@member.fsf.org> - 0.3
- Rebuilt for Fedora
* Sat Dec 25 2010 Yuri Myasoedov <omerta13@mandriva.org> 0.3-2mdv2011.0
+ Revision: 625104
- Fixed typo error in "Requires" section
- Fixed typo error in "Requires" section
* Sun Dec 05 2010 Yuri Myasoedov <omerta13@mandriva.org> 0.3-1mdv2011.0
+ Revision: 610850
- Fixed define section
- Fixed %%mkrel macro
- import bluemindo
