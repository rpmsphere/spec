%define automake_version %(rpm -q automake --qf='%%{version}' 2>/dev/null)
#%define ver %(rpm -q automake --qf %%{version} |cut -d "." -f 1,2)
#%define ver %(rpm -ql automake |cut -d "/" -f 4 |cut -d "-" -f 2 |grep 1)


Summary:        A GNOME-based clone of the Bomberman arcade game
Name:           bombermaze
Version:        0.6.6
Release:        9
License:        GPLv2+
Group:          Amusements/Games
URL:            http://www.nongnu.org/bombermaze/
Source:         %{name}-%{version}.tar.bz2
Patch0:		bombermaze-0.6.6-gcc3.4.patch
Patch1:		bombermaze-0.6.6-x86_64.patch
Patch2:		bombermaze-0.6.6-desktop.patch
Patch3:		bombermaze-0.6.6-gcc4.1.patch
Prefix:         %{_prefix}
Requires:	gdk-pixbuf >= 0.22.0
BuildPrereq:	gdk-pixbuf-devel >= 0.22.0
BuildRequires:	automake
BuildRequires:	gnome-libs-devel

%description
Bombermaze is a multiplayer action game in which players run around in a
square-grid maze while dropping bombs and collecting power-ups. The bombs
exlode after a short time delay, taking out any nearby bricks and players.
The last player left is the winner.

%prep
%setup -q
%patch0 -p1
%ifarch x86_64
%patch1 -p1
%endif
%patch2 -p1
%patch3 -p1

%build
##%ifarch x86_64
# XXX to resolve:
# checking host system type... Invalid configuration `x86_64-redhat-linux-gnu': machine `x86_64-redhat' not recognized
# we do this ugly hack (build require automake-1.9.5 was added for this)
%{__install} -m 0755 /usr/share/automake-1.11/config.sub . || %{__install} -m 0755 /usr/share/automake-%{automake_version}/config.sub | 2>/dev/null
##%endif
%configure --host=$HOSTTYPE
make %{?_smp_mflags} CPPFLAGS=-I%{_includedir}/gdk-pixbuf-1.0

%install
rm -rf $RPM_BUILD_ROOT
make DESTDIR=$RPM_BUILD_ROOT prefix="$RPM_BUILD_ROOT%{prefix}" \
	Gamesdir=%{_datadir}/applications \
	install
%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(-,root,root)
%doc AUTHORS COPYING INSTALL ChangeLog NEWS TODO
%doc doc/C/*.html
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/gnome/help/%{name}/*
%{_datadir}/pixmaps/%{name}.png
%{_datadir}/%{name}/*

%changelog
* Tue Mar 20 2018 Wei-Lun Chao <bluebat@member.fsf.org> - 
- Rebuild for Fedora
* Tue Jun  1 2011 Chris Lin <chris.lin@ossii.com.tw> - 0.6.6-9.ossii
- Fix BuildRequires: automake

* Tue Sep 29 2009 Wei-Lun Chao <bluebat@member.fsf.org> - 0.6.6-8.ossii
- Rebuild for OSSII

* Sat Jul  4 2008 Peter Hanecak <hany@hany.sk> 0.6.6-8
- reworked automake workaround so that it does not depend on preciselly
  automake 1.10

* Sun May 11 2008 Peter Hanecak <hany@hany.sk> 0.6.6-7
- build requires automake >= 1.10 and gnome-libs-devel

* Mon Feb 25 2008 Peter Hanecak <hany@hany.sk> 0.6.6-6
- more precise License tag: GPLv2+
- %%find_lang used

* Sun Jul  8 2007 Peter Hanecak <hany@hany.sk> 0.6.6-5
- rebuild for Doors 11.0 (F7)

* Sun Nov  5 2006 Peter Hanecak <hany@hany.sk> 0.6.6-4
- added % into spec
- added gcc-4.1 patch
- updated desktop file patch
- do not strip binary on install so that debuginfo package is not empty

* Wed Oct  5 2005 Peter Hanecak <hanecak@megaloman.sk> 0.6.6-3
- updated URL
- desktop file updated and moved to %%{_datadir}/applications
- patch and ugly hack to build on x86_64

* Thu Jul 14 2005 Peter Hanecak <hanecak@megaloman.sk> 0.6.6-2
- %%{?_smp_mflags} used with 'make'

* Fri Jan  4 2002 Peter Hanecak <hanecak@megaloman.sk>
[0.6.6-1]
- synchrionized with original spec
- s/Copyright/License

* Tue Aug 22 2000 Peter Hanecak <hanecak@megaloman.sk>
[0.5.1-2]
- added Vendor
- .bz2 source archive
- %%configure used instead of ./configure
- %%{prefix}/share/ changed to %%{_datadir}
- %%{prefix}/bin/ changed to %%{_bindir}
- 'rm -rf $RPM_BUILD_ROOT' in %%clean
- more documentation
- added Requires: gdk-pixbuf >= 0.8.0 and
  BuildPrereq: gdk-pixbuf-devel >= 0.8.0
- %%defattr used
- buildroot used
