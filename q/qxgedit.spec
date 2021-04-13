%global debug_package %{nil}

Summary:	Qt XG Editor
Name:		qxgedit
Version:	0.9.1
Release:	1
License:	GPL-2.0+
Group:		Productivity/Multimedia/Sound/Midi
Source0:	https://sourceforge.net/projects/qxgedit/files/qxgedit/%{version}/%{name}-%{version}.tar.gz
URL:		http://qxgedit.sourceforge.net/
BuildRequires:	qt5-qtbase-devel
BuildRequires:	qt5-linguist
BuildRequires:	qt5-qtx11extras-devel
BuildRequires:	alsa-lib-devel

%description
QXGEdit is a Qt GUI for editing MIDI System Exclusive files
for XG devices (eg. Yamaha DB50XG). 

%prep
%setup -q
[ -f Makefile.git ] && %__make -f Makefile.git
sed -i 's|set dummy qmake;|set dummy qmake-qt5;|' configure

%build
%configure
make

%install
make DESTDIR=%{buildroot} install
install -d %{buildroot}%{_datadir}/pixmaps
mv %{buildroot}%{_datadir}/icons/hicolor/scalable/apps/%{name}.svg %{buildroot}%{_datadir}/pixmaps/%{name}.svg

%clean
rm -rf %{buildroot}

%files
%doc AUTHORS COPYING ChangeLog README TODO
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/%{name}.svg
%{_datadir}/icons/hicolor/32x32/apps/%{name}.png
%{_libdir}/qt5/plugins/styles/libskulpturestyle.so
%{_datadir}/metainfo/%{name}.appdata.xml
%{_mandir}/man1/%{name}*.1.*
%{_mandir}/*/man1/%{name}*.1.*

%changelog
* Sun Apr 04 2021 Wei-Lun Chao <bluebat@member.fsf.org> - 0.9.1
- Rebuild for Fedora
* Mon Sep 21 2015 Rui Nuno Capela <rncbc@rncbc.org> 0.3.0
- Summer'15 release frenzy.
* Wed Mar  4 2015 Rui Nuno Capela <rncbc@rncbc.org> 0.2.0
- Fifth public release.
* Tue Dec 31 2013 Rui Nuno Capela <rncbc@rncbc.org> 0.1.2
- A fifth of a Jubilee release.
* Sat Sep 17 2011 Rui Nuno Capela <rncbc@rncbc.org> 0.1.1
- Third public release. 
* Mon May 17 2010 Rui Nuno Capela <rncbc@rncbc.org>
- Standard desktop icon fixing. 
* Wed Apr 21 2010 Rui Nuno Capela <rncbc@rncbc.org> 0.1.1
- Second public release.
* Sat Sep 19 2009 Rui Nuno Capela <rncbc@rncbc.org> 0.0.1
- First public release.
- Added skulpture theme/style plugin.
* Mon Jul 20 2009 Rui Nuno Capela <rncbc@rncbc.org>
- Created initial qxgedit.spec
