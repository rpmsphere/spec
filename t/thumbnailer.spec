%define snapshot_date 20150126

Name:		thumbnailer
Version:	1.3.%{snapshot_date}
Release:	1
Summary:	Thumbnail generator for all kinds of files
Group:		Graphics/Utilities
License:	LGPLv3
URL:		https://launchpad.net/thumbnailer
Source:		thumbnailer-%{snapshot_date}.tar.xz
BuildRequires:	cmake
BuildRequires:	gtest-devel
BuildRequires:	pkgconfig(gdk-pixbuf-2.0)
BuildRequires:	pkgconfig(gstreamer-1.0)
BuildRequires:	pkgconfig(gstreamer-plugins-base-1.0)
BuildRequires:	pkgconfig(libexif)
BuildRequires:	pkgconfig(libsoup-2.4)
BuildRequires:	pkgconfig(Qt5Core)
BuildRequires:	pkgconfig(Qt5DBus)
BuildRequires:	pkgconfig(Qt5Qml)
BuildRequires:	pkgconfig(Qt5Quick)
BuildRequires:  python2
BuildRequires:  gtest-src
#BuildRequires:  valgrind-devel boost-devel

%description
A simple shared library that produces and stores thumbnails of image,
audio and video files according to the Freedesktop thumbnail specification.

%package	devel
Summary:	Development files for %{name}
Group:		Development/Other
Requires:	%{name} = %{version}-%{release}

%description	devel
Development files for %{name}.

%prep
%setup -q -n %{name}

%build
%cmake
make

%install
%make_install

%files
%doc COPYING
/usr/etc/apport/blacklist.d/%{name}
%{_libdir}/%{name}
%{_datadir}/dbus-1/services/com.canonical.Thumbnailer.service
%{_datadir}/glib-2.0/schemas/com.canonical.Unity.Thumbnailer.gschema.xml
%{_datadir}/%{name}
%{_qt5_prefix}/qml/Ubuntu/Thumbnailer.*
%{_libdir}/*.so.*

%files devel
%doc COPYING
%{_libdir}/lib*.so
%{_libdir}/pkgconfig/*
%{_includedir}/*

%changelog
* Wed Jan 27 2016 Wei-Lun Chao <bluebat@member.fsf.org> - 1.3.20150126
- Rebuild for Fedora
* Wed Jan 14 2015 sander85 <sander85> 1.1-20150113.2.mga5
+ Revision: 810653
- Fix major version
* Wed Jan 14 2015 sander85 <sander85> 1.1-20150113.1.mga5
+ Revision: 810625
- imported package thumbnailer
