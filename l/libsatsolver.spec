Name:           libsatsolver
Version:        0.16.1
Release:        2.3
License:        BSD 3-Clause
URL:            git://git.opensuse.org/projects/zypp/sat-solver.git
Source:         satsolver-%{version}.tar.gz
Source1:        %{name}-rpmlintrc
Group:          Development/Libraries/C and C++

BuildRequires:  doxygen
BuildRequires:  perl-devel db4-devel ruby ruby-rdoc

BuildRequires:  expat-devel

BuildRequires:  cmake rpm-devel gcc-c++ ruby-devel swig perl python-devel
BuildRequires:  zlib-devel
# the testsuite uses the check framework
BuildRequires:  check-devel
Summary:        A new approach to package dependency solving

%description
A new approach to package dependency solving

Authors:
--------
    Michael Schroeder <mls@suse.de>
    Klaus Kaempf <kkaempf@suse.de>
    Stephan Kulow <coolo@suse.de>
    Michael Matz <matz@suse.de>
    Duncan Mac-Vicar P. <dmacvicar@suse.de>

%package devel
Summary:        A new approach to package dependency solving
Group:          Development/Libraries/C and C++
Requires:       satsolver-tools = %version
Requires:       rpm-devel

#%package devel-doc
#Summary:        satsolver developer documentation
#Group:          Documentation/HTML

%description devel
Development files for satsolver, a new approach to package dependency solving

#%description devel-doc
#Developer documentation for satsolver, a new approach to package dependency solving


Authors:
--------
    Michael Schroeder <mls@suse.de>
    Klaus Kaempf <kkaempf@suse.de>
    Stephan Kulow <coolo@suse.de>
    Michael Matz <matz@suse.de>
    Duncan Mac-Vicar P. <dmacvicar@suse.de>

%package -n satsolver-tools
Summary:        A new approach to package dependency solving
Group:          Development/Libraries/C and C++
Obsoletes:      libsatsolver <= 0.0.15
Provides:       libsatsolver = %{version}-%{release}
Requires:       gzip bzip2 coreutils

%description -n satsolver-tools
A new approach to package dependency solving.

%package demo
Summary:        Applications demoing the satsolver library
Group:          System/Management
Requires:       curl
Requires:       gnupg2


%description demo
Applications demoing the satsolver library.

%package -n ruby-satsolver
Summary:        Ruby bindings for sat solver
Group:          Development/Languages/Ruby

%description -n ruby-satsolver
Ruby bindings for sat solver.

%package -n python-satsolver
Requires:       python redhat-rpm-config
Summary:        Python bindings for sat solver
Group:          Development/Languages/Python

%description -n python-satsolver
Python bindings for sat solver.

%package -n perl-satsolver
Requires:       perl = %{perl_version}
Summary:        Perl bindings for sat solver
Group:          Development/Languages/Perl

%description -n perl-satsolver
Perl bindings for sat solver.


%prep
%setup -q -n satsolver-%{version}
sed -i 's|rpm/db.h|db4/db.h|' ext/repo_rpmdb.c

%build
export CFLAGS="$RPM_OPT_FLAGS"
export CXXFLAGS="$CFLAGS"

CMAKE_FLAGS=
CMAKE_FLAGS="-DFEDORA=1"

cmake   $CMAKE_FLAGS \
	-DCMAKE_INSTALL_PREFIX=%{_prefix} \
	-DPYTHON_SITEDIR=%{py_sitedir} \
	-DLIB=%{_lib} \
	-DCMAKE_VERBOSE_MAKEFILE=TRUE \
	-DCMAKE_BUILD_TYPE=Release \
	-DCMAKE_SKIP_RPATH=1 
make %{?jobs:-j %jobs}
make doc_forced

%if 0%{?run_testsuite}
  ln -s . build
  ctest .
%endif

%install
make DESTDIR=$RPM_BUILD_ROOT install
# we want to leave the .a file untouched
export NO_BRP_STRIP_DEBUG=true
#pushd doc/autodoc
#make install
#popd

%clean
rm -rf "$RPM_BUILD_ROOT"

%files -n satsolver-tools
%doc LICENSE*
#%exclude /usr/bin/deptestomatic
%exclude /usr/bin/helix2solv
%exclude /usr/bin/solv
/usr/bin/*

%files devel
%_libdir/libsatsolver.a
%_libdir/libsatsolverext.a
%_libdir/libappsatsolver.a
%dir /usr/include/satsolver
/usr/include/satsolver/*
#/usr/bin/deptestomatic
/usr/bin/helix2solv

%files demo
/usr/bin/solv

#%files devel-doc
#%dir %_docdir/satsolver
#%_docdir/satsolver/*

%files -n ruby-satsolver
%defattr(-,root,root,-)
%dir %{ruby_sitelib}/satsolver
%{ruby_sitelib}/satsolver.rb
%{ruby_sitelib}/satsolver/*.rb
%{ruby_sitearch}/satsolver.so
%doc bindings/ruby/html

%files -n python-satsolver
%defattr(-,root,root,-)
#%doc swig/python/examples/*.py
%{py_sitedir}/_satsolver.so
%{py_sitedir}/satsolver.py*

%files -n perl-satsolver
%defattr(-,root,root,-)
%{perl_vendorarch}/satsolver.so
%{perl_vendorlib}/satsolver.pm

%changelog
* Tue Mar 20 2018 Wei-Lun Chao <bluebat@member.fsf.org> - 
- Rebuilt for Fedora
* Wed Apr 13 2011 Wei-Lun Chao <bluebat@member.fsf.org>
- Rebuild for OSSII
* Fri Oct 22 2010 ma@suse.de
- updateinfoxml: Correctly parse 'issued date' field.
- 0.16.1
* Thu Sep  9 2010 mls@suse.de
- bump version to 0.16 to make it different from code11_3 branch
- 0.16.0
* Mon Sep  6 2010 dmacvicar@novell.com
- ruby bindings: fix bugs regarding include path loading
  (was hardcoded) and refactor the way the library path is defined
  (only once in a helper)
* Mon Sep  6 2010 dmacvicar@novell.com
- SLE10SP3 also has vendor_ruby
* Wed Aug 18 2010 kkaempf@novell.com
- refactor ruby-satsolver, pure-Ruby extensions added
- 0.15.1
* Thu May  6 2010 mls@suse.de
- fix bug in cleandeps code
- bump version to 0.15 to make it different from code11_2 branch
- 0.15.0
* Tue Mar 23 2010 ma@suse.de
- Parse an installed products <shortsummary> tag [bnc#586303]
* Mon Mar 22 2010 mls@suse.de
- dataiterator: reset parent when jumping to a solvid [bnc#589640]
- 0.14.17
* Thu Mar 11 2010 ma@suse.de
- parse global repository ids. [bnc#377568]
- fix pattern parsing in repomd format. [bnc#585000]
- 0.14.16
* Thu Mar 11 2010 mls@suse.de
- fix language code lookup for fallback languages [bnc#584644]
- change solvable_lookup_str_lang interface a bit for libzypp
* Fri Feb 19 2010 mls@suse.de
- make dup rules work when system repo is not first [bnc#581276]
- parse pattern visibility flag in repomd format
- 0.14.15
* Fri Jan 29 2010 mls@suse.de
- speed up createwhatprovides when many solvables provide the same dep
- fix choice rule creation for real (bnc#551637)
- 0.14.14
* Mon Jan 18 2010 mls@suse.de
- set repository:toolversion to 1.0 in common_write
- 0.14.13
* Mon Dec 21 2009 mls@suse.de
- disable update rule in noobsoletes case if installed package is to
  be kept [bnc#564239]
- work around rpm bug when --prefix is used [bnc#565525]
- add support for sparc architecture [bnc#566291]
- 0.14.12
* Mon Dec  7 2009 ma@suse.de
- Support optionally compressed product(s).xml in rpmmd metadata.
- 0.14.11
* Mon Nov  2 2009 mls@suse.de
- look at infarch/dup rules when creating choice rules, makes dup
  also install 32bit packages [bnc#551637]
- 0.14.10
* Wed Oct 14 2009 mls@suse.de
- ignore products element so that repo2solv works
- support MULTI_SEMANTICS
- add --withsrc option for installcheck
- add SOLVER_DROP_ORPHANED job type
- fix dropped package handling in removedisabledconflicts
- 0.14.9
* Thu Sep 24 2009 mls@suse.de
- fix bug in solvable_lookup_str_base
* Wed Sep 23 2009 mls@suse.de
- get missing translations from other solvables [bnc#386449]
- also look at triggers when ordering packages
- add support for REPOKEY_TYPE_BINARY
- 0.14.8
* Wed Sep 16 2009 mls@suse.de
- use repomdxml to query for the location [bnc#501425]
- fix assertion failue... again
- fix fp leak [bnc#535468]
- 0.14.7
* Fri Sep  4 2009 mls@suse.de
- fix multiversion handling for real
- fix speed regression in repo_susetags
- close fd leak [bnc#527506]
- remove db.h workaround
- 0.14.6
* Mon Aug 31 2009 mls@suse.de
- fix to build with rpm-4.7
* Fri Aug 28 2009 ma@suse.de
- add support for SOLVER_SOLVABLE_REPO
- 0.14.5
* Thu Jul 30 2009 mls@suse.de
- speed up file list parsing
- speed up addfileprovides
- fix bugs in pubkey handling
- fix bug in filelist handling when there are no abs paths
- 0.14.4
* Fri Jul 17 2009 mls@suse.de
- add satversion.h header file
- many changes regarding the load callback
- more dataiterator control functions
- add transaction ordering code
- add support for file conflict checking
- 0.14.3
* Mon Jun 22 2009 mls@suse.de
- create libsatsolverext.a
- 0.14.2
* Wed May  6 2009 ma@suse.de
- Fix to support sha256 hashes (bnc#501425)
* Wed Apr  1 2009 kkaempf@suse.de
- 0.14.1
  Core changes
  - fix potential NULL deref in srcrpm handling (mls)
  - clean up and fix suggested/recommended list creation code (mls)
  - kill obsolete and broken patchxml support (mls)
  - replace old solver_problemruleinfo with new solver_ruleinfo
    function (mls)
  - add solvable_selfprovidedep() function (mls)
  - add noinfarchcheck solver option (mls)
  - clone job queue to make the code more flexible (mls)
  - rewrite policy rule disabling/re-enabling (bnc#481836) (mls)
  - fix out-of-bounds in solver_printproblem() (mls)
  Bindings changes
  - provide 'Repo.attr(String)' accessor function (kkaempf)
  - provide 'Solver.sizechange' to compute the changes of the
    installed size after a transaction is applied (kkaempf)
  - solver result iterators for Python (jblunck)
  - add %%%%newobject to track newly created objects better (kkaempf)
  - generate rdoc documentation from swig input files (kkaempf)
  - add a no-op Pool destructor (bnc#483252) (kkaempf)
  - provide access to all flags and settings (kkaempf)
* Wed Mar  4 2009 mls@suse.de
- fix problem_to_solutions segfault
- bump version to 0.14 to make it different from code11 branch
- 0.14.0
* Mon Mar  2 2009 mls@suse.de
- add solver_trivial_installable() to fix multiversion patches [bnc#480303]
- 0.13.5
* Wed Feb 18 2009 ma@suse.de
- Use correct namespace (e.g. pattern:) even if solvable has no name [bnc#470011]
* Fri Jan 30 2009 mls@suse.de
- fix weakmap boundary check
- 0.13.3
* Tue Jan 27 2009 ma@suse.de
- Ignore trailing whitespace in content file parser.
* Mon Jan 26 2009 mls@suse.de
- fix segfault caused by whatprovides reallocation [bnc#468313]
- 0.13.1
* Tue Jan 20 2009 ma@suse.de
- repo_rpmdb: Fix conversion to UTF8
* Fri Dec  5 2008 kkaempf@suse.de
- enhance bindings to provide reasons for solver decisions
* Mon Dec  1 2008 mls@suse.de
- prefer patterns again until there's a real fix [bnc#450226]
* Mon Dec  1 2008 mls@suse.de
- susetags: fix file dependency parsing [bnc#450286]
* Fri Nov 28 2008 mls@suse.de
- correct problem solving algorithm
- 0.13.0
* Fri Nov 21 2008 dmacvicar@suse.de
- remove unused updaterepokey, replaced by repo
  product information
* Thu Nov 20 2008 dmacvicar@suse.de
- support content, distro and updates tag properly
- remove the unused products tag
* Mon Nov 17 2008 ma@suse.de
- Parse RELEASE tag from contentfile (bnc #444978)
- 0.12.3
* Fri Nov 14 2008 mls@suse.de
- fix bugs in multiversion handling
- bring perl bindings up to speed
- 0.12.2
* Fri Nov  7 2008 ma@suse.de
- fix SOLVID_POS dataiterator handling
* Fri Nov  7 2008 kkaempf@suse.de
- make repo_zyppdb more robust (bnc#441043)
* Thu Nov  6 2008 kkaempf@suse.de
- Add 'user_data' argument to all applayer iterator callbacks
  (bnc#418491)
* Wed Oct 29 2008 ma@suse.de
- Add 'sh4' architectures.
* Tue Oct 28 2008 ma@suse.de
- Add 'arm' architectures.
* Mon Oct 27 2008 kkaempf@suse.de
- Improve error detection and reporting when parsing 'content' file
* Fri Oct 24 2008 ma@suse.de
- Remember the /etc/products.d enties filename in .solv
  (bnc #432932)
- 0.12.1
* Thu Oct 23 2008 mrueckert@suse.de
- add zlib-devel as buildrequires, cmake is looking for it
  explicitely. rpm-devel used to require it but you dont really
  need it to link against librpm*
- requires rpm-devel in the devel package, it is required to link
  against libsatsolver.
* Wed Oct 22 2008 mls@suse.de
- add pool_set_installed()
- drop "installed" arguments from some functions
- 0.12.0
* Wed Oct 22 2008 dmacvicar@suse.de
- support the new standarized tags available in
  createrepo > 0.9.6
  saving of the distro tag still missing.
* Thu Oct 16 2008 mls@suse.de
- make iterator work with completely empty repos [bnc#435838]
* Tue Oct 14 2008 mls@suse.de
- the big solv data change
  * incompatible new file format
  * repodata handles are solvable ids
  * no more extra handles
  * no need to call repodata_extend anymore
- work around solver dup repo priority bug, real fix follows soon
- implement releasever
- repo_products.c is now more robust
* Mon Oct 13 2008 kkaempf@suse.de
- make product parsing more robust (bnc#433362)
* Thu Oct  2 2008 ma@suse.de
- Product arttributes: removed FLAVOR and REFERENCES, added PRODUCTLINE.
- revision 11233
- 0.11.0
* Tue Sep 30 2008 ma@suse.de
- repo_content.c: fix broken dependency parsing.
- revision 11214
* Mon Sep 29 2008 ma@suse.de
- rpms2solv failed to write out most solvable data (bnc #422338).
- revision 11201
* Fri Sep 26 2008 kkaempf@suse.de
- new fallback strategy for installed products in rpmdb2solv
  try /etc/products.d (code11 style) first
  if this fails, try /var/lib/zypp/db/products/*
  if this fails, fallback to /etc/*-release
  (bnc#429177)
- 0.10.16
* Thu Sep 25 2008 kkaempf@suse.de
- fully support Dataiterator in Python and Ruby bindings.
- 0.10.15
* Thu Sep 25 2008 dmacvicar@suse.de
- add support for keywords in susedata
* Wed Sep 24 2008 kkaempf@suse.de
- parse /etc/<xyz>-release if no /etc/products.d present
  (bnc#429177)
- 0.10.14
* Mon Sep 22 2008 dmacvicar@suse.de
- ability to parse suseinfo.xml for extended repomd.xml attributes
- fix susedata.xml parsing
- add CPE attribute to installed product
- real fix for segfault in multiarch parsing (bnc#427271)
- 0.10.13
* Thu Sep 18 2008 dmacvicar@suse.de
- fix segfault in multiarch parsing (bnc#427271)
* Wed Sep 17 2008 mls@suse.de
- fix segfault in provides iterator
- 0.10.12
* Fri Sep 12 2008 dmacvicar@suse.de
- support for susedata.xml
* Fri Sep 12 2008 dmacvicar@suse.de
- add repo_add_poolstr_array
- move updates="key,key.." to repomd.xml
- make product url ids more extensible
- 0.10.11
* Thu Sep 11 2008 dmacvicar@suse.de
- add REPOSITORY_UPDATES to match product -> repos
- make updateinfo.xml support id attribute in collection that
  leads to insert that the repository updates that id.
* Wed Sep 10 2008 dmacvicar@suse.de
- create one product per BASEARCHS
* Wed Sep 10 2008 ma@suse.de
- repo_products: Parse schemeversion, propagate product
  updaterepokey and flavor. Fix segfault on malformed
  xml.
- 0.10.10
* Wed Sep 10 2008 dmacvicar@suse.de
- accept the PATTERNS tag in content file
* Tue Sep  9 2008 kkaempf@suse.de
- rpmdb2solv changes:
  - fix bug when parsing multiple products
  - adapt to .prod file as of 9/9/08 7:20pm
- 0.10.9
* Tue Sep  9 2008 ma@suse.de
- Reenable -Werror and fix bindings.
- 0.10.8
* Tue Sep  9 2008 dmacvicar@suse.de
- disable -Werror for swig generated stuff
* Fri Sep  5 2008 kkaempf@suse.de
- adapt /etc/product.d parser to generated .prod files.
* Fri Sep  5 2008 ma@suse.de
- tools/repo_susetags.c: Parse packages vendor (bnc #422493).
- 0.10.7
* Thu Sep  4 2008 kkaempf@suse.de
- tools/rpmdb2solv: Adapt to xml-based /etc/products.d
- tools/rpmdb2solv: Add '-a <attribute>' to print
  distribution.target attribute of baseproduct.
* Tue Sep  2 2008 mls@suse.de
- make solver includes use "" instead of <>, fixes bnc#415920
- implement otherproviders()
- make patches do nevr matching
- make patch conflicts work with multiversion
- new job commands, now combinded from job type and select type
- support for distupgrade mode
- make SOLVER_ERASE_SOLVABLE work
- also check obsoletes when disabling update rules
- 0.10.6
* Fri Aug 22 2008 dmacvicar@suse.de
- add support for extensible metadata over primary +
  diskusage
- 0.10.5
* Fri Aug 15 2008 kkaempf@suse.de
- ensure existance of product solvable in repo_content(bnc#417594)
* Fri Aug 15 2008 kkaempf@suse.de
- follow /etc/products.d/baseproduct and mark product as 'base'
* Fri Aug 15 2008 kkaempf@suse.de
- Implement pre-code11 fallback for products, parse /etc/*-release
  if /etc/products.d is not available.
* Wed Aug 13 2008 kkaempf@suse.de
- provide installtime for installed products.
* Wed Aug 13 2008 dmacvicar@suse.de
- include new file search capability commited by matz
  (SEARCH_FILES)
- 0.10.4
* Wed Aug 13 2008 kkaempf@suse.de
- Honor rpmdb2solv's '-r <root>' also for the products.d path.
* Tue Aug 12 2008 kkaempf@suse.de
- Add .prod parsing for 'installed' products to rpmdb2solv.
- Improve python-bindings, add iterators.
* Thu Aug  7 2008 dmacvicar@suse.de
- implement relogin suggested support (fate#304889)
* Thu Aug  7 2008 ma@suse.de
- Susetags: Allow whitespace in file provides generated by
  autobuild (bnc#415115)
* Fri Aug  1 2008 dmacvicar@suse.de
- insert the checksum in rpmmd generated solv files
  (bnc#414002)
- 0.10.3
* Tue Jul 29 2008 mls@suse.de
- resolve job rules before installing system packages [bnc#411086]
- no more freshens. R.I.P.
- make repo2solv.sh also take repomd.xml in count
- install repomdxml2solv
- add Packager, Build Host, Distribution
- disallow arch/vendor changes even if the package name changes
* Sat Jul 12 2008 dmacvicar@suse.de
- infrastructure to save generated and expiration time
  stamp in rpm-md repositories (fate #301904)
- 0.10.1
* Wed Jul  9 2008 ma@suse.de
- Fix repo_content dependency parsing. Parser may lose up to
  two trailing dependencies.
* Tue Jul  1 2008 kkaempf@suse.de
- rename language bindings to {perl,python,ruby}-satsolver
  to follow naming conventions.
* Mon Jun 30 2008 dmacvicar@suse.de
- forward port
- add message tag to updateinfo.xml for displaying
  messages in the user interface
- Fix missing self provides for patches (bnc #397132).
- do not reorder binary rules if they are not rpm rules [bnc#397456]
- 0.10.0
* Mon Jun  2 2008 coolo@suse.de
- calculate recommendation list also if ignorealreadyrecommended is set,
  as some recommendations would be missing otherwise
- make dependency output less confusing (bnc#396309)
- 0.9.0
* Tue May 27 2008 coolo@suse.de
- compile with RPM_OPT_FLAGS
* Fri May 23 2008 mls@suse.de
- add "zypper" flag
- add "ignorealreadyrecommended" aka "zypper" solver option
* Thu May 22 2008 coolo@suse.de
- fixed language support in patterns (bnc#386524)
* Mon May 19 2008 dmacvicar@suse.de
- make solvable_look_bool more robust by allowing both
  the void or the num == 1 strategy.
* Thu May 15 2008 coolo@suse.de
- fix susetags parser
* Wed May 14 2008 dmacvicar@suse.de
- mls fix of satisfied patterns
- 0.0.33
* Tue May 13 2008 dmacvicar@suse.de
- use repodata_set_void for pattern visible attr
* Tue May 13 2008 jreidinger@suse.cz
- read description dir path from content file (bnc #389414)
* Tue May 13 2008 dmacvicar@suse.de
- a boolean is not a num attribute set to 1, but just a existing void
  attribute. (bnc#388818)
* Mon May 12 2008 coolo@suse.de
- provide libsatsolver to fix requires of debuginfo
* Sat May 10 2008 coolo@suse.de
- resubmit clean tar
* Fri May  9 2008 ma@suse.de
- Parse the products LABEL in content file to SUMMARY.
* Fri May  9 2008 dmacvicar@suse.de
- recognize 1 as true for reboot suggested and
  restart suggested (bnc#388818)
* Fri May  9 2008 kkaempf@suse.de
- move 'helix2solv' from satsolver-tools to satsolver-devel package
  (bnc#388595)
* Mon May  5 2008 coolo@suse.de
- add obsoleteusesprovides and implicitobsoleteusesprovides solver
  flags
- speed up solving by not recreating the watch chains every time
  some rule is enabled/disabled. To do this, the "disabled" flag
  had to be moved from w1 to d.
- fix bug that broke rule disabling when "forceResolve" was true
- fix bug in update rule calculation
- speed up solver a bit by creating a queue holding all assertion
  rules, so we do not have to scan all rules for assertions
- parse also DISTPRODUCT and DISTVERSION (for registration), and the other
  (often unused) attributes of products.
* Mon Apr 28 2008 coolo@suse.de
- (De-)Serialize structured types.  Dataiterator and repo_search support
  them too, but not yet nested, so that is unsupported for now.
- skipping kinds in matcher when a flag is specified.
- make --force behave a bit more like --noforce
* Fri Apr 25 2008 coolo@suse.de
- detect and skip empty lines (bnc#381828)
- fix endless loop
- move debug functions to solverdebug.c
- do not delete negative bitfield entries [bnc#381908]
- add "showinstalledrecommended" option to make the solver
  put installed packages on the suggestions/recommendations
  queues
- Fix content parsing if PRODUCT isn't the first entry.
- add more statistics
- add two assertions
- add support for susetags filelist
- plug mem join2 leak
- fix anchoring of filelist data
- susetags move files added to provides back into filelist
- ignore packages.FL for now
* Sun Apr 20 2008 coolo@suse.de
- fix build
* Sat Apr 19 2008 coolo@suse.de
- fix probleminfo if solvable conflicts with itself and has no requires
- Fix parsing dep lines of content files (bnc #380396).
- C++-guard also solver.h
- add support for feature rules
- fix a couple of small bugs
- use new interface
* Wed Apr 16 2008 coolo@suse.de
- fix (rare) case of crashing solver
* Tue Apr 15 2008 coolo@suse.de
- some fixes around updateinfo parsing
* Wed Apr  9 2008 jkupec@suse.cz
- enable regex matching in Dataiterator
* Fri Apr  4 2008 coolo@suse.de
- package deptestomatic in -devel
* Mon Mar 31 2008 coolo@suse.de
- truly restart when analyze_unsolvable is hit (fixes bnc#368209)
- make it work with really large directories
* Mon Mar 24 2008 coolo@suse.de
- install rpms2solv
* Mon Mar 17 2008 matz@suse.de
- Initialize all allocated array members for blocky arrays (when it
  matters, e.g. when extending also in blocks - bnc#371137)
* Fri Mar 14 2008 coolo@suse.de
- fix build on other distris
- fix requires of tools
* Wed Mar 12 2008 coolo@suse.de
- store datadir for susetags
- fixing assertion in rules learning
* Fri Mar  7 2008 coolo@suse.de
- several fixes in whatprovides (possibly root cause of bnc#367210)
* Mon Feb 25 2008 coolo@suse.de
- fixing rpmdb2solv argument handling
* Fri Feb 22 2008 coolo@suse.de
- support rpmdb2solv -r for chroots
* Thu Feb 21 2008 coolo@suse.de
- fix susetags parser for so called full trees
* Wed Feb 20 2008 coolo@suse.de
- no longer link against db43 but against rpmlib
* Tue Feb 19 2008 coolo@suse.de
- fix requires/obsoletes
* Tue Feb 19 2008 coolo@suse.de
- mls is back from vacation - several fixes and enhancements
* Fri Feb 15 2008 coolo@suse.de
- several fixes for the solv files
* Tue Feb 12 2008 kkaempf@suse.de
- add libappsatsolver, an application layer to ease coding
  against sat-solver.
* Tue Feb 12 2008 coolo@suse.de
- let susetags parse vendors
* Thu Feb  7 2008 coolo@suse.de
- rename libsatsolver in satsolver-tools
- several updates and fixes
* Fri Feb  1 2008 coolo@suse.de
- really don't strip
* Mon Jan 14 2008 coolo@suse.de
- update from SVN:
  - various fixes
  - less logging
* Tue Jan  8 2008 coolo@suse.de
- update to SVN again and don't strip
* Sat Dec 22 2007 coolo@suse.de
- update to SVN so libzypp compiles again
* Fri Nov 30 2007 schubi@suse.de
- update for libzypp integration
* Fri Nov 16 2007 coolo@suse.de
- update to SVN again to make libzypp compilable again
* Wed Nov 14 2007 schubi@suse.de
- further develpment. bugfix, logging, docu,...
* Mon Nov 12 2007 coolo@suse.de
- update to the latest version from SVN
  - compilation fixes
  - policy engine
* Thu Nov  8 2007 coolo@suse.de
- update to the latest version from SVN
* Tue Oct  2 2007 kkaempf@suse.de
- Initial release
