Name:		eleet
Version:	0.3.3
Release:	5.4
Summary:	Screensaver based on ships from Elite
Group:		Amusements/Graphics
License:	GPLv2
URL:		http://software.amiga-hardware.com/eleet.cgi
Source0:	http://software.amiga-hardware.com/software/eleet-0.3.3.tar.bz2
BuildRequires: libX11-devel libICE-devel libSM-devel
BuildRequires: SDL-devel SDL_image-devel SDL_ttf-devel
BuildRequires: mesa-libGL-devel mesa-libGLU-devel
BuildRequires: gnome-screensaver
BuildRequires: kdelibs qca2 udisks2

%description
A screensaver for use with Linux and UNIX, that pays homage to the classic
space trading game of Elite. Eleet displays textured rotating OpenGL models
of various spaceships, based on on those found in Elite.

A random ship is chosen from a pool of 53 models and rotated against a
starfield background, whilst the name of the ship orbits around it. Ships with
exhausts will also emit thrust particles.

%package kde
Summary:        eleet-screensaver for KDE
Requires: 	%{name} = %{version}-%{release}

%package xscreensaver
Summary:        eleet-screensaver for xscreensaver
Requires: 	%{name} = %{version}-%{release}
Requires:	xscreensaver

%description kde
eleet for KDE

%description xscreensaver
eleet as xscreensaver-hack

%prep
%setup -q
%configure

%build
make %{?_smp_mflags}

%install
make DESTDIR=$RPM_BUILD_ROOT install
rm -rf $RPM_BUILD_ROOT/%{_datadir}/doc/eleet/README
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/xscreensaver/hacks.conf.d/
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/xscreensaver/config/
install -m 644 xscreensaver/eleet.conf $RPM_BUILD_ROOT/%{_datadir}/xscreensaver/hacks.conf.d/
install -m 644 xscreensaver/eleet.xml $RPM_BUILD_ROOT/%{_datadir}/xscreensaver/config/

%clean
rm -rf $RPM_BUILD_ROOT

%post xscreensaver
if [ -x %{_sbindir}/update-xscreensaver-hacks ] ; then
    %{_sbindir}/update-xscreensaver-hacks || :
fi

%postun xscreensaver
if [ -x %{_sbindir}/update-xscreensaver-hacks ] ; then
    %{_sbindir}/update-xscreensaver-hacks || :
fi

%files
%doc COPYING README NEWS INSTALL AUTHORS
%{_bindir}/eleet
%{_datadir}/eleet/fonts/eleet.ttf
%{_datadir}/eleet/textures/

%files kde
%{_datadir}/kde4/services/ScreenSavers/eleet.desktop

%files xscreensaver
%config(noreplace) %{_datadir}/xscreensaver/config/eleet.xml
%{_datadir}//xscreensaver/hacks.conf.d/eleet.conf

%changelog
* Sun Apr 28 2013 Wei-Lun Chao <bluebat@member.fsf.org> - 0.3.3
- Rebuild for Fedora
* Mon Apr 08 2013 josef radinger <cheese@nosuchhost.net> - 0.3.3-3
- fix dependency on core-package
* Sun Apr 07 2013 josef radinger <cheese@nosuchhost.net> - 0.3.3-2
- add xscreensaver-support
* Sun Apr 07 2013 josef radinger <cheese@nosuchhost.net> - 0.3.3-1
- initial version
