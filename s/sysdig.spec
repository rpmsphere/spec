Name: sysdig
Version: 0.17.0
Release: 3.1
Summary: A system exploration and troubleshooting tool
Group: File tools
License: GPLv2
URL: https://github.com/draios/sysdig
Source0: https://github.com/draios/sysdig/archive/%version.tar.gz#/%name-%version.tar.gz
BuildRequires: cmake gcc-c++ jsoncpp-devel libdb4-devel ncurses-devel zlib-devel compat-lua-devel
BuildRequires: jq-devel libb64-devel openssl-devel curl-devel

%description
An open source system-level exploration and troubleshooting tool.

%prep
%setup -q
sed -i "s|add_subdirectory(driver)||g" CMakeLists.txt
sed -i '/curlbuild.h/d' userspace/libsinsp/marathon_http.cpp userspace/libsinsp/mesos_http.cpp

%build
# hack for userspace/libscap/scap.c:34:40: fatal error: ../../driver/driver_config.h
cd driver
cmake . || :
cd -

mkdir build
cd build
%cmake .. -DUSE_BUNDLED_LUAJIT:BOOL=off \
       -DUSE_BUNDLED_JSONCPP:BOOL=off \
       -DUSE_BUNDLED_ZLIB:BOOL=off \
       -DUSE_BUNDLED_NCURSES:BOOL=off \
       -DUSE_BUNDLED_OPENSSL:BOOL=off \
       -DUSE_BUNDLED_CURL:BOOL=off \
       -DUSE_BUNDLED_B64:BOOL=off \
       -DUSE_BUNDLED_JQ:BOOL=off
make

%install
cd build
%make_install
rm -rf %buildroot/%_datadir/zsh/
rm -rf %buildroot/usr/etc/

%files
%_bindir/%name
%_bindir/c%name
%_bindir/sysdig-probe-loader
%_mandir/man8/*
%_datadir/%name

%changelog
* Thu Aug 10 2017 Wei-Lun Chao <bluebat@member.fsf.org> - 0.17.0
- Rebuilt for Fedora
* Thu Jan 05 2017 Vitaly Lipatov <lav@altlinux.ru> 0.13.0-alt1
- new version 0.13.0 (with rpmrb script)
* Mon Aug 01 2016 Vitaly Lipatov <lav@altlinux.ru> 0.11.0-alt1
- new version 0.11.0 (with rpmrb script)
* Thu Jul 28 2016 Vitaly Lipatov <lav@altlinux.ru> 0.8.0-alt1
- new version 0.8.0 (with rpmrb script)
* Fri Jul 17 2015 Vitaly Lipatov <lav@altlinux.ru> 0.1.101-alt1
- new version 0.1.101 (with rpmrb script)
* Thu Jun 04 2015 Anton V. Boyarshinov <boyarsh@altlinux.ru> 0.1.89-alt2
- rebuild with c++11 ABI
* Sun Sep 28 2014 Vitaly Lipatov <lav@altlinux.ru> 0.1.89-alt1
- initial build for ALT Linux Sisyphus
