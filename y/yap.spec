%global __os_install_post %{nil}

Name:           yap
Version:        6.3.3
Release:        15.1
Summary:        High-performance Prolog Compiler
Group:          Development/Languages
License:        Artistic 2.0 or LGPLv2+
Source:         https://www.dcc.fc.up.pt/~vsc/Yap/yap-%{version}.tar.gz
URL:            https://www.dcc.fc.up.pt/~vsc/Yap
BuildRequires:  readline-devel, gmp-devel, texinfo

%description
A high-performance Prolog compiler developed at LIACC, Universidade do
Porto. The Prolog engine is based in the WAM (Warren Abstract
Machine), with several optimizations for better performance. YAP
follows the Edinburgh tradition, and is largely compatible with the
ISO-Prolog standard and with Quintus and SICStus Prolog.

%package devel
Summary:        C-Interface development files for Yap
Group:          Development/Languages
Requires:       %{name} = %{version}-%{release}

%description devel
C-Interface development files for Yap.

%package docs
Summary:        Documentation for Yap
Group:          Development/Languages
Requires:       %{name} = %{version}-%{release}

%description docs
Documentation for Yap.

%prep
%setup -q
sed -i 's|$(DESTDIR)$(LIBDIR)|$(DESTDIR)$(YAPLIBDIR)|' Makefile.in
sed -i -e 's|CONTEXT_PC NULL|CONTEXT_PC(scv) NULL|' -e 's|CONTEXT_BP NULL|CONTEXT_BP(scv) NULL|' C/gprof.c

# remove redundant rpath
#sed -i '/-Wl,-R/d' configure
# add soname to library
#sed -i 's/@YAPLIB@/@YAPLIB@.%{version}/g' Makefile.in
#sed -i 's/@DYNYAPLIB@/@DYNYAPLIB@.%{version}/g' Makefile.in
#sed -i 's/@DYNLIB_LD@/@DYNLIB_LD@ -Wl,-soname=@YAPLIB@.%{version} /g' Makefile.in

#find -name Makefile.in | xargs sed -i 's|$(ROOTDIR)/lib|$(ROOTDIR)/%{_lib}|'
#find -name Makefile.in | xargs sed -i 's|$(EROOTDIR)/lib|$(EROOTDIR)/%{_lib}|'

%build
# % define optflags $(echo $RPM_OPT_FLAGS | sed 's|-fstack-protector||')
export LDFLAGS=-Wl,--allow-multiple-definition
%configure \
        --enable-coroutining \
        --enable-max-performance \
        --enable-depth-limit \
        --enable-dynamic-loading

sed -i 's|-Wall|-fpermissive|' packages/CLPBN/horus/Makefile packages/swi-minisat2/C/Makefile
make %{?_smp_mflags}
#(cd docs; make info)

%install
rm -rf $RPM_BUILD_ROOT
%make_install
#mkdir -p $RPM_BUILD_ROOT%{_infodir}
#cp -f docs/yap.info* $RPM_BUILD_ROOT%{_infodir}
#cp -f LGPL/pillow/doc/pillow_doc.info $RPM_BUILD_ROOT%{_infodir}

# fix permissions and flags
#chmod 0644 $RPM_BUILD_ROOT%{_datadir}/Yap/pl/*
#chmod 0644 $RPM_BUILD_ROOT%{_includedir}/Yap/*
#find -name '*.lgt' -exec chmod 0644 '{}' ';'
#find -name '*.h' -exec chmod 0644 '{}' ';'
#find -name '*.c' -exec chmod 0644 '{}' ';'

#(cd $RPM_BUILD_ROOT%{_libdir}; ln -sf libYap.so.%{version} libYap.so)

# move examples to docdir
#mkdir -p $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}
#mv $RPM_BUILD_ROOT%{_datadir}/Yap/examples $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}
#rm -rf $RPM_BUILD_ROOT%{_datadir}/Yap/clpbn/examples

%files
%{_docdir}/Yap
%{_bindir}/*
%{_datadir}/Yap
%{_libdir}/Yap
#{_libdir}/libYap.so*
#{_infodir}/*

%files devel
#{_libdir}/libYap.so
%{_includedir}/Yap

#files docs
#doc LGPL/pillow/doc/pillow_doc_html/*
#doc LGPL/pillow/doc/article.ps.gz
#doc --parent Logtalk/manuals
#doc --parent Logtalk/examples

%changelog
* Tue Oct 30 2018 Wei-Lun Chao <bluebat@member.fsf.org> - 6.3.3
- Rebuilt for Fedora
* Mon Nov 30 2009 Dennis Gregorovic <dgregor@redhat.com> - 5.1.3-2.1
- Rebuilt for RHEL 6
* Mon Jul 27 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 5.1.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild
* Mon Jun 15 2009 Gerard Milmeister <gemi@bluewin.ch> - 5.1.3-1
- new release 5.1.3
* Sun Mar 01 2009 Ralf Corsépius <corsepiu@fedoraproject.org> - 5.1.1-13
- Add Yap-5.1.1-config.sub.patch: 
  Upgrade outdated config.sub to fix rebuild breakdown on ppc64.
* Fri Jul 11 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 5.1.1-11
- fix license tag
* Thu Apr 10 2008 Gerard Milmeister <gemi@bluewin.ch> - 5.1.1-10
- enable rpm_opt_flags
- patch for incorrect open call with O_CREAT
* Mon Feb 18 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 5.1.1-9
- Autorebuild for GCC 4.3
* Sat Oct 20 2007 Gerard Milmeister <gemi@bluewin.ch> - 5.1.1-8
- fix library path for 64-bit platforms
* Wed Aug 29 2007 Gerard Milmeister <gemi@bluewin.ch> - 5.1.1-7
- replaced ld -shared with gcc -shared
* Wed Aug 29 2007 Fedora Release Engineering <rel-eng at fedoraproject dot org> - 5.1.1-6
- Rebuild for selinux ppc32 issue.
* Thu Jul  5 2007 Gerard Milmeister <gemi@bluewin.ch> - 5.1.1-5
- also build libYap.so
* Fri May 11 2007 Gerard Milmeister <gemi@bluewin.ch> - 5.1.1-3
- remove -fstack-protector from optflags in order to enable
  loading of .so modules
* Mon Aug 28 2006 Gerard Milmeister <gemi@bluewin.ch> - 5.1.1-2
- Rebuild for FE6
* Mon May  1 2006 Gerard Milmeister <gemi@bluewin.ch> - 5.1.1-1
- new version 5.1.1
- split off devel and docs packages
* Fri Feb 17 2006 Gerard Milmeister <gemi@bluewin.ch> - 5.0.1-2
- Rebuilt for Fedora Extras 5
* Tue Oct 25 2005 Gerard Milmeister <gemi@bluewin.ch> - 5.0.1-1
- New Version 5.0.1
* Wed Sep  7 2005 Gerard Milmeister <gemi@bluewin.ch> - 5.0.0-1
- New Version 5.0.0
* Sat Jun 18 2005 Gerard Milmeister <gemi@bluewin.ch> - 4.5.5-5
- Use %%{_prefix}/lib for x86_64
* Sat Jun 18 2005 Gerard Milmeister <gemi@bluewin.ch> - 4.5.5-4
- Fix for non-i386 compilers
* Sat Jun 18 2005 Gerard Milmeister <gemi@bluewin.ch> - 4.5.5-3
- Compiler fix for FC4
* Fri Apr  7 2005 Michael Schwendt <mschwendt[AT]users.sf.net>
- rebuilt
* Sat Feb 12 2005 Gerard Milmeister <gemi@bluewin.ch> - 0:4.5.5-1
- New Version 4.5.5
* Mon Nov 29 2004 Gerard Milmeister <gemi@bluewin.ch> - 0:4.5.3-0.fdr.1
- New Version 4.5.3
* Sat Mar 13 2004 Gerard Milmeister <gemi@bluewin.ch> - 0:4.5.2-0.fdr.1
- New Version 4.5.2
* Sat Nov 22 2003 Gerard Milmeister <gemi@bluewin.ch> - 0:4.4.3-0.fdr.1
- First Fedora release
