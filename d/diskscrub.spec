Name: diskscrub
Version: 1.9
Release: 3.1
Summary: Disk scrubbing program
License: GPL
Group: System Environment/Base
URL: https://sourceforge.net/projects/diskscrub/
Source0: scrub-%{version}.tar.bz2

%description
This utility writes patterns on files or disk devices to make
retrieving the data more difficult.  It operates in one of three modes: 
1) the special file corresponding to an entire disk is scrubbed 
   and all data on it is destroyed.
2) a regular file is scrubbed and only the data in the file 
   (and optionally its name in the directory entry) is destroyed.
3) a regular file is created, expanded until 
   the file system is full, then scrubbed as in 2).

%prep
%setup -q -n scrub-%{version}

%build
export CFLAGS="%{optflags}"
export CXXFLAGS="%{optflags}"
sed -i -e "s@CFLAGS=.*@CFLAGS=$CFLAGS -Wall -fPIC -DPIC@g" Makefile
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{_bindir}
mkdir -p $RPM_BUILD_ROOT%{_mandir}/man1
install -m 755 scrub $RPM_BUILD_ROOT/%{_bindir}
install -m 644 scrub.1 $RPM_BUILD_ROOT/%{_mandir}/man1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%doc ChangeLog NEWS DISCLAIMER COPYING
%{_bindir}/scrub
%{_mandir}/man*/*

%changelog
* Tue Aug 21 2012 Wei-Lun Chao <bluebat@member.fsf.org> - 1.9
- Rebuilt for Fedora
* Sun May  6 2007 judas_iscariote@shorewall.net
- First build
