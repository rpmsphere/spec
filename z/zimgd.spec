%undefine _debugsource_packages

Name:     zimgd
Version:  3.2
Release:  1
Summary:  A lightweight and high performance image storage and processing system
Group:    System Environment/Deamons
License:  BSDv3
URL:      https://zimg.buaa.us
Source:   zimg-master.zip
BuildRequires: cmake
BuildRequires: libevent-devel
BuildRequires: libmemcached-devel
BuildRequires: ImageMagick-devel
Source1:  LuaJIT-2.1.0-beta3.tar.gz

%description
It's written in C and it has high performance in image field. It is designed
for high concurrency image server. It supports many features for storing and
processing images.

%prep
%setup -q -n zimg-master
rm deps/LuaJIT-2.0.3.tar.gz
cp %{SOURCE1} deps/
sed -i 's|2\.0\.3|2.1.0-beta3|g' Makefile src/CMakeLists.txt
sed -i 's|"/usr/lib" "/usr/local/lib"|"%{_libdir}"|' src/CMakeLists.txt
sed -i '45i #define luaL_reg luaL_Reg' src/zcommon.h

%build
export LDFLAGS="-Wl,--allow-multiple-definition"
make

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{_libexecdir}/%{name}
cp -a bin/* $RPM_BUILD_ROOT%{_libexecdir}/%{name}
mkdir -p $RPM_BUILD_ROOT%{_bindir}
cat > $RPM_BUILD_ROOT%{_bindir}/%{name} <<EOF
#!/usr/bin/bash
cd %{_libexecdir}/%{name}
exec ./zimg conf/zimg.lua
EOF
chmod +x $RPM_BUILD_ROOT%{_bindir}/%{name}

%files
%doc LICENSE README.md
%{_libexecdir}/%{name}
%{_bindir}/%{name}

%changelog
* Sun Dec 8 2024 Wei-Lun Chao <bluebat@member.fsf.org> - 3.2
- Rebuilt for Fedora
* Mon Sep 08 2014 <zp@buaa.us> 3.1.0
- Initial package
