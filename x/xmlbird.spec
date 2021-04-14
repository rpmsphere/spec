%undefine _debugsource_packages

Name:           xmlbird
Version:        1.2.9
Release:        6.1
License:        LGPLv3+
Summary:        XML parser
Group:          Development/Libraries/Other
URL:            http://birdfont.org/xmlbird.php
Source0:        http://birdfont.org/xmlbird-releases/lib%{name}-%{version}.tar.xz
BuildRequires:  python3 python
BuildRequires:  vala
BuildRequires:  glib2-devel

%description
XML parser with support for Vala iterators.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name} = %{version}-%{release}

%description    devel
Development files for the XML parser.

%prep
%setup -q -n lib%{name}-%{version}
./configure -p/usr -l%{_lib}

%build
./build.py

%install
./install.py -d%{?buildroot}

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%{_libdir}/libxmlbird.so.*

%files devel
%{_libdir}/libxmlbird.so
%{_libdir}/pkgconfig/xmlbird.pc
%{_includedir}/xmlbird.h
%{_datadir}/vala/vapi
%{_datadir}/vala/vapi/xmlbird.vapi

%changelog
* Tue Jan 02 2018 Wei-Lun Chao <bluebat@member.fsf.org> - 1.2.9
- Rebuilt for Fedora
* Wed Oct 28 2015 <johan.mattsson.m@gmail.com>
- New upstream release
* Wed Jun 3 2015 <johan.mattsson.m@gmail.com>
- New upstream release
* Tue Jun 2 2015 <johan.mattsson.m@gmail.com>
- Package name changed to libxmlbird
* Mon Jun 1 2015 <johan.mattsson.m@gmail.com>
- Rpm package for the XML parser
