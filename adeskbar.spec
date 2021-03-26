Name:           adeskbar
Version:        0.5.1
Release:        2.1
Summary:        A launcher for OpenBox
Group:          Graphical desktop/Openbox
License:        GPLv3
URL:            http://adeskbar.tuxfamily.org/
Source0:        http://download.tuxfamily.org/adeskbar/sources/%{name}-%{version}.tar.gz
BuildRequires:  python2
Requires:	pygtk2
Requires:	python2-cairo
Requires:	pygobject2
Requires:	libwnck
Requires:	python2-pyxdg
BuildArch:	noarch

%description
ADesk Bar is a easy, simple, unobtrusive application launcher for Openbox, yet
also works great under Gnome or XFCE.

%prep
%setup -q -n %{name}-0.5

%build
# Uh... Nothing to build.

%install
# Taken from the included install.sh file.
install -d $RPM_BUILD_ROOT/usr/share/adeskbar
install -d $RPM_BUILD_ROOT/usr/bin
install -d $RPM_BUILD_ROOT/usr/share/applications
install -d $RPM_BUILD_ROOT/usr/share/pixmaps

# mkdir $RPM_BUILD_ROOT/usr/share/adeskbar
cp -a src/*  $RPM_BUILD_ROOT/usr/share/adeskbar
# chown -R root: $RPM_BUILD_ROOT/usr/share/adeskbar
cp src/images/adeskbar.png $RPM_BUILD_ROOT/usr/share/pixmaps/
cp adeskbar.desktop $RPM_BUILD_ROOT/usr/share/applications/
cp adeskbar.sh $RPM_BUILD_ROOT/usr/bin/adeskbar

sed -i 's|/usr/bin/env python|/usr/bin/python2|' $RPM_BUILD_ROOT/usr/share/adeskbar/main.py

%clean
rm -rf $RPM_BUILD_ROOT

%files
%{_datadir}/%{name}/*
%{_datadir}/applications/
%{_datadir}/pixmaps/
%{_bindir}/%{name}

%changelog
* Mon Jul 16 2012 Wei-Lun Chao <bluebat@member.fsf.org> - 0.5.1
- Rebuild for Fedora
* Sat Jan 08 2011 Texstar <texstar at gmail.com> 0.4.2-3pclos2011
- add dep pyxdg
* Sun Oct 31 2010 Texstar <texstar at gmail.com> 0.4.2-2pclos2010
- convert source to tar.xz
- add proper menu
* Thu Oct 21 2010 Ertain <sirius-c at iname.com> 0.4.2-1pclos2010
- Initial package.
