%undefine _debugsource_packages

Name:           thorlib
Version:        0.1
Release:        7.1
Summary:        A small c++ helper library
Group:          Development/Libraries/C and C++
License:        GPLv2
URL:            http://code.google.com/p/gnchess/
Source0:        http://gnchess.googlecode.com/files/%{name}-%{version}.tar.gz

%description
Thor Library is a small c++ helper library.

%package        devel
Summary:        Development files for Thorlib
Group:          Development/Libraries/C and C++
Requires:      gcc-c++

%description    devel
Thor Library is a small c++ helper library.

%prep
%setup -q

%build
make

%install
rm -rf %{buildroot}
make install DESTDIR=%{buildroot}
%ifarch x86_64 aarch64
mv %{buildroot}/usr/lib %{buildroot}/usr/lib64
%endif

%clean
rm -rf %{buildroot}

%files devel
%{_bindir}/mkres
%{_libdir}/pkgconfig/*.pc
%{_includedir}/*

%changelog
* Sun Mar 3 2013 Wei-Lun Chao <bluebat@member.fsf.org> - 0.1
- Rebuilt for Fedora
