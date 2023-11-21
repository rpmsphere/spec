Name:           cyclone-bootstrap
Version:        0.20
Release:        1
Summary:        Install Cyclone Scheme on your machine
Group:          Development/Languages
License:        MIT
URL:            https://github.com/justinethier/cyclone-bootstrap
Source0:        %{name}-%{version}.tar.gz
BuildRequires:  libtommath-devel
BuildRequires:  ck-devel

%description
Cyclone cannot be built directly on a system that does not have Cyclone
binaries installed because the compiler is self-hosting. Instead, this
repository uses pre-generated C code to build and install Cyclone Scheme
on a fresh system.

%undefine _debugsource_packages

%prep
%setup -q
sed -i -e 's|-Iinclude|-Iinclude -I/usr/include/ck|' -e 's|/local||' Makefile.config
sed -i 's|FLAGS.*?=|FLAGS =|' Makefile.config

%build
#export CFLAGS+=" -Iinclude -I/usr/include/ck -fPIC "
%make_build

%install
rm -rf $RPM_BUILD_ROOT
%make_install
%ifarch aarch64 x86_64
mv $RPM_BUILD_ROOT/usr/lib $RPM_BUILD_ROOT/usr/lib64
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%files
%doc LICENSE README.*
%{_bindir}/*
%{_libdir}/libcyclone.a
%{_libdir}/libcyclonebn.a
%{_includedir}/cyclone
%{_datadir}/cyclone

%changelog
* Wed Aug 26 2020 Wei-Lun Chao <bluebat@member.fsf.org> - 0.20
- Rebuilt for Fedora
