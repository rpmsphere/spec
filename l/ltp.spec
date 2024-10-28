%undefine _debugsource_packages
%global __os_install_post %{nil}

Summary:        Linux Test Project
Name:           ltp
Version:        20240129
Release:        1
License:        GPLv2+
Group:          Development/Kernel
URL:            https://github.com/linux-test-project/ltp
Source0:        http://downloads.sourceforge.net/project/%{name}/LTP%20Source/%{name}-%{version}/%{name}-full-%{version}.tar.bz2
BuildRequires:  flex
BuildRequires:  rsync
Requires:       dialog
Patch0:         ltp-getcpu.patch

%description
The Linux Test Project is a joint project with SGI, IBM, OSDL, and Bull with a
goal to deliver test suites to the open source community that validate the 
reliability, robustness, and stability of Linux. The Linux Test Project is a 
collection of tools for testing the Linux kernel and related features. Our goal
is to improve the Linux kernel by bring test automation to the kernel testing 
effort. Interested open source contributors are encouraged to join the project.

%prep
%setup -q -n %{name}-full-%{version}
#sed -i 's| O_LARGEFILE| __O_LARGEFILE|' testcases/kernel/io/writetest/writetest.c
#sed -i -e 's| PACKAGE|"%{name}"|' -e 's| VERSION|"%{version}"|' tools/genload/stress.c tools/genload/genload.c
#sed -i 's|uintptr_t|intptr_t|' testcases/kernel/security/dirtyc0w/dirtyc0w_child.c
#sed -i 's|ustat||' testcases/kernel/syscalls/Makefile
#rm -rf testcases/kernel/syscalls/ustat
#sed -i '47i #include <sys/sysmacros.h>' include/old/test.h
#sed -i '54,58d' testcases/network/multicast/mc_gethost/mc_gethost.c
#patch0 -p 1
cp utils/sctp/func_tests/test_1_to_1_connect.c utils/sctp/func_tests/test_1_to_1_connectx.c
cp utils/sctp/func_tests/test_connect.c utils/sctp/func_tests/test_connectx.c
sed -i -e 's|pthread_mutex_t wait|pthread_mutex_t mywait|' -e 's|\&wait|\&mywait|' testcases/kernel/sched/nptl/nptl01.c

%build
make autotools
%configure
export CFLAGS="-fPIE -fPIC -D__USE_GNU -Wno-format-security -lpthread -Iinclude -I../include -I../../include -I../realtime/include -I/usr/include/tirpc -ltirpc"
sed -i 's|-Werror=format-security|-Wno-format-security|' `find . -name config.mk`
make

%install
%make_install
mkdir -p %{buildroot}%{_libdir}/%{name}/
mv %{buildroot}%{_prefix}/{runtest,testcases,testscripts,scenario_groups,Version} %{buildroot}%{_libdir}/%{name}/
mv %{buildroot}%{_prefix}/{IDcheck.sh,runltp,ver_linux} %{buildroot}%{_bindir}/
find %{buildroot} -type f -perm 775 -exec chmod 755 \{\} \;

sed -i 's|/usr/bin/python$|/usr/bin/python2|' %{buildroot}%{_libdir}/ltp/testcases/bin/*.py %{buildroot}%{_libdir}/ltp/testcases/data/file01/in.py
#sed -i 's|/usr/bin/env python$|/usr/bin/python2|' %{buildroot}%{_bindir}/execltp

%files
%{_libdir}/%{name}
%{_mandir}/man1/*
%{_mandir}/man3/*
%{_bindir}/*
/usr/kirk
/usr/libkirk
/usr/ltx
/usr/metadata/*
/usr/runltp-ng

%changelog
* Sun Apr 07 2024 Wei-Lun Chao <bluebat@member.fsf.org> - 20240129
- Rebuilt for Fedora
* Thu Aug 14 2014 Andrey Bondrov <andrey.bondrov@rosalab.ru> 0.20120903-4
+ Revision: ef5e311
- Spec cleanup, build with tirpc
