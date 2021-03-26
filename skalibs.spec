%global debug_package %{nil}

Name:		skalibs
Version:	2.6.3.1
Release:	3.1
Summary:	The skarnet.org development library
License:	BSD
Group:		Development/Other
URL:		http://www.skarnet.org/software/skalibs/
Source0:	http://www.skarnet.org/software/%{name}/%{name}-%{version}.tar.gz

%description
skalibs is a package centralizing the public-domain C
development files used for building other skarnet.org software.

%package devel
Group:          Development/C
Summary:        Development files for skalibs
Requires:       %{name}

%description devel
skalibs is a package centralizing the public-domain C
development files used for building other skarnet.org software.

skalibs can also be used as a sound basic start for C
development.  There are a lot of general-purpose libraries out
there; but if your main goal is to produce small and secure C
code, you will like skalibs.

skalibs contains exclusively public-domain code.  So you can
redistribute it as you want, and it does not prevent you from
distributing any of your executables.

%prep
%setup -q

%build
%configure
make

%install
rm -rf %{buildroot}
%make_install INSTALL=./tools/install.sh
%ifarch x86_64 aarch64
mv %{buildroot}/usr/lib/* %{buildroot}/usr/lib64/
%endif

%clean
rm -rf %{buildroot}

%files
%doc NEWS AUTHORS README COPYING
%{_libdir}/libskarnet.so.*

%files devel
%{_includedir}/%{name}
%{_libdir}/%{name}
%{_libdir}/libskarnet.a
%{_libdir}/libskarnet.so

%changelog
* Tue Mar 06 2018 Wei-Lun Chao <bluebat@member.fsf.org> - 2.6.3.1
- Rebuild for Fedora
* Sun Sep 20 2009 Thierry Vignaud <tvignaud@mandriva.com> 0.47-2mdv2010.0
+ Revision: 445130
- rebuild
* Sun Oct 26 2008 Funda Wang <fundawang@mandriva.org> 0.47-1mdv2009.1
+ Revision: 297428
- New version 0.47
* Fri Aug 08 2008 Thierry Vignaud <tvignaud@mandriva.com> 0.46-2mdv2009.0
+ Revision: 269251
- rebuild early 2009.0 package (before pixel changes)
* Wed May 07 2008 Vincent Danen <vdanen@mandriva.com> 0.46-1mdv2009.0
+ Revision: 202905
- import skalibs
