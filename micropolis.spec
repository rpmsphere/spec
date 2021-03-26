Summary:	City simulation based on Maxis SimCity
Name:		micropolis
Version:	4.0
Release:	37.4
Group:		Games/Strategy
URL:		http://www.donhopkins.com/home/micropolis/
# Also see http://dev.laptop.org/git?p=projects/micropolis-activity
Source:		micropolis-activity-source.tar.bz2
Source1:	micropolis.desktop
Patch1:		micropolis-path.patch
# From debian, optflags patch:
Patch2:		micropolis-makefile.patch
## (Anssi 01/2008): Fix some 64bit pointer warnings. It is likely they are
# harmless corner cases, but this code is so old I don't take any chances.
Patch3:		micropolis-64bit-warns.patch
# Lots of fixes from
# http://git.zerfleddert.de/cgi-bin/gitweb.cgi/micropolis
# curl http://rmdir.de/~michael/micropolis_git.patch > micropolis-zerfleddert.$(date +%Y%m%d).patch
Patch0:		micropolis-zerfleddert.20080302.patch.bz2
# fix "Function call is passing too few arguments to a *printf function"
Patch4:		micropolis-printf-arg.patch
Patch5:         micropolis-glibc-2.27.patch
Patch6:         micropolis-remove-matherr.patch
License:	GPLv3+ with additional terms
BuildRequires:  libXpm-devel
BuildRequires:	libX11-devel
BuildRequires:	libXext-devel
BuildRequires:  mesa-libGL-devel
BuildRequires:	SDL-devel
BuildRequires:	SDL_mixer-devel
BuildRequires:	bison
BuildRequires:	byacc
# Plays audio through aplay:
Requires:	alsa-utils

%description
City-building simulation game originally released as SimCity by
Maxis and subsequently released as free software, renamed to
Micropolis.

%prep
%setup -q -n micropolis-activity
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4
%patch5 -p1
%patch6 -p1

#[ $(sed -n 's,activity_version = ,,p' activity/activity.info) = %version ]
[ $(sed -r -n 's,^.*MicropolisVersion = "(.+)".*$,\1,p' src/sim/sim.c) = %version ]

perl -pi -e 's,GAMESDATADIR,%{_datadir},;s,LIBDIR,%{_libdir},' Micropolis

# Re-enable air crash:
perl -pi -e 's,-DNO_AIRCRASH,,' src/sim/makefile src/makefile
perl -pi -e 's,-Werror=format-security,-Wno-error,' src/sim/makefile src/makefile

%build
make -C src

%install
install -d -m 755 %{buildroot}%{_bindir}
install -d -m 755 %{buildroot}%{_datadir}/%{name}
install -d -m 755 %{buildroot}%{_libdir}/%{name}

install -m 755 src/sim/sim %{buildroot}%{_libdir}/%{name}
install -m 755 Micropolis %{buildroot}%{_bindir}/%{name}

cp -a cities images res %{buildroot}%{_datadir}/%{name}
chmod +x %{buildroot}%{_datadir}/%{name}/res/sounds/player
install -d %{buildroot}%{_datadir}/pixmaps
install -m 644 Micropolis.png %{buildroot}%{_datadir}/pixmaps/%{name}.png
install -d $RPM_BUILD_ROOT%{_datadir}/applications
install -m 644 %{SOURCE1} $RPM_BUILD_ROOT%{_datadir}/applications/%{name}.desktop

%clean
rm -rf %{buildroot}

%files
%doc manual/*
%{_bindir}/%{name}
%{_datadir}/%{name}
%{_libdir}/%{name}
%{_datadir}/pixmaps/%{name}.png
%{_datadir}/applications/%{name}.desktop

%changelog
* Tue Jul 05 2016 Wei-Lun Chao <bluebat@member.fsf.org> - 4.0
- Rebuild for Fedora
* Mon Aug  4 2008 prusnak@suse.cz
- fixed games datadir and binary dir in spec
- fix missing arg to printf (printf-arg.patch)
- repacked sources to bz2, pack zerfleddert patch with bz2
* Fri Jun  6 2008 claes.backstrom@fsfe.org
- Updated to revisionr 177743
- sync new fixes from Michael Gernoth's git repo (20080302)
* Thu Nov 22 2007 claes.backstrom@fsfe.org
- Initial package (4.0-6)
- Revision: 158681
