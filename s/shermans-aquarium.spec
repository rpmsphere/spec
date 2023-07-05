%undefine _debugsource_packages

Summary:	Applet with aquarium
Summary(pl):	Aplet z akwarium
Name:		shermans-aquarium
Version:	3.0.1
Release:	33.4
License:	GPL v2 (except for images - see COPYING)
Group:		X11/Window Managers/Tools
Source0:	https://dl.sourceforge.net/aquariumapplet/shermans_aquarium-%{version}.tar.bz2
Source1:	shermans_aquarium.desktop
Patch0:		shermans_aquarium-3.0.0-opt.patch
Patch1:		shermans_aquarium-libdir.patch
URL:		https://aquariumapplet.sourceforge.net/
BuildRequires:  libpng-devel
BuildRequires:	SDL-devel
BuildRequires:	autoconf
BuildRequires:	gai-devel sane-backends-devel
BuildRequires:	pkgconfig
BuildRequires:	zlib-devel
BuildRequires:	libbonobo-devel
BuildRequires:	w3m fedora-logos udisks2
Requires:	xscreensaver
Obsoletes:	gnome-applet-aquarium 
%define		_xscreensavdir	/etc/X11/xscreensaver

%description
This applet gives an aquarium with some randomly selected fishes. Some
other features this program gives is that the temperature scale on the
right side shows the current CPU load. It can also be configured to
display the time and show the status of numlock, capslock and
scrollock.

%description -l pl
Aplet akwarium z losowo wybranymi rybami. Innymi funkcjami programu
jakie oferuje jest to, e skala temperatury na prawo pokazuje aktualne
obcienie procesora. Aplet ten moe te by skonfigurowany do
wywietlania czasu i pokazywania statusu klawiszy numlock, capslock i
scrollock.

%prep
%setup -q -n shermans_aquarium-%{version}
%patch0 -p1
%patch1 -p1

%build
export LDFLAGS+=" -lX11 -lm -lSDL"
export CFLAGS=-Wno-format-security
%configure
%{__make} OPT="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_datadir}/applications,%{_xscreensavdir}}
export LDFLAGS='-lX11 -lm -lSDL'
%{__make} install DESTDIR=$RPM_BUILD_ROOT
install %{SOURCE1} $RPM_BUILD_ROOT%{_datadir}/applications
mv -f $RPM_BUILD_ROOT%{_datadir}/control-center/screensavers/* $RPM_BUILD_ROOT%{_xscreensavdir}
rm -rf $RPM_BUILD_ROOT%{_libdir}/bonobo/servers/*.server

%clean
rm -rf $RPM_BUILD_ROOT

%files
%doc AUTHORS ChangeLog README README.gai TODO XSCREENSAVER
%attr(755,root,root) %{_bindir}/*
%{_datadir}/applications/*
%{_datadir}/pixmaps/*
%{_xscreensavdir}/*

%changelog
* Wed May 18 2011 Wei-Lun Chao <bluebat@member.fsf.org> - 3.0.1
- Rebuilt for Fedora
* Fri Oct 22 2004 PLD Team <feedback@pld-linux.org>
All persons listed below can be reached at <cvs_login>@pld-linux.org
Revision 1.11  2004/10/22 02:11:47  havner
- rel 4
Revision 1.10  2004/10/21 17:54:35  yogib
- added typo patch send by author
Revision 1.9  2004/10/19 23:22:19  undefine
- release 3
Revision 1.8  2004/10/19 23:20:40  undefine
- fix build on amd64
Revision 1.7  2004/09/25 15:37:08  yogib
- switched to vfolders
Revision 1.6  2004/09/07 06:23:59  aflinta
- up to full version 3.0.0
Revision 1.5  2004/01/11 15:54:16  qboosh
- simplified Source0 URL, other cosmetics
Revision 1.4  2004/01/11 15:16:41  yogib
- md5 fix
Revision 1.3  2004/01/11 14:37:56  yogib
- added bcond: gai(applet support), R: xscreensaver
- moved shermans.xml to proper dir
Revision 1.2  2004/01/11 11:01:52  yogib
- up to 3.0.0pre2
- added bcond: sdl (Screensaver support), BR: zlib-devel
Revision 1.1  2003/12/23 22:51:10  yogib
- initial version
- this version supports other WM not only Gnome
