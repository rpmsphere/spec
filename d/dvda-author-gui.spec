%undefine _debugsource_packages
Name: dvda-author-gui
Summary: Qt GUI for dvda-author
Version: 10.05
Release: 1
License: GPLv3
Group: Applications/Multimedia
Source: %{name}-%{version}.tar.gz
URL: https://dvd-audio.sourceforge.net/GUI.shtml
BuildRequires: qt4-devel
Requires: dvda-author

%description
DVDA-Author Qt 4.4 graphical user interface aims at facilitating disc authoring.
It may optionally launch mkisofs after dvda-author. In this case, the output
will be an .iso file that may be burned by common tools.
Almost all command lines switches of the processing application are implemented.

%prep
%setup -q
sed -i 's|/usr/local/share/pixmaps/dvda-author.png|dvda-author|' %{name}.desktop

%build
qmake-qt4 gui.pro
make

%install
rm -rf $RPM_BUILD_ROOT
install -Dm755 gui $RPM_BUILD_ROOT%{_bindir}/%{name}
install -Dm644 %{name}.desktop $RPM_BUILD_ROOT%{_datadir}/applications/%{name}.desktop
install -Dm644 images/dvda-author.png $RPM_BUILD_ROOT%{_datadir}/pixmaps/dvda-author.png

%files
%doc README COPYING ChangeLog GUI.shtml images
%{_datadir}/applications/*
%{_datadir}/pixmaps/*
%{_bindir}/*

%changelog
* Tue Mar 20 2018 Wei-Lun Chao <bluebat@member.fsf.org> - 10.05
- Rebuilt for Fedora
* Sun Dec 05 2010 Oden Eriksson <oeriksson@mandriva.com> 09.02-2mdv2011.0
+ Revision: 610309
- rebuild
* Fri Dec 25 2009 Per Øyvind Karlsen <peroyvind@mandriva.org> 09.02-1mdv2010.1
+ Revision: 482281
- import dvda-author-gui
* Fri Dec 25 2009 Per Øyvind Karlsen <peroyvind@mandriva.org> 09.02-1
- initial release
