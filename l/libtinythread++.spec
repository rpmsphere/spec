%undefine _debugsource_packages

Name:           libtinythread++
Version:        1.1
Release:        2
Summary:        A fairly compatible subset of the C++11 thread management classes
Group:          System Environment/Libraries
License:        zlib
URL:            https://tinythreadpp.bitsnbites.eu/
Source0:        https://tinythreadpp.bitsnbites.eu/files/TinyThread++-%version-src.tar.bz2
BuildRequires:  gcc-c++

%description
TinyThread++ implements a fairly compatible subset of the C++11
thread management classes.  It has minimal overhead -- most functions
generate compact inline code, and library includes a very fast user
space mutex class (fast_mutex).

%package        devel
Summary:        Development files for %{name}
Group:          Development/Libraries
Requires:       %{name} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
%setup -q -n TinyThread++-%version

%build
pushd source
c++ $CXXFLAGS -fPIC -shared -pthread -Wl,--as-needed -Wl,-soname,%name.so.1.0 -o %name.so.1.0 tinythread.cpp
popd

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%_libdir $RPM_BUILD_ROOT%_includedir
install source/%name.so.1.0 $RPM_BUILD_ROOT%_libdir
install -m 644 source/*.h $RPM_BUILD_ROOT%_includedir
ln -s %name.so.1.0 $RPM_BUILD_ROOT%_libdir/%name.so

%check
pushd test
make
./hello && ./fractal && test -f fractal.tga && ./test
popd

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%doc README.txt
%{_libdir}/*.so.*

%files devel
%doc doc
%{_includedir}/*
%{_libdir}/*.so

%changelog
* Tue May 03 2016 Wei-Lun Chao <bluebat@member.fsf.org> - 1.1
- Rebuilt for Fedora
* Wed Aug 27 2014 Dave Love <d.love@liverpool.ac.uk> - 1.1-2
- Build with -pthread and specify soname
- Install headers 0644
* Wed Jun  4 2014 Dave Love <d.love@liverpool.ac.uk> - 1.1-1
- Initial packaging
