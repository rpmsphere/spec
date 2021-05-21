Name:		bobs
Version:	0.2.3
Release:	7.4
Summary:	Screensaver with small bobs 
Group:		Amusements/Graphics
License:	GPLv2
URL:		http://software.amiga-hardware.com/bobs.cgi
Source0:	http://software.amiga-hardware.com/software/bobs-0.2.3.tar.bz2
#BuildRequires: libX11-devel libICE-devel libSM-devel
BuildRequires: SDL-devel SDL_image-devel
BuildRequires: mesa-libGL-devel mesa-libGLU-devel
BuildRequires: pkgconfig
BuildRequires: gnome-screensaver
BuildRequires: kdelibs qca2 udisks2

%description
A simple screensaver for Linux and UNIX which displays animated 'Bobs'.

%package kde
Summary:    bobs-screensaver for KDE
Requires: 	%{name} = %{version}-%{release}

%package xscreensaver
Summary:    bobs-screensaver for xscreensaver
Requires: 	%{name} = %{version}-%{release}
Requires:	xscreensaver

%description kde
bobs for KDE

%description xscreensaver
bobs as xscreensaver-hack

%prep
%setup -q
%configure

%build
make %{?_smp_mflags}

%install
make DESTDIR=$RPM_BUILD_ROOT install
rm -rf $RPM_BUILD_ROOT/%{_datadir}/doc/bobs/README
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/xscreensaver/hacks.conf.d
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/xscreensaver/config
install -m 644 xscreensaver/bobs.conf $RPM_BUILD_ROOT/%{_datadir}/xscreensaver/hacks.conf.d
install -m 644 xscreensaver/bobs.xml $RPM_BUILD_ROOT/%{_datadir}/xscreensaver/config

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
%{_bindir}/bobs
%{_datadir}/bobs/textures

%files kde
%{_datadir}/kde4/services/ScreenSavers/bobs.desktop

%files xscreensaver
%config(noreplace) %{_datadir}/xscreensaver/config/bobs.xml
%{_datadir}/xscreensaver/hacks.conf.d/bobs.conf

%changelog
* Sun Apr 28 2013 Wei-Lun Chao <bluebat@member.fsf.org> - 0.2.3
- Rebuilt for Fedora
* Sat Apr 20 2013 josef radinger <cheese@nosuchhost.net> - 0.2.3-1
- initial package
