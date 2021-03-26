Name: cpplinda
Summary: C++ LINDA implementation
Version: 1.0
Release: 15.1
Group: Development/Libraries
License: GPLv2
URL: http://sourceforge.net/projects/cpplinda/
Source0: http://sourceforge.net/projects/cpplinda/files/cpplinda/%5BUnnamed%20release%5D/%{name}_v%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildRequires: boost-devel
BuildRequires: boost-static

%description
CppLINDA is a C++ LINDA implementation of the LINDA coordination language for
Linux Operating Systems. This Library consists of a client and server
implementation and , moreover, some new operations.

%prep
%setup -q -n Library
sed -i '1i #include <cstdio>' src/linda/core/channel.cpp
sed -i '1i #include <cstring>\n#include <unistd.h>' src/linda/network/space_network.cpp
sed -i -e 's|-WI|-Wl|' -e 's| /usr| %{buildroot}/usr|' -e 's|/lib|/%{_lib}|' src/Makefile
%if 0%{fedora} < 20
sed -i 's|-lboost_thread|-lboost_thread-mt|' src/Makefile
%endif

%build
make %{?_smp_mflags} -C src

%install
mkdir -p %{buildroot}%{_libdir} %{buildroot}%{_includedir}
make -C src install

%files
%doc README *.pdf
%{_includedir}/linda
%{_libdir}/lib*

%changelog
* Mon Oct 21 2013 Wei-Lun Chao <bluebat@member.fsf.org> - 1.0
- Rebuild for Fedora
