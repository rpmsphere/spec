Summary: Z Window Manager
Name: zwin
Version: 0.8
Release: 2
License: LGPL
Group: System/Libraries
URL: http://people.debian.org.tw/~chihchun/debian/g11n/
Source: %{name}-%{version}.tar.gz
Vendor: Brian Lin <foxman@xlinux.com>
BuildRequires: vgl, g11n

%description
Z Window Manager is developed by Brian Lin <foxman@wahoo.com.tw>
as a toolkit for g11n windowing under console.

%prep
%setup -q
%{__sed} -i 's/ifdef 0/ifdef TESTING/' bulletin.c sidebar.c

%build
%{__make} RPM_OPT_FLAGS="$RPM_OPT_FLAGS"

%install
%{__rm} -rf %{buildroot}
%{__make} install ROOTDIR=%{buildroot}

%clean
%{__rm} -rf %{buildroot}

%files
%doc docs/*
%{_includedir}/keymap.h
%{_includedir}/zwin.h
%{_libdir}/libzwin.a
%{_libdir}/libzwin.so
%{_libdir}/libzwin.so.0
%{_libdir}/libzwin.so.0.8

%changelog
* Tue Mar 20 2018 Wei-Lun Chao <bluebat@member.fsf.org> - 
- Rebuild for Fedora
* Fri Jan 11 2008 Wei-Lun Chao <bluebat@member.fsf.org>
- Rebuild for M6(CentOS5).

* Thu Dec 23 1999 FongRong Kuo <fongrong@xinux.com>
- change Group

* Wed Dec 15 1999 Brian Lin <foxman@xlinux.com>
- create an automatic build script
