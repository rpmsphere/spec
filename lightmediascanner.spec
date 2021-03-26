Summary:	Lightweight media scanner
Name:		lightmediascanner
Version:	0.4.1.0
Release:	8.1
License: 	LGPLv2
Group: 		Applications/Multimedia
Source:		https://garage.maemo.org/frs/download.php/8852/%{name}-%{version}.tar.bz2
URL:		http://lms.garage.maemo.org/
BuildRequires:	sqlite-devel, libogg-devel, libvorbis-devel, flac-devel, libmp4v2-devel

%description
Lightweight library to scan media, parsing and storing into SQLite3 database.
Provides safe execution by executing the parsers in another process, that will
be monitored and killed if it takes more time than allowed.

%package devel
Summary: Development files for %{name}
Group: Development/C
Requires: %{name}

%description devel
The %name-devel package contains libraries and header files for
developing applications that use %name.

%prep
%setup -q
sed -i 's|MP4Close(mp4_fh);|MP4Close(mp4_fh,0);|' src/plugins/mp4/mp4.c
sed -i 's|MP4Read(finfo->path, 0);|MP4Read(finfo->path);|' src/plugins/mp4/mp4.c

%build
%configure
make

%install
rm -fr $RPM_BUILD_ROOT
make DESTDIR=$RPM_BUILD_ROOT install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%doc AUTHORS COPYING* README
%{_libdir}/%{name}
%{_libdir}/lib%{name}.so.*

%files devel
%exclude %{_libdir}/lib%{name}.*a
%{_libdir}/lib%{name}.so
%{_libdir}/pkgconfig/%{name}.pc
%{_includedir}/*

%changelog
* Sun Oct 30 2011 Wei-Lun Chao <bluebat@member.fsf.org> - 0.4.1.0
- Rebuild for Fedora
