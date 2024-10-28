Name:           fakeroot-ng
Version:        0.18
Release:        24.1
Summary:        Fooling a program into thinking it is running as root
License:        GPL-2.0+
Group:          Development/Other
URL:            https://sourceforge.net/projects/fakerootng
Source:         https://downloads.sourceforge.net/fakerootng/%{name}-%{version}.tar.gz
BuildRequires:  gcc-c++

%description
Fakeroot-ng uses the debug interface (PTRACE) to fool programs into thinking
they are running with root permission.

%prep
%setup -q
#sed -i '1i #include <unistd.h>' parent.cpp
#sed -i -e 's|"PID_F|" PID_F|g' -e 's|PID_F"|PID_F "|g' parent.cpp process.cpp file.cpp ptrace.cpp
#sed -i -e 's|"DEV_F|" DEV_F|g' -e 's|DEV_F"|DEV_F "|g' -e 's|"INODE_F|" INODE_F|g' -e 's|INODE_F"|INODE_F "|g' file.cpp file_lie.cpp
#sed -i -e 's|"UID_F|" UID_F|g' -e 's|UID_F"|UID_F "|g' -e 's|"GID_F|" GID_F|g' -e 's|GID_F"|GID_F "|g' -e 's|sysconf(_SC_PAGESIZE)|4096|' file.cpp
sed -i '/linux\/ptrace\.h/d' arch/linux/os.c
sed -i '4i #include <sys/types.h>' arch/linux/i386/platform_specific.h
%ifarch aarch64
cp -f /usr/lib/rpm/redhat/config.* .
%endif
sed -i '26i #include <sched.h>' process.cpp

%build
./configure --prefix=/usr
make %{?_smp_mflags} CPPFLAGS="%{optflags}"

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT

%files
%doc AUTHORS
%{_bindir}/*
%{_mandir}/man1/*

%changelog
* Fri Jan 03 2014 Wei-Lun Chao <bluebat@member.fsf.org> - 0.18
- Rebuilt for Fedora
