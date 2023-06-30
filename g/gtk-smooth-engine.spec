Summary: 	The Smooth engine for GTK+-2.0
Name: 		gtk-smooth-engine
Version: 	2.14.3
Release: 	16.1
License:	LGPLv2+ and GPLv2+
URL: 		https://sourceforge.net/projects/smooth-engine
Source0: 	https://ftp.de.debian.org/debian/pool/main/g/gtk-smooth-engine/%{name}_%{version}+deb5.tar.gz
Group: 		User Interface/Desktops
Patch0:     gtk-smooth-engine_automake.patch
Requires:	gtk2
BuildRequires: 	gtk2-devel >= 2.4.0
BuildRequires:	pango-devel >= 1.6.0
BuildRequires: 	glib2-devel >= 2.4.0
BuildRequires: 	libtool
BuildRequires: 	autoconf

%description
The Smooth engine for GTK+-2.0

%prep
%setup -q -n %{name}-%{version}+deb5
%patch0 -p1 -b .automake
NOCONFIGURE=1 ./autogen.sh

%build
%configure --disable-static
make %{?_smp_mflags}

%install
%{make_install}
find $RPM_BUILD_ROOT -name '*.la' -exec rm -f {} ';'

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%doc COPYING NEWS README AUTHORS ChangeLog
%{_libdir}/gtk-2.0/2.10.0/engines/libsmooth.so
%{_datadir}/gtk-engines/smooth.xml

%changelog
* Mon Mar 07 2016 Wei-Lun Chao <bluebat@member.fsf.org> - 2.14.3
- Rebuilt for Fedora
* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.14.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild
* Sun Jun 08 2014 Wolfgang Ulbrich <chat-to-me@raveit.de> - 2.14.3-4
- fix build for Fedora_21_Mass_Rebuild
* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.14.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild
* Sun Aug 18 2013 Wolfgang Ulbrich <chat-to-me@raveit.de> - 2.14.3-2
- fix license information
- update 'make install' macro
* Fri Feb 01 2013 Wolfgang Ulbrich <chat-to-me@raveit.de> - 2.14.3-1
- initial build
- build for f19
