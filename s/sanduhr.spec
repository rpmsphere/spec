Summary: A sand-glass alarm clock
Name: sanduhr
Version: 1.93
Release: 16.4
License: GPL
Group: Amusements/Graphics
URL: https://www.seehuhn.de/pages/sanduhr
Source: https://m.seehuhn.de/programs/%{name}-%{version}.tar.gz
BuildRequires: gtk2-devel
BuildRequires: libgnomeui-devel
BuildRequires: libbonobo-devel
BuildRequires: ORBit2-devel
BuildRequires: w3m udisks2
Requires: compat-openssl10

%description
SandUhr is a sand-glass alarm clock. The program uses the X Window System and
the GNOME desktop environment. The alarm is either rings the console bell, by
playing a sound file, or by starting an external program of your choice.

%prep
%setup -q

%build
%configure
make

%install
%makeinstall
mkdir -p %{buildroot}%{_datadir}/applications
mv %{buildroot}%{_datadir}/gnome/apps/Utilities/sanduhr.desktop %{buildroot}%{_datadir}/applications
sed -i -e 's|Icon=|Icon=/usr/share/pixmaps/|' -e '8i Categories=Utility;' %{buildroot}%{_datadir}/applications/sanduhr.desktop

%files
%doc AUTHORS COPYING ChangeLog NEWS README TODO
%{_bindir}/*
%{_datadir}/idl/sanduhr.idl
%{_mandir}/*/*
%{_datadir}/pixmaps/sanduhr
%{_datadir}/sounds/sanduhr
%{_datadir}/omf/sanduhr
%{_datadir}/locale/*/*/*
%{_datadir}/applications/sanduhr.desktop
%{_datadir}/gnome/help/sanduhr
%{_libdir}/bonobo/servers/sanduhr.server

%changelog
* Tue Oct 15 2013 Wei-Lun Chao <bluebat@member.fsf.org> - 1.93
- Rebuilt for Fedora
* Thu Feb 15 2001 Nalin Dahyabhai <nalin@redhat.com>
- add -D__STRICT_ANSI__ to the CFLAGS used
* Mon Sep 18 2000 Tim Powers <timp@redhat.com>
- initial package for Powertools
