%define _name zig

Summary: Zig system programming language
Name: ziglang
Version: 0.4.0git
Release: 1
License: MIT
Group: Development/Languages
#Source: https://github.com/ziglang/zig/archive/%{version}.tar.gz#/%{_name}-%{version}.tar.gz
Source: zig-master.zip
URL: https://github.com/ziglang/zig
BuildRequires: cmake
BuildRequires: llvm-devel
BuildRequires: clang-devel
BuildRequires: elfutils-libelf-devel
BuildRequires: libstdc++-static

%description
Zig is an open-source programming language designed for robustness, optimality, and clarity.

%prep
#setup -q -n %{_name}-%{version}
%setup -q -n zig-master
sed -i 's|-Werror | |' CMakeLists.txt
sed -i '287i "${CMAKE_SOURCE_DIR}/deps/SoftFloat-3e/source/8086/s_propagateNaNF64UI.c"' CMakeLists.txt
sed -i '287i "${CMAKE_SOURCE_DIR}/deps/SoftFloat-3e/source/8086/s_propagateNaNF32UI.c"' CMakeLists.txt

%build
%cmake
make

%install
rm -rf $RPM_BUILD_ROOT
%make_install
mkdir -p %{buildroot}%{_libdir}
mv zig_cpp/* %{buildroot}%{_libdir}

%files 
%doc README.md LICENSE
%{_bindir}/%{_name}
#/usr/lib/%{_name}
%{_libdir}/lib*

%clean
rm -rf $RPM_BUILD_ROOT

%changelog
* Tue Jul 16 2019 Wei-Lun Chao <bluebat@member.fsf.org> - 0.4.0git
- Rebuild for Fedora
