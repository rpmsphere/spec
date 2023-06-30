%undefine _debugsource_packages

Name:         al
Summary:      Assembly Line Library
URL:          https://www.ossp.org/pkg/lib/al/
Group:        Libraries
License:      MIT/X11-style
Version:      0.9.3
Release:      20080111.1
Source0:      ftp://ftp.ossp.org/pkg/lib/al/%{name}-%{version}.tar.gz

%description
OSSP al defines an abstract data type of a data buffer that can
assemble, move and truncate chunks of data in a stream but avoids
actual copying. It was built to deal efficiently with communication
streams between software modules. It especially provides flexible
semantical data attribution through by-chunk labeling. It also
has convenient chunk traversal methods and optional OSSP ex based
exception handling.

%prep
%setup -q

%build
%ifarch aarch64
cp -f /usr/lib/rpm/redhat/config.* .
%endif
%configure
%{__make} %{_smp_mflags -O}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} %{_smp_mflags} install DESTDIR=$RPM_BUILD_ROOT

%files
%{_bindir}/al-config
%{_includedir}/al.h
%{_libdir}/libal.*
%{_mandir}/man3/al.3.*

%clean
rm -rf $RPM_BUILD_ROOT

%changelog
* Wed Sep 25 2013 Wei-Lun Chao <bluebat@member.fsf.org> - 0.9.3
- Rebuilt for Fedora
