Summary: 	Enlightenment video and media library
Name: 		emotion
Version: 	0.2.0.65643
Release: 	1%{?dist}
License: 	BSD
Group: 		Graphical desktop/Enlightenment
URL: 		http://www.enlightenment.org/
Source: 	http://download.enlightenment.org/snapshots/LATEST/%{name}-%{version}.tar.bz2
BuildRoot: 	%{_tmppath}/%{name}-buildroot
# Common
##BuildRequires:	xine-devel
BuildRequires:	ffmpeg
Buildrequires:  gstreamer-ffmpeg 
BuildRequires:	gstreamer-plugins-good
BuildRequires:	gstreamer-devel
BuildRequires:	gstreamer-plugins-base-devel
BuildRequires:	keyutils-libs-devel
# Enlightenment BR
BuildRequires:	libeina-devel
BuildRequires: 	eet-devel
BuildRequires:  evas-devel
BuildRequires:	ecore-devel
BuildRequires:	efreet-devel
BuildRequires:	embryo-devel
BuildRequires:	edje-devel


%description
Emotion is a video & media object library designed to interface with Evas and
Ecore to provide autonomous "video" and "audio" objects that can be moved,
resized and positioned like any normal object, but instead they can play video
and audio and can be controlled from a high-level control API allowing the
programmer to quickly piece together a multi-media system with minimal work.

This package is part of the Enlightenment DR17 desktop shell.

%package devel
Summary: Headers and development libraries from %{name}
Group: Graphical desktop/Enlightenment
Requires: %name = %{version}
Provides: lib%{name}-devel = %{version}-%{release}
Provides: %name-devel = %{version}-%{release}

%description devel
%{name} development headers and libraries

%prep
%setup -q

%build
./configure --enable-gstreamer --enable-xine --disable-vlc --disable-static --prefix=/usr
%__make

%install
rm -rf $RPM_BUILD_ROOT
make DESTDIR=$RPM_BUILD_ROOT install

%post
/sbin/ldconfig

%postun
/sbin/ldconfig

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc AUTHORS COPYING README
%{_bindir}/%{name}_*
%{_datadir}/%name
%{_libdir}/%name
%_libdir/lib*.so.*
%{_libdir}/edje
%{_libdir}/edje

%files devel
%defattr(-,root,root)
%{_libdir}/pkgconfig/*
%{_libdir}/*.so
%{_libdir}/*.la
%{_includedir}/emotion-0


%changelog
* Fri Mar 09 2012 Wei-Lun Chao <bluebat@member.fsf.org> 0.2.0
- Update to r65643

* Tue Jan 04 2011 Wei-Lun Chao <bluebat@member.fsf.org>
- Rebuild for OSSII

* Sat Dec 25 2010 Texstar <texstar at gmail.com> 20101225-1pclos2010
- update svn

* Wed Dec 15 2010 Texstar <texstar at gmail.com> 20101215-1pclos2010
- update svn 55246
