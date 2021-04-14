Name:           drawpile
Version:        1.0.6
Release:        4.4
Summary:        A collaborative drawing program
Group:          Amusements/Graphics
License:        GPLv2+
URL:            http://drawpile.sourceforge.net/
Source0:        https://github.com/drawpile/Drawpile/archive/%{version}.tar.gz#/Drawpile-%{version}.tar.gz
BuildRequires:  libpng-devel
BuildRequires:  gcc-c++ libzip-devel cmake desktop-file-utils
BuildRequires:  qt5-qtbase-devel
BuildRequires:  qt5-qtmultimedia-devel
BuildRequires:  qt5-qtsvg-devel
BuildRequires:  qca-qt5-devel

%description
DrawPile is a sketching oriented drawing program with a twist:
you can share your drawing live with other users.
There are no restrictions on who may draw where; every user has full access
to the whole picture simultaneously.

Feature highlights:
    * Antialiased drawing and multiple blending modes
    * Layers
    * Text annotations
    * Tablet pressure sensitivity
    * Image may be rotated freely while drawing
    * Built-in server for hosting shared sessions
    * Chat

%prep
%setup -q -n Drawpile-%{version}
sed -i '24i #include <QItemSelection>' src/client/widgets/userlistwidget.h

%build
%cmake
make VERBOSE=1 %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT
install -Dm644 desktop/%{name}-32x32.png $RPM_BUILD_ROOT%{_datadir}/pixmaps/%{name}.png
install -Dm644 desktop/%{name}.desktop $RPM_BUILD_ROOT%{_datadir}/applications/%{name}.desktop
install -m644 COPYING ChangeLog AUTHORS README.md $RPM_BUILD_ROOT%{_datadir}/doc/%{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%{_datadir}/doc/%{name}
%{_bindir}/drawpile*
%{_mandir}/man1/drawpile*.1.*
%{_datadir}/applications/drawpile.desktop
%{_datadir}/pixmaps/%{name}.png
%{_datadir}/%{name}
%{_datadir}/appdata/*

%changelog
* Fri Feb 02 2018 Wei-Lun Chao <bluebat@member.fsf.org> - 1.0.6
- Rebuilt for Fedora
* Sun Mar 28 2010 Julian Aloofi <julian at, fedoraproject.org> 0.6.0-1
- initial package
