Name:           cint
Version:        5.18.00
Release:        21.1
License:        MIT
Summary:        Stand-alone C/C++ Interpreter
URL:            http://root.cern.ch/drupal/content/cint
Group:          Development/Languages/C and C++
Source:         http://root.cern.ch/drupal/sites/default/files/%{name}-%{version}.tgz
BuildRequires:  gcc-c++
BuildRequires:  readline-devel

%description
CINT is a C/C++ interpreter which is aimed at processing C/C++ scripts. Scripts
are programs which perform specific tasks. Generally execution time is not
critical, but rapid development is. Using an interpreter the compile and link
cycle is dramatically reduced facilitating rapid development. CINT makes C/C++
programming enjoyable even for part-time programmers.

%prep
%setup -q
sed -i '1052s|operator void\*|operator bool|' cint/src/dict/gcc4strm.cxx

%build
# This is a custom configure script
./configure --prefix=%{_prefix} \
            --libdir=%{_libdir} \
            --readlinelib=%{_libdir}/libreadline.so
#ifarch %{arm} x86_64
export RPM_OPT_FLAGS="${RPM_OPT_FLAGS} -fPIC -fpermissive -Wno-narrowing"
#endif
echo "G__CFG_CFLAGS := ${RPM_OPT_FLAGS}" >> Makefile.conf
echo "G__CFG_CXXFLAGS := ${RPM_OPT_FLAGS} -DG__GNUREADLINE" >> Makefile.conf
make %{_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
install -D -m 0755 bin/cint $RPM_BUILD_ROOT%{_bindir}/cint
install -D -m 0755 lib/libCint.so $RPM_BUILD_ROOT%{_libdir}/libCint.so
install -D -m 0644 doc/man1/cint.1 $RPM_BUILD_ROOT%{_mandir}/man1/cint.1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%{_bindir}/cint
%{_libdir}/libCint*
%{_mandir}/man1/cint.1.*
%doc COPYING README.txt RELNOTE.txt

%changelog
* Thu Aug 16 2012 Wei-Lun Chao <bluebat@member.fsf.org> - 5.18.00
- Rebuild for Fedora
* Thu Jun 28 2012 dvaleev@suse.com
- disable ppc64
  see: https://savannah.cern.ch/bugs/index.php?70542
* Sun Oct 16 2011 mhrusecky@suse.cz
- supporting $RPM_OPT_FLAGS
- compiling with -fPIC on ARM and x86_64 (fixed build)
* Sat Sep 17 2011 jengelh@medozas.de
- Remove redundant tags/sections from specfile
* Mon May  9 2011 idoenmez@novell.com
- Initial release
