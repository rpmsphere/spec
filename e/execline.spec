Name:		execline
Version:	2.8.0.0
Release:	1
Summary:	A light non-interactive scripting language
License:	BSD
Group:		Shells
URL:		http://www.skarnet.org/software/execline/
Source0:	http://www.skarnet.org/software/%{name}/%{name}-%{version}.tar.gz
BuildRequires:  skalibs-devel

%description
execline is a very light, non-interactive scripting language, which is 
similar to a shell. Simple shell scripts can be easily rewritten in the 
execline language, improving performance and memory usage. execline was 
designed for use in embedded systems, but works on most Unix flavors.

%package devel
Summary: Development files for %{name}
Requires: %{name}

%description devel
Header files and libraries for the package %{name}.

%prep
%setup -q

%build
%configure --with-sysdeps=%{_libdir}/skalibs/sysdeps
make

%install
rm -rf %{buildroot}
%make_install
rm %{buildroot}%{_bindir}/cd %{buildroot}%{_bindir}/umask
mv %{buildroot}%{_bindir}/wait %{buildroot}%{_bindir}/execline-wait

%clean
rm -rf %{buildroot}

%files
%doc NEWS AUTHORS README COPYING
%{_bindir}/*

%files devel
%{_includedir}/%{name}
%{_libdir}/lib%{name}.a

%changelog
* Sun Apr 4 2021 Wei-Lun Chao <bluebat@member.fsf.org> - 2.8.0.0
- Rebuilt for Fedora
* Thu Dec 09 2010 Oden Eriksson <oeriksson@mandriva.com> 1.08-4mdv2011.0
+ Revision: 618247
- the mass rebuild of 2010.0 packages
* Thu Sep 10 2009 Thierry Vignaud <tv@mandriva.org> 1.08-3mdv2010.0
+ Revision: 437503
- rebuild
* Wed Jan 28 2009 Oden Eriksson <oeriksson@mandriva.com> 1.08-2mdv2009.1
+ Revision: 335008
- build against glibc to make it work again
* Wed Jan 28 2009 Oden Eriksson <oeriksson@mandriva.com> 1.08-1mdv2009.1
+ Revision: 334960
- 1.08 (source from freebsd)
* Thu Aug 07 2008 Thierry Vignaud <tv@mandriva.org> 1.07-2mdv2009.0
+ Revision: 266738
- rebuild early 2009.0 package (before pixel changes)
* Wed May 07 2008 Vincent Danen <vdanen@mandriva.com> 1.07-1mdv2009.0
+ Revision: 202938
- import execline
