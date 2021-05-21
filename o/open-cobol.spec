%define cobvers 1.1

Name:           open-cobol
Version:        1.1
Release:        5.1
Summary:        OpenCOBOL - COBOL compiler
Group:          Development/Languages
License:        GPLv2+ and LGPLv2+
URL:            http://www.opencobol.org
Source:         http://downloads.sourceforge.net/%{name}/%{name}-%{version}.tar.gz
BuildRequires:  gmp-devel >= 4.1.4
BuildRequires:  readline-devel
BuildRequires:  libdb-devel
BuildRequires:  libtool-ltdl-devel
Requires:       gcc
Requires:       glibc-devel
Requires:       libcob = %{version}
Obsoletes:      libcob-devel < 1.0.90

%description
OpenCOBOL is an open-source COBOL compiler, which translates COBOL
programs to C code and compiles it using GCC.

%package -n libcob
Summary:        OpenCOBOL runtime library
Group:          Development/Libraries
Requires(post): /sbin/ldconfig
Requires(postun):       /sbin/ldconfig

%description -n libcob
%{summary}.
Runtime libraries for OpenCOBOL

%prep
%setup -q -n %{name}-%{cobvers}
sed -i '1078,1084s|const int attr|cob_field *scroll, const int attr|' libcob/screenio.c

%build
export CFLAGS="$RPM_OPT_FLAGS -fPIC -Wno-format-security -O"
export CPPFLAGS="$CFLAGS"
%configure --disable-rpath
sed -i 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' libtool
sed -i 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' libtool

make %{?_smp_mflags} 

%install
make install DESTDIR=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT/%{_libdir} -type f -name "*.*a" -exec rm -f {} ';'
rm -rf $RPM_BUILD_ROOT/%{_infodir}/dir

%find_lang %{name}

%files -f %{name}.lang
%doc AUTHORS COPYING ChangeLog
%doc NEWS README THANKS
%{_bindir}/cobc
%{_bindir}/cob-config
%{_bindir}/cobcrun
%{_datadir}/open-cobol
%{_infodir}/open-cobol.info*
%{_includedir}/*
%{_libdir}/libcob.so

%files -n libcob
%doc COPYING.LIB
%{_libdir}/libcob.so.*

%clean
rm -rf $RPM_BUILD_ROOT

%post 
/sbin/install-info %{_infodir}/open-cobol.info %{_infodir}/dir 2>/dev/null || :

%postun 
if [ $1 = 0 ]; then
  /sbin/install-info --delete %{_infodir}/open-cobol.info %{_infodir}/dir 2>/dev/null || :
fi

%post -n libcob -p /sbin/ldconfig

%postun -n libcob -p /sbin/ldconfig

%changelog
* Mon Feb 26 2018 Wei-Lun Chao <bluebat@member.fsf.org> - 1.1
- Rebuilt for Fedora
* Mon Jan 25 2016 Psychotic Build System <builder@psychotic.ninja> - 1.1-5
- Initial build for Psychotic Ninja
* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild
* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild
* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild
* Sat Aug 31 2013 Jochen Schmitt <Jochen herr-schmitt de> - 1.1-1
- Use source file from sourceforge.net
- Fix issue with FORTIFY_SOURCE
- Add libdb-devel as a BR
* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1-0.20090211.2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild
* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1-0.20090210.2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild
* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1-0.20090209.2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild
* Wed Oct 26 2011 Marcela Mašláňová <mmaslano@redhat.com> - 1.1-0.20090208.2
- rebuild with new gmp without compat lib
* Wed Oct 12 2011 Peter Schiffer <pschiffe@redhat.com> - 1.1-0.20090208.1
- rebuild with new gmp
* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1-0.20090208
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild
* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1-0.20090207
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild
* Mon Mar 23 2009 Jochen Schmitt <Jochen herr-schmitt de> 1.1-0.20090206
- Adapt version to naming guidelines
* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.95-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild
* Mon Dec  1 2008 Jochen Schmitt <Jochen herr-schmitt de> 1.0.95-3
- Obsoleting libcob-devel
* Tue Oct 21 2008 Jochen Schmitt <Jochen herr-schmitt de> 1.0.95-2
- Fix Changelog entry
- Rebuild
* Mon Oct 20 2008 Jochen Schmitt <Jochen herr-schmitt de> 1.0.95-1
- New upstream relase
- Fix FORTIFY_SOURCE issue (#464554)
* Mon Sep 15 2008 Jochen Schmitt <Jochen herr-schmitt de> 1.0.90-4
- Remove _FORTIFY_SOURCE as adviced by the upstream
* Thu Sep 11 2008 Jochen Schmitt <Jochen herr-schmitt de> 1.0.90-3
- Add -D__NO_STRING_INLINES for the i86 arch
* Sun Aug 17 2008 Jochen Schmitt <Jochen herr-schmitt de> 1.0.90-2
- Fix dependency open-cobol -> libcob
* Tue Aug 12 2008 Jochen Schmitt <Jochen herr-schmitt de> 1.0.90-1
- Prerelease of opben-cobol-1.1
* Tue Aug  5 2008 Jochen Schmitt <Jochen herr-schmitt de> 1.0-3
- Blocking Test #98 to failing
* Wed Jul 30 2008 Jochen Schmitt <Jochen herr-schmitt de> 1.0-2
- OpenCOBOL req. libcob-devel
- Fix URIs
- Fix tiwce groups
* Wed Jul 30 2008 Jochen Schmitt <Jochen herr-schmitt de> 1.0-1
- Initional Fedora RPM package

