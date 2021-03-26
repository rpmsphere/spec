%global debug_package %{nil}

Summary: JavaScript engine for the Internet of Things
Name: jerryscript
Version: 2.0git
Release: 1
License: Apache 2.0
Group: Development/Language
URL: http://jerryscript.net/
Source: %{name}-master.zip
BuildRequires: cmake

%description
JerryScript is a lightweight JavaScript engine for resource-constrained
devices such as microcontrollers. It can run on devices with less than
64 KB of RAM and less than 200 KB of flash memory.

%package devel
Summary:        Development files for package %{name}
Requires:       %{name} = %{version}

%description devel
Libraries and header files for %{name}.

%prep
%setup -q -n %{name}-master

%build
%cmake
make

%install
%make_install
%ifarch x86_64 aarch64
mv %{buildroot}/usr/lib %{buildroot}/usr/lib64
%endif

%files
%doc LICENSE *.md
%{_bindir}/jerry

%files devel
%{_includedir}/jerry*
%{_libdir}/libjerry*
%{_libdir}/pkgconfig/libjerry*.pc

%changelog
* Fri Sep 20 2019 Wei-Lun Chao <bluebat@member.fsf.org> - 2.0git
- Rebuild for Fedora
