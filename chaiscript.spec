%global debug_package %{nil}

Name:         chaiscript
Summary:      C++ Scripting Language
URL:          http://www.chaiscript.com/
Group:        Development/Language
License:      BSD
Version:      6.1.0
Release:      4.1
Source0:      https://github.com/ChaiScript/ChaiScript/archive/v%{version}.tar.gz#/ChaiScript-%{version}.tar.gz
BuildRequires:	gcc-c++, cmake

%description
ChaiScript is one of the first (and perhaps only) embedded scripting
language designed from the ground up to directly target C++. Being
a native C++ application, it has some advantages over existing
embedded scripting languages: it uses a header-only approach, which
makes it easy to integrate with existing projects; it maintains
type safety between your C++ application and user scripts; and it
supports a variety of C++ techniques including callbacks, overloaded
functions, class methods, and STL containers.

%prep
%setup -q -n ChaiScript-%{version}

%build
cmake -DCMAKE_INSTALL_PREFIX=/usr .
make

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT
%ifarch x86_64 aarch64
mv $RPM_BUILD_ROOT/usr/lib $RPM_BUILD_ROOT/usr/lib64
%endif

%files
%{_bindir}/chai
%{_includedir}/%{name}
%{_datadir}/%{name}
%{_libdir}/%{name}
%{_libdir}/pkgconfig/%{name}.pc

%clean
rm -rf $RPM_BUILD_ROOT

%changelog
* Thu May 31 2018 Wei-Lun Chao <bluebat@member.fsf.org> - 6.1.0
- Rebuild for Fedora
