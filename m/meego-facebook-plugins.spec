Name:       meego-facebook-plugins
Summary:    Facebook plugins for MeeGo
Version:    1.0
Release:    3.1
Group:      System/GUI/Other
License:    LGPL 2.1
URL:        http://www.meego.com
Source0:    %{name}-%{version}.tar.bz2
Requires:   libsocialweb-keys
BuildRequires:  pkgconfig(gconf-2.0)
BuildRequires:  pkgconfig(rest-0.6)
BuildRequires:  pkgconfig(rest-extras-0.6)
BuildRequires:  pkgconfig(gnome-keyring-1)
BuildRequires:  pkgconfig(json-glib-1.0)
BuildRequires:  pkgconfig(libsocialweb-module)
BuildRequires:  pkgconfig(libsocialweb-keyfob)
BuildRequires:  pkgconfig(libsocialweb-keystore)
BuildRequires:  pkgconfig(bisho)
BuildRequires:  libmx-devel
BuildRequires:  pkgconfig(webkit-1.0)
BuildRequires:  intltool
Buildrequires:	libbisho-common0

%description
Facebook plugins for libsocialweb


%prep
%setup -q 

%build
autoreconf -fi
sed -i 's/0\.6\.4/0.6.1/' configure*
%configure --disable-static
make %{?jobs:-j%jobs}

%install
%makeinstall
find %{buildroot}%{_libdir} -name '*.la' -delete -print

%files
%defattr(-,root,root,-)
%{_libdir}/bisho/liboauth2-facebook.so
%{_libdir}/libsocialweb/services/libfacebook.so
%{_datadir}/libsocialweb/services/facebook.keys

%clean
rm -rf %{buildroot}


%changelog
* Tue Mar 20 2018 Wei-Lun Chao <bluebat@member.fsf.org> - 
- Rebuilt for Fedora
* Tue Oct 26 2010 Wei-Lun Chao <bluebat@member.fsf.org>
- Rebuild for OSSII
* Mon Sep 20 2010 awafaa@opensuse.org
- Fix build errors, removing .la files and correct BR
* Wed Sep 15 2010 awafaa@opensuse.org
- Initial import for openSUSE version 1.0
