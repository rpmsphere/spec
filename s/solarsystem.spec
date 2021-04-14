Name:		solarsystem
Version:	0.2.2
Release:	5.4
Summary:	Solarsystem Screensaver
Group:		Amusements/Graphics
License:	GPLv2
URL:		http://software.amiga-hardware.com/solarsystem.cgi
Source0:	http://software.amiga-hardware.com/software/solarsystem-0.2.2.tar.bz2
#BuildRequires: libX11-devel libICE-devel libSM-devel
BuildRequires: SDL-devel SDL_image-devel
BuildRequires: mesa-libGL-devel mesa-libGLU-devel
BuildRequires: pkgconfig 
BuildRequires: gnome-screensaver 
BuildRequires: kdelibs 
BuildRequires: qca2 udisks2

%description
A screensaver that displays the planets of the Solar System (inc Pluto).
A random planet is chosen and rotated on screen against a starfield background.
As the planet orbits the sun, it transitions from light into darkness
and a corona effect appears.

%package kde
Summary:        solarsystem-screensaver for KDE
Requires: 	%{name} = %{version}-%{release}

%package xscreensaver
Summary:        solarsystem-screensaver for xscreensaver
Requires: 	%{name} = %{version}-%{release}
Requires:	xscreensaver

%description kde
solarsystem for KDE.

%description xscreensaver
solarsystem as xscreensaver-hack.

%prep
%setup -q

%build
export LDFLAGS=-Wl,--allow-multiple-definition
%configure
make %{?_smp_mflags}

%install
make DESTDIR=$RPM_BUILD_ROOT install
rm -rf $RPM_BUILD_ROOT/%{_datadir}/doc/solarsystem/README
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/xscreensaver/hacks.conf.d/
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/xscreensaver/config/
install -m 644 xscreensaver/solarsystem.conf $RPM_BUILD_ROOT/%{_datadir}/xscreensaver/hacks.conf.d/
install -m 644 xscreensaver/solarsystem.xml $RPM_BUILD_ROOT/%{_datadir}/xscreensaver/config/

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
%{_bindir}/solarsystem
%{_datadir}/solarsystem/textures/

%files kde
%{_datadir}/kde4/services/ScreenSavers/solarsystem.desktop

%files xscreensaver
%config(noreplace) %{_datadir}/xscreensaver/config/solarsystem.xml
%{_datadir}//xscreensaver/hacks.conf.d/solarsystem.conf

%changelog
* Sun Apr 28 2013 Wei-Lun Chao <bluebat@member.fsf.org> - 0.2.2
- Rebuilt for Fedora
* Fri Apr 20 2013 josef radinger <cheese@nosuchhost.net> - 0.2.2-1
- initial package

