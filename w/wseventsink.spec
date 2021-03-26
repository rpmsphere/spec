Name:           wseventsink
BuildRequires:  gcc-c++ libwsman-devel pkgconfig
BuildRequires:  curl-devel
Version:        0.0.2
Release:        14.1
URL:            http://www.openwsman.org/
License:        BSD3c
Group:          System/Management
Summary:        Opensource Implementation of WS-Management - Event Sink Handler
Source:         %{name}-%{version}.tar.bz2

%description
Part of Openwsman, an Opensource Implementation of WS-Management.

Authors:
--------
    Liang Hou <houliang@intel.com>

%prep
%setup -q -n %{name}-%{version}
sed -i '44i #include <u/debug.h>' lib/eventlistener.h

%build
sh ./bootstrap
%configure --disable-static
sed -i -e 's|-Werror=format-security||' -e 's|-Werror||' Makefile */Makefile
make %{?jobs:-j%jobs}

%install
make DESTDIR=$RPM_BUILD_ROOT install
%{__rm} -rf $RPM_BUILD_ROOT/%{_libdir}/*a

%clean
rm -rf $RPM_BUILD_ROOT

%files
%{_bindir}/wseventsink
%{_libdir}/libwseventlistener.so*

%changelog
* Mon Feb 13 2012 Wei-Lun Chao <bluebat@member.fsf.org> - 0.0.2
- Rebuild for Fedora
* Fri Dec 10 2010 kkaempf@novell.com
- Initial version 0.0.2
