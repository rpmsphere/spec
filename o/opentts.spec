%global __os_install_post %{nil}

Name:          opentts
Version:       0.1
Release:       7.4
Summary:       A text-to-speech framework for POSIX operating systems
Group:         Applications/Accessibility
URL:           https://www.opentts.org
Source:        https://files.opentts.org/opentts/opentts-%{version}.tar.gz
License:       LGPL
BuildRequires: glib2-devel
BuildRequires: alsa-lib-devel
BuildRequires: libao-devel
##BuildRequires: libaudio-devel
BuildRequires: dotconf-devel
BuildRequires: espeak-devel
BuildRequires: libtool-ltdl-devel
BuildRequires: python2-devel
BuildRequires: libsndfile-devel
BuildRequires: libXau-devel

%description
A text-to-speech framework for POSIX operating systems.

%package devel
Summary:       Devel package for %{name}
Group:         Development/Libraries
Requires:      %{name} = %{?epoch:%epoch:}%{version}-%{release}

%description devel
A text-to-speech framework for POSIX operating systems.

This package contains static libraries and header files need for development.

%prep
%setup -q

%build
export PYTHON=/usr/bin/python2
%configure
make CFLAGS+="-Wl,--allow-multiple-definition -Wno-format-security"

%install
rm -rf $RPM_BUILD_ROOT
make DESTDIR=$RPM_BUILD_ROOT install

# remove conflict with speech-dispatcher
rm -f $RPM_BUILD_ROOT%{_infodir}/ssip.info*

sed -i 's|/usr/bin/python$|/usr/bin/python2|' %{buildroot}%{_bindir}/*

%files
%dir %{_sysconfdir}/opentts
%config(noreplace) %{_sysconfdir}/opentts/openttsd.conf
%config(noreplace) %{_sysconfdir}/opentts/clients/*.conf
%config(noreplace) %{_sysconfdir}/opentts/modules/*.conf
%{_bindir}/openttsd
%{_bindir}/otts-conf
%{_bindir}/otts-say
%{_bindir}/otts-send
%{_libdir}/libopentts.so.*
%dir %{_libdir}/opentts
%{_libdir}/opentts/audio
%{_libdir}/opentts/modules
%{_datadir}/opentts/conf/clients/*.conf
%{_datadir}/opentts/conf/desktop/opentts.desktop
%{_datadir}/opentts/conf/modules/*.conf
%{_datadir}/opentts/conf/openttsd.conf
%dir %{_datadir}/sounds/opentts
%{_datadir}/sounds/opentts/*.wav
%dir %{python2_sitearch}/opentts
%{python2_sitearch}/opentts/*
%{python2_sitearch}/opentts_config/*
%{_infodir}/*.info*
%exclude %{_infodir}/dir
%doc AUTHORS COPYING README TODO

%files devel
%{_libdir}/libopentts.a
%{_libdir}/libopentts.la
%{_libdir}/libopentts.so
%dir %{_includedir}/opentts
%{_includedir}/opentts/*.h
%{_libdir}/pkgconfig/*.pc

%changelog
* Wed Jun 29 2011 Wei-Lun Chao <bluebat@member.fsf.org> - 0.1
- Rebuilt for Fedora
* Sat Aug 21 2010 Silvan Calarco <silvan.calarco@mambasoft.it> 0.1-1mamba
- package created by autospec
