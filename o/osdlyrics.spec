Name:           osdlyrics
Version:        0.4.3
Release:        5.1
Summary:        A third-party lyrics display program
Group:          Applications/Multimedia
License:        GPLv3	
URL:            http://code.google.com/p/osd-lyrics/
Source0:        http://osd-lyrics.googlecode.com/files/%{name}-%{version}.tar.gz
BuildRequires:  libpng-devel
BuildRequires:  gcc-c++, autoconf, automake, sqlite-devel, intltool
BuildRequires:  gtk2-devel, dbus-glib-devel, libcurl-devel, libglade2-devel, sane-backends-devel
BuildRequires:  gettext-devel, libnotify-devel, notification-daemon
Requires:       gtk2, dbus-glib, libcurl, libglade2

%description
Osd-lyrics is a third-party lyrics display program, 
and focus on OSD lyrics display.

%prep
%setup -q
sed -i '1i #include <inttypes.h>' src/ol_singleton.c
sed -i '1i AUTOMAKE_OPTIONS = subdir-objects' lib/chardetect/Makefile.am src/tests/Makefile.am

%build
autoreconf -ifv
%configure
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files 
%doc AUTHORS ChangeLog INSTALL README COPYING
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/*/*/*
%{_datadir}/%{name}
%{_datadir}/locale/*/LC_MESSAGES/*

%changelog
* Fri Jul 19 2013 Wei-Lun Chao <bluebat@member.fsf.org> - 0.4.3
- Rebuilt for Fedora
* Tue Sep 22 2009 Liang Suilong <liangsuilong@gmail.com> 0.2.20090919-2
- Add gettext-devel as BuildRequires
* Sat Sep 19 2009 Liang Suilong <liangsuilong@gmail.com> 0.2.20090919-1
- Inital package for Fedora
