Summary:        3D Matrix Screensaver
Summary(pl.UTF-8):      Trójwymiarowy wygaszacz ekranu
Name:           matrixgl
Version:        2.3.2
Release:        13.1
License:        GPLv2+
Group:          X11/Applications
Source0:        https://downloads.sourceforge.net/matrixgl/%{name}-%{version}.tar.gz
URL:            https://sourceforge.net/projects/matrixgl/
BuildRequires:  mesa-libGLU-devel
BuildRequires:  mesa-libGL-devel
BuildRequires:  xscreensaver

%description
Matrixgl is a 3D screensaver for (partially for KDE) based on "The
Matrix Reloaded". It supports widescreen setups.

%description -l pl.UTF-8
Matrixgl to trójwymiarowy wygaszacz ekranu (częściowo dla KDE) oparty
na "Matrix: Reaktywacja". Posiada możliwość pracy na pełnym ekranie.

%package xscreensaver
Summary: XScreenSaver support for matrixgl
Requires: %{name}
Requires: xscreensaver

%description xscreensaver
This package contains the files needed to use matrixgl with XScreenSaver.

%prep
%setup -q

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install DESTDIR=$RPM_BUILD_ROOT
rm %{buildroot}%{_libexecdir}/xscreensaver/matrixgl
ln -s ../../bin/%{name} %{buildroot}%{_libexecdir}/xscreensaver/matrixgl

%files
%doc AUTHORS ChangeLog NEWS README TODO
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1*
%exclude %{_infodir}/dir
%{_infodir}/matrixgl.info.*

%files xscreensaver
%{_libexecdir}/xscreensaver/%{name}
%{_datadir}/xscreensaver/config/%{name}.xml

%changelog
* Thu Aug 27 2015 Wei-Lun Chao <bluebat@member.fsf.org> - 2.3.2
- Rebuilt for Fedora
* Thu Jun 24 2010 PLD Team <feedback@pld-linux.org>
- up to 2.3
- add new patches:
        -compiler.patch (checking for c++ compiler causes error)
        -Makefile.patch (remove bogus entry from Makefile.am)
- fix cvs entry (0.2.8 -> 2.2.8)
- no more sedding required
- xscreensaver.patch is now obsolete, but there is still bogus entry in configure.ac, so we need to run sed to fix that typo
- no matrixgl dir here
- initial PLD release
