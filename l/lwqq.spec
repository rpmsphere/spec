Name:       lwqq
Version:        0.2
Release:        10.1
License:        GPLv3
Summary:        A Linux WebQQ Client
URL:    https://github.com/mathslinux/lwqq
Group:  Internet/Instant Messenger
Source: %{name}-master.zip
BuildRequires:  cmake
BuildRequires:  gtk3-devel
BuildRequires:  libev-devel
BuildRequires:  sqlite-devel
BuildRequires:  libcurl-devel

%description
This Project is based on kernelhcy's gtkqq project, i rewrite the qq
library to impove its stability.

%package devel
Summary: Development files for %{name}
Requires: %{name} = %{version}

%description devel
Header files and libraries for the package %{name}.

%prep
%setup -q -n %{name}-master
sed -i 's| lib| %{_lib}|' lib/CMakeLists.txt

%build
%cmake
%cmake_build

%install
%cmake_install

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%{_bindir}/*
%{_libdir}/lib*.so

%files devel
%{_includedir}/%{name}
%{_libdir}/lib*.a

%changelog
* Mon Nov 11 2013 Wei-Lun Chao <bluebat@member.fsf.org> - 0.2
- Rebuilt for Fedora
