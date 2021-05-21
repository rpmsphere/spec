%{!?python_sitelib: %define python_sitelib %(%{__python} -c "from distutils.sysconfig import get_python_lib; print get_python_lib()")}
%if 0%{?suse_version}
%{!?ruby_vendorarch: %define ruby_vendorarch %(ruby -rrbconfig -e 'puts Config::CONFIG["vendorarchdir"] ')}
%else
%{!?ruby_vendorarch: %define ruby_vendorarch %(ruby -rrbconfig -e 'puts Config::CONFIG["sitearchdir"] ')}
%endif

Name:           libzypp-bindings
Version:        0.5.8
Release:        1.2
License:        GPL v2 or later
Summary:        Bindings for libzypp
Group:          Development/Sources
BuildRequires:  cmake gcc-c++ python-devel ruby ruby-devel
BuildRequires:  swig >= 1.3.40
BuildRequires:  libzypp-devel >= 5.8.0
Source:         %{name}-%{version}.tar.gz
Patch1:         remove-perl-binding.patch
Patch2:         support-arm-architectures.patch

%description
This package provides bindings for libzypp, the library for package management.

%prep
%setup -q
%patch1 -p1
%patch2 -p1

%build
mkdir build
cd build
cmake -DCMAKE_INSTALL_PREFIX=%{prefix} \
      -DPYTHON_SITEDIR=%{python_sitelib} \
      -DRUBY_VENDORARCH_DIR=%{ruby_vendorarch} \
      -DLIB=%{_lib} \
      -DCMAKE_VERBOSE_MAKEFILE=TRUE \
      -DCMAKE_C_FLAGS_RELEASE:STRING="%{optflags}" \
      -DCMAKE_CXX_FLAGS_RELEASE:STRING="%{optflags}" \
      -DCMAKE_BUILD_TYPE=Release \
      -DCMAKE_SKIP_RPATH=1 \
      ..
make %{?jobs:-j %jobs}

%install
cd build
make install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf "$RPM_BUILD_ROOT"

%package -n ruby-zypp
Summary:        Ruby bindings for libzypp
Group:          Development/Languages/Ruby

%description -n ruby-zypp
Ruby bindings of libzypp

%files -n ruby-zypp
%defattr(-,root,root,-)
%{ruby_vendorarch}/zypp.so

%package -n python-zypp
Summary:        Python bindings for libzypp
Group:          Development/Languages/Python
%description -n python-zypp
Python bindings of libzypp

%files -n python-zypp
%defattr(-,root,root,-)
%{python_sitelib}/_zypp.so
%{python_sitelib}/zypp.py*

%changelog
* Tue Mar 20 2018 Wei-Lun Chao <bluebat@member.fsf.org> - 
- Rebuilt for Fedora
* Wed Apr 13 2011 Wei-Lun Chao <bluebat@member.fsf.org>
- Rebuild for OSSII
* Tue Jan  4 2011 Yi Yang <yi.y.yang@intel.com> - 0.5.8
- Support builtin arm architectures
* Fri Dec 17 2010 Yi Yang <yi.y.yang@intel.com> - 0.5.8
- Update to 0.5.8
* Thu Nov 25 2010 Yi Yang <yi.y.yang@intel.com> - 0.5.7
- Update to 0.5.7
* Thu Apr  8 2010 ma@suse.de
- Adapt to swig 1.3.40
- version 0.5.4
* Wed Mar 24 2010 ma@suse.de
- Work around swig not understanding nested class.
* Mon Dec  7 2009 ma@suse.de
- Pass python_sitelib macro from .spec file to cmake.
- version 0.5.3
* Tue Nov 24 2009 ma@suse.de
- Fix to build on sle11-sp1
* Tue Sep 22 2009 ma@suse.de
- Remove reference to dead zypp::ScanDBReport.
- version 0.5.2
* Sun Aug  9 2009 coolo@novell.com
- use new python macros
* Mon Aug  3 2009 ma@suse.de
- Adappt to boost-1.39
- version 0.5.1
* Tue Jul 14 2009 ma@suse.de
- Fix specfile data.
* Wed Jun  3 2009 ma@suse.de
- Bump factory version
- version 0.5.0
* Wed Dec 17 2008 ma@suse.de
- Compile with -fPIC
- revision 11945
* Tue Nov 11 2008 ma@suse.de
- Ignore Pathname operator<.
- revision 11649
* Mon Oct 13 2008 ma@suse.de
- Fix makefile to build.
- revision 11318
* Fri Sep 19 2008 ma@suse.de
- Add KeyRing::DefautAccept
* Tue Sep 16 2008 dmacvicar@suse.de
- add ZConfig
* Fri Sep  5 2008 ma@suse.de
- Fix basic resolvabe attributes as needed by list_resolvables.py
  example.
- revision 10952
* Thu Sep  4 2008 ma@suse.de
- Added lost RepoInfo and ServiceInfo.
- revision 10928
* Fri Aug  8 2008 ma@suse.de
- Remove ProductInfo. We don't replace Product.
- revision 10799
* Fri Aug  1 2008 ma@suse.de
- Remove obsolete TranslatedText
- Add ProductInfo which is going to replace Product
- revision 10716
* Thu Jul 31 2008 ma@suse.de
- Work around undefined symbols in libzypp. (bnc #391831)
- Adapt to zypp::Service being renamed to ServiceInfo
- revision 10707
- version 0.4.7
* Fri Jul 25 2008 ma@suse.de
- Removed almost all local copies of zypp header files. This also
  removed some old classes no longer present in libzypp.
- Re-enabled building of python and perl bindings. (bnc #391831)
- revision 10666
- version 0.4.6
* Mon Jul 14 2008 ma@suse.de
- Remove obsolete references to Script/Message/Atom.
- Remove obsolete references to Dependencies.
* Tue May  6 2008 coolo@suse.de
- compile ruby
* Fri Apr 25 2008 coolo@suse.de
- remove obsolete ResPool methods
* Fri Apr 11 2008 coolo@suse.de
- adapt to libzypp 4.10
* Thu Apr  3 2008 coolo@suse.de
- adapt to libzypp 4.7
* Wed Mar 19 2008 coolo@suse.de
- adapt to libzypp 4.5
* Mon Mar  3 2008 schubi@suse.de
- sat/repo moved to repository
- Revision 8981
- version 0.4.5
* Thu Feb 28 2008 coolo@suse.de
- fix build
* Thu Dec  6 2007 aschnell@suse.de
- readded cmp for ResObject
* Mon Dec  3 2007 ma@suse.de
- Add Pool iterator for python.
* Sat Oct 13 2007 aschnell@suse.de
- fixed build in beta
* Thu Oct  4 2007 aschnell@suse.de
- don't generate a debuginfo package (bug #297711)
* Mon Sep 17 2007 aschnell@suse.de
- generate Perl bindings
- use ZYpp Url class
* Mon Sep  3 2007 schwab@suse.de
- Fix broken compiler flags.
* Thu Aug 30 2007 aschnell@suse.de
- some work on python bindings
* Tue Aug 28 2007 aschnell@suse.de
- added KeyRing and PublicKey classes
* Thu Aug 23 2007 aschnell@suse.de
- added to_a functions
* Thu Aug 23 2007 aschnell@suse.de
- added some comparison functions
* Wed Aug 22 2007 aschnell@suse.de
- renamed ruby module to zypp
* Fri Aug 17 2007 aschnell@suse.de
- moved ruby files to vendor_ruby (bug #301127)
* Mon Aug 13 2007 aschnell@suse.de
- added exceptions
* Tue Jul 31 2007 aschnell@suse.de
- improved bindings for various classes
- adoptions to libzypp changes
* Tue Jul 24 2007 aschnell@suse.de
- added Python bindings
* Thu Jul 19 2007 aschnell@suse.de
- New package with swig generated bindings for libzypp
