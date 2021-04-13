Summary: Real-Time Framework for Linux
Name: xenomai
Version: 3.1
Release: 1
Source0: https://xenomai.org/downloads/xenomai/stable/%{name}-%{version}.tar.bz2
License: GPL
Group: Networking/Other
URL: http://www.xenomai.org
Requires: %{name}-libs
BuildRequires: gcc-c++

%description
Xenomai is a real-time development framework cooperating with the Linux kernel, 
in order to provide a pervasive, interface-agnostic, hard real-time support to 
user-space applications, seamlessly integrated into the GNU/Linux environment.

Xenomai is based on an abstract RTOS core, usable for building any kind of real-time
interfaces, over a nucleus which exports a set of generic RTOS services. Any number 
of RTOS personalities called skins can then be built over the nucleus, providing
their own specific interface to the applications, by using the services of a single 
generic core to implement it. 

%package libs
Summary: Xenomai libraries
Group: Networking/Other

%description libs
Library files for xenomai

%package devel
Summary: Xenomai libraries - header files
Group: Development/C
Requires: %{name}-libs

%description devel
header files for xenomail Library files

%package static
Summary: Xenomai static libraries
Group: Development/C
Requires: %{name}-devel

%description static
Static xenomai Library files

%prep
%setup -q
sed -i 's|-Werror ||' configure*

%build
autoreconf -fisv
./configure --prefix=/usr/ --includedir=/usr/include/xenomai --libdir=%{_libdir}
make 

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT SUDO=false
#rm -f $RPM_BUILD_ROOT/%{_libdir}/posix.wrappers
#rm -f $RPM_BUILD_ROOT/%{_bindir}/xeno-info

%files
%{_bindir}/*
%{_sbindir}/*
#{_mandir}/man1/*.1*
#doc %_docdir/xenomai
/usr/demo/*
/usr/etc/*

%files libs
%{_libdir}/lib*.so*

%files devel
%{_includedir}/xenomai
#{_libdir}/pkgconfig/*.pc
%{_libdir}/cobalt.wrappers
%{_libdir}/dynlist.ld
%{_libdir}/modechk.wrappers
%{_libdir}/xenomai

%files static
%{_libdir}/lib*.a*
%exclude %{_libdir}/lib*.la

%changelog
* Sun Apr 11 2021 Wei-Lun Chao <bluebat@member.fsf.org> - 3.1
- Rebuild for Fedora
* Mon Apr 15 2013 Dmitry V. Levin (QA) <qa_ldv@altlinux.org> 2.4.8-alt1.qa1
- NMU: rebuilt for debuginfo.
* Tue Jun 02 2009 Michail Yakushin <silicium@altlinux.ru> 2.4.8-alt1
- 2.4.8 
* Mon May 18 2009 Michail Yakushin <silicium@altlinux.ru> 2.4.7-alt1
- intial build for ALT 
