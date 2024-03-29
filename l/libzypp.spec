Name:           libzypp
License:        GPLv2+
Group:          System/Packages
Summary:        Package, Patch, Pattern, and Product Management
Version:        8.8.0
Release:        2.2
Source:         %{name}-%{version}.tar.gz
Source1:        %{name}-rpmlintrc
Patch1:		add-armv7hl-and-armv7nhl-arches.patch
Provides:       yast2-packagemanager
Obsoletes:      yast2-packagemanager

BuildRequires:  cmake
BuildRequires:  openssl-devel
BuildRequires:  libudev-devel
BuildRequires:  boost-devel
BuildRequires:  dejagnu
BuildRequires:  doxygen
BuildRequires:  gcc-c++
BuildRequires:  gettext-devel
BuildRequires:  graphviz
BuildRequires:  libxml2-devel

BuildRequires:  libsatsolver-devel >= 0.14.17
Requires:       satsolver-tools

# required for testsuite, webrick
BuildRequires:  ruby

BuildRequires:  expat-devel

BuildRequires:  glib2-devel
BuildRequires:  popt-devel
BuildRequires:  rpm-devel

Requires:       gnupg2

# ---------------------------------------------------------------
# This is >=11.2 (better not sles11-sp1)
# need CURLOPT_REDIR_PROTOCOLS:
%define min_curl_version 7.19.4
# No requirement, but as we'd use it in case it is present,
# check for a sufficient version:
%define min_aria_version 1.1.2
Conflicts:      aria2 < %{min_aria_version}
# ---------------------------------------------------------------

Requires:       libcurl >= %{min_curl_version}
BuildRequires:  libcurl-devel >= %{min_curl_version}

BuildRequires:	PolicyKit-gnome

%description
Package, Patch, Pattern, and Product Management

Authors:
--------
    Michael Andres <ma@suse.de>
    Jiri Srain <jsrain@suse.cz>
    Stefan Schubert <schubi@suse.de>
    Duncan Mac-Vicar <dmacvicar@suse.de>
    Klaus Kaempf <kkaempf@suse.de>
    Marius Tomaschewski <mt@suse.de>
    Stanislav Visnovsky <visnov@suse.cz>
    Ladislav Slezak <lslezak@suse.cz>

%package devel
Requires:       libzypp = %{version}
Requires:       libxml2-devel
Requires:       openssl-devel
Requires:       rpm-devel
Requires:       glibc-devel
Requires:       zlib-devel
Requires:       bzip2
Requires:       popt-devel
Requires:       boost-devel
Requires:       libstdc++-devel
Requires:       libudev-devel
Requires:       cmake
Requires:       libcurl-devel >= %{min_curl_version}

Requires:       libsatsolver-devel

Summary:        Package, Patch, Pattern, and Product Management - developers files
Group:          System/Packages
Provides:       yast2-packagemanager-devel
Obsoletes:      yast2-packagemanager-devel

%description -n libzypp-devel
Package, Patch, Pattern, and Product Management - developers files

Authors:
--------
    Michael Andres <ma@suse.de>
    Jiri Srain <jsrain@suse.cz>
    Stefan Schubert <schubi@suse.de>
    Duncan Mac-Vicar <dmacvicar@suse.de>
    Klaus Kaempf <kkaempf@suse.de>
    Marius Tomaschewski <mt@suse.de>
    Stanislav Visnovsky <visnov@suse.cz>
    Ladislav Slezak <lslezak@suse.cz>

%prep
%setup -q
%patch1 -p1

%build
mkdir build
cd build
export CFLAGS="$RPM_OPT_FLAGS"
export CXXFLAGS="$RPM_OPT_FLAGS -DLIBUDEV_I_KNOW_THE_API_IS_SUBJECT_TO_CHANGE"
cmake -DCMAKE_INSTALL_PREFIX=%{_prefix} \
      -DDOC_INSTALL_DIR=%{_docdir} \
      -DLIB=%{_lib} \
      -DCMAKE_BUILD_TYPE=Release \
      -DCMAKE_SKIP_RPATH=1 \
      %{?use_translation_set:-DUSE_TRANSLATION_SET=%use_translation_set} \
      ..
make %{?_smp_mflags} VERBOSE=1
make -C doc/autodoc %{?_smp_mflags}
make -C po %{?_smp_mflags} translations

%if 0%{?run_testsuite}
  make -C tests %{?_smp_mflags}
  pushd tests
  LD_LIBRARY_PATH=$PWD/../zypp:$LD_LIBRARY_PATH ctest .
  popd
%endif

#make check

%install
rm -rf "$RPM_BUILD_ROOT"
cd build
make install DESTDIR=$RPM_BUILD_ROOT
make -C doc/autodoc install DESTDIR=$RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{_sysconfdir}/zypp/repos.d
mkdir -p $RPM_BUILD_ROOT%{_sysconfdir}/zypp/services.d
mkdir -p $RPM_BUILD_ROOT%{_prefix}/lib/zypp
mkdir -p $RPM_BUILD_ROOT%{_prefix}/lib/zypp/plugins
mkdir -p $RPM_BUILD_ROOT%{_prefix}/lib/zypp/plugins/commit
mkdir -p $RPM_BUILD_ROOT%{_prefix}/lib/zypp/plugins/services
mkdir -p $RPM_BUILD_ROOT%{_prefix}/lib/zypp/plugins/system
mkdir -p $RPM_BUILD_ROOT%{_prefix}/lib/zypp/plugins/urlresolver
mkdir -p $RPM_BUILD_ROOT%{_var}/lib/zypp
mkdir -p $RPM_BUILD_ROOT%{_var}/log/zypp
mkdir -p $RPM_BUILD_ROOT%{_var}/cache/zypp

make -C po install DESTDIR=$RPM_BUILD_ROOT
# Create filelist with translations
cd ..
%{find_lang} zypp


%post
/sbin/ldconfig
if [ -f /var/cache/zypp/zypp.db ]; then rm /var/cache/zypp/zypp.db; fi

# convert old lock file to new
# TODO make this a separate file?
# TODO run the sript only when updating form pre-11.0 libzypp versions
LOCKSFILE=%{_sysconfdir}/zypp/locks
OLDLOCKSFILE=%{_sysconfdir}/zypp/locks.old

is_old(){
  # if no such file, exit with false (1 in bash)
  test -f ${LOCKSFILE} || return 1
  TEMP_FILE=`mktemp`
  cat ${LOCKSFILE} | sed '/^\#.*/ d;/.*:.*/d;/^[^[a-zA-Z\*?.0-9]*$/d' > ${TEMP_FILE}
  if [ -s ${TEMP_FILE} ]
  then
    RES=0
  else
    RES=1
  fi
  rm -f ${TEMP_FILE}
  return ${RES}
}

append_new_lock(){
  case "$#" in
    1 )
  echo "
solvable_name: $1
match_type: glob
" >> ${LOCKSFILE}
;;
    2 ) #TODO version
  echo "
solvable_name: $1
match_type: glob
version: $2
" >> ${LOCKSFILE}
;;
    3 ) #TODO version
  echo "
solvable_name: $1
match_type: glob
version: $2 $3
" >> ${LOCKSFILE}
  ;;
esac
}

die() {
  echo $1
  exit 1
}

if is_old ${LOCKSFILE}
  then
  mv -f ${LOCKSFILE} ${OLDLOCKSFILE} || die "cannot backup old locks"
  cat ${OLDLOCKSFILE}| sed "/^\#.*/d"| while read line
  do
    append_new_lock $line
  done
fi


%postun -p /sbin/ldconfig

%clean
rm -rf "$RPM_BUILD_ROOT"

%files -f zypp.lang
%defattr(-,root,root)
%dir               %{_sysconfdir}/zypp
%dir               %{_sysconfdir}/zypp/repos.d
%dir               %{_sysconfdir}/zypp/services.d
%config(noreplace) %{_sysconfdir}/zypp/zypp.conf
%config(noreplace) %{_sysconfdir}/zypp/systemCheck
%config(noreplace) %{_sysconfdir}/logrotate.d/zypp-history.lr
%dir               %{_var}/lib/zypp
%dir               %{_var}/log/zypp
%dir               %{_var}/cache/zypp
%{_prefix}/lib/zypp
%{_datadir}/zypp
%{_datadir}/applications/package-manager.desktop
%{_datadir}/icons/hicolor/scalable/apps/package-manager-icon.svg
%{_datadir}/icons/hicolor/16x16/apps/package-manager-icon.png
%{_datadir}/icons/hicolor/22x22/apps/package-manager-icon.png
%{_datadir}/icons/hicolor/24x24/apps/package-manager-icon.png
%{_datadir}/icons/hicolor/32x32/apps/package-manager-icon.png
%{_datadir}/icons/hicolor/48x48/apps/package-manager-icon.png
%{_bindir}/*
%{_libdir}/libzypp*so.*
%doc %{_mandir}/man5/locks.5.*

%files devel
%defattr(-,root,root)
%{_libdir}/libzypp.so
%{_docdir}/%{name}
%{_includedir}/zypp
%{_datadir}/cmake/Modules/*
%{_libdir}/pkgconfig/libzypp.pc

%changelog
* Tue Mar 20 2018 Wei-Lun Chao <bluebat@member.fsf.org> - 
- Rebuilt for Fedora
* Wed Apr 13 2011 Wei-Lun Chao <bluebat@member.fsf.org>
- Rebuild for OSSII
* Wed Jan  5 2011 Yi Yang <yi.y.yang@intel.com> - 8.8.0
- Add two more arches armv7nhl and armv7hl
* Sun Nov  7 2010 ma@suse.de
- Update zypp-po.tar.bz2
* Wed Nov  3 2010 dheidler@suse.de
- added metalink support
- version 8.8.0 (7)
* Thu Oct 21 2010 ma@suse.de
- Feed the ProvideFilePolicy progress callback in addition to any
  connected media::DownloadProgressReport (bnc#545106)
- version 8.7.1 (7)
* Wed Oct 13 2010 dheidler@suse.de
- Make MetaLinkParser accept InputStreams
- Make MetaLinkParser accept Pathnames insted of strings
- Fix MetaLinkv4 hash parsing
- Add MetaLinkParser test
- version 8.7.0 (7)
* Mon Oct 11 2010 ma@suse.de
- Use timeouts in plugin script communication.
- Fix ExternalProgram to correctly remember exit status.
- version 8.6.0 (5)
* Sun Oct 10 2010 ma@suse.de
- Update zypp-po.tar.bz2
* Fri Oct  8 2010 dmacvicar@novell.com
- fix services not being linked to their file after being
  saved
* Thu Oct  7 2010 jkupec@suse.cz
- Don't use aria2c for FTP (bnc #641328)
* Wed Oct  6 2010 dmacvicar@novell.com
- implementation for url resolver plugins
- version 8.5.0 (5)
* Wed Oct  6 2010 dheidler@suse.de
- Use DownloadInHeaps as default, when there is nothing configured
  and when the target root is set to "/". (bnc#591476)
- version 8.4.0 (4)
* Tue Sep 28 2010 dheidler@suse.de
- fixed replacing releasever (for fedora systems) - (bnc#637470)
- version 8.3.0 (0)
* Fri Sep 24 2010 mls@suse.de
- fix metalink4 parsing [bnc#641484]
* Thu Sep 23 2010 ma@suse.de
- Update zypp-po.tar.bz2
* Mon Sep 20 2010 dmacvicar@novell.com
- Allow per repository proxy settings like yum does.
  Including setting it to _none_ overriding the
  system proxy.
  Patch from Zhang, Qiang <qiang.z.zhang@intel.com>
- version 8.2.1 (0)
* Fri Sep 10 2010 dheidler@suse.de
- fixed replacing basearch (for fedora systems) - (bnc#637473)
- version 8.2.0 (0)
* Fri Sep 10 2010 ma@suse.de
- Report download failures in commit result (bnc#431854)
- Fix Solvable::onSystemByUser returning true for uninstalled solvables.
- version 8.1.3 (0)
* Tue Aug 31 2010 ma@suse.de
- Fix download-only not to omit source packages (bnc#635596)
- version 8.1.2 (0)
* Thu Aug 26 2010 ma@suse.de
- Update zypp-po.tar.bz2
* Fri Aug 13 2010 dmacvicar@novell.com
- fix basearch url variable
- use the right release package name on fedora
* Tue Aug 10 2010 ma@suse.de
- MediaDISK: Use blkid to verify disk volumes. (bnc#623226)
- version 8.1.1 (0)
* Sun Aug  8 2010 ma@suse.de
- Update zypp-po.tar.bz2
* Thu Aug  5 2010 ma@suse.de
- Update zypp-po.tar.bz2
* Tue Aug  3 2010 ma@suse.de
- Fix memory leaks.
* Mon Aug  2 2010 ma@suse.de
- Enhance PoolItem interface to assist patch classification. (bnc#627316)
- version 8.1.0 (0)
* Tue Jul 27 2010 ma@suse.de
- Fix bug in PoolQuery::addDependency
- Disable MediaAria and enable MultiCurl as default http/ftp backend.
  MultiCurl implements MetaLink and Zsync support using libcurl. In
  case of trouble set ZYPP_MULTICURL=0 in the envirionment to disable
  the new backend.
- version 8.0.1 (0)
* Mon Jul 26 2010 ma@suse.de
- Bump heads major version after 11.3 branched away.
- version 8.0.0 (0)
* Thu Jul 22 2010 ma@suse.de
- Update zypp-po.tar.bz2
* Wed Jul  7 2010 ma@suse.de
- Add PoolQuery for name, edition AND architecture in one go. (bnc#614362)
- version 7.8.0 (6)
* Mon Jul  5 2010 ma@suse.de
- Fix requirement to /usr/bin/uuidgen (bnc#613304)
* Sun Jul  4 2010 ma@suse.de
- Update zypp-po.tar.bz2
* Tue Jun 29 2010 ma@suse.de
- Fix CURLOPT_MAX_RECV_SPEED_LARGE expecting a curl_off_t argument.
* Tue Jun 29 2010 ma@suse.de
- Respect zypp.conf policy settings when solving for update.
* Fri Jun 25 2010 ma@suse.de
- Don't bloat logfile by logging install progess values.
* Thu Jun 10 2010 ma@suse.de
- Update zypp-po.tar.bz2
* Mon Jun  7 2010 ma@suse.de
- Add missing Date constant declarations.
- version 7.7.5 (6)
* Mon Jun  7 2010 ma@suse.de
- Prevent against daemons launched in rpm %%%%post, that do not close
  their filedescriptors. Original fix was accidentally reverted.
  (bnc#174548)
- version 7.7.4 (6)
* Sun Jun  6 2010 ma@suse.de
- Update zypp-po.tar.bz2
* Fri Jun  4 2010 ma@suse.de
- Fix default evaluation of recommendations of installed
  packages (bnc#605490)
- version 7.7.3 (6)
* Thu Jun  3 2010 ma@suse.de
- Update zypp-po.tar.bz2
* Fri May 21 2010 ma@suse.de
- Fix broken IdStringType comparison (bnc#607572)
- version 7.7.2 (6)
* Thu May 20 2010 ma@suse.de
- Fix packages provided via delta rpm being placed in
  the wrong package cache (bnc#607583)
- version 7.7.1 (6)
* Thu May 20 2010 ma@suse.de
- Update zypp-po.tar.bz2
* Tue May 18 2010 ma@suse.de
- Fix arch detection on sprac (bug #566291)
- Arch: add sparc64v and sparcv9v and armv7l
- RepoManager: refresh repo if last refresh is in the future (bnc#593617)
- version 7.6.1 (6)
* Mon May 17 2010 ma@suse.de
- Fix package-manager-su to support LXDE (Andrea Florio) (bnc#582235)
- Cleanup spec file (Pavol Rusnak)
- version 7.6.0 (6)
* Sun May 16 2010 ma@suse.de
- Update zypp-po.tar.bz2
* Wed May 12 2010 ma@suse.de
- Add methods to evaluate gpg geys expiration dates.
- Export all rpmDb keys to the zypp trusted keyring in one go.
- version 7.6.0 (6)
* Wed May 12 2010 ma@suse.de
- Update zypp-po.tar.bz2
* Sun May  9 2010 ma@suse.de
- Update zypp-po.tar.bz2
* Sat May  8 2010 ma@suse.de
- Update zypp-po.tar.bz2
* Fri May  7 2010 ma@suse.de
- Update zypp-po.tar.bz2 (Revision: 54959)
* Wed May  5 2010 ma@suse.de
- Update zypp-po.tar.bz2 (Revision: 54959)
* Tue May  4 2010 ma@suse.de
- Update translations.
* Mon May  3 2010 ma@suse.de
- Improve solver.cleandepsOnRemove result by evaluating the install
  history to find packages installed on behalf of a user request (not
  auto added by the solver).
- version 7.5.0 (5)
* Sat May  1 2010 ma@suse.de
- Update translations.
* Fri Apr 30 2010 ma@suse.de
- Update translations.
* Thu Apr 29 2010 ma@suse.de
- Cleanup when deleting packages. New zypp.conf expert option
  solver.cleandepsOnRemove telling whether the solver should per
  default try to remove packages exclusively required by the ones
  he's asked to delete (default false).
- Resolver::cleandepsOnRemove API to allow applications to change
  the solver option.
- version 7.4.0 (4)
* Thu Apr 29 2010 ma@suse.de
- Update translations.
* Wed Apr 28 2010 ma@suse.de
- Enable splitprovides on update.
* Wed Apr 28 2010 ma@suse.de
- Update translations.
* Tue Apr 27 2010 ma@suse.de
- Selectable: Classify broken but locked patch as isUnwanted (bnc#577118)
- version 7.3.0 (2)
* Tue Apr 27 2010 ma@suse.de
- Use libudev to detect available cd/dvd devices (bnc#590707,fate#308980)
- Fix specfile to BuildRequire libudev-devel.
- version 7.2.0 (2)
* Mon Apr 26 2010 ma@suse.de
- Support URLs and ISOs ending on 'Media1', 'Media2', etc., when
  rewiting the URL to access a specific media number. By now only
  nanmes ending on 'CD' or 'DVD' were supported. (bnc#594850)
* Fri Apr 23 2010 ma@suse.de
- Update translations.
* Wed Apr 21 2010 ma@suse.de
- Update translations.
* Tue Apr 20 2010 ma@suse.de
- /etc/zypp/locks: Allow to specify edition ranges with
  solvable:name and dependencies.
- version 7.1.1 (1)
* Thu Apr 15 2010 ma@suse.de
- Provide name of the lock holder in ZYppFactoryException. (bnc#580513)
- version 7.1.0 (1)
* Wed Apr 14 2010 ma@suse.de
- Using boost-1.42 requires -fno-strict-aliasing (bnc#595545)
- Bump major version for 11.3 development.
- version 7.0.0 (0)
* Tue Apr 13 2010 ma@suse.de
- Fix parsing port from IPv6 URL (bnc#593385)
* Fri Mar 26 2010 ma@suse.de
- Propagate ZConfig::setTextLocale to pool. (bnc#588850)
- version 6.31.3 (31)
* Fri Mar 26 2010 ma@suse.de
- Fix guessing package spec to match package names only. (bnc#590864)
- version 6.31.2 (31)
* Tue Mar 23 2010 ma@suse.de
- Add static Target::distributionLabel to return the baseproducts
  shortName and summary. Mainlu used for the bootloader menu. (bnc #586303)
- version 6.31.1 (31)
* Thu Mar 18 2010 ma@suse.de
- Fix broken bit values in enum VendorSupportOption (bnc#589331)
- version 6.31.0 (31)
* Fri Mar 12 2010 ma@suse.de
- Fix handling of symlinked packages in package cache. (bnc #585409)
- version 6.30.5 (19)
* Tue Feb 23 2010 jkupec@suse.cz
- Avoiding use of 'guest' if 'credentials' is used when moutning
  a CIFS share. This caused 'permission denied' error with certain
  server configurations (bnc #560496).
* Tue Feb 23 2010 ma@suse.de
- Check if a downloaded file actually exists even if aria2c returned 0.
  (bnc #564816)
- version 6.30.3 (19)
* Mon Feb 22 2010 jkupec@suse.cz
- Made CURLE_PARTIAL_FILE an auto-retry error (bnc #471436)
* Mon Feb 22 2010 ma@suse.de
- Turn off cookies when retrieving services repoindex.xml (bnc #573897)
- Consider pending disable requests when removing service repositories. (bnc #572634)
- version 6.30.1 (19)
* Sun Feb 21 2010 jkupec@suse.cz
- RepoManager::cleanCacheDirGarbage added for removing directories
  which do not belong to any of known repos (bnc #467693)
- version 6.30.0 (19)
* Thu Feb 11 2010 ma@suse.de
- On SLE aria2 is not required, so conflict with a too old aria2
  version installed. (bnc #578052)
- version 6.29.5 (19)
* Wed Feb 10 2010 ma@suse.de
- Fix package-manager script wrongly escaping UTF-8 chars in path
  names (bnc #571410)
- version 6.29.4 (19)
* Mon Feb  8 2010 ma@suse.de
- Support an alternate SLE-SP1 translation set.
- version 6.29.3 (19)
* Wed Feb  3 2010 ma@suse.de
- Remember the enabled state of removed service repositories. This
  way we are able to restore service repositories correctly after a
  subscrition expired and gets renewed. (bnc #572634)
- version 6.29.2 (19)
* Thu Jan 28 2010 jkupec@suse.cz
- Abort aria2c download when the progress callback receives 'false'
  (bnc #545106)
* Tue Jan 19 2010 ma@suse.de
- Evaluate SolvAttr::repositoryToolVersion to prevent loading
  outdated solv files. (bnc #570623)
- version 6.29.0 (19)
* Fri Jan 15 2010 jkupec@suse.cz
- Use regex to parse aria2c progress lines (bnc #570917)
- version 6.28.1 (19)
* Thu Jan  7 2010 jkupec@suse.cz
- Set SignatureFileChecker context even if the key is not known
  (bnc #495977)
- version 6.28.0 (19)
* Thu Dec 10 2009 jkupec@suse.cz
- RepoInfoBase::label() added for use in UI messages, plus
  ZConfig::repoLabelIsAlias()
* Tue Dec  8 2009 ma@suse.de
- Fix transaction building in presence of multiversion installable items.
- version 6.27.1 (19)
* Fri Dec  4 2009 ma@suse.de
- Improve multiversion status handling and installation. (fate #305311)
- version 6.27.0 (19)
* Fri Dec  4 2009 jkupec@suse.cz
- Don't allow an alias to start with '.' (bnc #473834)
* Thu Dec  3 2009 ma@suse.de
- PickList and status interface for handling packages which are
  installable in multiple versions. (fate #305311)
- version 6.26.0 (19)
* Wed Dec  2 2009 ma@suse.de
- Add Selectable::highestAvailableVersionObj. Returns the highest
  available package version, ignoring priorities and policies. (bnc #557557)
- version 6.25.0 (19)
* Mon Nov 30 2009 ma@suse.de
- Also parse <product> tag from .prod files <upgrade> section.
- version 6.24.3 (19)
* Fri Nov 27 2009 ma@suse.de
- Fix chroot execution of update scripts. (bnc #558813)
- version 6.24.3 (19)
* Thu Nov 26 2009 jkupec@suse.cz
- Fixed parsing of download speed from aria2c (bnc #537870)
* Wed Nov 25 2009 ma@suse.de
- Add ui::Selecatble interface for picking specific package versions
  to install or delete if multiversion install is on.
- version 6.24.0 (19)
* Fri Nov 20 2009 ma@suse.de
- Parse zypp.conf multiversion option and make the setting available
  in pool and resolver.
- version 6.23.0 (19)
* Mon Nov 16 2009 ma@suse.de
- Specfile fixes to build on sle11-sp1.
- Fix repository probing and building in presence of productdir. (bnc #553712)
- version 6.22.3 (19)
* Thu Nov 12 2009 dmacvicar@suse.de
- Forward port and document already present changes
  from Code11-Branch
  * void SEGV if trying to access data of installed packages, that were
    deleted behind our back (bnc #530595)
  * ProxyInfoSysconfig: take care variables get initialized.
  * Fix parsing of rpm.install.excludedocs option (bnc #518883)
  * Use rpm variables in specfile. (bnc #512466)
  * Fix to compile with -Werror=format-security
  * Fix packageand() in testcase generation
  * Don't link unneeded libraries. (bnc #490895)
  * Fix Patch::categoryEnum.
  * Adapt to changed satsolver API. (bnc #480303)
  * Taking ALL translations for generating GMO files (bnc #458739)
  * Advice users to contact NCC if access to a 'novell.com'
    repository is denied (bnc #464586).
- version 6.22.2 (19)
* Thu Nov 12 2009 ma@suse.de
- Raised the limit of redirections from 3 to 6 (bnc #465532)
- Following redirections also for https (bnc #545722).
- Following https redirections requires at least libcurl4-7.19.4. (bnc #553895)
- Do not report cached packages as being downloaded. (bnc #545295)
- Per default do not collect and report deleted files outside bin and lib
  directories for 'zypper ps'. (bnc #554480)
- version 6.22.1 (19)
* Wed Nov 11 2009 ma@suse.de
- CheckAccessDeleted: Per default do not collect and report deleted files
  that outside bin and lib directories. 'zypper ps' reporting false positive
  seems to confuse. (bnc #554480)
* Wed Nov 11 2009 ma@suse.de
- Following https redirections requires at least libcurl4-7.19.4. (bnc #553895)
* Fri Nov  6 2009 ma@suse.de
- dup: Process drop list only if product actually changes. (bnc #552180)
- Selectable: Consider allowed arch/noarch changes when comuting candiadates.
- version 6.22.0 (19)
* Mon Nov  2 2009 ma@suse.de
- Enhance interface for zypper. (bnc #551956)
- version 6.21.4 (19)
* Mon Nov  2 2009 ma@suse.de
- CIFS/SMB: Support mountoption 'noguest' to prevent passing 'guest' option
  to mount. "cifs://server/share/path?mountoptions=noguest,ro" (bnc #547354)
- version 6.21.3 (19)
* Mon Nov  2 2009 ma@suse.de
- CheckAccessDeleted: Avoid reporting false positive due to insufficient
  permission.
* Mon Nov  2 2009 ma@suse.de
- Don't try to access droplist of dropped products. (bnc #551697)
- version 6.21.2 (19)
* Fri Oct 30 2009 ma@suse.de
- Don't try to use an empty proxy string. (bnc #551314)
- MediaSMB failed to pass the --workgroup option to mount. (bnc #547354)
- version 6.21.1 (19)
* Fri Oct 30 2009 ma@suse.de
- New class PoolItemBest: Find the best candidates e.g. in a PoolQuery
  result. ui::Selectabe enhancements. Both will aid applications to
  install package sets determined by query results. (bnc # 548392)
- Fix upgradeRepo solution to keep obsolete packages. (bnc #550915)
- Updated iso3166-1 country codes (bnc #531350)
- version 6.21.0 (19)
* Tue Oct 27 2009 ma@suse.de
- Add Resolver::upgradingRepo demanded by GUI. (bnc #548551)
- version 6.20.0 (19)
* Thu Oct 22 2009 ma@suse.de
- Fixes to make libzypp-bindings compile.
- version 6.19.3 (19)
* Tue Oct 20 2009 ma@suse.de
- Credentials are passed as commandline options to aria2c, so strip any
  'user@' from the URL. Otherwise aria will use an empty password for
  this URL and authentication will fail. (bnc #544634)
- version 6.19.2 (19)
* Mon Oct 19 2009 ma@suse.de
- Repository::setInfo: Propagate priority changes to the solver to
  avoid reloading the whole repo (bnc #498266).
- version 6.19.1 (19)
* Thu Oct 15 2009 ma@suse.de
- ResStatus: add isOrphaned to test whether a package is not provided
  by any enabled repository. Orphaned packages are usually good candidates
  for cleanup unless the providing repository was intentionally disabled.
- version 6.19.0 (19)
* Thu Oct 15 2009 dmacvicar@suse.de
- aria2: pass credentials in a file instead of the command line
  which is logged.
- aria2: we get the url in the progress if there is no response
  from the server yet, handle that to avoid flooding the log.
- version 6.18.2 (17)
* Thu Oct 15 2009 ma@suse.de
- Performing a dist upgrade the solver may try to delete old and no
  longer provided (dropped) packages, even if they do not cause any
  dependency problem. This behaviour may be trurned off via zypp.conf
  option solver.upgradeRemoveDropedPackages. (bnc #539543)
- New zypp.conf option solver.upgradeRemoveDropedPackages (true).
- Add Product::droplist: List of dropped packages, i.e. packages no
  longer provided by a product.
- version 6.18.1 (17)
* Wed Oct  7 2009 ma@suse.de
- Return update messages via ZYppCommitResult. Support variable
  substitution in notification command. (fate #301175)
- Fix evaluation of no_proxy entries (bnc #543337)
- aria/curl: Fix header data in case the target is
  not initialized when downloading.
- version 6.18.0 (17)
* Thu Sep 24 2009 ma@suse.de
- Add zypp.conf option update.messages.notify: Command to be invoked
  to send update messages. (fate #301175)
- version 6.17.2 (17)
* Tue Sep 22 2009 ma@suse.de
- Add Selectable::updateCandidateObj returning the candidate for
  update, if there is one. The updateCandidate must not violate
  any active solver policy.
- version 6.17.1 (17)
* Fri Sep 18 2009 ma@suse.de
- Make sure rpmReadConfigFiles was called before using librpm (bnc #539603).
- Remove dead rpm database caching code from class RpmDb.
- version 6.17.0 (17)
* Fri Sep 11 2009 ma@km13.de
- New commit.downloadMode option in zypp.conf. Allows to set a
  prefered download policy for commit.
- version 6.16.0 (11)
* Thu Sep 10 2009 ma@suse.de
- Support nfs4 (nfs4://... or nfs://...?type=nfs4) (fate #306451)
- Added Url::schemeIsLocal, schemeIsRemote, schemeIsVolatile and
  schemeIsDownloading.
- version 6.15.0 (11)
* Wed Sep  9 2009 ma@suse.de
- Add Capability::guessPackageSpec; parser also supporting "name-ver-rel.arch"
  formats for building Capabilities(originally "name.arch=ver-rel").
- version 6.14.3 (11)
* Mon Sep  7 2009 ma@suse.de
- Fix resolution to force installation even if dependencies are missing.
  (bnc #531564)
- Rephrase solver resolution to point out if a package will break.
  (bnc #520083)
* Fri Sep  4 2009 ma@suse.de
- Lock rpms architecture only on distupgrade of the running system.
  (bnc #458520)
- version 6.14.2 (11)
* Thu Sep  3 2009 ma@suse.de
- Fix PoolQuery comparison (bnc #528755)
- Fix serialization and restore of predicated PoolQueries.
- version 6.14.0 (11)
* Mon Aug 31 2009 ma@suse.de
- package-manager script: Fall back to package selection if no
  packages are passed on the commandline. (bnc #529137)
* Fri Aug 28 2009 dmacvicar@suse.de
- package-manager script:
  do not fail if kpackagekit is not installed (bnc #529510)
- version 6.13.3 (11)
* Wed Aug 26 2009 ma@suse.de
- Tune CheckAccessDeleted to focus on libraries and executables.
- version 6.13.2 (11)
* Thu Aug  6 2009 ma@suse.de
- Provide class CheckAccessDeleted and command zypp-CheckAccessDeleted
  to check for running processes which access meanwhile deleted files or
  libraries.  This may be used after commit, when trying to figure out
  which services need to be restated. (fate #300763).
- version 6.13.1 (11)
* Mon Aug  3 2009 ma@suse.de
- New Resolver::addUpgradeRepo to perform a dist upgrade restricted to
  certain repositories.
- version 6.13.0 (11)
* Fri Jul 31 2009 ma@suse.de
- Remove confusing newlines in vendor change info (bnc #503859)
- Removing a package lock was not counted as state change (bnc #501850)
- Take solver_allowVendorChange option into account when computing the
  Selectables default candidate.
- version 6.12.0 (11)
* Wed Jul 29 2009 ma@suse.de
- Avoid deadlock after fork and failed exec. (bnc 493152)
- No need to manually detect the location of aria2 binary.
- version 6.11.4 (11)
* Tue Jul 28 2009 jkupec@suse.cz
- Fixed parsing of download rate report (changed in aria2 1.4.0)
  (bnc #513944)
* Mon Jul 27 2009 ma@suse.de
- Create LogControl on demand instead of using a static var. (bnc #525339)
- version 6.11.2 (11)
* Wed Jul 22 2009 ma@km13.de
- New misc::defaultLoadSystem: Convenience to create the ZYpp instance
  and load target and enabled repositories.
* Wed Jul 22 2009 ma@suse.de
- New class InstanceId to build strings to identify/retrieve specific
  Solvables.
- version 6.11.1 (11)
* Mon Jul 20 2009 ma@km13.de
- Add download policies to ZYppCommitPolicy, supporting DownloadOnly
  and DownloadInAdvance. (fate #302159, fate #305624)
- version 6.11.0 (11)
* Thu Jul 16 2009 dmacvicar@suse.de
- add support to the package-manager script to use kpackagekit
  or gnome-packagekit if available, which allows to install local
  rpms with one click from file manager following desktop policies
  and fetching other dependencies if required.
  (fate #306526)
- version 6.10.5 (10)
* Thu Jul 16 2009 ma@suse.de
- New solver.upgradeTestcasesToKeep option in zypp.conf. It tells
  how many dist upgrade solver testcases should be kept on the system.
  Per default just the last two are kept.
- version 6.10.4 (10)
* Wed Jul 15 2009 ma@suse.de
- Don't write a solver testcase when solving for dist upgrade,
  but when actually committing.
- version 6.10.3 (10)
* Wed Jul 15 2009 ma@suse.de
- Add new string Match::Mode STRINGSTART and STRINGEND.
* Wed Jul 15 2009 jkupec@suse.cz
- log redirections when cURL media backend is used (fate #305320).
* Tue Jul 14 2009 ma@suse.de
- Support "product version" detection on systems not using
  /etc/product.d/baseproduct by looking for the first package
  providing ZConfig::distroverpkg (defaults to redhat-release).
- version 6.10.2 (10)
* Fri Jul 10 2009 ma@suse.de
- Adapt to boost_unit_test_framework-1.38.
- version 6.10.1 (10)
* Wed Jul  8 2009 ma@suse.de
- Remove obsolete UpgradeStatistics class from libzypp.
* Tue Jul  7 2009 ma@suse.de
- Fix HistoryLog to initialize on demand.
- version 6.10.0 (10)
* Fri Jul  3 2009 ma@suse.de
- Fix parsing of rpm.install.excludedocs option (bnc #518883)
* Fri Jul  3 2009 ma@suse.de
- When unmounting ISO images, don't mix up exceptions thrown by the
  loop mounted ISO and those thrown by the media containing it.
  (bnc #517856)
* Thu Jul  2 2009 ma@suse.de
- Adapt to satsolvers improved dataiterator handling.
- version 6.9.3 (8)
* Wed Jul  1 2009 ma@suse.de
- Support PoolQuery for sub-structures attributes. (fate #305503)
- version 6.9.2 (8)
* Wed Jul  1 2009 ma@suse.de
- Running as non-root user use a temporary @System solvfile in case the
  global one is outdated and needed refresh. (bnc #517183)
- version 6.9.1 (8)
* Tue Jun 30 2009 ma@suse.de
- Enhance LookupAttr to allow direct query of attributes within
  sub-structures (flexarrays).
* Fri Jun 26 2009 ma@suse.de
- Enhance PoolQueryIterator to allow detailed inspection of attribute
  matches.
- Prefer datadir stored as repo attribute, but fallback searching in
  solvbales (old solv files do this).
- version 6.9.0 (8)
* Tue Jun 23 2009 ma@suse.de
- Allow building libzypp with rpm-5 (experimental)
- version 6.8.3 (8)
* Wed Jun 17 2009 ma@suse.de
- Allow building libzypp without HAL (not recommended). Without HAL
  CD/DVD device detection is limited to /dev/dvd and /dev/cdrom.
- version 6.8.2 (8)
* Fri Jun  5 2009 ma@suse.de
- Fix solver to use IdSting to avoid failing vendor checks.
- version 6.8.1 (8)
* Thu Jun  4 2009 ma@suse.de
- Cleanup and remove deprecated interface methods.
- version 6.8.0 (8)
* Fri May 29 2009 ma@suse.de
- Improve PoolQuery to allow queries on dependencies. (bnc #475682)
- version 6.7.0 (6)
* Thu May 28 2009 ma@suse.de
- New solver.allowVendorChange expert option in zypp.conf.
- version 6.6.0 (6)
* Wed May 20 2009 ma@suse.de
- Fix lost housekeeping data in modifyRepo (bnc #503207)
* Fri May  8 2009 ma@suse.de
- Allow service refresh to change a repositories url (bnc #502157)
* Tue May  5 2009 ma@suse.de
- Detect and compile with rpm 4.7 (bnc #444211)
- version 6.5.2 (5)
* Mon May  4 2009 ma@suse.de
- Improve problem report on broken systemCheck rule (bnc #475144)
* Mon Apr 27 2009 ma@suse.de
- In update repos providing multiple release package versions for
  the same product, link a product to the latest version. (bnc #497696)
* Mon Apr 27 2009 ma@suse.de
- New classes wraping satsolver datamatcher (Match and sat::AttrMatcher)
- Extend LookupAttr to support matching specific string patterns.
- Rewrote PoolQuery::Iterator (adapt to AttrMatcher, fixes and speedup)
- version 6.5.0 (5)
* Thu Apr 16 2009 ma@suse.de
- Soft lock packages deleted on behalf of a user request.
- version 6.4.1 (2)
* Tue Mar 31 2009 ma@suse.de
- New zypp.conf option 'download.media_preference': Hint which media
  to prefer when installing packages (download vs. CD).
- version 6.4.0 (2)
* Thu Mar 12 2009 ma@suse.de
- Add Resolver::setSolveSrcPackages. Per default disable solving
  of source package dependencies. We will later allow to enable
  it per package.
- version 6.3.0 (2)
* Fri Mar  6 2009 dmacvicar@suse.de
- aria2: show the download speed in the right unit
- aria2: show the filename in progress, not the repository
- aria2: don't show done twice
* Thu Mar  5 2009 ma@suse.de
- Remove a lock if the locking process is in zombie state. (bnc #481577)
* Wed Mar  4 2009 jkupec@suse.cz
- zypp.conf: fixed and enabled 'servicesdir'
* Tue Mar  3 2009 dmacvicar@suse.de
- aria2: implement speed indicators (bnc#475506)
- aria2: implement progress indicators correctly (bnc#473846)
- aria2: fix broken pipe when looking for aria2c which caused
    a fallback to curl. (bnc#480930)
- aria2: implement saving and reading mirror stats data in
    /var/cache/zypp/aria2.stats
- aria2: handle failover correctly (bnc#481115)
- aria2: various improvements in error and report  handling
- aria2: curl: reset settings on attach to avoid duplicate
  headers
- version 6.2.1 (2)
* Tue Mar  3 2009 ma@suse.de
- Adapt to changed satsolver API.
* Fri Feb 27 2009 dmacvicar@suse.de
- Make sure Fetcher pass optional files as non-interactive
- Fixes file does not exist error when key/sig does not exist
- version 6.2.0 (2)
* Thu Feb 26 2009 ma@suse.de
- Use correct default for zconfig(solver.checkSystemFile) (bnc# 475144)
* Thu Feb 26 2009 ma@suse.de
- Prevent ResStatus from overriding user locks. (bnc #475230)
* Sun Feb 22 2009 ma@suse.de
- Never refresh repositories from CD/DVD, once they are created. (bnc #476429)
* Sat Feb 21 2009 dmacvicar@suse.de
  Implemented the following options with aria backend:
- download.max_concurrent_connections (default 2)
  download.min_download_speed (default no limit)
  download.max_download_speed (default no limit)
  download.max_silent_tries (default 5)
* Fri Feb 20 2009 dmacvicar@suse.de
- MediaAria2c: allow disabling aria2 using ZYPP_ARIA2C=0.
  Various improvements including file existence checking
  Disable HEAD request if aria2c >= 1.20
  Restrict max connections to 2 for now.
* Wed Feb 18 2009 ma@suse.de
- Neither lose packages with empty name, nor SEGV when processing them. (bnc #470011)
* Tue Feb 17 2009 ma@suse.de
- Compute obsoletes based on names only (not considering provides) (bnc #471023)
* Tue Feb 17 2009 jkupec@suse.cz
- Fixed FTP authentication (bnc #472879)
* Wed Feb 11 2009 ma@suse.de
- Follow IEC and use the binary prefixes (KiB,MiB,GiB) for printing Byte
  counts based on a power of 1024 (formerly just K,M,G). Byte counts based
  on a power of 1000 stay unaffected (kB,MB,GB).
* Mon Feb  9 2009 ma@suse.de
- Fix installation prompting for the wrong CD/DVD. (bnc #472892)
* Tue Feb  3 2009 ma@suse.de
- Send any output from rpm install/delete scripts via callback, so
  applications are able to display it. (bnc #369450)
* Mon Feb  2 2009 ma@suse.de
- Add missing translations (bnc #256289)
* Wed Jan 28 2009 jkupec@suse.cz
- HistoryLogReader added
* Tue Jan 27 2009 ma@suse.de
- Respect content-file DATDIR when downloading packages. (bnc #468612)
* Tue Jan 27 2009 jkupec@suse.cz
- Enabled CredentialManager for MediaSMB (bnc #460970).
- Ignore URL's username, password, and query string in AuthData
  comparator in CredentialManager.
* Mon Jan 26 2009 ma@suse.de
- Let vendor checks per default differ between 'openSUSE Build Service'
  and 'openSUSE' (bnc #467262).
* Fri Jan 23 2009 ma@suse.de
- Fix handling of plaindir repos on mounted devices (e.g. USB) (bnc #464778)
- Fix plaindir checksum computation not to to follow symlinks (bnc #464778)
* Thu Jan 22 2009 ma@suse.de
- Tell satsolver about product buddies (bnc #466565)
* Fri Jan  9 2009 jkupec@suse.cz
- handle HTTP 503 reponses as temporary errors (bnc #462545)
* Thu Dec 18 2008 ma@suse.de
- Fixed lost user request to abort during commit. (bnc #388810, bnc #450273)
- revision 11954
- version 5.25.0 (23)
* Thu Dec 18 2008 ma@suse.de
- Add Package::filelist, faster and less memory consuming
  implementation of Package::filenames (now deprecated).
- revision 11949
* Thu Dec 11 2008 ma@suse.de
- Add str::hexencode and str::hexdecode to encode special characters
  in a string as %%%%XX.
- Hexdecode modalias strings in rpm dependencies because rpm does not
  allow comma, blank and other special chars. (bnc #456695)
- revision 11927
* Thu Dec 11 2008 ma@suse.de
- Catch and report media errors when proving packages. (bnc #457652)
- revision 11926
* Wed Dec 10 2008 ma@suse.de
- Remove obsolete zypp.conf::productsdir and deprecate
  ZConfig::productsPath().
- Monitor /etc/products.d to determine if @system.solv needs to be
  rebuilt. (bnc #457933)
- revision 11923
- version 5.24.7 (23)
* Mon Dec  8 2008 ma@suse.de
- Execute patch scripts chroot to the installed system. (bnc #456795)
- revision 11908
* Mon Dec  8 2008 schubi@suse.de
- Make the solver reset function public (bnc #439373)
- Revision 11904
* Sun Dec  7 2008 coolo@suse.de
- note for coolo: do not trust bash advisory from TPM colleagues
* Fri Dec  5 2008 ma@suse.de
- Fix solvers inappropriate selection as byUSER (bnc 455965)
- revision 11891
- version 5.24.6 (23)
* Thu Dec  4 2008 coolo@suse.de
- fix %%%%post script to not warn on fresh install
* Mon Dec  1 2008 ma@suse.de
- Fix install order computation losing some installed packages
  pre-requirements. (bnc #439802)
- revision 11845
- version 5.24.5 (23)
* Fri Nov 28 2008 ma@suse.de
- Prune soft locks to prevent installation but not update of
  already installed packages.
- revision 11829
- version 5.24.4 (23)
* Fri Nov 28 2008 schubi@suse.de
- Taking solutions which based on user requirements/conflict
  "by User" solutions (bnc #442718)
- revision 11825
* Fri Nov 28 2008 ma@suse.de
- Take into account the requirements of all obsoleted packages uninstall
  scripts when computing the installation order. (bnc #439802)
- revision 11823
- version 5.24.3 (23)
* Thu Nov 27 2008 dmacvicar@suse.de
- fix maybeUnsuported() method returning wrong result
- add testcase for future coverage
- don't force time based uuid for anonymous id string (bnc #449654)
- RELEASE: 5.24.2 (23)
* Wed Nov 26 2008 ma@suse.de
- Call 'repo2solv -R' (recursive scan) for plaindir repos. (bnc #443350)
- revision 11810
* Wed Nov 26 2008 dmacvicar@suse.de
- SHA1SUMS.key is not imported by zypp as known key (bnc #446188)
- path and url in add_on_products.xml is evaluated wrong
  (bnc #446170)
* Mon Nov 24 2008 schubi@suse.de
- activate locking for doUpdate (bnc #447684)
- revision 11792
- RELEASE: 5.24.1 (23)
* Fri Nov 21 2008 dmacvicar@suse.de
- remove unused updaterepokey, replaced by repo
  product information
* Fri Nov 21 2008 jkupec@suse.cz
- fixed uninitialized value in OnMediaLocation (bnc #447010)
- revision 11770
* Thu Nov 20 2008 ma@suse.de
- Fix retrieval of deltarpm info.
- revision 11764
- version 5.24.0 (23)
* Thu Nov 20 2008 ma@suse.de
- Fix retrieval of Repository attributes like timestamps, keywords
  and product info.
- revision 11760
* Thu Nov 20 2008 ma@suse.de
- Enhance class LookupAttr and add convenience class LookupRepoAttr to
  iterate those solv file attributes which are not acssociated with a
  solvable. E.g. product or deltarpm info.
- revision 11754
* Wed Nov 19 2008 jkupec@suse.cz
- encode user-supplied URL strings before using them in the Url object
  (bnc #446395, bnc #444267)
- revision 11720
* Wed Nov 19 2008 ma@suse.de
- Support loading helix files.
- revision 11719
* Tue Nov 18 2008 ma@suse.de
- Add class filesystem::Glob to find pathnames matching a pattern
  by using ::glob.
- revision 11708
* Thu Nov 13 2008 schubi@suse.de
- Taking care for ppc64 while distupgrade (bnc #443685)
- revision 11670
* Wed Nov 12 2008 ma@suse.de
- Add Capability ctor from Arch and Name: (Arch_i386, "name") or
  (Arch_i386, "name == 1.0").
- revision 11669
* Wed Nov 12 2008 ma@suse.de
- Take care to always reset CURLOPT_TIMECONDITION to prevent incomplete
  downloads. (bnc #444109)
- revision 11656
- version 5.23.0 (23)
* Wed Nov 12 2008 ma@suse.de
- Check for modaliases below /sys (bnc #430179)
- revision 11653
* Tue Nov 11 2008 ma@suse.de
- Avoid superfluous file copying and gpg invocation in keyring handling.
- revision 11650
* Tue Nov 11 2008 ma@suse.de
- Prevent fetcher from processing the same index file twice. (bnc #443644)
- revision 11648
- version 5.22.0 (21)
* Fri Nov  7 2008 ma@suse.de
- Fix retrieval of patch contents and references attributes. (bnc #442200)
- revision 11641
- version 5.21.0 (21)
* Fri Nov  7 2008 ma@suse.de
- Add CheckSum::asString.
- revision 11634
* Fri Nov  7 2008 ma@suse.de
- revision 11631
- version 5.20.0 (20)
* Thu Nov  6 2008 dmacvicar@suse.de
- re-add the flavor to the http header now using a flavor
  cache that is updated on every target load.
  Target::dstributionFlavor provides access to this cache
  in case you need the last used flavor without loading
  the target.
* Thu Nov  6 2008 schubi@suse.de
- added flag: ignorealreadyrecommended to the testcases (bnc #432136)
- revsion 11539
* Thu Nov  6 2008 schubi@suse.de
- Adding rule rpm-arch for installed rpm package in order to avoid
  unneeded architecture change. (bnc #441004)
- revision 11585
* Tue Nov  4 2008 jkupec@suse.cz
- handle MediaTimeoutException also in MediaSetAccess::provideFile()
  (bnc #439983)
- revision 11568
* Mon Nov  3 2008 dmacvicar@suse.de
- merge contributions by Jon Nelson, the patches resolve
  the following issues:
- disable the "Pragma: nocache" header which is automatically
  used by curl.
  re-enables the use of a caching http proxy (like squid or others)
  and corrects (bnc #326208)
- don't generate an If-Modified-Since header if we don't have a
  previous file to work with
- don't generate a Proxy-Authenticate header if one is not called
  for.
* Fri Oct 31 2008 ma@suse.de
- Do not save solver locks (by APPL_HIGH).
- revision 11558
* Fri Oct 31 2008 dmacvicar@suse.de
- fetcher.setOptions( Fetcher::AutoAddIndexes ) allows
  for automatic signed index discovery.
- enqueueDir with checksum checking s now enqueueDigestedDir
* Thu Oct 30 2008 schubi@suse.de
- solutions: keep/lock will be done by APPL_HIGH. So they will not be
  saved in the lockfiles
- "keep obsolete" will be handled with lock by APPL_HIGH (bnc #439134)
- revision  11549
* Wed Oct 29 2008 jkupec@suse.cz
- throw a MediaTimeoutException also on http 504 (gateway timeout)
  (bnc #425035)
- revision 11535
* Wed Oct 29 2008 ma@suse.de
- Add 'sh4' architectures.
- revision 11534
* Tue Oct 28 2008 dmacvicar@suse.de
- don't free the header before curl_perform as curl does not
  copy it. (bnc#439532)
* Tue Oct 28 2008 ma@suse.de
- Add 'arm' architectures.
- revision 11525
* Tue Oct 28 2008 schubi@suse.de
- regarding "keep obsolete" in the solutions (bnc #439134)
- revision 11517
* Mon Oct 27 2008 dmacvicar@suse.de
- fix broken aria2c command line (bnc#438971)
* Sun Oct 26 2008 coolo@suse.de
- adding svn r11488 to fix compile of PackageKit
* Fri Oct 24 2008 ma@suse.de
- Remove error prone methods from OnMediaLocation API to prevent
  accidental missuse. (bnc #437328)
- revision 11487
- version 5.19.0 (19)
* Fri Oct 24 2008 ma@suse.de
- Provide the /etc/products.d enties filename as Product::referenceFilename.
  Use it to remove orphan products. (bnc #432932)
- Fix media exception handling in commit (bnc #395704)
- revision 11485
- version 5.18.0 (17)
* Fri Oct 24 2008 schubi@suse.de
- Taking "unlock" instead of setTransact(false) in the solutions (bnc #436923)
- revision 11468
- version 5.17.0 (17)
* Wed Oct 22 2008 ma@suse.de
- For retrieving a product license fall back to license.tar.gz. (bnc #372386)
- revision 11447
* Wed Oct 22 2008 dmacvicar@suse.de
- move anonymous unique id to a private http header
  X-ZYpp-AnonymousUniqueId (bnc#431571 )
* Wed Oct 22 2008 ma@suse.de
- Adapt to satsolver-0.12 API.
- Add Locale:: bestMatch to find the best match within a set of
  available Locales.
- revision 11441
* Mon Oct 20 2008 ma@suse.de
- RepoInfo: Add methods to handle repository licenses. (bnc #372386)
- revision 11419
* Mon Oct 20 2008 ma@suse.de
- Adapt to changed satsolver dataiterator API.
- revision 11418
* Fri Oct 17 2008 ma@suse.de
- Secure download of license file on repo refresh (bnc #372386)
- revision 11398
* Fri Oct 17 2008 ma@suse.de
- Call 'repo2solv.sh -o' instead of using output redirection. (bnc #420046)
- revision 11397
* Thu Oct 16 2008 jkupec@suse.cz
- repository license methods added to RepoManager (bnc #372386)
- revision 11377
* Thu Oct 16 2008 dmacvicar@suse.de
- don't take into account stat information when looking
  for remote SHA1SUMS (part of bnc#409927)
* Wed Oct 15 2008 jkupec@suse.cz
- MediaSetAccess::provideOptionalFile() added
- revision 11369
* Wed Oct 15 2008 jkupec@suse.cz
- version 5.16.1 (16)
* Tue Oct 14 2008 jkupec@suse.cz
- don't initialize servicesTargetDistro via global ZYpp instance in
  RepoManagerOptions() constructor (bnc #435184)
- revision 11342
* Mon Oct 13 2008 jkupec@suse.cz
- repository probing: check for other types of repo even on
  MediaException, throw only if all fail (bnc #335906)
- revision 11332
* Mon Oct 13 2008 ma@suse.de
- Adapt to satsolver changes.
- revision 11331
- version 5.16.0 (16)
* Mon Oct 13 2008 ma@suse.de
- Fix reading delta rpm checksum from solv file.
- revision 11313
* Mon Oct 13 2008 ma@suse.de
- Fix package-manager script to properly quote arguments. (bnc #30903)
- revision 11311
* Mon Oct 13 2008 schubi@suse.de
- regarding orphaned resolvables
- removed old distupgrade algorithm
- revision 11307
* Sun Oct 12 2008 jkupec@suse.cz
- handle ftp response 530 (login failed) like http 403
  (bnc #433537)
- revision 11305
* Thu Oct  9 2008 ma@suse.de
- Adapt to satsolvers 'big solv data change'.
- revision 11294
* Thu Oct  9 2008 schubi@suse.de
- Taking the right solution actions for locked resolvables (bnc #400840)
- revision 11289
* Thu Oct  9 2008 ma@suse.de
- Add required copy-ctor and assignment operator to WhatProvides.
  (bnc #433087)
- revision 11276
* Wed Oct  8 2008 jkupec@suse.cz
- detect and use unused loop device for mounting ISO images
  (bnc #428009)
- revision 11262
- version 5.15.1 (13)
* Wed Oct  8 2008 jkupec@suse.cz
- fixed segfault when saving the probed repo type in
  RepoManager::refreshMetadata() (bnc #431963)
- revision 11261
* Wed Oct  8 2008 dmacvicar@suse.de
- improve log message (bnc#429114)
* Wed Oct  8 2008 lslezak@suse.cz
- disk usage - ignore /proc filesystem (bnc#418783)
- revision 11258
* Tue Oct  7 2008 ma@suse.de
- Fixed detection of loopback mounted iso-files. The mtab entry does
  not necessarily mention the iso-file. (bnc #432504)
- revision 11252
- version 5.15.0 (13)
* Thu Oct  2 2008 ma@suse.de
- Add zypp.conf option 'download.use_deltarpmr.always' to enable using
  delta rpms even if the package is available on a local source.
  (Axel C. Frinke)
- revision 11235
- version 5.14.0 (13)
* Thu Oct  2 2008 ma@suse.de
- Add product attribute: PRODUCTLINE.
- revision 11234
* Thu Oct  2 2008 ma@suse.de
- Do not consider self provided requirements whan computing the
  installation order.
- revision 11231
* Wed Oct  1 2008 ma@suse.de
- Rephrase missleading error message. (bnc #431229)
- revision 11222
* Tue Sep 30 2008 ma@suse.de
- Allow computation of disk usage per solvable.
- revision 11218
* Mon Sep 29 2008 dmacvicar@suse.de
- Merge aria2c Media handler code from Google SOC 2008
  (Gerard Farras)
- Only activated by making env var ZYPP_ARIA=1
* Mon Sep 29 2008 jkupec@suse.cz
- history: tell which package failed before logging rpm output or
  error message (bnc #430585)
- no localization for history log comments
- revision 11202
* Mon Sep 29 2008 ma@suse.de
- Fix zypp::WhatProvides::empty returning inverse result.
- revision 11200
- version 5.13.1 (13)
* Sat Sep 27 2008 jkupec@suse.cz
- fixed endless loop when CredentialManager returns bad password
- CredentialManager now correctly updates password of existing
  credentials
- revision 11187
* Fri Sep 26 2008 ma@suse.de
- Fix computation of Product::flavor.
- Add Product::productLine. A vendor specific string denoting the
  product line.
- revision 11182
- version 5.13.0 (13)
* Fri Sep 26 2008 jkupec@suse.cz
- save user credentials after asking for them
- revision 11181
* Thu Sep 25 2008 jkupec@suse.cz
- ZConfig::credentialsGlobal{File,Dir}() added
  (/etc/zypp/credentials.{cat,d})
- revision 11176
* Thu Sep 25 2008 jkupec@suse.cz
- Target::setInstallationLogfile() removed from zypp/Target.h
- revision 11171
* Thu Sep 25 2008 ma@suse.de
- Remove obsolete zypp-query-pool binary. zypper provides all
  the information one needs.
- revision 11160
* Wed Sep 24 2008 jkupec@suse.cz
- HistoryLog added and used to log package installs/removes and
  repository adds, removes, url and alias changes into
  history.logfile (/var/log/zypp/history) (fate #110205)
- str::escape(string, char) added
- revision 11150
- version 5.12.1 (12)
* Tue Sep 23 2008 jkupec@suse.cz
- CredentialManager: look for credentials with
  wanted_url.startsWith(stored_url)
- RepoManager: don't pass service credentials down to repos if
  their urls are not based on service's url.
- revision 11134
* Mon Sep 22 2008 ma@suse.de
- Remove superfluous PRODUCT_REFERENCES attribute.
- revision 11127
* Mon Sep 22 2008 ma@suse.de
- Add Url::hasCredentialsInAuthority test for username or password
  being encoded in the authority component. I.e. user:pass@host.
- Handle repos to be disabled disable in service refresh.
- revision 11126
* Mon Sep 22 2008 jkupec@suse.cz
- provided context to keyring callbacks (bnc #370223)
- merged trust & import callbacks (bnc #366467)
  (don't worry, still allows to trust && !import)
- revision 11113
* Fri Sep 19 2008 ma@suse.de
- Moved DefaultAcceptBits enum to class KeyRing (formerly KeyRingReort).
- revision 11102
* Thu Sep 18 2008 ma@suse.de
- Use service alias as namespace for it's repositories aliases.
- revision 11097
- version 5.11.0 (11)
* Thu Sep 18 2008 jkupec@suse.cz
- pass service's credentials down to repos
- support ?credentials=filepath in URL to specify credentials
- revision 11092
* Thu Sep 18 2008 ma@suse.de
- Add Product::isTargetDistribution to identify the systems installed
  baseproduct. This should replace tests for Product::type is "base".
- revision 11089
* Wed Sep 17 2008 jkupec@suse.cz
- save user credentials when adding repos/services with URLs containing
  the credentials (bnc #425462)
- revision 11085
* Wed Sep 17 2008 ma@suse.de
- Adapt to rpms new way of quoting whitespace in pathnames.(bnc #426924)
- revision 11082
* Tue Sep 16 2008 ma@suse.de
- Service handling fixes. Added ServiceException.
- revision 11077
* Mon Sep 15 2008 ma@suse.de
- Fix building of transaltions.
- revision 11064
* Sat Sep 13 2008 jkupec@suse.cz
- ServiceInfo.clearReposTo{Enable,Disable}() methods added
- revision 11060
* Fri Sep 12 2008 ma@suse.de
- Create new Service repos in disbaled sate.
- revision 11056
- version 5.10.0 (10)
* Fri Sep 12 2008 ma@suse.de
- Make registerTarget and registerRelease abvailable for installed
  product. Required for registration.
- revision 11043
* Fri Sep 12 2008 ma@suse.de
- Add url lists query to Product interface. A generic query and
  convenience methods to query urls for "releasenotes", "register",
  "updateurls", "extraurls",  "optionalurls" and "smolt" (bnc #413444)
- revision 11029
* Fri Sep 12 2008 jkupec@suse.cz
- ServiceType and ServiceInfo::type() added (contains only RIS for
  now), service type probing added.
- Avoiding the use of 'path' for services (appending
  the repoindex.xml's 'path' to the baseurl of created repos)
- renamed ServiceInfo::*catalog*() methods to *repo*() methods
- revision 11022
* Thu Sep 11 2008 dmacvicar@suse.de
- add Repostiroy::updateKeys and
  Repository::providesUpdatesForKey(string) for repo and
  product matching
- Provide Repository::isUpdateRepo
* Thu Sep 11 2008 ma@suse.de
- Fix evaluation of vendor support flags.
- Adapt retrieval of registration data (targetDistribution,
  targetDistributionRelease and targetDistributionFlavor).
- revision 11013
* Wed Sep 10 2008 ma@suse.de
- Follow gpgcheck tag in .repo file and do no check if disabled.
- revision 11010
- version 5.9.0 (8)
* Wed Sep 10 2008 jkupec@suse.cz
- added dumpAsXMLOn(stream,string) to ServiceInfo to print services
  with content (repos)
- revision 11004
* Wed Sep 10 2008 ma@suse.de
- Remove obsolete product attributes.
- Store less packages in /var/lib/zypp/SoftLocks (bnc #418050)
- revision 11001
* Wed Sep 10 2008 ma@suse.de
- Provide product::updaterepoKey: Update repository indicator string.
- revision 11000
* Tue Sep  9 2008 dmacvicar@suse.de
- provide context about the repository (name/alias) if available when
  checking signatures (bnc#370223)
- 5.8.0
* Tue Sep  9 2008 ma@suse.de
- Add ServiceInfo interface to define a set of catalogs (repository
  aliases) to be enabled on next refresh.
- revision 10970
* Tue Sep  9 2008 ma@suse.de
- Fix reading of Traget::targetDistribution.
- Allow to configure default answers in signature verification workflow.
- revision 10968
* Mon Sep  8 2008 jkupec@suse.cz
- CredentialManager added to manage stored credentials
- MediaCurl adapted to use CredentialManager to read credentials
- revision 10958
* Fri Sep  5 2008 jkupec@suse.cz
- operator ==, !=, < definition moved to RepoInfoBase from
  the derived classes
- fixed RepoInfo::dumpAsIniOn() to not print 'type' if it is unknown
  (bnc #407515)
- {Repo,Service}Info::dumpAsXMLOn(ostream) added
- RepoInfo::dumpRepoOn() deprecated in favor of dumpAsIniOn()
- use shared_ptr instead of itrusive for {Repo,Service}Info
- revision 10931:10942
* Thu Sep  4 2008 jkupec@suse.cz
- RepoInfo{,Base} setters made void
- revision 10931
* Wed Sep  3 2008 jkupec@suse.cz
- skip repositories with non-matching target distro when reading
  repoindex
- revision 10926
* Tue Sep  2 2008 schubi@suse.de
- Enabled distupgrade of the SAT solver. In order to use the old
  distupgrade you can set the environment variable ZYPP_NO_SAT_UPDATE.
  This variable will can be used until the old distupgrade mechanism will
  be removed from libzypp. Have a look to above changelogs.
- revision 10911
- version 5.7.0 (5)
* Tue Aug 19 2008 dmacvicar@suse.de
- add Package::maybeUnsupported to remove duplicated
  code in clients dealing with Package::vendorSupport
* Tue Aug 19 2008 schubi@suse.de
- Reset transaction only if this solvable has no buddy (bnc #417799)
  e.g. do not reset Products cause the concerning release package
  could not already be installed.
- revision 10883
- version 5.6.1 (5)
* Mon Aug 18 2008 dmacvicar@suse.de
- don't report "may be outdated" for @System repo.
* Fri Aug 15 2008 ma@suse.de
- Add Target::targetDistribution. Returns "distribution-arch" of
  the installed base product. Used for registration and Service
  refresh. (for Fate #304915)
- revision 10877
- version 5.6.0 (5)
* Fri Aug 15 2008 ma@suse.de
- Add method Product::replacedProducts to identify installed
  Products that would be replaced by installing a new Product.
  (for Fate #301997)
- revision 10876
* Fri Aug 15 2008 ma@suse.de
- Fixes to Selectable doing staus manipulation on non-USER level.
- revision 10873
* Fri Aug 15 2008 ma@suse.de
- Add method ZYpp::getTarget that returns the Target or a NULL pointer,
  if it is not yet initialized. This is to avoid try/catch blocks just
  to test whether the Target is initialized. (bnc #417556)
- Add method Target::assertRootPrefix. Pass a pathname and get back the
  path prefixed with the tragets root, unless it already had that prefix.
- revision 10870
* Thu Aug 14 2008 schubi@suse.de
- Regarding error messages for Products correctly (FATE #304502)
- rev 10863
* Thu Aug 14 2008 ma@suse.de
- Let Selectable default to USER level.
- revision 10850
- version 5.5.1 (5)
* Wed Aug 13 2008 ma@suse.de
- Change Selectable API to support doing staus manipulation on
  non-USER level.
- revision 10847
- version 5.5.0 (5)
* Wed Aug 13 2008 dmacvicar@suse.de
- support sat solver API for searching files
* Wed Aug 13 2008 ma@suse.de
- Add ResPool::reposFind to get repositories by alias.
- revision 10835
* Tue Aug 12 2008 ma@suse.de
- Advise rpmdb2solv to parse the product database.
- revision 10824
- version 5.4.0 (4)
* Tue Aug 12 2008 ma@suse.de
- Offer a simpler, fate based status manipulation in ui::Selectable.
  This is easier to handle, as the ui::Status always distinguishes
  wheter an object is installed or not.
- revision 10814
* Mon Aug 11 2008 ma@suse.de
- Propagate default rpm install flags from zypp.conf via ZConfig and
  ZYppCommitPolicy down to the installer. (FATE #302952)
- revision 10813
* Mon Aug 11 2008 ma@suse.de
- Add base::Flags (like qt's QFlags) a type-safe way of storing
  OR-combinations of enum values.
- revision 10811
* Fri Aug  8 2008 ma@suse.de
- Add static ui::Selectable::get methods as convenient ctor
  substitute.
- revision 10806
* Fri Aug  8 2008 ma@suse.de
- Adapt zypp-query-pool to new product handling.
- revision 10803
* Fri Aug  8 2008 ma@suse.de
- Don't pass epoch to 'rpm -e', it does not support it.
- revision 10800
* Fri Aug  8 2008 ma@suse.de
- Adapt to new product handling. Products are no longer pseudo
  installed objects verified by the solver, but actually installed.
  Thus removed satisfiedProduct iterator, fixed Selctables.
- Removed class ProductInfo as we keep Product.
- revision 10797
* Thu Aug  7 2008 dmacvicar@suse.de
- implement relogin suggested support (fate#304889)
* Wed Aug  6 2008 ma@suse.de
- Detect correct download path even if repository type
  is not set. (bnc #386386)
- revision 10768
* Wed Aug  6 2008 ma@suse.de
- Cleanup, mostly by removing, unused parser code and related classes.
- revision 10765
* Wed Aug  6 2008 ma@suse.de
- Don't let exception escape MediaSetAccess dtor (bnc #415017)
- revision 10763
* Mon Aug  4 2008 ma@suse.de
- Add new product attributes (flavor,referencePackage).
- Add PoolItem buddies, i.e. two PoolItems sharing the same status
  object. This is used to keep the product resolvable and the
  package providing the product metadata in sync.
- revision 10742
* Sat Aug  2 2008 jkupec@suse.cz
- support an optional url attribute in repoindex.xml's <repo>
- revision 10729
* Thu Jul 31 2008 ma@suse.de
- New class ProductInfo to provide product related metadata that
  might be associated with a package. This will replace the Product
  resolvable.
- revision 10715
* Thu Jul 31 2008 dmacvicar@suse.de
- generate a unique anonymous unique string per target
  and add it to the agent string for better statistics
* Thu Jul 31 2008 ma@suse.de
- Follow solver policy and make repository priority the highest
  key, when ordering packages. Then architecture, and edition last.
- revision 10710
* Wed Jul 30 2008 ma@suse.de
- /var/lib/zypp and /var/cache/zypp should be owned by libzypp
  (bnc #412094)
- revision 10702
* Wed Jul 30 2008 jkupec@suse.cz
- Service renamed to ServiceInfo
- RepoInfoBase added; RepoInfo and ServiceInfo now derive from it
- revision 10695
* Tue Jul 29 2008 jkupec@suse.cz
- fixed yum repos to work with non '/' base url post fix
  (bnc #341617)
- revision 10662
* Mon Jul 28 2008 ma@suse.de
- Fixed SolvIterMixin::Selectable_iterator eating some solvables
  (bnc #411339)
- revision 10680
* Fri Jul 25 2008 ma@suse.de
- Several changes to make libzypp-bindings compile using the original
  header files and no private copies. (bnc #391831)
- revision 10668
- version 5.3.0
* Wed Jul 23 2008 jkupec@suse.cz
- Service::enabled() added
- revision 10657
* Tue Jul 22 2008 jkupec@suse.cz
- Removed FRESHENS dependency type
- revision 10643
* Thu Jul 17 2008 schubi@suse.de
- Allow parallel installation of packages which have been defined
  in zypp.conf (parameter "multiversion") Fate #302050
- Additional check for broken system.
  (defined in zypp.conv: solver.checkSystemFile)
- revision 10600
* Wed Jul 16 2008 ma@suse.de
- Add ui::Selectable::isNeeded to indicate patch relevance (bnc #409150)
- revision 10596
* Wed Jul 16 2008 ma@suse.de
- Remove Atom, Script, Message and other obsolete classes.
- revision 10592
* Mon Jul 14 2008 ma@suse.de
- Also report the name of the locking process in ZYppFactoryException
  (bnc #280537)
- revision 10572
* Mon Jul 14 2008 schubi@suse.de
- corrected logging of solver settings
- regard locking while doUpdate (bnc #405427)
- revision 10564
* Sat Jul 12 2008 jkupec@suse.cz
- make curl use the right transfer mode
  (CURLOPT_PROXY_TRANSFER_MODE) when proxy is used (bnc #306272)
- revision 10559
* Sat Jul 12 2008 jkupec@suse.cz
- reuse existing disk mounts (applied Marius' patch) (bnc #208222)
- revision 10557
* Wed Jul  9 2008 ma@suse.de
- Provide Package::url() if available in solv file. (bnc #402434)
- A missing cookie file must not be treated as an error. Simply
  rebuild the cache (bnc #405867)
- Add 22x22 and 24x24 icons (bnc #329635)
- revision 10528
* Mon Jul  7 2008 schubi@suse.de
- Do not update an already updated package (bnc #400422)
- revision 10504
* Fri Jul  4 2008 ma@suse.de
- Also check if the fingerprint matches before importing updated keys.
  (bnc #393160)
- revision 10500
* Mon Jun 30 2008 dmacvicar@suse.de
- forward port add message attribute to patches.
- port import newer keys if a trusted key is updated
- (bnc#393160)
- version 5.0.2
* Mon Jun 30 2008 ma@suse.de
- Fix permanent duplication of gpg keys in the rpm database. Also
  retrieve correct creation and expire dates. (bnc #401259)
- Invoke gpg with --homdir, otherwise command fails if executed
  within a wrapper. (bnc #401259)
- revision 10487
* Thu Jun 26 2008 schubi@suse.de
- version 5.0.1
- revision 10464
* Thu Jun 19 2008 ma@suse.de
- Handle new patch messages and scripts in commit. Provide callbacks
  to display the patch messages and give visual feedback on script
  execution. (bnc #401220)
- revision 10411
* Thu Jun 19 2008 ma@suse.de
- Fix wrong parenthesis causing bug 399320
- version
- revision
* Tue Jun 10 2008 jreidinger@suse.cz
- improve performance of gsub
- change replace_all to replaceAll (same name convency)
- add tests for gsub and replaceAll
- revision 10366
* Fri Jun  6 2008 ma@suse.de
- Handle application/x-redhat-package-manager in package-manager.desktop
  (bnc #391183)
- revision 10361
* Thu Jun  5 2008 jkupec@suse.cz
- X-SuSE-ControlCenter-System category added
  to package-manager.desktop (bnc #302324)
- revision 10353
* Wed Jun  4 2008 ma@suse.de
- Fix crash when requesting disk usage without a target loaded. (bnc #396755)
- revision 10340
* Wed Jun  4 2008 ma@suse.de
- Fix memory corruption in curl media handler (bnc #396979)
- revision 10338
* Tue Jun  3 2008 ma@suse.de
- Take care satsolver recognizes 'Capability( "srcpackage:zypper" )'
  as 'source package named zypper'. So these capabilities can be used
  together with sat::Whatprovides or in resolver requests. (bnc #369893)
- revision 10335
* Tue Jun  3 2008 jreidinger@suse.cz
- allow aborting progress during removing packages. (bnc #389238)
- revision 10331
* Mon Jun  2 2008 schubi@suse.de
- New option for ignoring Obsoletes. This is used for installing more than
  one pacakges with the same name but different versions.
  Often used by kernel.
- r 10299
* Sun Jun  1 2008 ma@suse.de
- Revert inappropriate Selectable cleanup. Fix Selectable
  status computation. Unmaintained packages were wrongly
  reported as unsinstalled. (bnc #394630)
- version 5.0.0 (4.x continued in SuSE-Linux-11_0-Branch)
- revision 10295
* Fri May 30 2008 tgoettlicher@suse.de
- fixed typo
* Wed May 28 2008 ma@suse.de
- Reenable diskusage calculation (bnc #395051)
- version 4.25.1
- revision 10273
* Wed May 28 2008 jkupec@suse.cz
- RepoManager::packagesPath(RepoInfo) added (bnc #394728)
- revision 10271
* Wed May 28 2008 jkupec@suse.cz
- RepoInfo: don't overwrite flags that have already been set externally
  (bnc #394728)
- revision 10256
* Wed May 28 2008 ma@suse.de
- Create missing directories when saving config files. (bnc #395026)
- Fix undefined behaviour in RepoManager.
- revision 10255
* Wed May 28 2008 schubi@suse.de
- SOLVER_ERASE_SOLVABLE_NAME: As we do not know, if this request has come
  from resolvePool or resolveQueue we will have to take care for both
  cases. (bnc#393969)
- r 10252
* Tue May 27 2008 coolo@suse.de
- compile with RPM_OPT_FLAGS
* Mon May 26 2008 jkupec@suse.cz
- old2new locks file converter script added to %%%%post (jredinger)
- r 10227
* Mon May 26 2008 schubi@suse.de
- Do not regard packages with the same name while upgrading obsoleted
  packages (bnc#394367)
- r 10219
* Sat May 24 2008 dmacvicar@suse.de
- revert commit don't check for existence of keys,
  to avoid a non needed HEAD request. (related bnc#381280)
  as it creates popup error callbacks due to the 404's in
  the keys. Leave however the OnMediaLocation::optional()
  API to look for another fix strategy.
* Fri May 23 2008 dmacvicar@suse.de
- define path for messages and scripts and document
  them in zypp.conf
* Fri May 23 2008 schubi@suse.de
- Added IgnoreAlreadyRecommended flag. So recomments/suggest will
  be ignored for already INSTALLED packages (bnc #389694)
- r 10202
* Fri May 23 2008 schubi@suse.de
- Packages which obsoletes and do NOT required other installed
  packages will be installed if no other packages obsolete the installed package too.
- r 10196
* Thu May 22 2008 dmacvicar@suse.de
- fix filelist for installed packages (bnc#392544)
- fix changelog retrieval for installed packages
* Wed May 21 2008 dmacvicar@suse.de
- deprecate Repository::name() and use alias() to
  be consistent. Related to (bnc#383553)
- don't check for existence of keys, to avoid a non needed
  HEAD request. (helps bnc#381280)
- 4.25.0
* Wed May 21 2008 schubi@suse.de
- added onlyRequires in the testcase (bnc #389184)
* Tue May 20 2008 jreidinger@suse.cz
- allow installation and refreshing from repository with alias that
  contains ' or " (bnc #392426)
- r10158
* Mon May 19 2008 jkupec@suse.cz
- delta rpm support reenabled
- r10150
* Mon May 19 2008 schubi@suse.de
- Resetting Delete Details in ResStatus correctly (bnc #391785)
- r 10145
* Mon May 19 2008 dmacvicar@suse.de
- when setting status to non installed for uninstalled packages
  set the user transaction so they go to soft locks.
  (related to bnc#389739 )
* Fri May 16 2008 schubi@suse.de
- Added new calls : isInstalledBy (const PoolItem item);
    installs (const PoolItem item);
- r 10125
- 4.23.0
* Fri May 16 2008 jreidinger@suse.cz
- don't run merge in save when toAdd/Remove queue is empty
- throw when locks cannot load its file
- r10124
* Fri May 16 2008 jreidinger@suse.cz
- throw more describing exception when repo probing failed
  (bnc #389690)
- revision 10118
* Thu May 15 2008 jreidinger@suse.cz
- allow call only merge old locks and newly added/removed without
  saving it to file
- -revision 10104
* Tue May 13 2008 dmacvicar@suse.de
- report non packages as keep installed if satisfied to the
  user interace (Selectables)
- 4.21.3
* Tue May 13 2008 jkupec@suse.cz
- create /etc/zypp/products.d on install
* Mon May 12 2008 jkupec@suse.cz
- /etc/zypp/products.d added to file list (bnc #385868)
- revision 10049
- version 4.21.2
* Mon May 12 2008 jkupec@suse.cz
- call RemoveResolvableReport::problem() before finish() on error
  (bnc #388810)
- revision 10045
* Sat May 10 2008 coolo@suse.de
- fix file list
* Fri May  9 2008 ma@suse.de
- Product now retrieves all attributes from the solv file.
- version 4.21.1
- revision 10031
* Fri May  9 2008 ma@suse.de
- Add zypp.conf option configdir (/etc/zypp) and arrange
  all config files and directories to follow {configdir}
  per default.
- Fix zypp-query-pool to print satisfied products and additional
  products defined in {configdir}/products.d for registration.
  (bnc #385868)
- version 4.21.0
- revision 10029
* Fri May  9 2008 jreidinger@suse.cz
- implement remove duplicate entries in lock file (bnc#385967)
* Fri May  9 2008 ma@suse.de
- Speedup rpmdb2solv by reusing an existing solv file.
- version 4.20.1
- revision 10012
* Thu May  8 2008 ma@suse.de
- Fix failed package download due to unkown repository type (bnc #386386)
- revision 9995
* Thu May  8 2008 ma@suse.de
- Support optional root argument to RepoManagerOptions, to prefix all
  path names taken from ZConfig. (bnc #388265)
- version 4.20.0
- revision 9993
* Thu May  8 2008 schubi@suse.de
- new solution action for removing requirements/conflicts (bnc #387631)
- revision 9988
* Thu May  8 2008 ma@suse.de
- Provide enumerated patch category 'Patch::categoryEnum()' (bnc #159100)
- revision 9984
* Wed May  7 2008 schubi@suse.de
- DistUpgrade: searching for providers -> regarding name onl
- r 9977
* Tue May  6 2008 dmacvicar@suse.de
- add flag --registrable (-r) to query pool to avoid
  using system as a filter
- 4.19.1
* Tue May  6 2008 coolo@suse.de
- return values in non-void functions
* Mon May  5 2008 jkupec@suse.cz
- support multiple search strings in PoolQuery (ORed)
- revision 9945
* Mon May  5 2008 schubi@suse.de
- Switch off the upgrade mode of the
  SAT solver cause the packages have already been evaluated by
  the distupgrade machanism of libzypp. (bnc #386375)
- rev 9943
* Fri May  2 2008 jreidinger@suse.cz
- release file after copy to cache as soon as possible.
  (bnc #381311)
- r9940
* Fri May  2 2008 schubi@suse.de
- Bugfix: keep states by user has been removed it the
  package has not been installed BUT has been recommended by another package.
  (bnc #385832)
- rev 9938
* Fri May  2 2008 jreidinger@suse.cz
- add isLocal function to Url which say if scheme is local or
  internet.
- r9932
* Fri May  2 2008 jreidinger@suse.cz
- cache decision for repository depend on his url.
- http,ftp and smb cache packages.
- revision 9929
* Wed Apr 30 2008 ma@suse.de
- Load and maintain persistent hard locks stored in /etc/zypp/locks.
  Locks are loaded together with the target, and changes are writen
  back on commit. zypp.conf option locksfile.apply can be used to turn
  this feature on or off. (FATE #120352)
- version 4.18.0
- revision 9927
* Wed Apr 30 2008 ma@suse.de
- Add zypp.conf option solvfilesdir: Path where the repo solv files
  are created. Default value: {cachedir}/solv.
- Target and repositories now save their solvfiles below {solvfilesdir}
  in directories named after the repositories alias.
- version 4.18.0
- revision 9913
* Wed Apr 30 2008 jkupec@suse.cz
- fixed filesystem::expandlink(Pathname) (bnc #368477)
- r9906
* Tue Apr 29 2008 schubi@suse.de
- cleanup in return values of doUpgrade and doUpdate
- r9886
- 4.17.0
* Mon Apr 28 2008 jkupec@suse.cz
- check for valid pool in begin(), improve the code (bnc #384337)
- r9872
- 4.16.0
* Mon Apr 28 2008 mvidner@suse.cz
- Updated package-manager-su from xdg-utils-1.0.2-48 (bnc#339549).
* Mon Apr 28 2008 schubi@suse.de
- added translations
* Mon Apr 28 2008 jkupec@suse.cz
- ostream operator<<(ostream,TriBool) added
- r9833
* Fri Apr 25 2008 ma@suse.de
- Prevent target::unload from creating a system repo in order
  to unload it. (bnc 382297)
- version 4.15.2
- revision 9822
* Fri Apr 25 2008 ma@suse.de
- Prevent deselected or deleted items from being re-selected due to
  recommends (aka. persistent soft locks). Unlike hard locked, those
  items will be automatically selected if required. The list of soft
  locked items is stored in /var/lib/zypp/SoftLocks.
- version 4.15.1
- revision 9818
* Wed Apr 23 2008 ma@suse.de
- Remove obsolete AdditionalCapabilities interface from ResPool.
  Forward sat::Pool::RepositoryIterator. There's no more need to
  maintain an extra Repository list in ResPool.
- revision 9806
* Wed Apr 23 2008 ma@suse.de
- Support dependencies requiring a specific architecture:
  "name[.arch] [op edition]". See class Capability for details
  about how to construct dependencies. (bnc #305445)
- version 4.15.0
- revision 9805
* Tue Apr 22 2008 dmacvicar@suse.de
- patch attributes and deprecate old ones
- 4.14.0
* Tue Apr 22 2008 jreidinger@suse.cz
- change locks api -
- make more functions const
- replace add/remove by selectable to add/remove by ident or name and kind
- rename iterator to const_iterator to avoid confusion
- revision 9781
* Tue Apr 22 2008 schubi@suse.de
- Do architecture changes while "dup" in the external distribution
  upgrade ONLY. bnc #382274
- Added "ignore" to the solutions
- Added "self-conflicts" to the solution
- added new solver mechanism "resolveQueue"
- Bugfix broken/satisfied products
- rev 9776
* Tue Apr 22 2008 ma@suse.de
- Added Pattern::core returning the packages required by a pattern.
  (see also Pattern::depends and Pattern::contents).
- revision 9771
* Mon Apr 21 2008 ma@suse.de
- Added Target::release(), returning the targets distribution
  release string.
- revision 9761
* Sat Apr 19 2008 ma@suse.de
- per default abort if package installation fails. (bnc #381203)
- version 4.13.3
- revision 9725
* Fri Apr 18 2008 dmacvicar@suse.de
- add ZYpp and curl version to http agent string
  (bnc #381280)
* Thu Apr 17 2008 ma@suse.de
- Fixed pools package index wrongly including source packages. (bnc #380283)
- version 4.13.2
- revision 9683
* Wed Apr 16 2008 ma@suse.de
- Disable fast creation of @System.solv. It may produce wrong results
  e.g. after a rebuilddb.
- version 4.13.1
- revision 9666
* Wed Apr 16 2008 ma@suse.de
- initializeTarget now takes an additional option, telling whether to
  rebuild an existing rpm database before using it. Default is false.
  (bnc #308352)
- version 4.13.0
- revision 9664
* Tue Apr 15 2008 jreidinger@suse.cz
- save do nothing if no locks added/removed
- fix bug with multiple save lock
- don't save same query multiple times
- improve tests
- revision 9644
* Tue Apr 15 2008 schubi@suse.de
- added new translations
- activate zypp-query-pool
- Revision 9637
- 4.12.1
* Mon Apr 14 2008 jkupec@suse.cz
- Locks API cleaned-up, iterator added, light read() added
- PoolQuery::attribute(SolvAttr) getter added
- revision 9609
* Mon Apr 14 2008 dmacvicar@suse.de
- reenable zypp-query-pool
- 4.11.1
* Mon Apr 14 2008 ma@suse.de
- Enable evaluation of hardware dependencies.
- Enable evaluation of filesystem dependencies.
- revision 9605
* Sun Apr 13 2008 jkupec@suse.cz
- RawMetadataRefreshPolicy: CheckIfNeededIgnoreDelay added
  needed for explicit refresh request
- revision 9574
* Fri Apr 11 2008 ma@suse.de
- Install ResPoolProxy index to speedup Solvable to Selectable
  conversion.
- version 4.11.0
- revision 9558
* Fri Apr 11 2008 kkaempf@suse.de
- Implement update scripts installed by packages. After every
  package install /var/adm/update-scripts is scanned for the first
  file starting with "<name>-<version>.<release>-", which is then
  executed.
- revision 9547
* Fri Apr 11 2008 ma@suse.de
- Fix SolvIterMixin to avioid multiple visits of the same Selectable.
- Add Resolvable::poolItem() providing access to the corresponding
  PoolItem. API to query isRelevant/isSatisfied/isBroken was moved
  to PoolItem.
- Add ResPool::satisfiedProductsBegin/End iterator over all products
  whose dependencies are satisfied. This reflects the status determined
  by the last solver run. (#368104)
- revision 9535
* Fri Apr 11 2008 jreidinger@suse.cz
- switch to new locks api
- revision 9524
* Wed Apr  9 2008 ma@suse.de
- Enable ui::Selectable lookup by Solvable/PoolItem in ResPoolProxy.
- Add SolvIterMixin: Base class providing PoolItem_iterator and
  Selectable_iterator iterator types based on a Solvable iterator.
- Enhanced WhatProvides and SolvableSet to PoolItem_iterator to offer
  PoolItem_iterator and Selectable_iterator.
- Add Solvable::SplitIdent: Helper class that splits an identifier
  into kind and name.
- Provide methods Pattern::contents returning a collection of packages
  associated with the pattern/patch.
- revision 9496
* Tue Apr  8 2008 jreidinger@suse.cz
- add comparing to PoolQuery
- revision 9466
* Tue Apr  8 2008 jreidinger@suse.cz
- move RepoInfo to universal RepoException. This can enable more verbose output - for frontend. (helps with bnc #377137)
- revision 9452
* Tue Apr  8 2008 jreidinger@suse.cz
- initial implementation of new locks (FATE #120118 and #120352)
- revision 9442
* Mon Apr  7 2008 dmacvicar@suse.de
- selectable API updates and changes
- 4.10.0
* Fri Apr  4 2008 jreidinger@suse.cz
- add split with respect to escaped delimeters and also for quotes
- revision 9373
* Thu Apr  3 2008 ma@suse.de
- Fixed some missing package and source package attributes.
- revision 9348
* Thu Apr  3 2008 ma@suse.de
- Allow to store a media label in MediaSetAccess. This label is
  passed to a media change requests to describe which CD is
  requested.  (bnc #330094)
- Fixed some missing package and source package attributes.
- revision 9347
* Wed Apr  2 2008 schubi@suse.de
- Moved poolItem.status().isSatisfied(),.... to poolItem.isSatisfied()
- Removed establish state in ResStatus
- revision 9337
- version 4.7.0
* Wed Apr  2 2008 ma@suse.de
- Add PoolItem::isSatisfied()/isBroken() to test whether
  the items requirements are met.
- revision 9334
* Tue Apr  1 2008 ma@suse.de
- Extend sat::WhatProvides to allow to query for possible providers
  of a collection of capabilies. E.g. all providers of a packages
  requirements.
- Fixed retrieval of translated texts from .solv files, provided the
  solv file contains them.
- revision 9328
* Tue Apr  1 2008 jreidinger@suse.cz
- initial implementation of serialize/recovery PoolQuery
  (needed by FATE #120118)
- revision 9325
* Wed Mar 26 2008 ma@suse.de
- Allow prioritizing repos by adding a line 'priority=N' to the
  .repo file. Where N is an integer number from 1 (highest prio)
  to 99 (least and default). (bnc #369827, fate #302872)
- version 4.6.1
- revision 9276
* Mon Mar 24 2008 coolo@suse.de
- support plaindir again (at least the most important parts)
* Fri Mar 21 2008 jreidinger@suse.cz
- Throwing special exception MediaBadCAException in case of SSL
  certificate validation failure.(bnc #223512)
- revision 9250
* Fri Mar 21 2008 jreidinger@suse.cz
- add new error IO_SOFT to media request callback for temporary
  connection problem. (bnc #328822)
- add new media exception timeout when somethink fail due to exceed
  timeout
- mediacurl throw timeout exception when timeouted
- revision 9246
* Thu Mar 20 2008 jreidinger@suse.cz
- return more information from checking if metadata need refresh,
  so user can get better info. (bnc #307249)
- revision 9231
* Tue Mar 18 2008 ma@suse.de
- class sat::LocaleSupport: Convenience methods to manage support
  for language specific packages.
- revision 9197
* Tue Mar 18 2008 jkupec@suse.cz
- removed obsolete capability handling stuff (ma)
- version 4.5.0
* Tue Mar 18 2008 jreidinger@suse.cz
- Don't mask skip and abort exception in Fetcher
- revision 9188
* Tue Mar 18 2008 jreidinger@suse.cz
- action is correctly set in mediaRequest callback
- revision 9186
* Mon Mar 17 2008 ma@suse.de
- Fix SEGV in commit (bnc# 371137)
- version 4.4.3
- revision 9174
* Fri Mar 14 2008 ma@suse.de
- version 4.4.2
* Fri Mar 14 2008 dmacvicar@suse.de
- look for openssl in cmake, actually we build require it
- explicitely link against openssl and crypto, required to
  compile in all platforms/distros.
* Fri Mar 14 2008 jreidinger@suse.cz
- Save repo type during refresh if type is NONE (f.e. lazy probing).
- revision 9153
* Fri Mar 14 2008 jreidinger@suse.cz
- replace gpg escaped semicolon with real semicolon (bnc #355434)
- revision 9151
* Fri Mar 14 2008 jreidinger@suse.cz
- make strings from RpmDb and Keyring exceptions translatable
- revision 9146
* Thu Mar 13 2008 dmacvicar@suse.de
- fix retrieving keys (bnc #368099)
- version 4.4.1
* Thu Mar 13 2008 jreidinger@suse.cz
- enable frontend to rewrite add_probe settings.(bnc #309612)
- Correct adding repo without type to lazy probing.
- revision 9135
* Thu Mar 13 2008 jreidinger@suse.cz
- get better message if something fail when trying run rpm
  (bnc #344584)
- revision 9133
* Thu Mar 13 2008 ma@suse.de
- Add ExternalProgram::execError and ExternalProgram::command
  to improve error reporting.
- revision 9112
* Thu Mar 13 2008 jkupec@suse.cz
- release all media before requesting another (bnc #336881)
- revision 9110
* Thu Mar 13 2008 jkupec@suse.cz
- getDetectedDevices added (fate #120298)
- revision 9108
* Wed Mar 12 2008 jkupec@suse.cz
- media backend release() methods changed to take string & instead
  of bool (needed for FATE #120298)
- media label, detected device list and current device arguments
  added to the requestMedia callback
- version 4.4.0
* Wed Mar 12 2008 coolo@suse.de
- fix for bnc#369543
* Mon Mar 10 2008 jkupec@suse.cz
- provide download rate info (average and curent) in the
  media::DownloadProgressReport for ftp/http (bnc #168935)
- r9074
* Mon Mar 10 2008 jkupec@suse.cz
- cleanCache(): clean also .cookie files
- cleanTargetCache() added
- use escaped_alias() in rawcache_path_for_repoinfo() and
  packagescache_path_for_repoinfo()
- r9068
* Fri Mar  7 2008 jkupec@suse.cz
- fixed location of RPMs in subdirs when parsing plaindir repo
  recursively (bnc #368218)
- revision 9060
* Thu Mar  6 2008 ma@suse.de
- Do not filter any installed solvables.
- revision 9031
- version 4.3.2
* Wed Mar  5 2008 ma@suse.de
- Try to rebuild broken solv files in Target::load.
- revision 9015
* Tue Mar  4 2008 ma@suse.de
- Try to rebuild broken solv files in RepoManager::loadFromCache.
- Fix RepoStatus::operator&& and RepoStatus testsuite.
- revision 9008
* Tue Mar  4 2008 schubi@suse.de
- improved problem description while a vendor change
- improved problem description if a requirement cannot be fulfilled. Bug #358560
- revision 9002
* Tue Mar  4 2008 ma@suse.de
- Save and restore requested locales on target load/commit.
- revision 8999
* Mon Mar  3 2008 schubi@suse.de
- (Update) Prevent reinstallation of installed packages.
- revision 8984
* Sun Mar  2 2008 coolo@suse.de
- refresh metadata if there is no cache to unbreak compat with
  kiwi (that relied on "zypper sa <url> <alias>" to create a repo
  that "zypper in" could work on)
* Sun Mar  2 2008 coolo@suse.de
- create cache directory before calling rpmdb2solv (in an empty
  chroot)
- version 4.3.1
* Thu Feb 28 2008 jkupec@suse.cz
- special exception message if server returns 403 response
  (forbidden) (port from SP2)
- MediaException messages marked for translation
* Wed Feb 27 2008 dmacvicar@suse.de
- make sure we have target cache on target initialize
- version 4.3.0
* Tue Feb 26 2008 lslezak@suse.cz
- DiskUsageCounter.cc - ignore "vfat", "fat", "ntfs" and "ntfs-3g"
  file systems (#333166)
- rev. 8915
* Tue Feb 26 2008 ma@suse.de
- Fixed Capabilites iterator exposing prereq marker.
- revision 8914
* Tue Feb 26 2008 schubi@suse.de
- postinstall script fixed
- version 4.2.10
* Mon Feb 25 2008 schubi@suse.de
- Testcases regards modaliases, rpmlib, ... correctly
- Revision 8904
* Mon Feb 25 2008 ma@suse.de
- Remove obsolete sql database. (bnc#363224)
- revision 8898
* Fri Feb 22 2008 ma@suse.de
- Take care target uses --root when creating solv files (bnc #363789)
- revision 8881
* Fri Feb 22 2008 schubi@suse.de
- Unmaintained packages which does not fit to the updated system
  (broken dependencies) will be deleted.
- revision 8867
* Fri Feb 22 2008 coolo@suse.de
- let libzypp-devel require libsatsolver-devel
* Wed Feb 20 2008 ma@suse.de
- Cleanup unused /var/lib/zypp/cache in migrate_sources (#305160)
- revision 8833
* Tue Feb 19 2008 jkupec@suse.cz
- media: fixed DownloadProgressReport.finish() url argument in
  doGetFileCopy()
- revision 8815
* Tue Feb 19 2008 dmacvicar@suse.de
- hardlink when possible to optimize data transfer
  and space across caches.
- version 4.2.8
* Tue Feb 19 2008 coolo@suse.de
- added some locale support to sat::Solvable
- version 4.2.7
* Mon Feb 18 2008 dmacvicar@suse.de
- handle error messages better in doesFileExist too which is
  used during probing. (bnc #362608)
* Sun Feb 17 2008 dmacvicar@suse.de
- Fetcher::reset() should not reset cache directories.
  (bnc #348050)
- version 4.2.6
* Sat Feb 16 2008 dmacvicar@suse.de
- Use CURLOPT_NOBODY instead of a CURLOPT_RANGE of 1 byte
  for http and https, but this time set CURLOPT_HTTPGET back to 1
  so it actually works. This makes Media::doesFileExist
  efficient for http and https.
  (related to bnc #348050)
- version 4.2.5
* Fri Feb 15 2008 coolo@suse.de
- using .solv files only now (fate #303018)
- revision 8699
* Tue Feb 12 2008 coolo@suse.de
- fix architectures on distupgrade
* Fri Feb  8 2008 coolo@suse.de
- fixes from trunk merged
* Fri Feb  1 2008 jkupec@suse.cz
- fixed renaming a repo to an existing one (bnc #228216)
- revision 8431
* Sun Jan 27 2008 coolo@suse.de
- fix changelog
* Thu Jan 24 2008 jkupec@suse.cz
- read .curlrc more robustly to obtain user-proxy (#330351)
- revision 8368
* Fri Jan 18 2008 coolo@suse.de
- always buildrequire openssl-devel
- replacing strange utf-8 chars in changelog
- revision 8317
* Thu Jan 17 2008 jkupec@suse.cz
- Saner NFS timeo default (#350309)
- revision 8314
* Thu Jan 17 2008 kkaempf@suse.de
- support 'patterns.pat' and 'patterns.pat.gz' to read all
  patterns in one go.
- rev 8309
* Tue Jan 15 2008 lslezak@suse.cz
- added RpmDb::removePubkey(), call it from
  KeyRing::Impl::deleteKey() - remove the GPG key from RPM when it
  is removed from the trusted keyring
- revision 8288
* Mon Jan 14 2008 schubi@suse.de
- Textchanges
- reduced logging in SAT-solver
- ordering solutions
- version 4.1.8
- revision 8276
* Thu Jan 10 2008 schubi@suse.de
- Enabled SAT solver via default. (removed ZYPP_SAT_SOLVER)
  ZYPP_RC_SOLVER=1 will enable the old RedCapet solver
- Revision 8255
- Version 4.1.7
* Wed Jan  2 2008 jkupec@suse.cz
- Pathname zypp::filesystem::expandlink(const Pathname &) added
- if the provided file is a symlink, expand it (#274651) (this
  probably won't work for schemes other than file/dir and cd/dvd)
- revision 8179
* Tue Dec 18 2007 aschnell@suse.de
- fixed password handling in URLs (bug #347273)
- revision 8118
* Mon Dec 17 2007 ma@suse.de
- Fixed default text locale detection not to use static variables. (#346872)
- version 4.1.6
- revision 8116
* Mon Dec 10 2007 ma@suse.de
- Log more details about zypp lock owner. (#294094)
- revision 8088
* Fri Dec  7 2007 ma@suse.de
- Remove runtime dependency for libboost_filesystem (#345773)
- version 4.1.5
- revision 8061
* Fri Nov 30 2007 schubi@suse.de
- Enable SAT solver via environment variable ZYPP_SAT_SOLVER.
  e.g.: ZYPP_SAT_SOLVER=1 zypper install foo
- version 4.1.4
- revision 7998
* Wed Nov 28 2007 aschnell@suse.de
- make IniParser more strict (bug #306697)
* Mon Nov 26 2007 ma@suse.de
- Fix missing packages in patch content list. (#340896)
- revision 7925
* Fri Nov 16 2007 coolo@suse.de
- fix build
* Wed Nov 14 2007 ma@suse.de
- Output date strings in UTF-8. (#339423)
- revision 7807
* Tue Nov 13 2007 schubi@suse.de
- fixes for new gcc
- version 4.1.3
- r7788
* Mon Nov  5 2007 ma@suse.de
- Don't mark failed patch scripts as installed. (#327523)
- version 4.1.2
- revision 7744
* Wed Oct 31 2007 dmueller@suse.de
- update rpmlint suppression
* Fri Oct 26 2007 aschnell@suse.de
- fixed retrieval of epoch from rpmdb (bug #246680)
* Thu Oct 25 2007 aschnell@suse.de
- allow non-existing "packages" file in susetags parser (bug
  [#309235])
* Fri Oct 12 2007 ma@suse.de
- SMBIOS DMI modalias matching added (#333152)
- revision 7494
* Sat Oct  6 2007 jkupec@suse.cz
- do not download the same file multiple times in one attach session
  (#307098), r7456
- special cdrom detection code for SCSI / Virtual CDROMs on iSeries
  removed - should be correctly detected by HAL now
  (#167629, #163971), r7452
- version 4.1.1
* Fri Oct  5 2007 aschnell@suse.de
- filter architecture in plaindir parser (bug #330791)
* Thu Oct  4 2007 ma@suse.de
- Throw constructing malformed checksums. (#189096)
- revision 7441
* Thu Oct  4 2007 mvidner@suse.cz
- Renamed templates back because proper qualification makes it work
  too.
- 4.1.0
* Thu Oct  4 2007 aschnell@suse.de
- only look for repositories in file ending ".repo" (bug #294779)
* Wed Oct  3 2007 mvidner@suse.cz
- Fixed compilation errors with GCC 4.3 by adding missing includes
  and renaming templates: MaxBits to MaxBitsT, Mask to MaskT,
  Compare<Edition> to CompareEd.
- r7426
* Mon Oct  1 2007 ma@suse.de
- Incorporated patch from Michael Matz to speedup cache reading.
- revision 7413
* Fri Sep 28 2007 schubi@suse.de
- Resolvertestcase:
  - log Repository info
  - set keep state in the testcase
  - handle vendor
- r 4707
* Thu Sep 27 2007 ma@suse.de
- Fixed pattern parser SEGV on broken pattern files. (#328546)
- revision 7402
* Wed Sep 26 2007 schubi@suse.de
- QueuItemRequire: Filter out all provider which have worser architecture,
  are NOT noarch and have not the same name as the requirement. The
  last one is needed for updating packages via patch/atoms.
  Bug 328081
- Revert changes of r 7340
- r 7386
* Tue Sep 25 2007 ma@suse.de
- Add missing '--install' parameter in desktop file. (#308640)
- version 4.0.0
- revision 7369
* Tue Sep 25 2007 jkupec@suse.cz
- release all attached media before attempting to eject (#293428)
- fixed parsing of --proxy-user parameter of .curlrc (#309139)
- revision 7352
- version 3.26.0
* Mon Sep 24 2007 dmacvicar@suse.de
- provide a way to retrieve the metadata path. Used for
  installation, which incorrectly creates a repository in
  cache without adding it first, so metadata path is not
  set and therefore it is not possible to setup a media
  verifier on installation. Part of fix for (#293428)
- 3.25.0
* Mon Sep 24 2007 schubi@suse.de
- If more than one resolvables provide a requirements and have different
  architecture take thatone with the best architecture. (Not regarding the
  name). Bug: Branching too much while an installation of a multi-arch-DVD
- r 7340
- version 3.24.8
* Fri Sep 21 2007 schubi@suse.de
- Checking the queue if an item will be deleted. If yes, the requirements
  are not needed anymore. Bug 326384
- version 3.24.7
- r 7329
* Thu Sep 20 2007 jkupec@suse.cz
- don't probe the repository type upon saving if disabled (#326769)
- version 3.24.6
- revision 7319
* Thu Sep 20 2007 ma@suse.de
- Avoid calling rpm repeatedly in case of an error. This is fault-prone,
  esp. if the error occurred executing the packages post-install script.
- version 3.24.5
- revision 7317
* Thu Sep 20 2007 ma@suse.de
- If a package is deselected by user, apply this soft lock to all
  available versions of this package.
- version 3.24.4
- revision 7316
* Wed Sep 19 2007 schubi@suse.de
- Update: Do not set an item to installation if there has been already set
  one for installation which has the same NVA. Bug  326286
- version 3.24.3
- r 7311
* Wed Sep 19 2007 ma@suse.de
- Enable package cache during commit. (#326249)
- revision 7309
* Tue Sep 18 2007 schubi@suse.de
- Do not regarding requirements for packages which will be deleted in the
  same solver run. Bug 310618
- r 7292
- version 3.24.2
* Mon Sep 17 2007 jkupec@suse.cz
- don't download filelists.xml.gz (#307105)
- version 3.24.1
- revision 7269
* Mon Sep 17 2007 ma@suse.de
- Improve estimated diskusage while there is no valid
  solver result. (#325617)
- revision 7266
* Mon Sep 17 2007 schubi@suse.de
-Bugfix in vendor change of a required resolvable (Correct error message)
  Bug 310455
- r 7262
* Mon Sep 17 2007 lslezak@suse.cz
- fixed DU parsing in inst-sys (#308659)
- revision 7256
* Fri Sep 14 2007 ma@suse.de
- Enable using patch and delta rpms. (#309124)
- version 3.24.0
- revision 7253
* Thu Sep 13 2007 ma@suse.de
- On update do not delete unmaintained non-SuSE packages.
- version 3.23.2
- revision 7239
* Thu Sep 13 2007 lslezak@suse.cz
- ZYppImpl::getPartitions() - don't return the current partitioning
  when the partitioning hasn't been set - fixes DU parsing in
  inst-sys (#308659)
* Thu Sep 13 2007 dmacvicar@suse.de
- Throw specific exceptions during commit (#308511)
- 3.23.1
* Wed Sep 12 2007 ma@suse.de
- Various disk space calculation fixes. Susetags, plaindir and rpmdb
  now provide more detailed disk usage information.
  Yum metadata don't, so we book the package size to '/'. (#308362)
- version 3.23.0
- revision 7225
* Wed Sep 12 2007 schubi@suse.de
- Regarding keep state while recycle old valid solver results. Bug 286889
- r 7209
* Wed Sep 12 2007 jkupec@suse.cz
- report 100%%%% progress on finishing RPM removal (bug #309431)
- revision 7200
* Tue Sep 11 2007 schubi@suse.de
- Update: rename language packages --> take that package which fits to the
  selected language Bug 308098
- r 7919
* Tue Sep 11 2007 dmacvicar@suse.de
- restore deltas and patch rpms from the cache (#309124)
- 3.22.8
* Tue Sep 11 2007 ma@suse.de
- Don't fail if a product is deleted multiple times (e.g. due to
  obsoletes and an explicit deleted request). (#308746)
- version 3.22.7
- revision 7184
* Tue Sep 11 2007 jkupec@suse.cz
- SYSCONFDIR variable added for modifying /etc
* Tue Sep 11 2007 schubi@suse.de
- uninstallable resolvable -->suggested solution: delete; Bug 308164
- r 7177
* Mon Sep 10 2007 schubi@suse.de
- new translations added
- r 7166
- version 3.22.6
* Mon Sep 10 2007 lslezak@suse.cz
- fixed disk usage counting of updated packages (#308362)
* Mon Sep 10 2007 schubi@suse.de
- Splitting packages: Take the package with the best
  architecture,edition ONLY; Bug 308591
- r 7160
* Mon Sep 10 2007 lslezak@suse.cz
- properly report fallback disk usage size (in kB instead of bytes)
  when disk usage is not known (YUM repos) (#308475)
* Fri Sep  7 2007 ma@suse.de
- Install a sample /etc/zypp.conf. (#306615)
- Fixed missing soversion symlink in package.
- version 3.22.5
- revision 7150
* Fri Sep  7 2007 schubi@suse.de
- RequirementIsMet: return true only if ALL Atoms are NOT incomplete; Bug
  308252
- r 7143
* Thu Sep  6 2007 schubi@suse.de
- Error: Select two candidate with the same name while update.
  Solution: If there is a candidate which is already selected for installation -->
  take thatone #308082
- r 7132
* Thu Sep  6 2007 ma@suse.de
- Work arround installed patterns providing an empty vendor string. (#307743)
- Let the solver treat vendor suse and opensuse as equivalent.
- version 3.22.4
* Thu Sep  6 2007 schubi@suse.de
- Checking item before evaluating the concerning vendor. bug #307941
- r 7119
* Thu Sep  6 2007 dmacvicar@suse.de
- Fix for bug #307163 - empty package descriptions
  a.k.a shared tag not 100%%%% implemented
- r 7117
- version 3.22.3
* Wed Sep  5 2007 schubi@suse.de
- logging "reverse" NEEDED_BY in the detail description of solver
  problems.
- improved error message if a requiremnt is not fulfilled Bug 307743
- Add "ignore" option to the solution if a requirement is not fulfilled
  Bug 304276
- revision 7113
* Wed Sep  5 2007 jkupec@suse.cz
- fixed the order of operands of susetags local metadata status
  computation which caused the YaST repositories to always get
  refreshed (part of bug #304310)
- revision 7107
- version 3.22.2
* Tue Sep  4 2007 schubi@suse.de
- comparing vendor with VendorAttr::equivalent
- revision 7103
* Mon Sep  3 2007 schwab@suse.de
- Use $RPM_OPT_FLAGS.
* Mon Sep  3 2007 ma@suse.de
- Reset transact bits when switching status from
  "update" to "protected" (#246976)
- version 3.22.1
- revision 7094
* Mon Sep  3 2007 schubi@suse.de
- new translations added
- rev 7083
* Fri Aug 31 2007 ma@suse.de
- Added ability to switch off use of patch and delta rpms via zypp.conf (#305864)
  [main]
  download.use_patchrpm = no
  download.use_deltarpm = no
- version 3.22.0
- revision 7069
* Fri Aug 31 2007 ma@suse.de
- On demand translate patch requirements into a list of atoms.
  Required by the UI to display packages acssociated with a patch.
  (#300612)
- version 3.21.1
- revision 7065
* Fri Aug 31 2007 kkaempf@suse.de
- enrich ResolverInfo with the reason if a user-initiated request
  fails (#304325, #306240)
- r 7051
* Thu Aug 30 2007 jkupec@suse.cz
- added missing implementation of LogControl::setLineFormater()
  (lslezak)
- version 3.21.0
- revision 7041
* Thu Aug 30 2007 jkupec@suse.cz
- enable changing url in requestMedia callback (#294481)
- revision 7037
* Thu Aug 30 2007 ma@suse.de
- Filter readonly mount points in DiskUsageCounter (#297405)
- revision 7030
* Thu Aug 30 2007 jkupec@suse.cz
- remember the cause of the RepoException when refreshing metadata
  (#301022)
- r7023
* Thu Aug 30 2007 ma@suse.de
- Safe fix for bug #299680.
- version 3.20.1
- revision 7026
* Thu Aug 30 2007 schubi@suse.de
- Bugfix: If a requirement has been fulfilled by more than one language
  resolvables only thatone will be taken which fits to the selected
  language.
- r 7018
* Thu Aug 30 2007 jkupec@suse.cz
- correct error code for media errors in MediaCurl::doGetFileCopy()
  affects only zypper error output, does not affect YaST
- r7013
* Wed Aug 29 2007 jkupec@suse.cz
- reverted blocking of requestMedia from r6271 (#301710)
- r6999
* Wed Aug 29 2007 kkaempf@suse.de
- prevent progress report in destructor (#299680)
- r6998
* Wed Aug 29 2007 jkupec@suse.cz
- treat non-filelists.xml <file> entries as file provides capabilities
  in YUM parser (#304701)
- r6992
* Wed Aug 29 2007 kkaempf@suse.de
- the media.1/media uniquely identifies a 'susetags' repo, not
  the content file (#304200)
* Wed Aug 29 2007 jkupec@suse.cz
- fixed locale dir (#304649)
- r6984
* Wed Aug 29 2007 kkaempf@suse.de
- don't treat normal package license as "license to confirm"
  (#305906)
* Wed Aug 29 2007 ma@suse.de
- Fixed fix for #293039. Segfault due to uninitialzed data.
- version 3.19.3
- revision 6980
* Wed Aug 29 2007 schubi@suse.de
- reduced too much verbosed ResolverContext logging; Bug 303971
- r 6977
* Wed Aug 29 2007 ma@suse.de
- Fixed PlainDir repositories to provide real disk usage data. For
  repomd and others that do not provide any detailed disk usage info,
  assume the packgage size is required below "/". Peviously they were
  treated as being empy.
- version 3.19.2
- revision 6972
* Wed Aug 29 2007 schubi@suse.de
- Add a new solver solution in the case of running in a timeout:
  ProblemSolutionDoubleTimeout.h
  [#]Bug 302496
- revision 6970
* Wed Aug 29 2007 dmacvicar@suse.de
- bug in fix for (#292986)
* Tue Aug 28 2007 dmacvicar@suse.de
- (#297001) - libzypp: can't skip broken packages
- re enable importing zypp keyring from rpm.(#302379)
- 3.19.1
* Tue Aug 28 2007 kkaempf@suse.de
- rename ResolvableQuery::iterateResolvablesByKindsAndStrings
  to ResolvableQuery::iterateResolvablesByKindsAndStringsAndRepos
  in order to support query-by-repo (#305384)
- fix iterateResolvablesByKindsAndStringsAndRepos to take any
  number of kinds, names, or repos (#305347)
- remove ResolvableQuery::iterateResolvablesByKind, not needed
- version 3.19.0
- rev 6935
* Tue Aug 28 2007 dmacvicar@suse.de
- real fix for reading signature ids. (#390535).
- delete metadata when removing repo (#301037).
* Mon Aug 27 2007 dmacvicar@suse.de
- following behaviour for setPartitions
  - if they are not set, they are detected
  - if they are set, that value is used.
  - if value set or detected is empty, all disk usage
    information is read. Otherwise just values in those
    mount points.
    Should work for installation as long as detectPartitions
    is empty at installation.(#293039)
* Mon Aug 27 2007 kkaempf@suse.de
- Add ZConfig::overrideSystemArchitecture() to override zypp arch
  from external, e.g. for the testcases
- Honor ZYPP_CONF environment variable to override the buit-in
  /etc/zypp/zypp.conf
- Check architecture at handout() to prevent NULL ptr reference.
- Bug 301286
- rev 6908
* Mon Aug 27 2007 schubi@suse.de
-The solver generate an establish call for all
  resolvables which has filesystemcaps if there is not a valid result from a
  former solver run available. This covers:
  * Initial solver run
  * Changing of filesystem whithin a workflow, cause the solver results will
  be reset if the filesystem dependencies have been changed
  Bug 271912
- r 6901
* Sun Aug 26 2007 kkaempf@suse.de
- pass location to plaindir package (#303751)
- Add name of file in question to checksum/signature related
  exceptions.
- pass basename of file to verifyFileSignatureWorkflow (instead of
  empty string).
- filter out incompatible architectures when parsing sustags
  repos (first half of #301286)
- r 6882
* Fri Aug 24 2007 dmacvicar@suse.de
- don't run source migration if yast is running in
  intsys mode (#297136)
- signature and checksum verification fixes. Still pending
  problem ZYpp getting no output from gpg when running from zypper.
  (#302059)
* Thu Aug 23 2007 schubi@suse.de
- Do not strip resolvables which have the same name but different kind
  (ResolverInfo*)
- Flag info NEEDEDBY correctly if it will be used by freshen/supplement
- r 6830
* Wed Aug 22 2007 mvidner@suse.cz
- Do not use "a-z" in regexes. Fixes "Invalid Url scheme 'http'" in
  the Estonian locale (#302525).
* Wed Aug 22 2007 aschnell@suse.de
- added remembering of exception history at various places
* Wed Aug 22 2007 schubi@suse.de
- Bugfixes concerning vendor handling:
- first bug:
  Installed A-1.0(vendor SuSE)
  Available A-2.0(other vendor)
  A will not be regarded as "unmaintained". So it will not be deleted.
- second bug:
  A need B-2.0. B-1.0 is installed but has another vendor. Report a
  proper errmessage.
- Testcase : solution-tests/vendor-test.xml
- r 6812
- 3.18.4
* Tue Aug 21 2007 dmacvicar@suse.de
- ignore HASH key for download (#300982)
* Tue Aug 21 2007 schubi@suse.de
- Added explicitly_requested as parameter in ResolverContext::Uninstall
  Bug 299819
- revision 6794
* Tue Aug 21 2007 dmacvicar@suse.de
- If no mount information is available, parse all DU entries.
- read only hack mode for migrate-sources. We actually do add
  repositories with it, but no harm. (#292986)
- fix some typos in exceptions (#301331)
- 3.18.3
* Mon Aug 20 2007 schubi@suse.de
- Do not regard explicit request in order to recognize updated packages
  correctly. Bug 301676
- Updated translations
- r 6766
- 3.18.2
* Mon Aug 20 2007 mvidner@suse.cz
- package-manager script: Call /sbin/yast2 with full path because of
  gnomesu (#269873).
* Mon Aug 20 2007 dmacvicar@suse.de
- add support for the HASH key. (#300982)
- Use ContentFileParser in Downloader (instead of implementing
  the parser again, it has a reason, Downloader was written first)
- update testcases and data to cover the new HASH key
- 3.18.1
* Mon Aug 20 2007 kkaempf@suse.de
- unify query API for kind and name, summary, description
  (incomplete)
- rev 6761, version 3.18.0
* Fri Aug 17 2007 kkaempf@suse.de
- add iterateResolvablesByKindsAndName
- rev 6735, version 3.17.13
* Fri Aug 17 2007 kkaempf@suse.de
- rename ResolvableQuery::queryByName to iterateResolvablesByName
- fix reading of kind and repository in ResolvableQuery
- add reverse lookups in CacheTypes
- add iterateResolvablesByKind
- rev 6733
* Fri Aug 17 2007 schubi@suse.de
- shorten solver error messages Bug 259894
- rev 6723
* Thu Aug 16 2007 kkaempf@suse.de
- fix ResolvableQuery::query(), add ResolvableQuery::queryByName()
  install zypp/cache header files.
- rev 6719, version 3.16.13
* Thu Aug 16 2007 kkaempf@suse.de
- discard pattern files with incompatbile architecture, both
  for download and for parsing. (#298716)
- rev 6711
* Thu Aug 16 2007 kkaempf@suse.de
- run sqlite asynchronously and add sql index files where
  appropriate, gives 6x performance on certain operations.
  Bumping cache schema version to 1004.
  (#300998)
- rev 6710
* Thu Aug 16 2007 kkaempf@suse.de
- fix String::endsWith (#301038)
- rev 6709
* Thu Aug 16 2007 schubi@suse.de
- added an _explicitly_requested in QueueItemConflict ( as already in
  QueueItemEstablish, QueueItemInstall, QueueItemUninstall ) in order to
  remove the conflicting item without an error message. Bug 299819
- rev 6699
* Thu Aug 16 2007 jkupec@suse.cz
- forgot to set default refresh policy in checkIfToRefreshMetadata
- repo.refresh.delay default set to 10 minutes
- 6693
* Wed Aug 15 2007 schubi@suse.de
- Bugfix while regarding correct vendor in update
- r6677
- version 3.15.0
* Wed Aug 15 2007 jkupec@suse.cz
- repo.refresh.delay=<minutes> (ZConfig, "main" section) support
  added to delay next check & refresh until the specified number of
  minutes has passed from the last check or refresh (FATE #301991).
  Revisions: 6654, 6656, 6666, and 6667.
- filesystem::touch(Pathname) added (r6666)
- RepoManager::touchIndexFile(RepoInfo) added
- RepoManager::checkIfToRefreshMetadata(RepoInfo,Url,policy):
  decision to do the refresh moved to this public method.
- r6667
* Wed Aug 15 2007 schubi@suse.de
- generate a resolver problem if addRequires does not find a resovable
  [#299486]
- rev 6660
* Tue Aug 14 2007 schubi@suse.de
- Prioritized delete request by the user BEFORE delete requests due
  missing dependencies or conflicting dependencies. Bug 298322
- rev 6640
* Fri Aug 10 2007 jkupec@suse.cz
- support also "Plaindir" as valid repo type name (#298622)
- revision 6616
- version 3.14.0
* Fri Aug 10 2007 dmacvicar@suse.de
- fix segfault in Progress reporting
- progress report use name instead of alias (#298035)
- repoinfo returns alias if name is empty
* Fri Aug 10 2007 dmacvicar@suse.de
- merge patch by dmueller to get rid of boost-regex
* Fri Aug 10 2007 dmacvicar@suse.de
- dont create a second CacheStore in the same scope, will lock...
  [#297627]
* Thu Aug  9 2007 jkupec@suse.cz
- fixed some RepoManager exception docs & history
- r6558
* Thu Aug  9 2007 dmacvicar@suse.de
- feature #302135: Graceful update of 3rd party packages
  Automatic upgrading only sees packages from same vendor
  This allows not needed to have those locked.
- Add persistent locks file which allow wildcards. Users
  can lock certain packages adding lines like "kde* < 3.5"
- add applyLocks() to apply persistent locks before solving
* Thu Aug  9 2007 schubi@suse.de
-  recognize changes in the pool (e.g. changing /etc/sysconfig/storage
  [#271912] wq
- Added locking resolvables in the testcases
- rev 6544
* Wed Aug  8 2007 dmacvicar@suse.de
- add migrate-sources to %%%%post (#292986)
- 3.13.15
* Wed Aug  8 2007 jkupec@suse.cz
- fixed bug with using wrong files from raw metadata cache
  (bug #297611) (duncanmv) (r6501, already released in 3.13.14)
* Wed Aug  8 2007 schubi@suse.de
- fix in "ignore conflicts" if the conflict has been caused by an obsolete
  Bug# 297795
- r 6517
* Tue Aug  7 2007 dmacvicar@suse.de
- implement susetags support for compressed metadata
  and testcases. (feature #301916)
- implement disk usage in cache. For installation requires
  some changes in YaST to setup the ZYpp getPartitions()
  before repos are cached. (bug #293039)
- added testcases for diskusage
- 3.13.14
* Mon Aug  6 2007 jkupec@suse.cz
- fixed YUM parser to properly create source packages
- disabled reading of filelists.xml.gz by default (the data are
  currently not stored anyway)
- revision 6481
- version 3.13.13
* Sat Aug  4 2007 ma@suse.de
- Don't download unwanted translation files (#293740).
- revision 6470
* Fri Aug  3 2007 ma@suse.de
- Fix susetags repo to parse dikusage data (#293039)
- revision 6467
- version 3.13.12
* Fri Aug  3 2007 ma@suse.de
- Add product attribute 'type' (aka 'category' which is now
  deprecated). Adapted sustags and yum parsers to parse and
  provide this value.
- revision 6464
- version 3.13.11
* Fri Aug  3 2007 dmacvicar@suse.de
- fix modalias rel column number
- version 3.13.10
* Fri Aug  3 2007 dmacvicar@suse.de
- Implemented option repo.add.probe to allow probing
  the added repositories
- version 3.13.9
* Fri Aug  3 2007 schubi@suse.de
- Fixed detection of renamed packages while update.
- Added new translations
- rev 6445
* Fri Aug  3 2007 ma@suse.de
- Speed up retrieving MediaNr attribute, as it slows down install
  order calculation. (#297173)
- revision 6442
* Fri Aug  3 2007 dmacvicar@suse.de
- Fixed cache schema upgrade
* Fri Aug  3 2007 ma@suse.de
- Fixed pattern includes and extends attributes.
- revision 6431
- version 3.13.8
* Fri Aug  3 2007 schubi@suse.de
- API for retrieving additional dependencies" solver/detail/Resolver.h
- Handle additional dependencies in the testcases
- Handle system and language dependencies in the testcases correctly.
- r 6418
* Thu Aug  2 2007 ma@suse.de
- Indicate changed pool content if /etc/sysconfig/storage USED_FS_LIST
  has changed. Resolver must discard any cached filesystem dependencies.
  (required for #271912)
- revision 6404
* Thu Aug  2 2007 ma@suse.de
- Indicate changed pool content to the resolver. (required for #271912)
- revision 6398
- version 3.13.7
* Thu Aug  2 2007 schubi@suse.de
- speedup error handling. Do not log ResolveInfo anymore. Set limit of 20
  problems. Bug 280387
- r 6378
- version 3.13.6
* Wed Aug  1 2007 ma@suse.de
- Added interface to install source packages via zypper.
- revision 6373
- version 3.13.5
* Tue Jul 31 2007 ma@suse.de
- Added package attributes Package::sourcePkgName and
  Package::sourcePkgEdition. Name and edition of the source
  rpm this package was built from.
- Added ZYpp::installSrcPackage to install a single source package.
- revision 6353
- version 3.13.4
* Tue Jul 31 2007 ma@suse.de
- Temorary files and directories created by makeSibling use the
  same protection as the original.
- revision 6344
- version 3.13.3
* Tue Jul 31 2007 schubi@suse.de
- Removed keepExtras from resolvePool. This will be handled
  in the solver internally now. #294727
- Checking if item really exists (#295544; ResolverInfoContainer.cc)
- revision 6317
- version 3.13.2
* Mon Jul 30 2007 ma@suse.de
- Remove tribool from RepoInfo's interface.
- revision 6301
- version 3.13.1
* Mon Jul 30 2007 ma@suse.de
- Fixed wrong media number reported by script, message and patch.
- Fixed script API to provide the scripts location on media (if not
  inlined).
- Introduced ScripProvider to make a script available on the local
  disk.
- revision 6288
- version 3.13.0
* Fri Jul 27 2007 jkupec@suse.cz
- don't request media chage if the media is not changeable (like
  e.g. http)
- revision 6271
- version 3.12.1
* Fri Jul 27 2007 dmacvicar@suse.de
- progress ticks for clean cache
- ZConfig: remove default from names.
- re enable reading cache callbacks
- ini parser without boost::regexp
  patch by dmueller (#152447)
* Fri Jul 27 2007 ma@suse.de
- Fixed package to provide the location media number. (#294496)
- revision 6263
* Fri Jul 27 2007 jkupec@suse.cz
- RepoFileReader - ignore empty url keys (baseurl, mirrorlist,
  gpgkey) instead of throwing bad url exception
- revision 6259
* Thu Jul 26 2007 kkaempf@suse.de
- Make clearing of extra dependencies/conflicts configurable when
  resolvePool(). Leave the default as before (clear extras).
  Bug # 294727
- revision 6233
- version 3.12.0
* Thu Jul 26 2007 dmacvicar@suse.de
- /var/lib/zypp/cache -> /var/cache/zypp
  (#292419)
- ini parser without boost::regexp, patch by dmueller
  (#152447)
* Wed Jul 25 2007 ma@suse.de
- Make temp directory configurable  via environment
  variable ZYPPTMPDIR.
- revision 6202
- version 3.11.11
* Tue Jul 24 2007 ma@suse.de
- Fixed bug in smart pointer comparison.
* Mon Jul 23 2007 ma@suse.de
- Fix failing rename of metadata download directories across
  filesystem boundaries.
* Fri Jul 20 2007 ma@suse.de
- Fixed malicious gettext include.
- Make ZConfig a singleton.
- revision 6123
* Thu Jul 19 2007 ma@suse.de
- Fixed repo::provideFile to set a deleter for downloaded files
  (#293004).
- revision 6094
- version 3.11.10
* Thu Jul 19 2007 ma@suse.de
- Query ByRepository now takes as well an alias.
* Wed Jul 18 2007 dmacvicar@suse.de
- fix retrieval of container attributes in cache
  (#292698)
* Wed Jul 18 2007 ma@suse.de
- Port zypp-query-pool (#292404)
- revision 6069
- version 3.11.9
* Wed Jul 18 2007 schubi@suse.de
- added new calls in Resolver.h: addRequire,addConflict
* Wed Jul 18 2007 ma@suse.de
- Fixed IniParser to allow '=' in values (#292669)
- revision 6063
* Wed Jul 18 2007 dmacvicar@suse.de
- allow / in alias (#292628)
* Wed Jul 18 2007 ma@suse.de
- Fixed repo::provideFile to throw on error.
- Fixed ResolvableQuery to use 0 as default for non existing
  numerical values.
- revision 6058
* Tue Jul 17 2007 ma@suse.de
- Fixed OnMediLocation to use safe defaults. Added setLocaltion and
  additional ctor for convenience.
- revision 6047
* Tue Jul 17 2007 schubi@suse.de
- Evalute update canditate:
  Take canditates only which are really installable. Bug 292077
  r 6034
* Mon Jul 16 2007 jkupec@suse.cz
- fixed some tribool bugs in RepoInfo
- revision 6022
* Mon Jul 16 2007 dmacvicar@suse.de
- fix reading of non existant repo
- r6018
- first submission to stable
- fix keywords parsing in susetags parser
- version 3.11.8
* Wed Jul 11 2007 jkupec@suse.cz
- make resolvable query complete exceptionless with the database
- test that packages have some attributes
- disable progress adaptor for now
- revision 5977
- version 3.11.7
* Wed Jul 11 2007 ma@suse.de
- fixed unresolved symbols
- revision 5972
- version 3.11.6
* Wed Jul 11 2007 ma@suse.de
- fixed TranslatedText creating unwanted entries.
- fixed capability processing
- revision 5964
- version 3.11.5
* Tue Jul 10 2007 jkupec@suse.cz
- MediaSetAccess::release() added
- Use attachDesiredMedia in MediaProducts
- Progress reporting improved
- revision 5959
- version 3.11.4
* Tue Jul 10 2007 ma@suse.de
- fixed parsing translated texts.
- added source packages.
- revision 5947
- version 3.11.3
* Tue Jul 10 2007 jkupec@suse.cz
- repo callbacks fixed
- Fixed YUM parser progress reporting
- Added CombinedProgressData
- make RepoImpl::resolvables() load lazy
- MediaProducts added for scanning products file
- Implement cache schema versioning and automatic invalidation of
  cache when schema changes
- revision 5942
- version 3.11.2
* Fri Jul  6 2007 ma@suse.de
- Propagate pools repository_iterator to the UI
- revision 5911
- version 3.11.1
* Thu Jul  5 2007 ma@suse.de
- Package::location is now returns an OnMediaLocation
- archivesize() renamed to downloadSize()
- Allow to iterate all Repositories that contribute
  Resolvables to the Pool.
- MediaSetAccess::provideDir added
- remove useless url check
- add old-api-style wrapper
- Add MediaProducts class
- revision 5892
- version 3.11.0
* Thu Jul  5 2007 schubi@suse.de
- function isInstalledBy/installs
  Added an initial installation flag which shows if the item has been
  triggered for installation, or the dependency is already satisfied.
- Revision 5884
- Version 3.4.0
* Tue Jul  3 2007 jkupec@suse.cz
- removed unused %%%%{prefix}/lib/zypp from %%%%files in spec file
- revision 5870
* Tue Jul  3 2007 jkupec@suse.cz
- Old API (SourceManager, metadata parsers) dropped in favor of the
  new refactored ones (RepoManager, RepoParser(s), cache subtree,
  repo subtree).
- Some new API improvements.
- revision 5868
- version 3.10.0 (bumped minor to 10 to indicate refactoring branch)
* Fri Jun 22 2007 schubi@suse.de
- New API calls which provides more information about one
  resolvable after a solverrun:
  isInstalledBy (const PoolItem_Ref item);
  installs (const PoolItem_Ref item);
- Revision 5835
* Thu Jun 21 2007 adrian@suse.de
- fix changelog entry order
* Wed Jun 20 2007 schubi@suse.de
- Ignore conflicting items which are uninstallable
- Create a "needed by" info if a requirement is still fulfilled.
- Allow only one needed_by and needed_by_capability in QueueItemInstall
- Added capability and type (REQUIRE, RECOMMEND,....) to
  ResolverInfoNeededBy
- Evaluate ResolverInfoNeededBy for more information in the error
  messages
- Enlarge detail description in the error messages
- Revision 5807
* Tue Jun 19 2007 ma@suse.de
- Fixes for gcc-4.2
- revision 5786
- version 3.3.1
* Mon Jun 18 2007 mvidner@suse.cz
- fixed so versioning from libtool to cmake
- 3.3.0
* Mon Jun 18 2007 dmacvicar@suse.de
- Use gpg2 instead of gpg for keyring and make
  the package depend on it (#284211)
* Mon Jun 11 2007 schubi@suse.de
- Required kmp packges FOR EACH installed/to_be_installed kernel will be installed.
  New dependency "packageand(foo:bar)" which provides an AND dependency by
  injecting a supplement/freshen.
  e.G. package novell-cluster-services-kmp-smp
  supplements: packageand(kernel-smp:novell-cluster-services-kmp)
  Bug 255011
- Dont check for architecture changes in atoms (#266178)
- Revision 5720
* Wed May 23 2007 ma@suse.de
- Fixed package-manager script (#275847)
- revision 5614
* Wed May 23 2007 schubi@suse.de
- fixed cmake
- version 3.2.2
* Wed May 23 2007 schubi@suse.de
- Reduced logging in order to speedup solving Bug 275100
- revision 5603
- version 3.2.1
* Tue May 15 2007 ma@suse.de
- Fix excess calls to releaseFile. (#274357)
- revision 5545
* Wed May  9 2007 dmacvicar@suse.de
- Fix importing keys into rpm. (#270125)
- r5527
* Wed Apr 18 2007 ma@suse.de
- Support filesystem dependencies to add needed filesystem RPMs
  automatically (Fate 301966).
- revision 5404
- version 3.2.0
* Mon Apr 16 2007 jkupec@suse.cz
- avoiding attaching media where not needed (#263207)
- r5381
* Fri Apr 13 2007 dmacvicar@suse.de
- fix FileCap with attributes
- r5376
* Thu Apr 12 2007 ma@suse.de
- Fixed computation of install order. Take requirements of
  an installed packages uninstall scripts into account, if
  the package is updated. (#258682)
- revision 5349
- version 3.1.1
* Wed Apr 11 2007 ma@suse.de
- Parse and provide package keywords. (Fate 120368)
- revision 5338
- version 3.1.0
* Thu Apr  5 2007 schubi@suse.de
- Upgrade: Do NOT delete packages which have unresolved dependencies -->
  Ask the user. Bug 258322
- revision 5305
- version 3.0.3
* Wed Apr  4 2007 ma@suse.de
- Fix restoring of Sources id root prefix is used. (#238165)
- revision 5299
- version 3.0.2
* Wed Apr  4 2007 jkupec@suse.cz
- MediaManager::attachDesiredMedia() added to support multiple
  (CD/DVD) drives (fate #3974)
- r5296
* Wed Mar 14 2007 schubi@suse.de
- If there is no valid solver result and NOT all resolvables ( other
  architecture) has been regarded, let the user decide making a new
  solver run with ALL available resolvables. Bug 223440
- reducing logging (error -> debug)  bug 252921
- Revision 5219
* Fri Mar  9 2007 ma@suse.de
- Allow configuration of trusted vendors via
  /var/lib/zypp/db/trustedVendors. (#186636)
- revision 5194
- version 3.0.1
* Wed Mar  7 2007 dmacvicar@suse.de
- libzypp-devel -> libzypp requirement is not versioned
  (#251086)
- r5181
* Tue Mar  6 2007 schubi@suse.de
- Using already existing valid solver results for further solver runs.
  (partiell solving)
- r5169
* Fri Mar  2 2007 dmacvicar@suse.de
- fix link order
- r5165
* Tue Feb 27 2007 dmacvicar@suse.de
- merging from 10.2 / SP1
- #247459 ftp probing
  denied == dont exists in ftp
- r5124
* Tue Feb 27 2007 schubi@suse.de
- Merging solver related stuff from SuSE-Linux-10_2-Branch ( till r5111):
- Simultaneouqusly establishing of items which are conflicting eachother is
  useless. So only one will be established. Fixed in QueueItemInstall.cc
  Bug 243595
- Added new upgrade options to fine tune version and patch handling.
  (F301990)
- The context of establishPool will be stored in Resolver and will be
  regarded for the next solver run everytime. So it will be not reset by
  any solver run anymore.
  bug 191810 ( A broken patch will not be installed again)
* Fri Feb 23 2007 jkupec@suse.cz
- adding sotf,timeo=X nfs mount options by default (#235211)
- r5093
* Fri Feb 23 2007 jkupec@suse.cz
- support for HTTP authentication prompt added (#190609)
- fixed problem with empty path in URL
  in MediaCurl::doGetFileCopy()
- r5085
* Mon Feb 12 2007 jkupec@suse.cz
- Merged revisions 4926-4993,4995,4998-5006 via svnmerge from
  SuSE-Linux-10_2-Branch
- verifySystem: Regarding patterns too. Bug 239750 (schubi)
- verifySystem: The result will be set to APPL_HIGH, so it will be not
  reset by a second "normal" solver run. #239281 (schubi)
- yast2 reports invalid URL as 'unknown source type'
  (#209961) (dmacvicar)
- Added freshen language dependency in supplemements too if there is no
  entry in supplements.
  [#240617];IPA fonts are not installed even if select Japanese
  language (schubi)
- Setting allowed authentication methods to "basic,digest" if none
  provided in URL (#243006) (jkupec)
- Stopping after 50 valid solver results. Anymore would be useless. Bug
  243595 (schubi)
- r 5007
* Mon Feb 12 2007 mvidner@suse.cz
- package-manager: use a generic su script from XDG (#235303, #244442)
* Fri Feb  9 2007 jkupec@suse.cz
- Setting allowed authentication methods to "basic,digest" if none
  provided in URL (#243006)
- fixed gettext and rpath problems in configure.ac and Makefile.cvs
  (mvidner)
- r4999
* Wed Feb  7 2007 jkupec@suse.cz
- MediaCurlException::dumpOn() adjusted for ncurses dialogue
  (#222602)
- 4984
* Mon Jan 29 2007 dmacvicar@suse.de
- Merged revisions 4907-4926 from SuSE-Linux-10_2-Branch
- update packages: changing architecture is only valid while an
  system update and NOT while an update via a patch. Last fix does
  not fit for every case.
  Bug 230685
- Patch has selected not the concerning package for update but
  a package which has provided the required dependencies too.
  Algorithmus: If there are exactly two providers which differ in architecture
  prefer the better arch.
  Fix: Regarding NVRA too. ( only if equal )
  Bug 238284
- Download only English and Local translation
  (#208457)
- Added solver parameter:
  tryAllPossibilities: regarding every solver branch ( not only
    branches with e.G. best architectures
  preferHighestVersion: Prefer solver results which have a higher
    version number.
  Bug #238087
- update packages: changing architecture is only valid while an
  system update and NOT while an update via a patch.
  Bug 230685 - x86_64 MozillaFirefox binaries in security update
  repository
  Fix of version 2.11.2 has not worked if the first founded item
  had had another architecture.
- r4927
* Wed Jan 24 2007 lslezak@suse.cz
- added ZYpp::getPartitions() - return the partitinoning
* Wed Jan 24 2007 dmacvicar@suse.de
- Merged revisions 4705-4906 via svnmerge from SuSE-Linux-10_2-Branch
- Corrupt download cannot be skipped
  (#217425 and #224216)
- Enable package read ahead/caching in commit per default to reduce
  interactive media changes. If the environment variable
  ZYPP_COMMIT_NO_PACKAGE_CACHE is set, caching will be disabled. (F100182)
- added parameter not to reset resolver results while calling
  freshen pool Bug: 235761
- Prepare package read ahead/caching of packages in commit. Adatped the
  workflow. Caching details are now hidden inside CommitPackageCache.
  The current implementation still performs no read ahead. (for F100182)
- Skip invalid or broken rpm database entries. (#231211)
- verifySystem: check if the solution is valid after calling freshenPool()
  Bug: 235761
- Added own call for Resolver::verifySystem with additional
  hardware/language check in order to keep binary compatibility
  Fate #301224
- Rpm requires additional quoting of special chars in filenames.
  (#233967)
- Resolver::verifySystem checks for new hardware now by calling
  freshenPool. This is configureable. Fate #301224
- merged texts from proofread
- Don't consider patch/delta rpms if package architecture changes.
  (#231254)
- update packages: changing architecture is only valid while an
  system update and NOT while an update via a patch.
  Bug 230685 - x86_64 MozillaFirefox binaries in security update repository
- verifySystem: Do only regard items which will be on the system after the
  commit. Fate 301178
- feature #301369
  Import listed GPG Keys from an trusted installation source
- fix return call in new xml parser
- Enable system resolvables in Helix parser (Revision 4787)
- deptestomatic:
  Resetting transaction with the correct call;
  bugfix; Added kind in keep state (Revision 4788)
- Wrong behaviour in soft install/uninstall. --> Setting Transact with
  soft (Revision 4789)
- New call added: maySetToBeUninstalledSoft (Revision 4789)
  Both are only functions for the solver (Revision 4789)
- Resetting "by causer" in order to distinguish from state
  "keep by user". ( function setLock in order to remove lock)
  (Revision 4789)
- Better fix for Bug 217574: Checking if the resolveable CAN be deleted soft
  in QueueItemUninstall.cc (Revision 4790)
- Regarding "keep state by user". So avoiding "reselecting" by
  other requirements.
  Give a corresponding problem solution if a resolvable satisfy
  a dependency, but has been set to keep by the user.
  Bug : 222531 (Revision 4791)
- Allow to disable autoprotection of foreign vendor items. Required
  in zmd-backend. (F301735).
- use sqlite-zmd if using > 10.2 in spec. Use the one available
  durin compile.
- Item could has already been selected to soft uninstall (e.G. remove
  pattern which recommend this item ). Do not throw an exception anymore.
  bug#225278
- Added syscontent::Reader: Parse serialized set of ResObjects.
  (for F300729)
- If there has already been selected another item by the solver (e.g. from
  another source) we will take thatone in order to avoid parallel
  installation and there concerning error messages.
  Bug 224698
- In order to handle conflicting resolvable we try to update the
  conflicting item. While evaluating these canditates an already selected
  candidate will not be regarded. So it could be that an older package
  will be selected for update although a newer has already been selected. Revision 4765
- Conflicting items: The resolvable will be obsoleted by another. So it is useless finding an
  update candidate and evaluate additional branches.
- r4907
* Mon Dec  4 2006 mt@suse.de
- Improved realpath() wrapper in media handler class (#222521).
- revision 4758
* Thu Nov 30 2006 ma@suse.de
- version 3.0.0 (2.x.x now in SuSE-Linux-10_2-Branch)
- revision 4713
* Wed Nov 29 2006 dmacvicar@suse.de
- use sqlite-zmd package for the non yet shipped zypp2/ stuff
  because backend uses this sqlite and it is no fun to
  install one and the other to develop (as the -devel packages)
  conflict.
- add cmake support for building zypp/ lib.
  TODO: soinfo, compile testcases, devel, zypp2,docs
  find rpm, curl and others.
- dont serialize interactive, as it is
  calculated now.
  (it was already fixed as we don't reimplement
  the method, but we still serialized, parsed)
- r4709
* Tue Nov 28 2006 ma@suse.de
- fixed Patch::interactive to return true as well, if the patch
  itself has a licence. (#224192)
- revision 4702
- version 2.9.2
* Tue Nov 28 2006 mt@suse.de
- Added search for /sbin/vol_id tool - that is in /lib/udev/vol_id
  on the installation image (#213852).
- revision 4700
* Tue Nov 28 2006 schubi@suse.de
- Avoid duplicate pool entries; Bug 223750; second part of the fix
- r4698
- Version 2.9.1
* Mon Nov 27 2006 schubi@suse.de
- Pool has multi instances of an item in the pool. Reduced this error
  to items which are identically at least. #217574 and #223750
- r4695
* Mon Nov 27 2006 dmacvicar@suse.de
- replace spaces to underscores in product names
- 2.8.7
- r4688
* Mon Nov 27 2006 dmacvicar@suse.de
- Mark some strings for translation (#219783 need it)
- r4682
* Mon Nov 27 2006 mt@suse.de
- Added translations marks to hal, url and mutex exceptions (#23771)
- revision 4680
* Wed Nov 22 2006 dmacvicar@suse.de
- don't make libzypp-devel depend on sqlite-devel as
  headers from zypp2 are not installed yet
- r4663
* Wed Nov 22 2006 ma@suse.de
- Return an error if fork failed. (#204807)
- Make Script execution abortable by user request. (#212949, F100233)
- revision 4660
- version 2.8.6
* Tue Nov 21 2006 mvidner@suse.cz
- Added package-manager wrapper script, with icon and .desktop (#222757).
  (Used by gnome-main-menu)
- version 2.8.5
- r4640
* Tue Nov 21 2006 mt@suse.de
- Fixed target/hal - one more dbus_connection_close found (#216035)
- revision 4636
- version 2.8.4
* Mon Nov 20 2006 schubi@suse.de
- translation added
  rev 4630
  version 2.8.3
* Mon Nov 20 2006 ma@suse.de
- Process obsoletes when installing non-package objects. (#217352)
- revision 4621
- version 2.8.2
* Fri Nov 17 2006 mt@suse.de
- Implemented volume device check using /sbin/vol_id (#213852).
- Revision 4619
* Fri Nov 17 2006 schubi@suse.de
- new translation added
* Fri Nov 17 2006 mt@suse.de
- Implemented an reuse of already existing foreign CD/DVD mount points
  (e.g. automounted) - depends on REUSE_FOREIGN_MOUNTS flag (#220206).
- Added a fallback check of the volume.mount_point HAL property to
  isAutoMountedMedia(); info.hal_mount.created_mount_point seems
  to be not avaliable in newer HAL versions (on 10.2).
- Revision 4615
- Version 2.8.1
* Thu Nov 16 2006 ma@suse.de
- removed unused methods from Patch and PatchImplIf. Provided
  reasonable default implementation for Patch::interactive.
  (#221476).
- revision 4610
- Version 2.8.0
* Thu Nov 16 2006 dmacvicar@suse.de
- Handle media eject failures (#216545)
- r4606
* Wed Nov 15 2006 ma@suse.de
- Reimplemented RpmDb::checkPackage using librpm API instead
  of parsing "rpm --checksig" output. (#163202)
- Version 2.7.4
- revision 4600
* Wed Nov 15 2006 schubi@suse.de
- NEW behaviour of the solver:
  Obsolete virtual provides. E.G.:
  Installed:
  - ----------
  Name:           test-1.0-0
  Name:           moretest-1.0-0
  Provides:       test
  To be installed
  - -----------------
  Name:           nomoretest-1.0-0
  Obsoletes:      test
  Result
  - -------
  test-1.0-0 AND  moretest-1.0-0 will be deleted. In former versions only
  test-1.0-0 had been deleted. Bug 220999
- Translations added
  Version 2.7.3
  rev 4593
* Tue Nov 14 2006 schubi@suse.de
- Bugfix in generating solver testcases:
  - added kind of capabilities in description file
  - removed unneded channel from uninstall in command file
* Mon Nov 13 2006 mt@suse.de
- Try to call /bin/eject utility if the eject-ioctl fails.
- r4568
* Mon Nov 13 2006 dmacvicar@suse.de
- ignore empty capabilities
- r4565
* Fri Nov 10 2006 dmacvicar@suse.de
- make progress strings translatable (#219783)
- r4556
* Tue Nov  7 2006 schubi@suse.de
-  While deleting a selection all concerning recommended
  packages will be deleted too.
  BUT those packages should not be deleted which have been
  set to KEEP by the user. bug 217574
  rev 4526
  VERSION: 2.7.2
* Tue Nov  7 2006 schubi@suse.de
- Makefile in zypp2 fixed
  Revision 4520
* Tue Nov  7 2006 schubi@suse.de
- Translations added
  Revision 4514
  VERSION: 2.7.1
* Mon Nov  6 2006 dmacvicar@suse.de
- Make the parser more strict, rejecting broken sources
  but showing the error line.
  Last fix making the parser relax would break multitag
  descriptions with empty lines, now we check dependencies
  at a higher level. (reference #160607)
- r4501
* Fri Nov  3 2006 schubi@suse.de
- New problem solution added: Unlock ALL resovables in order to speed up
  problem solution. Bug 206453
* Fri Nov  3 2006 schubi@suse.de
- Translations added
* Thu Nov  2 2006 mt@suse.de
- Fixed target/hal - removed dbus_connection_close calls, because
  the connections are shared; unref the ref-counted handle only.
  (#216035)
- r4442
* Thu Nov  2 2006 dmacvicar@suse.de
- skipping unreachable packages won't work
  (#215445)
- r4468
* Wed Oct 25 2006 dmacvicar@suse.de
- (#213793) Target store fails to recreate stored install-time (other
  Date and ByteCount values as well)
- skip comments and blank lines in multilists
  fixes (#214877) - zen-updater is not installed by default
- Automatically fix broken products when reading
  the product database.
  still pending: honour the read-only flag
  Changes to make this possible include
  using read_dir instead of boost directory
  iterator.
* Wed Oct 25 2006 schubi@suse.de
- added new class for generating solver testcases:
  Testcase
* Wed Oct 25 2006 ma@suse.de
- Finalized ui::PatternContents. (F301229)
- version 2.7.0
- revision 4413
* Wed Oct 25 2006 mvidner@suse.cz
- Moved zypper and zypp-checkpatches(-wrapper) to zypper.rpm
- version 2.6.0
* Tue Oct 24 2006 ma@suse.de
- Added ui::PatternContents: Helper class that will compute a patterns
  expanded install_packages set. (UI interface for F301229)
- revision 4387
* Tue Oct 24 2006 mvidner@suse.cz
- removed the last reference to /usr/lib64 to fix the build
* Mon Oct 23 2006 mvidner@suse.cz
- added "zypper info" (jkupec)
- version 2.5.2
* Mon Oct 23 2006 dmacvicar@suse.de
- fix rpm db timestamp
- add extra urls and optional urls to product API
- r4378
* Fri Oct 20 2006 mvidner@suse.cz
- zypper: nicer progress reports, with or without --verbose.
* Fri Oct 20 2006 ma@suse.de
- Fixed reloading of target data after commit. Broken since
  rev 3880.
- version 2.5.1
- revision 4365
* Fri Oct 20 2006 dmacvicar@suse.de
- put query-pool in /usr/lib/zypp and not lib64
- r4363
* Fri Oct 20 2006 dmacvicar@suse.de
- revert keyring changes, causes endless loop (obvious)
- add dist-product information, adapt store
- version 2.5.0
- r4355
* Fri Oct 20 2006 ma@suse.de
- zypp-query-pool: For products show additionally distributionName
  and distributionEdition. (required by #205392)
- revision 4349
* Thu Oct 19 2006 ma@suse.de
- Add accessor for Product distributionName and distributionEdition.
  (required by #205392)
- revision 4347
* Thu Oct 19 2006 dmacvicar@suse.de
- added test case for KeyRing
- fire trustedKeyAdded in all calls to import trusted key
  not only in signature check workflow.
- r4342
* Thu Oct 19 2006 mvidner@suse.cz
- zypper update: implemented minimal version (patches only)
- zypper list-updates: changed default type from package to patch,
  consider patches affecting the package manager separately
* Thu Oct 19 2006 dmacvicar@suse.de
- version 2.4.1
- r4338
* Thu Oct 19 2006 dmacvicar@suse.de
- add zypp-query-pool, so registration doesn't depend on
  libzypp-zmd-backend being installed. Will remove from
  backend when suseregister gets updated.
* Thu Oct 19 2006 schwab@suse.de
- Make sure config.rpath is present.
* Wed Oct 18 2006 mvidner@suse.cz
- zypper search: fixed uninitialized members that made all searches
  exact and case sensitve
* Wed Oct 18 2006 dmacvicar@suse.de
- zypp-checkpatches, write in the right file
- r4328
* Wed Oct 18 2006 schubi@suse.de
- Install resolvables although they are unneeded
  if they have NOT the kind patch/atoms
  Bug 210538 - freshens/supplements does not work with patterns
- r4326
* Tue Oct 17 2006 mvidner@suse.cz
- zypper service-add -r http://example.org/foo.repo (F#300641).
* Tue Oct 17 2006 dmacvicar@suse.de
- zypp-checkpatches:
  save version of the generated xml to
  regenerate it if it changes.
  save a random token in case of error to
  force recreating xml file
- r4321
* Tue Oct 17 2006 dmacvicar@suse.de
- remove permissions for zypp checkpatches from spec
- r4318
* Tue Oct 17 2006 dmacvicar@suse.de
- registration fails because of wrong product data
  (#205392)
  use DISTPRODUCT,DISTVERSION to create the product
  resolvable. have this resolvable provide
  PRODUCT = VERSION
- r4312
* Mon Oct 16 2006 mvidner@suse.cz
- zypper service-add -r ./foo.repo (F#300641).
* Mon Oct 16 2006 jkupec@suse.cz
- zypper: added case-sensitive search, search in descriptions and
  summaries, search by resolvable type, substring and word
  matching, support for wildcards
- Revision 4303
* Mon Oct 16 2006 mvidner@suse.cz
- Prevent the user from sending signals to zypp-checkpatches-wrapper
  (#211286).
* Mon Oct 16 2006 schubi@suse.de
- Dont incomplete an uninstalled resolvable, even not when establishing.
  Incomplete only makes sense for installed resolvables (when they have broken
  deps), for patches (because they are needed) and for atoms (because they are
  used during patch calculation)
  Bug 198379
- Do not branch for packages with the same NVE but different architectures.
  Take the best architecture.
* Fri Oct 13 2006 dmacvicar@suse.de
- implement rename source in sourcemanager
- r4286
* Fri Oct 13 2006 dmacvicar@suse.de
- YaST sources: set alias to product summary if empty
- show alias on logs.
- r4281
* Thu Oct 12 2006 dmacvicar@suse.de
- version 2.4.0 (bin incompat due to callback fixes)
- r4272
* Thu Oct 12 2006 ma@suse.de
- Provide additional solver status information to the UI.
  (#162164,F301272)
- Fixed UI satus computation in presence of multiple available
  candidates.
- revision 4264
- version 2.3.1
* Thu Oct 12 2006 dmacvicar@suse.de
- remove const in MediaChangeReport requestMedia that
  broke cd changing.
- r4262
* Wed Oct 11 2006 mvidner@suse.cz
- zypper: added search (jkupec)
- removed the suid bit from zypp-checkpatches-wrapper so that the
  build passes until permissions.rpm is updated (~#211286).
- r4253
* Tue Oct 10 2006 dmacvicar@suse.de
- Log microseconds if ZYPP_PROFILING env var is enabled.
- r4252
* Mon Oct  9 2006 dmacvicar@suse.de
- YaST sources:
  Factory cannot be set with 'refresh' enabled
  (#204957)
- get rid of some const bool signatures in Source classes
- r4247
* Mon Oct  9 2006 mvidner@suse.cz
- Added zypp-checkpatches and a suid-root zypp-checkpatches-wrapper.
* Fri Oct  6 2006 schubi@suse.de
- select the best solution: prefering the total amount of install/update
  packages BEFORE source preferences. Bug 208784
* Fri Oct  6 2006 dmacvicar@suse.de
- Introduce a method to see if a source supports a
  kind of resolvable at that time, so we can
  init a YUM source like factory but avoid parsing
  it if it contains no patches.
- add TODO
- zypp-checkpatches xml output
- r4235
* Mon Oct  2 2006 mvidner@suse.cz
- added a CLI preview: zypper
- revision 4214
- version 2.2.3
* Mon Oct  2 2006 dmacvicar@suse.de
- FATE #100165:
  Make Content File Aware of Different Architectures
  expand %%%%a in release notes with architecture
* Fri Sep 29 2006 ma@suse.de
- Extended pattern parser to support includes/extends tags as hint
  for the IO. (F301229)
- revision 4199
- version 2.2.2
* Thu Sep 28 2006 ma@suse.de
- Enabled sending of ScriptResolvableReport.
- Changed ScriptResolvableReport::start to send local path
  of script to be executed.
- revision 4190
- version 2.2.1
* Wed Sep 27 2006 ma@suse.de
- Added ScriptResolvableReport. Callbacks triggered on script
  execution during commit. (F100233)
- revision 4187
- version 2.2.0
* Mon Sep 25 2006 mvidner@suse.cz
- fix: Url::getRegisteredSchemes() would always return nothing
* Fri Sep 22 2006 jkupec@suse.cz
- Made the build dependency on gettext-devel explicit
* Tue Sep 19 2006 jsrain@suse.cz
- adapted multi-media YUM sources according to official YUM
  specification (F300743)
* Mon Sep 18 2006 lslezak@suse.cz
- use RPM_OPT_FLAGS (meissner@suse.de)
* Mon Sep 18 2006 lslezak@suse.cz
- SourceFactory::createFrom() - don't loose url,...
- r4160
* Mon Sep 18 2006 kkaempf@suse.de
- reduce logging in ResolvableImpl.cc
- rev 4157
* Thu Sep 14 2006 schubi@suse.de
- Replaced requirementIsMet by requirementIsInstalledOrUnneeded
  in QueueItemInstall and QueueItemRequire
  Bug 192535/204913
  removed fix:Thu Sep  7 18:31:46 CEST 2006 - schubi@suse.de
* Thu Sep 14 2006 lslezak@suse.cz
- fixed SourceFactory::createFrom() - don't loose alias,
  cachedir,... parameters
* Thu Sep 14 2006 mvidner@suse.cz
- Use RPM Enhances only if detected at configure time, to allow
  compilation with older rpm.
- callback params: use const string & instead of string (dmacvicar)
* Thu Sep  7 2006 schubi@suse.de
- Do not regarding SATISFIED (regarding UNNEEDED) in isPresent if it is
  a package/script/message
  Bug: 192535
* Thu Sep  7 2006 dmacvicar@suse.de
- add Source_Ref::checksum() which in combination with
  timestamp can give an idea of a source change.
- r4106
* Thu Sep  7 2006 mvidner@suse.cz
- Implemented fgzstreambuf::compressed_tell and fXstream::getbuf to
  enable progress reporting on compressed streams.
* Wed Sep  6 2006 dmacvicar@suse.de
- better error propagation
- r4096
* Tue Sep  5 2006 mt@suse.de
- Removed libblkid dependency - the workaround using libblkid to
  check filesystem on XEN vbd mapped devices is obsolete, because
  the info is avaliable via /dev/disk/by-label link now. (#197107)
- revision 4087
* Thu Aug 31 2006 ma@suse.de
- PackageProvider: Fixed broken retry. (#202163)
- revision 4071
* Wed Aug 30 2006 ma@suse.de
- Fixed RpmDb::makePackageFromHeader: Catch NULL Header passed as argument and refuse
  to create a Package from a source package header.
- Added method Pathname::extension: Return all of the characters in name
  after and including the last dot in the last element of name.
- PlaindirImpl: Disable rpm signature verification when scaning a directory for
  rpms. Otherwise we'd need access to the rpm database to get the keys.
- revision 4069
* Wed Aug 30 2006 schubi@suse.de
- Do not regarding SATISFIED/UNNEEDED in isPresent if it is
  a package/script/message
  Bug: 192535
* Wed Aug 30 2006 ma@suse.de
- Speedup computation of number of rpm database entries.
- revision 4058
* Tue Aug 29 2006 schubi@suse.de
- Fixed endless loop in transactResObject
  Bug 198095 - YaST2 Installaler crashes when selecting Gnome pattern to a KDE installation
* Tue Aug 29 2006 dmacvicar@suse.de
- fix some testcases for tar file parser changes
- r4045
* Tue Aug 29 2006 dmacvicar@suse.de
- missing includes
- clean old callbacks
- r4041
* Fri Aug 25 2006 schubi@suse.de
- zyppPattern->install_packages returns SUGGESTED package too.
  Bug 201476
  Revision 4036
* Fri Aug 25 2006 schubi@suse.de
- New behaviour in the solver: try with 'best' package first, try with 'all'
  packages if this fails.
  Bug :Bug 191983
* Fri Aug 25 2006 dmacvicar@suse.de
- libzypp 2.1.0
- bump version due to incompatible callback changes in KeyRing
  Sources
* Thu Aug 24 2006 dmacvicar@suse.de
- new keyring callbacks
- separate trust key from import key
- use PublicKey class instead of params, to be able
  to add more info like photos later (pending #181682)
- update zmart with those callbacks.
- better error handling (Exception types)
- make tmp file names more readable depending on the context
- r4026
* Tue Aug 22 2006 dmacvicar@suse.de
- decouple probing from source creation, using the new
  media test for existence functions.
- r4019
* Tue Aug 22 2006 mt@suse.de
- Fixed getDoesFileExist to reset the transfer range
- Added logging of curl debug messages to the zypp log.
  The env var ZYPP_MEDIA_CURL_DEBUG=1 logs curl infos,
  ZYPP_MEDIA_CURL_DEBUG=2 logs the in/out headers.
- r4018
* Fri Aug 18 2006 kkaempf@suse.de
- remove the /etc/sysconfig/zypp:REWRITE_KERNEL_DEPS = yes check;
  see rev 3810 below. (#190163)
- rev 3998
* Thu Aug 17 2006 dmacvicar@suse.de
- fix uninstalling of atoms (noop)
- r3995
* Wed Aug 16 2006 dmacvicar@suse.de
- Implement initial verson of Media
  doesFileExist, for future source probing.
- r3984
* Tue Aug 15 2006 dmacvicar@suse.de
- more dbus_connection_close fixes
- r3974
* Tue Aug 15 2006 kkaempf@suse.de
- clean up 'incomplete' handling in QueueItemEstablish.
- rev 3973.
* Tue Aug 15 2006 kkaempf@suse.de
- Don't set 'incomplete' for uninstalled patterns or products.
  (#198379)
- rev 3970.
* Mon Aug 14 2006 schubi@suse.de
- Added new API calls:
  setAdditionalProvide
  setAdditionalConflict
  setAdditionalRequire
* Mon Aug 14 2006 dmacvicar@suse.de
- don't link examples to testsuite library.
* Sat Aug 12 2006 schwab@suse.de
- Disable profiling to work around compiler bug.
* Fri Aug 11 2006 dmacvicar@suse.de
- forward port 3924:3939
- Add explicit finish callbacks for subtasks during ProvidePackage
   to avoid UI confusion.
- rev3957
* Fri Aug 11 2006 dmacvicar@suse.de
- Introduce examples/
- fix some svn ignores
- fix compilation. Use: dbus_connection_close
- rev 3943
* Thu Aug 10 2006 dmacvicar@suse.de
- Initial support for plain directory with rpms as source
- r3935
* Tue Aug  8 2006 dmacvicar@suse.de
- Move the target query by kind function to
  a iterator, so we dont make a copy of the restore
  the iterator works loading by demand too
* Mon Aug  7 2006 dmacvicar@suse.de
- rename the new initTarget to initializeTarget,
  leave the old one as is, but deprecate it.
- r3903
* Mon Aug  7 2006 dmacvicar@suse.de
- forward port from SLES10 branch , till 3888
- Prefer to use available DeltaRpm or PatchRpm instead of downloading
  full packages. (#168844)
- rpmdb : Do not use the deprecated POSIX API, but boost::regex
- version 2.0.0
- rev 3893
* Fri Aug  4 2006 dmacvicar@suse.de
- Separate target init from adding resolvables, getting rid of the
  uggly bool flag.
- dont clear the store each time Target::resolvables is called
- Load target resolvables on demand by kind, keep them cached later
- add Target::resolvablesByKind(kind) to allow query specific kind
  without reading all kinds. Used to port TargetProduct, which
  was reading the whole rpm database only to displayy base product
  name in YaST help.
- commit to pkg-bindings and packager will follow.
- jsrain will port more yast stuff, especially inst_source which
  startup time should by reduced by half afterwards.
- rev 3880
* Tue Aug  1 2006 dmacvicar@suse.de
- forward port:
  rev 3786 fix to stalle tmpfiles broke patches.
  SLES was released with this broken. 10.1 has a blocked
  zypp update because this.
  Attempt to fix this. (#192535)
- fix configure.ac sqlite-source build path
- rev 3858
* Fri Jul 21 2006 dmacvicar@suse.de
- link correctly
* Wed Jul 19 2006 dmacvicar@suse.de
- dont link sqlite in the main lib.
- rev 3826
* Tue Jul 18 2006 dmacvicar@suse.de
- susetags: parse product parser regexp only once
- parse yum factory 5 sec. (from 30) faster using
  another string find algorithm
- rev 3824
* Tue Jul 18 2006 dmacvicar@suse.de
- Digest: Don't read the stream character wise but reading blocks,
    as advised by matz profiling.
- r3819
* Mon Jul 17 2006 ma@suse.de
- Add "openSUSE", "ATI Technologies Inc." and "Nvidia" to
  trusted vendors. (#189573)
- revision 3804
* Thu Jul 13 2006 dmacvicar@suse.de
- backport fix for stalle tmpfile (#191311)
- rev 3788
* Wed Jun 28 2006 mt@suse.de
- deactivated media manager code that was disabling the
  automounter (#172419)
- rev 3724
* Mon Jun 26 2006 dmacvicar@suse.de
- fix autorefresh (#186115)
- revision 3708
* Fri Jun 23 2006 ma@suse.de
- forward port from SLE branch
- Set default permission for logfiles to 0640. (#187044)
- revision 3696
* Thu Jun 22 2006 ma@suse.de
- forward port from SLE branch
- Fixed installation of SP or Add-On product switching to media 2
  too early. (#186607)
- revision 3691
* Wed Jun 21 2006 dmacvicar@suse.de
- forward port from SLE branch
- Strip self provides without edition in Resolvable ctor.
  (#186079)
- Source::provideResolvables not implemented in yum source type.
  Product not set for packages that are available from update source
  (#186920)
- Hook modalias() supplements without package to "kernel" (#184840)
- Allow on-demand SourceManager::restore() (#186678)
- Hook modalias() supplements without package to "kernel" (#184840)
- rev 3676
* Mon Jun 19 2006 mt@suse.de
- Fix adding resolving of path names for mount points (#181606)
- rev 3658
* Mon Jun 19 2006 dmacvicar@suse.de
- merge download algorithm and refactoring from branch
  (#181204)
* Thu Jun 15 2006 mvidner@suse.cz
- autodocs: use find+xargs to overcome command length limit,
  do not call doxygen unnecessarily (#185334).
- rev 3645
* Thu Jun 15 2006 kkaempf@suse.de
- Dont use getZYpp in static constructor (#185198)
  Bugfix #178292 was wrong.
- Only warn on incompleting installed resolvables (#185197)
- rev 3644
* Wed Jun 14 2006 kkaempf@suse.de
- Atoms might only be installed via patches (#184714)
- rev 3642
* Wed Jun 14 2006 dmacvicar@suse.de
- fix for the last stall tmpfile (#178292)
- r3637
* Wed Jun 14 2006 mt@suse.de
- Implemented transfer timeout inside of the progress callback.
  The timeout value can be set using timeout url parameter, the
  default transfer timeout is 180 seconds. (#181602)
- Added ssl_verify and ssl_capath url options used in https scheme,
  allowing to change or disable the ssl verify options. (#171622)
- Added fallback on read failures of /etc/mtab to /proc/mounts.
  Improved verbosity in mount and mount check related failure cases,
  incl. /etc/mtab dump. (#181606)
- rev 3623
* Wed Jun 14 2006 kkaempf@suse.de
- combine knownAliases and knownUrls in a single function.
- rev 3616
* Mon Jun 12 2006 kkaempf@suse.de
- honor parallel installs in resolver context (#181103)
- rev 3592
* Mon Jun 12 2006 dmacvicar@suse.de
- right fix for tmpdir initialized in static constructor
- catch around provideJustFile in providePackage
-rev 3654
* Mon Jun 12 2006 dmacvicar@suse.de
- fix #182003 YUM packages without size
- rev 3587
* Mon Jun 12 2006 kkaempf@suse.de
- Allow to restore and remove by Url
- rev 3583
* Mon Jun 12 2006 kkaempf@suse.de
- make atoms parallel installable (#181103)
- rev 3580
* Fri Jun  9 2006 dmacvicar@suse.de
- Allow to restore by alias
- r3568
* Fri Jun  9 2006 mvidner@suse.cz
- Do not fork in a global destructor, perl dislikes it (#182672).
  Fixes hanging ag_ldapserver and yast2-perl-bindings tests.
* Thu Jun  8 2006 ma@suse.de
- Installation: Assert product information is stored to libzypp
  database before reboot. (#181198)
- Version 1.2.0; revision 3553
* Wed Jun  7 2006 visnov@suse.cz
- Synchronize keys with rpm database before
  closing access to it (#182338)
- rev 3533
* Wed Jun  7 2006 mt@suse.de
- Changed to just prefer DVD drives in "dvd:" scheme, instead of
  filter out the non-DVD drives completely. Allows a fallback to
  drives without the dvd HAL property e.g. in VMWare. (#177457)
- rev 3530
* Wed Jun  7 2006 dmacvicar@suse.de
- Merge fix for stalle tmpdir due to cyclic references, using a master
  TmpDir for zypp. (#178292) . There is still 1 tmpdir to fix.
- rev 3521
* Wed Jun  7 2006 dmacvicar@suse.de
- Fixes unneeded file download, and add download callbacks
  (still need yast side) #181204 and #160206
- Fix stalle tmpdir due to cyclic references, using a master
    TmpDir for zypp. # 178292
* Tue Jun  6 2006 ma@suse.de
- fixed memory leak in PersistentStorage (#168690)
- revision 3519
* Tue Jun  6 2006 ma@suse.de
- fixed memory leak in XMLSourceCacheParser (#168690)
- revision 3517
* Fri Jun  2 2006 schubi@suse.de
-latest fi translation added
  Revision 3502
* Thu Jun  1 2006 schubi@suse.de
-All installed resolvables has been set to "satisfied" in
  ResolverContext::unneeded . BUT:
  Patch concerning resolvables have to be set to
  "unneeded" although they are installed. In order
  getting the state "no longer applicable" (Bug 171590)
- rev 3496
* Thu Jun  1 2006 kkaempf@suse.de
- compute status for scripts and messages so their freshens get
  properly honored (aj with postgresql-server)
- rev 3494
* Thu Jun  1 2006 dmacvicar@suse.de
- revert not-used-yet rpmdb timestamp, as
  it broke rpmdb::init(). (#180040)
- rev 3490
* Thu Jun  1 2006 schubi@suse.de
- updating gmo files, if po files has been changed; bug 164449
* Wed May 31 2006 dmacvicar@suse.de
- Dont download twice if starting from 1st time
- fix typo
- rev 3481
* Wed May 31 2006 dmacvicar@suse.de
- set cache dir only if storeMetadata is called as a public method.´
- rev 3475
* Wed May 31 2006 kkaempf@suse.de
- schedule a package for installation if
  - it freshens / supplements something
  - it is not installed yet
  (#178721)
- rev 3473
* Wed May 31 2006 dmacvicar@suse.de
- make susetags also implement download and check first.
- rev 3470
* Tue May 30 2006 dmacvicar@suse.de
- make yum more robust. Never parse from provideFile
  but only from local disk. Make sure the cache
  is consistent before recreating it.
  the code is easier to follow and probably
  faster. checksum and signatures are
  checked on caching not on parsing.
  Required to implement refresh for #154990
- rev 3452
* Wed May 24 2006 dmacvicar@suse.de
- implement timestamp for YUM and SuseTags
- actually use the license to confirm in yum patches
- add prerequires tag in yum optonally to the bad designed
  and nonintuitive pre=1
- rev 3448
* Wed May 24 2006 dmacvicar@suse.de
- dont pass root on init but before.
- implement rpm db modification timestamp
    not used yet
- move Helix source to testsuite out of the solver
  so we can use it for target, storage tests
- add Source_Ref::timestamp(), default to now()
    in order to implement smart sync of sources by zmd
- don't parse desc and summary twice
- fix a segfault with tranlated text
- fix broken size tag introduced in rev 3427
- rev 3446
* Tue May 23 2006 dmacvicar@suse.de
- dont accept corrupt sources, improve logs
* Tue May 23 2006 ma@suse.de
- Added PoolItem_Ref::statusReset. Resets the PoolItem status without
  loosing autoprotection (eg. for foreign vendor). (assists #177469)
- rev 3431
* Tue May 23 2006 jsrain@suse.cz
- added mediaNr() to PatchRpm and DeltaRpm classes
- rev 3430
* Tue May 23 2006 dmacvicar@suse.de
- enable YUM license to confirm.
  needed for #174476
- adapt store to serialize and read all new resobject fields
- use install-time to now() when serializing (#174653)
- rev 3427
* Mon May 22 2006 ma@suse.de
- Do not violate install order when restricting commit to a certain
  mediaNumber. (#170079)
- Version 1.1.0; rev 3423
* Mon May 22 2006 mvidner@suse.cz
- Added SourceManager::findSourceByUrl to overcome alias mismatches
  (#177543).
- rev 3420
* Mon May 22 2006 ma@suse.de
- Order all objects according to prerequirements, not just packages.
  (#173690)
- rev 3419
* Mon May 22 2006 schubi@suse.de
- Added new translation
* Fri May 19 2006 dmacvicar@suse.de
- fix missing homedir option for gpg (#171055)
- rev 3415
* Thu May 18 2006 ma@suse.de
- Prevent against daemons launched in rpm %%%%post, that do not close
  their filedescriptors. (#174548)
- Version 1.0.1; rev 3413
* Thu May 18 2006 jsrain@suse.cz
- fixed media number of package retrieved as a part of a patch
  (#174841)
- rev 3409
* Thu May 18 2006 dmacvicar@suse.de
- fix missing package descriptions due to filtered packages
  by incompatible architectures. (#159109)
- rev 3404
* Thu May 18 2006 kkaempf@suse.de
- decrease logging in DiskUsageCounter and Modalias (#163186)
- rev 3406
* Thu May 18 2006 ma@suse.de
- Stay backward comapatible.
* Tue May 16 2006 ma@suse.de
- Make basic attributes available through ResObject.
- Let ResObjects which do not require media access during
  commit return ZERO sourceMediaNr (required for #173690)
- Version 1.0.0
- rev 3390
* Tue May 16 2006 kkaempf@suse.de
- reduce logging verbosity (#163186)
- rev 3381
* Tue May 16 2006 schubi@suse.de
- setCandidate accept candidates with compatible architectures too. Not
  only with the same architecture. Bug 172594 - If update package has
  differet arch, UI display is wrong
* Tue May 16 2006 mvidner@suse.cz
- Added Source_Ref::resStoreInitialized.
  If we know that noone has seen the resolvables yet, we can skip
  them too, eg. when deleting a source. (#174840)
- rev 3378
* Mon May 15 2006 kkaempf@suse.de
- Honor freshens as conditionals independant from the installed/
  uninstalled status (#174797)
- rev 3376
* Mon May 15 2006 kkaempf@suse.de
- State modifier "unneeded" is transitive for patches (#171590)
- rev 3375
* Thu May 11 2006 schubi@suse.de
- Do not transact itself (update) in the transactResObject mechanism
  Bug 174290
* Thu May 11 2006 mt@suse.de
- Reenabled improved large file support flags (unintentionally
  removed in rev 1544). Fixes bug #173753.
- Added large file support flags to libzypp.pc file allowing
  consistence checks in the application using features variable
- rev 3366
* Thu May 11 2006 mvidner@suse.cz
- SourceManager: moved source deletion before creation
  so that we can recreate a deleted one (#174295)
- removed dead code dealing with known_caches from SourceManager::store
  (see r3195)
- r3362
* Thu May 11 2006 jsrain@suse.cz
- fixed returning product short name and summary if product read
  from target store (#148625)
- rev 3360
* Wed May 10 2006 jsrain@suse.cz
- set media verifier on redirected medium (#172599)
- rev 3359
* Mon May  8 2006 kkaempf@suse.de
- fix 'transactResKind' to collect best providers by capability
  and to recursively transact items of same kind (#170114)
- rev 3355
* Mon May  8 2006 dmacvicar@suse.de
- serialize the full URL to avoid missing password and other
  url settings (#148108)
- rev 3353
* Fri May  5 2006 mt@suse.de
- Added a 60 sec connect timeout to MediaCurl (#172860)
- rev 3348
* Thu May  4 2006 kkaempf@suse.de
- re-fetch also .asc and .key files before checking signature
  (#172597)
- rev 3350 (3345-10.1)
* Wed May  3 2006 dmacvicar@suse.de
- Fix yum key verification, because a double variable declaration
* Wed May  3 2006 dmacvicar@suse.de
- use --no-default-keyring to avoid creating a
    default gpg dir in / (#171055)
- rev 3335
* Wed May  3 2006 dmacvicar@suse.de
- Fix YUM signature checking, we were passing the key instead of the
  signature.
- When the user trust a key, sync again. Bye to the session trusted
  keys and user being asked all the time. (#171213)
- r3332
* Wed May  3 2006 ma@suse.de
- Cleanup index tables when removing items from pool (#170564).
* Wed May  3 2006 kkaempf@suse.de
- backout rev 3246->3275 of TargetImpl.cc
- add missing testsuite/utils/TestUtils.h
- rev 3330
* Wed May  3 2006 dmacvicar@suse.de
- more fixes for #171062, there were some files still not being
  read from cache.
- r3327
* Tue May  2 2006 dmacvicar@suse.de
- cache keys and signature. Remove lot of duplicated code. (#171062)
- r3320
* Tue May  2 2006 mt@suse.de
- Disabled isUseableAttachPoint check in MediaDIR -- we do not
  mount here anything, so it is OK to use any dir (171351).
- rev 3318
* Tue May  2 2006 kkaempf@suse.de
- parse "license-to-confirm" in primary.xml (#168437)
- rev 3312
* Mon May  1 2006 kkaempf@suse.de
- Don't try to store 'Atom', not needed and the backend store
  rejects them anyways (addtion to #168610)
- rev 3306
* Mon May  1 2006 mt@suse.de
- Improved device check in MediaDISK using libblkid (Bug #158529)
- Allow to provide sysfs path via $SYSFS_PATH in MediaCD.cc and
  added a check if it is a directory
- Added libcurl and libblkid checks to configure.ac
- Added e2fsprogs(-devel) requires to the spec file
- rev 3303
* Sat Apr 29 2006 kkaempf@suse.de
- dont download "other" during key check (#171041)
- rev 3294
* Sat Apr 29 2006 kkaempf@suse.de
- allow parallel installs of atoms (used to fulfill patch require-
  ments, atoms aren't installed anyways) (#170098)
- some testsuite improvements.
- rev 3288
* Fri Apr 28 2006 dmacvicar@suse.de
- get rid of autobuild check when throwing exceptions without throw
  but with a macro, returning a null pointer at the end (never reached).
* Fri Apr 28 2006 ma@suse.de
- Do not violate install order when restricting commit to a certain
  mediaNumber. (#170079)
* Fri Apr 28 2006 dmacvicar@suse.de
- Don't use throw directly!
  use ZYPP_THROW with a Exception class, otherwise package bindings
  will not catch them.
  Should fix crashes when reading broken sources with yast.
- rev 3272
* Fri Apr 28 2006 schubi@suse.de
- Bug 162064 - font packages are not installed for locale, e.g. khmer font not installed after CD1
  revision 3269
* Fri Apr 28 2006 kkaempf@suse.de
- revert bugfix #168906 (fom rev 3219), it filters too many errors.
- further improve on #168840 (from rev 3231), match on name-edition
  when filtering by best arch. (#170098)
- rev 3268
* Fri Apr 28 2006 dmacvicar@suse.de
- #170093 , lot of package descriptions missing
- rev 3263
* Thu Apr 27 2006 dmacvicar@suse.de
- try to fix wrong permissions of /var/lib/zypp created
  by old zypp, only when running as root they are fixed
  (#169094)
- YUM: Verify signatures on factoryInit.
  Dont provide other.xml. Cleanups, better logging.
  When refreshing signed soruces, don't refresh is source
  has not changed.
- YaST sources: don't refresh if media file has not changed.
- Show full url of index files in sources for signature validation
  (mentioned in #170139 comment #3)-
* Thu Apr 27 2006 jsrain@suse.de
- udpated media ID syntax for external scripts (to be consistent
  with packages) (#170247)
- rev 3256
* Thu Apr 27 2006 jsrain@suse.de
- set media ID to 1 if not specified in YUM metadata (#167452)
- rev 3255
* Thu Apr 27 2006 kkaempf@suse.de
- If freshen and supplement are fulfilled, install any kind of
  resolvable if not yet installed (#165746)
- rev 3249
* Wed Apr 26 2006 kkaempf@suse.de
- make downloaded script executable. (#169191)
- rev 3247
* Wed Apr 26 2006 kkaempf@suse.de
- Improve on last fix, compare only compatible archs.
- rev 3233
* Tue Apr 25 2006 kkaempf@suse.de
- Only choose best arch of multiple package atoms with identical
  name (#168840)
- rev 3231
* Tue Apr 25 2006 dmacvicar@suse.de
- pass empty strings to UI as key properties if unknown key
  (#169114)
- rev 3228
* Tue Apr 25 2006 kkaempf@suse.de
- refrain from parsing 'other.xml' (#159316)
- rev 3226
* Tue Apr 25 2006 visnov@suse.cz
- in source refresh, clean up the cache dir if fails
- do not require repomd.xml.asc when creating a cache (#163765)
- rev 3224
* Tue Apr 25 2006 dmacvicar@suse.de
- Check if a file exists before providing it, and just handling the
  exception is not sufficient, because it can release the media.
  it nows get all possible packages.X translations an then
  it selects the candidate from the existing ones (#168654)
- rev 3221
* Tue Apr 25 2006 kkaempf@suse.de
- dont report conflicts if item is neither installed
  nor to-be-installed (#168906)
- rev 3219
* Tue Apr 25 2006 dmacvicar@suse.de
- #168060 , propagate the file description or original
  name to the UI and not the checked filename path,
  which could be a tmp file.
  Requires changes in pkg-manager, and probably zmd-helpers.
- rev 3215
* Mon Apr 24 2006 dmacvicar@suse.de
- /var/lib/zypp/db/languages/* are empty files (##168355)
- r3206
* Mon Apr 24 2006 dmacvicar@suse.de
- All resolvables must honor arch, so Arch_noarch in
  target/store/XMLFilesBackend.cc is wrong (#160792)
- Introduced code to honour shared package descriptions
  (#159109)
- r3204
* Mon Apr 24 2006 jsrain@suse.de
- replace '_' in YUM elements/attributes with '-' (#168762)
- rev 3201
* Mon Apr 24 2006 mt@suse.de
- Fixed iseries workaround - interchanged variables for scsi
  devices, added debug messages about the steps (#163971).
- Added getenv NULL ptr check and verify of the $HOME dir's
  and ~/.curlrc file's ownership (#163203).
- rev 3199
* Mon Apr 24 2006 ma@suse.de
- Use filesystem::TmpDir to create unique and unused Source cache
  directories. (#168051)
* Mon Apr 24 2006 ma@suse.de
- Enable signature checks per default. (#168525)
* Mon Apr 24 2006 visnov@suse.cz
- fix callbacks for providing a single file (#160206)
* Sun Apr 23 2006 kkaempf@suse.de
- If an installed package looses a dependency, the solver tries
  to upgrade it. Limit the upgrade candidates to best arch, best
  edition.
- filter 'other' entries with incompatible arch in yum parser.
- rev 3177
* Fri Apr 21 2006 jsrain@suse.de
- initialize the product category according to source (#168061)
- rev 3172
* Fri Apr 21 2006 mvidner@suse.cz
- delete only one older version of a xml-store resolvable
  (half-baked, but the previous attempt was charred)
* Fri Apr 21 2006 jsrain@suse.de
- moved license_to_confirm to primary.xml
- rev 3170
* Fri Apr 21 2006 ma@suse.de
- Removed deprecated oldstyle commit methods.
* Fri Apr 21 2006 mvidner@suse.cz
- when installing a xml-store resolvable (all except package,
  message, script), delete older versions (#160792).
- read selection edition from the XML store
- rev 3167
* Thu Apr 20 2006 kkaempf@suse.de
- properly clear transaction flag after successful commit
  (see rev 3122, #164365, #167285)
- rev 3157
* Thu Apr 20 2006 kkaempf@suse.de
- recursively soft-uninstall recommended package on real uninstall,
  not on update (#167603)
- rev 3155
* Thu Apr 20 2006 dmacvicar@suse.de
- fix #167605 (importing keys to rpm multiple times due to
  wrong interpretation of rpm gpg versioning.
- add support for reading the rpm keys, with full id and fingerprint
- rev 3153
* Wed Apr 19 2006 kkaempf@suse.de
- don't add duplicate error infos to ResolverContext (#167309)
- rev 3146
* Wed Apr 19 2006 kkaempf@suse.de
- fix Resolver::transactReset() (see rev 3122) (#167285)
- rev 3140
* Wed Apr 19 2006 ma@suse.de
- Introduced $ZYPP_KEYRING_DEFAULT_ACCEPT_ALL. If this environment
  variable is present, all signature checking callbacks will default
  to 'accept', in case no recipient is present.
* Wed Apr 19 2006 dmacvicar@suse.de
- read content file on construction, and make
  provideProduct only insert the already
  read product object into the store (#165826)
  (dmacvicar)
- When the signature is not found, warn the
  user about a unsigned source. When the
  key is not found, do nothing, it can be in the
  keyring already. (#166016) (dmacvicar)
- enable key verification only if
  ZYPP_CHECKSIG env var is set (dmacvicar)
- r1529
* Tue Apr 18 2006 kkaempf@suse.de
- fix bugfix 164365, fix bug 167285
  Actually clear the transcation state instead of locking it
  to 'dont transact'
- rev 3122
* Tue Apr 18 2006 visnov@suse.cz
- revert the signature/digest checking callbacks
- rev 3115
* Tue Apr 18 2006 kkaempf@suse.de
- Bugfix #165670
  - Honor keep requests.
  - Dont flag "locked uninstall" as error if a keep request was
    issued before.
- rev 3114
* Tue Apr 18 2006 kkaempf@suse.de
- rule out locked items during distribution upgrade as early
  as possible. (#165670)
- rev 3110
* Mon Apr 17 2006 kkaempf@suse.de
- Bugfix #166212
  - use APPL_LOW as 'ui initiated, by solver' in transactKind() and
    transactResObject().
  - resetTransaction(APPL_LOW) before resolving
  - enhance transactCaps by using the same algorithm as in
    QueueItemRequire
    (before: transact all requires and recommends by name
    now: transact best requires and recommends by provides)
- rev 3107
* Fri Apr 14 2006 visnov@suse.cz
- new callbacks for failing digest
- rev 3098
* Thu Apr 13 2006 visnov@suse.cz
- ask for file without a checksum (#165125)
* Thu Apr 13 2006 kkaempf@suse.de
- dont install satisfied resolvables (#165843)
- rev 3095
* Thu Apr 13 2006 kkaempf@suse.de
- dont abort on failed "dry_run" (#164583)
- rev 3091
* Thu Apr 13 2006 visnov@suse.cz
- Ask user if signature file does not exist (#163765)
- handle repomd.xml.asc as optional file (#163765)
- rev 3089
* Thu Apr 13 2006 schubi@suse.de
- Bug 164365 - build 906: Deselecting a selection, all packages are still selected
- rev 3087
* Thu Apr 13 2006 kkaempf@suse.de
- Dont do transitive uninstalls on uninstalled or upgraded items.
  (#165798)
- rev 3083
* Wed Apr 12 2006 ma@suse.de
- Added 'rpmNoSignature' to ZYppCommitPolicy (#163862)
* Wed Apr 12 2006 mvidner@suse.cz
- Product::updateUrls: restore it from the XML store;
  fixed content parsing (#163192).
- restore product flags fro the XML store
- rev 3074
* Wed Apr 12 2006 kkaempf@suse.de
- Only consider best arch/version (#165477)
- rev 3069
* Wed Apr 12 2006 ma@suse.de
- No need to parse tags at all if there is no item to store values
  (e.g. data for unwanted arch). Fixed segv trying to store data in
  NULL item. (#165479)
- rev3065
* Tue Apr 11 2006 mt@suse.de
- Improved Url path name "//" vs. "/%%%%2f" handling; now if the
  url has an authority, "/%%%%2f" is used for ftp only (#163784)
- rev 3062
* Tue Apr 11 2006 jsrain@suse.de
- fixed storing patch scripts to target store (#159928)
- rev 3058
* Tue Apr 11 2006 kkaempf@suse.de
- if a patch is bad, only skip this patch, not everything
  (#165200)
- rev 3057
* Tue Apr 11 2006 ma@suse.de
- Susetags:Selections: Allow parsing older .sel file formats. (#159851)
- Susetags:Pattern: Fixed parser.
* Tue Apr 11 2006 kkaempf@suse.de
- when uninstalling, only re-establish installed items
  supplementing the to-be-uninstalled one. (variant of #165111)
- rev 3054
* Tue Apr 11 2006 ma@suse.de
- Susetags:Package: Parse and provide ins/delnotify texts.
* Tue Apr 11 2006 kkaempf@suse.de
- when checking freshens/supplements at install, only consider
  best architecture/edition (#164453)
- rev 3051
* Tue Apr 11 2006 kkaempf@suse.de
- when checking for supplements, only consider best arch, best
  edition for installation (#165111)
- rev 3047
* Tue Apr 11 2006 schubi@suse.de
- Bug 165117: build 910: Update: Splitted packages are selected for
  all archs
* Tue Apr 11 2006 visnov@suse.cz
- ask user if a file exists but does not have a checksum (#162797)
- rev 3044
* Mon Apr 10 2006 jsrain@suse.de
- parse time and size elements from delta and patch RPM
- rev 3043
* Mon Apr 10 2006 mt@suse.de
- Added detection of iSeries virtual CD (/dev/iseries/vcd[a-h])
  devices - on powerpc only (#163971)
- rev 3042
* Mon Apr 10 2006 kkaempf@suse.de
- fix endless loop in patches parsing.
- rev 3039
* Mon Apr 10 2006 jsrain@suse.de
- fixed media handling in SuSEtags source (#164879)
- rev 3037
* Mon Apr 10 2006 kkaempf@suse.de
- honor 'dry_run' on package remove (#164732)
- rev 3036
* Mon Apr 10 2006 kkaempf@suse.de
- add files from yum filelist as provides to package (#164731)
- rev 3032
* Mon Apr 10 2006 kkaempf@suse.de
- honor "+Enh:/-Enh:" in packages file (#156513)
* Mon Apr 10 2006 visnov@suse.cz
- fix callback receiver signature to match the callback for removing
  package
* Mon Apr 10 2006 mvidner@suse.cz
- Added Product::updateUrls, from content/UPDATEURLS (#163192).
- rev 3024
* Sat Apr  8 2006 schubi@suse.de
- Bug 164440; Taking wrong architecture while updating obsoletes
  splitted packages
- rev 3022
* Sat Apr  8 2006 kkaempf@suse.de
- allow relative paths with url file:
- dont filter atoms from going into pool, multi-arch patch
  requirements need them. Instead, treat atoms with incompatible
  architecture as unneeded.
- rev 3018
* Fri Apr  7 2006 jsrain@suse.de
- product now provides short name
- rev 3013
* Fri Apr  7 2006 jsrain@suse.de
- read metadata for packages from correct tags in patches (#163220)
- rev 3011
* Fri Apr  7 2006 kkaempf@suse.de
- more detailed resolver error reports (#162994)
- rev 3010
* Fri Apr  7 2006 visnov@suse.cz
- report package download progress (#160966)
- rev 3007
* Fri Apr  7 2006 kkaempf@suse.de
- transact also for languages (#163819)
- rev 3004
* Fri Apr  7 2006 kkaempf@suse.de
- loop through all affected ResObjects in transactResKind (#163819)
- rev 3002
* Fri Apr  7 2006 kkaempf@suse.de
- allow re-installation of non-packages (#162906)
- rev 2998
* Fri Apr  7 2006 mt@suse.de
- Added loop checking for scsi cdroms (/sys/block/srX) in case
  HAL does not provide any drives like on iSeries (#163971).
- rev 2995
* Fri Apr  7 2006 kkaempf@suse.de
- add 'licenceToConfirm()' to Product. (#164375)
* Fri Apr  7 2006 ma@suse.de
- Avoid excessive CD hopping on commit. But still far from
  being perfect. (#159679)
- Fixed Target::commit: Despite dry_run set True, packages
  were depeted.
* Fri Apr  7 2006 visnov@suse.cz
- honour if user decides to skip a package in commit (#156031)
* Thu Apr  6 2006 jsrain@suse.de
- fixed parsing external reference to script in patch (#163221)
- r2981
* Thu Apr  6 2006 dmacvicar@suse.de
- cache and provide content.asc/key optionally. Dont show a
  popup if they dont exists. (dmacvicar)
- Actually abort when verify signature workflow is false. (dmacvicar)
- r2978
* Thu Apr  6 2006 jsrain@suse.de
- fixed setting autorefresh flag for installation sources
* Thu Apr  6 2006 kkaempf@suse.de
- drop patches with incompatible architecture.
- rev 2972
* Thu Apr  6 2006 mt@suse.de
- Added info method to media verifier base and more debug info
- rev 2970
* Wed Apr  5 2006 kkaempf@suse.de
- Dont deny the "/" attach point in MediaDIR, since this is used
  for all "file:" urls, esp. local packages.
- rev 2962
* Wed Apr  5 2006 schubi@suse.de
- Bug 159673 - only one conflict solvable per page
* Wed Apr  5 2006 kkaempf@suse.de
- parse all dependencies of 'packages' file (#163773)
- rev 2957
* Wed Apr  5 2006 dmacvicar@suse.de
- Use the original media descr_dir on refresh for
  suse tags source (#163196)
- r2952
* Wed Apr  5 2006 kkaempf@suse.de
- add Source::setUrl() for zmd backend helper.
- rev 2946
* Wed Apr  5 2006 dmacvicar@suse.de
- implement rpm keyring / zypp tmp keyring two-way syncronization at rpm
  target init. (dmacvicar)
- r2949
* Wed Apr  5 2006 mt@suse.de
- Fixed MediaDISK to use a mount -oro,bind id the disk
  partition is already attached e.g. by the automounter.
  Try to mount it a second time may fail (#163486).
- rev 2944
* Wed Apr  5 2006 kkaempf@suse.de
- honor optional 3rd parameter to "=Loc:" key of packages (#154337)
- rev 2940
* Wed Apr  5 2006 visnov@suse.cz
- only try to create a source of a given type when restoring
  from the persistent store (#162111)
* Wed Apr  5 2006 kkaempf@suse.de
- parse all dependencies for patterns (.pat) files (#160602)
- drop YOUPATH and YOUURL from content file.
- rev 2924
* Wed Apr  5 2006 visnov@suse.cz
- properly initialize autorefresh for non-remote sources (#154990)
- rev 2919
* Tue Apr  4 2006 mt@suse.de
- Added flag to MediaManager::isUseableAttachPoint, whether
  to check against system mount entries or not.
- Disallow to use the attachpoints of another media handlers
  as source path in MediaDIR.
- rev 2917
* Tue Apr  4 2006 dmacvicar@suse.de
-implement callbacks for when package verification (checksum)
  fails, offer to retry or abort
* Tue Apr  4 2006 dmacvicar@suse.de
- Fix construction of checksum objects when using non-standard
  checksum algorithms
- Fix broken YUM cache
- r2913
* Tue Apr  4 2006 kkaempf@suse.de
- Keep packages with no version upgrade installed during
  distribution upgrade (#162972)
- add 'transactReset()' helper function for UI.
- rev 2908
* Tue Apr  4 2006 dmacvicar@suse.de
- r2906
* Tue Apr  4 2006 ma@suse.de
- Fixed candidate handling in ui::Selectable. (#156589)
* Tue Apr  4 2006 dmacvicar@suse.de
- fix #162984 , gpg hangs because the matching data file
  for the key cannot be find. (dmacvicar)
- Fix restore of YUM source using the same cache dir semantics as
  susetags instead of assuming there is a cache if a cache_dir
  was given. (dmacvicar)
* Tue Apr  4 2006 kkaempf@suse.de
- use DISTPRODUCT/DISTVERSION from content file to generate the
  product name, version, and release.
- rev 2902
* Mon Apr  3 2006 mt@suse.de
- Removed broken forcing of absolute ftp paths added in rev2705 to
  MediaCurl, refined cleanupPathName/setPathName in url (#154197).
- rev 2900
* Mon Apr  3 2006 kkaempf@suse.de
- add Resolver::freshenPool() (#156980)
- rev 2893
* Mon Apr  3 2006 kkaempf@suse.de
- skip incompatible archs in filelist parsing.
- restrict pathes to 'interesting' ones (/bin/, /sbin/, /lib/,
  /lib64/, ...)
- rev 2886
* Sun Apr  2 2006 kkaempf@suse.de
- skip incompatible archs in primary parsing.
- rev 2883
* Sun Apr  2 2006 kkaempf@suse.de
- allow setting of source when parsing local .rpm (#147765)
- rev 2880
* Fri Mar 31 2006 schubi@suse.de
- Do not update packages over other architectures
* Fri Mar 31 2006 sh@suse.de
- Added zypp/ui/UserWantedPackages to support the UI's
  "automatic changes" dialog (bug #152700)
* Fri Mar 31 2006 jsrain@suse.de
- use KeyRing class to validate repomd.xml (#160909)
* Fri Mar 31 2006 dmacvicar@suse.de
- Product resolvables should be readable by normal users.
  (#162474) (dmacvicar)
- implemented keyring and metadata signature verification
  in susetags source
- dont delete the lock if we did not acquire it
- r2847
* Fri Mar 31 2006 mt@suse.de
- Added disabling of the automounter while MediaManager
  init and restoring of the old state on exit (#154326).
- Implemented check if media (CD) is automounted or not
- rev 2840
* Fri Mar 31 2006 mt@suse.de
- Implemented several hal get/set/removeDeviceProperty wrappers
- Improved HalException to allow to fetch HAL/DBUS error componets
- rev 2830
* Fri Mar 31 2006 kkaempf@suse.de
- honor subscription status of catalogs (#162350)
- rev 2827
* Fri Mar 31 2006 mt@suse.de
- Enabled CD eject error reporting exceptions (#154326)
- rev 2822
* Fri Mar 31 2006 kkaempf@suse.de
- support "dry run" (#159467)
- implement "transactResKind" (#161400)
- rev 2817
* Thu Mar 30 2006 jsrain@suse.de
- add checksum for external patches (#159928)
* Thu Mar 30 2006 kkaempf@suse.de
- calculate product architecture (#158198)
* Wed Mar 29 2006 jsrain@suse.de
- fixed checking checksum of YUM metadata, added sha1 vs. sha256
  detection
* Wed Mar 29 2006 ma@suse.de
- Auto protect installed packages from unknown vendor. (#157446)
* Wed Mar 29 2006 visnov@suse.de
- added support for external scripts to metadata (#159928) (jsrain)
- fixed handling of Language resolvables (ma)
- fix leak in rpmdb (dmacvicar)
- added softlock for autoyast (#159466) (ma)
- Fixed exceptions in doGetFileCopy() to show full url
  including the file instead of just the media base url. (mt)
- Provide Language::summary (ma)
- check patterns and selections file exist
  before veryfing them (#161300) (dmacvicar)
- added YUM metadata checksum computation (jsrain)
- added interface to patch of a message (jsrain)
- r2734
* Mon Mar 27 2006 jsrain@suse.de
- added support for external scripts to metadata (#159928)
- r2709
* Sat Mar 25 2006 jsrain@suse.de
- report separate exception when trying to start source cache again to
  suppress incorrect error message in XEN installation
- r2682
* Fri Mar 24 2006 schubi@suse.de
- Implement inter process locking in zypp.
- Added No medium found output
- splitting modaliases in supplements TOO
- parse also the available signing keys
* Fri Mar 24 2006 visnov@suse.cz
- release all media when removing source (#159754) (visnov)
- more testsuites (schubi)
- updated translations (schubi)
- added MediaNotEjectedException (mt)
- rev 2652
* Thu Mar 23 2006 dmacvicar@suse.de
- fix patches descriptions (dmacvicar)
- fix source serialization (dmacvicar)
- metadata for kernel test (schubi)
- Arch tests updated (ma)
- classify NULL Ptr as unique (ma)
- Added host check, because file Url allows it now. (mt)
- prepare modalias fix (#159766) (ma)
- Provide iterator based access to SourceManager data. (ma)
- Fixed "file:" Url scheme config to allow relative paths; (mt)
  RFC1738 says, it may contain a hostname as well...
- revision 2633
* Wed Mar 22 2006 visnov@suse.cz
- pkg-config support (mvidner)
- close all medias when destructing MediaSet (jsrain)
- rev 2622
* Wed Mar 22 2006 dmacvicar@suse.de
- Bug 159976 - build 804: Adding AddOn CD via ftp gives error (dmacvicar)
- Message callback implemented to show patch messages (visnov)
- Bug 159696 (schubi)
- provide transform_iterators to iterate over a maps keys or values (ma)
- added 'bool Arch::empty() const' test for an empty Arch string (ma)
- added script and message installation (jsrain)
- chooses the 'right' kernel now (kkaempf)
- Use noarch if no arch is specified in patches (dmacvicar)
- rev 2611
* Tue Mar 21 2006 mvidner@suse.cz
- Added some debug output including the access id (mt)
- Bug #154326: Enabled FORCE_RELEASE_FOREIGN flag causing
  release with eject=true on attached media, to umount
  other mounts as well. (mt)
- 159483 - solver does not blame missing dependency (schubi)
- Added a variant of MediaHandler::forceRelaseAllMedia (ma)
- Fixed MediaCD::forceEject() to handle DELAYED_VERIFY
  and use forceRelaseAllMedia if FORCE_RELEASE_FOREIGN=1 (ma)
- fixed ZYPP_RETHROW (#156430) (ma)
- patch for #156114 (visnov)
- fixed container.erase loops (ma)
- Fixed to reset desired (cached) flag before the action (mt)
- Removed return in forceRelaseAllMedia (void function) (mt)
- Parse nonexisting architecture to noarch so patches dont get
  filtered by the pool (dmacvicar)
- 159512 - yast2-qt does not show label of to be installed products
  anymore (dmacvicar)
- 159765 - Hidden patterns still visible (dmacvicar)
- Use noarch if no arch is specified. (dmacvicar)
- r2594
* Tue Mar 21 2006 visnov@suse.de
- properly report error for media change callback
- rev 2579
* Mon Mar 20 2006 ma@suse.de
- fixed memory leak in XMLNodeIterator (#157474)
- disabled storing filelist (YUMFileListParser) and changelog (YUMOtherParser)
- Renamed private MediaManager::forceMediaRelease
  function to forceReleaseShared (more exact name)
- Implemented forceRelaseAllMedia() that can be
  used to release also foreign (user) mounts.
- Added use of forceRelaseAllMedia for CD/DVDs
  if FORCE_RELEASE_FOREIGN is 1 (default 0)
- little cleanup of the checkAttached function
- r2578
* Mon Mar 20 2006 mvidner@suse.cz
- don't try to attach without exception handling (#158620)
- fix descriptions, as a new tag Des for selections exists now.
- fix #157683: failure after adding add-on product to install
  sources
- added more files for translation
- resolve-dependencies.cc: establish pool
- parse-metadata.cc: catch bad URL
- set zmdid for atoms
- r2574
* Sun Mar 19 2006 kkaempf@suse.de
- fix testsuite.
- provide edition and architecture for all kinds of yum
  resolvables.
- fix ResStatus output.
- establish atoms correctly.
- treat requires to unneeded resolvables as fulfilled.
- rev 2559
* Sun Mar 19 2006 kkaempf@suse.de
- fix the build
- only consider best architecture/version (#157594)
- prefer providers which supplement/enhance installed or
  to-be-installed packages (fixes the tpctl-kmp issue)
- rev 2546
* Sat Mar 18 2006 kkaempf@suse.de
- provide more filters for pkg-bindings (#158602)
- add SystemResObject to provide system (modalias, hal, ...)
  capabilities.
- handle this during resolving.
- make the modalias and hal capability match the SystemResObject
  by default, thereyby triggering a modalias (resp. hal)
  evaluation.
- xmlstore: decouple target store from YUM schema.
- clean up moving of hal() and modalias() from provides to
  supplements in ResolvableImpl.
- add PatchContents() for UI.
- handle Edition::noedition as empty string.
- r2537
* Tue Mar 14 2006 jsrain@suse.de
- releasing all medias when asking for CD (#156981)
- r2471
* Tue Mar 14 2006 mvidner@suse.cz
- ResStatus::resetTransact must return a value.
- Fixed random build failures in LanguageCode.cc.
  (Rewrote the CodeMaps constructor so that gcc does not
  optimize a 500-statement basic block.)
- Fix constructions of patch objects. Actually insert atoms in atoms
  list. Insert atoms for package even if the package does not exists
  in the source. Fixes #157628 (dmacvicar).
- Fixed license reading from susetags, #151834 (dmacvicar).
- r2468
* Tue Mar 14 2006 mvidner@suse.cz
- added ResStatus::resetTransact (ma)
- bugfix for #156439 (schubi)
- Added Source_Ref::setAlias (#154913).
- Do not assume there is a product file when scanning for products
  (visnov)
- function to disable all sources in the persistent store (visnov)
- dependency errors go to stdout, not stderr; output resolver info
  directly to stderr (kkaempf)
- rev 2464
* Tue Mar 14 2006 kkaempf@suse.de
- fix merging of resolver info (needed for #157684).
- errors are also important in ResolverInfo.
- improve debug output in ResolverContext.
- rev 2455
* Mon Mar 13 2006 jsrain@suse.de
- delete RPMs downloaded via HTTP/FTP after installnig them
  (#157011)
- fixed product registration (reverted autorefresh patch) (#157566)
* Mon Mar 13 2006 kkaempf@suse.de
- if root!="/", always prefer the upgrade candidate (#155472)
- implement license confirmed api for UI.
- prefer architecture over version in distribution upgrade
  (#157501)
- clean up media handling.
- rev 2448
* Sun Mar 12 2006 kkaempf@suse.de
- init Modalias properly.
- fix warnings in testcases.
- rev 2432
* Sat Mar 11 2006 kkaempf@suse.de
- drop libjpeg-devel and sqlite-devel from build requires.
* Sat Mar 11 2006 kkaempf@suse.de
- implement 'modalias()' capability (#157406)
- make dependencies consistent, its 'freshens'.
- cope with user umounts of devices.
- add debug to SourceManager.
- rev 2418
* Fri Mar 10 2006 kkaempf@suse.de
- allow version downgrade during distribution upgrade if the
  newer package is coming from a trusted vendor (#155472)
- implement locale fallback
- 'freshen' -> 'freshens' in schema definitions to make it
  consistent with all other dependency definitions.
- better error reporting for .pat and .sel files.
- rule out packages from dependency resolutions which are
  de-selected by user (#155368)
- use locale fallbacks in package translations.
- refresh source when re-enabling it.
- rev 2406
* Tue Mar  7 2006 kkaempf@suse.de
- split of libzypp-zmd-backend subpackage as a stand-alone
  leaf package.
- encapsulate bool test for Source_Ref better.
- fixed stack overflow (ma).
- make testsuite build again.
- rev 2346
* Tue Mar  7 2006 kkaempf@suse.de
- fixed URL rewriting for CD2 and following (#154762)
- fixed ResPoolProxy diffState (for proper ok/cancel support
  in UI)
- added special exception class for aborting installation
  (#154936)
- only auto-change directories if they end in CDn or DVDn.
- rev 2320.
* Tue Mar  7 2006 kkaempf@suse.de
- silently ignore multiple installs of the same package.
- fix disk usage for installs and uninstalls.
- rev 2308
* Mon Mar  6 2006 kkaempf@suse.de
- zmd-backend: filter out incompatible architectures from
  repository.
- rev 2298
* Mon Mar  6 2006 kkaempf@suse.de
- sync libzypp media data with mtab.
- improve resolver error and solution reports.
- fix source cache reading (#155459).
- default cached sources to enabled (#155459).
- let each source provide public keys.
- rev 2297
* Sun Mar  5 2006 kkaempf@suse.de
- only write by-sovler transactions back (#154976)
- rev 2278
* Sat Mar  4 2006 kkaempf@suse.de
- release last used source at end of commit (#155002)
- rev 2277
* Fri Mar  3 2006 kkaempf@suse.de
- cope with NULL values in zmd catalogs table (#153584)
- set YAST_IS_RUNNING in transact zmd helper (#154820)
- run SuSEconfig after transact zmd helper (#154820)
- add softTransact to honor user vs. soft requirements (#154650)
- honor all build keys provided by a package source.
- add source metadata refresh.
- add progress callbacks to zmd helpers.
- rev 2276
* Thu Mar  2 2006 kkaempf@suse.de
- include .diffs into main source.
- catch exception when ejecting media which was unmounted externally
  (#154697).
- init source in zmd-backend correctly (#154667)
- implement disk usage info for YaST.
- clean up XML schema files.
- catch CPUs identifying as 'i686' but being 'i586'.
- allow definition of preferred attach (mount) point for media.
- make resolver results more readable.
- use language fallbacks if none of multiple language providers
  matches.
- get rid of ignoring wrong arch in resolver, having the wrong
  architecture is prevented by other means.
- prepare for translations in exceptions.
- fix 'abort does not abort'
- implement 'flag' I/O in target cache backend.
- skip incompatibles architectures in packages.<lang>
- rev 2228
* Thu Mar  2 2006 kkaempf@suse.de
- dont even provide src/nosrc from the source.
- rev 2169 + diffs
* Wed Mar  1 2006 kkaempf@suse.de
- Initialize commit result (#154409)
- release media if its wrong (#154326)
- dont copy src/nosrc packages to the pool (#154627)
- reduce XML logging.
- rev 2169 + diffs
* Tue Feb 28 2006 kkaempf@suse.de
- fix path of .po files (#154074).
- parse the correct package.<lang> file (kinda #154074).
- complain about bad "=Sel:" or "=Pat:" lines (#153065).
- reattach all released medias.
- raise exception instead of abort() on XML errors (#154104).
- update translations.
- PathInfo: implemented a copy_dir_content (variant of copy_dir)
  and is_empty_dir utility function
- rev 2169
* Tue Feb 28 2006 kkaempf@suse.de
- check freshens and supplements for packages (#154074).
- only complain about incomplete installed resolvables,
  if they are uninstalled, schedule them for installation.
  (#154074)
- add testcases for locale() provides.
- add lang_country -> lang fallback.
- have locale(parent:...) deps match any provides of 'parent'
  also when uninstalling a package.
- rev 2148
* Tue Feb 28 2006 kkaempf@suse.de
- change the locale(...) separator to ";" (#153791)
- complete "find-files" of zmd-backend.
- rev 2140
* Tue Feb 28 2006 visnov@suse.de
- avoid attaching media when initializing source
- rev 2139
* Mon Feb 27 2006 kkaempf@suse.de
- warn about misspelled 'locale(...)' provides
- add testcases
- rev 2134
* Mon Feb 27 2006 kkaempf@suse.de
- fix the build
- rev 2129
* Mon Feb 27 2006 kkaempf@suse.de
- provide available locales to application (#153583)
- honor 'requestedLocales' (language dependant packages)
- honor release requests for all holders of a device.
- silently re-attach after a forced release.
- solver improvements.
- handle source caches.
- proper logging in zmd backend helpers.
- rev 2127
* Mon Feb 27 2006 kkaempf@suse.de
- upgrade always to best version and arch (#153577)
- reset 'transact' state for obsoleted packages (#153578)
- translation updates
- rev 2113
* Mon Feb 27 2006 kkaempf@suse.de
- add support for 'local' .rpm packages to zmd-backend.
- rev 2101
* Sun Feb 26 2006 kkaempf@suse.de
- fix build of zmd/backend.
- actually fill 'files' table in package-files.
- rev 2094
* Sun Feb 26 2006 kkaempf@suse.de
- improve testcases.
- add 'setPossibleLocales()' to ZYpp, this defines the set
  of possible locales to choose from (#153583)
- provide LanguageImpl and create 'Language' resolvables for
  each 'possible' locale.
- fix YUM parsing of patches, insert 'atoms' to link patches
  with packages.
- replace gzstream/ with own, existing implementation.
- honor locks in solver (#150231)
- sync pool with target after commit() properly (#150565, #153066)
- new zmd helper 'package-files'
- rev 2093
* Thu Feb 23 2006 kkaempf@suse.de
- prevent multiple initializations of the target (#153124)
- implement 'loopback mounted ISO images'
- retain old package sources on upgrade.
- support compressed .xml files in 'repodata' type repositories.
- rev 2025
* Thu Feb 23 2006 kkaempf@suse.de
- parse locale(...) provides and construct correct dependencies.
* Thu Feb 23 2006 kkaempf@suse.de
- always upgrade to candidate (#152760).
- fix typo in package sorting.
- prepare handling of locale provides.
- rev 1995
* Thu Feb 23 2006 kkaempf@suse.de
- sort src/nosrc package to right list during commit.
- revert installtime/buildtime in susetags parser (#152760)
- rev 1990
* Thu Feb 23 2006 kkaempf@suse.de
- reset state after successful commit (#153030)
- run "rpm -e" always with "--nodeps" (#153026)
- provide separate resolvable kind for src packages.
- extend status field for LOCK and LICENSE.
- add sameState()/diffState() for UI.
- provide 'best' candidate for UI.
- set 60 sec timeout for curl access.
- don't cross-compare solver results, takes too much time.
- provide sizes of installed packages.
- extend REQUIRES semantics in content file.
- add "parse-metadata" helper to zmd-backend.
- rev 1987
* Wed Feb 22 2006 kkaempf@suse.de
- provide complete disk usage data (#152761)
- include upgrade flag when copying solver solution
  back to pool (#152717)
- rev 1959
* Wed Feb 22 2006 kkaempf@suse.de
- don't insert incompatible architectures to the pool (#151933)
- don't accept incompatible architectures from a repository
  (#151933)
- separate rpm log (#151431).
- allow extended product requires.
- rev 1954
* Tue Feb 21 2006 kkaempf@suse.de
- provide the XML schema files in the main package. (#152593)
* Tue Feb 21 2006 kkaempf@suse.de
- provide arch compat handling.
- implement data upload to zmd.
- fix source metadata caching on target.
- add 'supplements' dependencies to 'yum' parser.
- provide user agent identification to curl calls.
- move resolver branches (multiple alternatives) back in queue
  (resolve known things first, then the unknown ones).
- clean up 'packages' parser.
- rev 1947
* Tue Feb 21 2006 kkaempf@suse.de
- improve media mount/umount interface
- prepare class ArchCompat for proper architecture ordering
  and compatibility handling.
- add returns to dummy functions in DbAccess.
- rev 1913
* Mon Feb 20 2006 kkaempf@suse.de
- don't explictly delete to-be-upgraded packages.
- finish query-system, resolve-dependencies, and transact for
  libzypp-zmd-backend.
- provide Pattern::category.
- move system architecture to toplevel.
- make target store pathname settable.
- speed up rpmdb reading by properly filtering unwanted file
  provides.
- rev 1905
* Sun Feb 19 2006 kkaempf@suse.de
- new translations.
- proofread texts.
- when comparing solutions, prefer higher versions.
- provide generic 'SafeBool' for bool conversions.
- add PtrTypes testsuites.
- rev 1876
* Fri Feb 17 2006 kkaempf@suse.de
- integrate all diffs
- move Target::commit to toplevel API
- generalize dependency iterators and hash dependency
  information in pool (for speedup)
- add 'supplements' as dependency
- make more pattern attributes available
- drop "smbfs" in favour of "cifs" (#151476)
- add metadata cache to sources (Beta4 bug)
- run "rpm -e"  with name-version-release
- fix update conflicts
- rev 1864
* Thu Feb 16 2006 kkaempf@suse.de
- fix-mediachange.diff: dont skip CD but retry after media change
- cd-eject-button.diff: fix CD url so YaST recognizes it and shows
  'eject' button
- release-forced-eject-no-ptrfix.diff: fix refcounting in ptrs
  so media handle gets actually released and media unmounted.
* Thu Feb 16 2006 kkaempf@suse.de
- implement arch scoring
- prefer better arch (#151427)
- transitive depedencies of weak requirements are non-weak
  (#151446)
- rev 1778 + diff
* Wed Feb 15 2006 kkaempf@suse.de
- ignore self and to-be-updated conflicts (#150844)
- fix enable of target store (for non-packages)
- rev 1778
* Wed Feb 15 2006 kkaempf@suse.de
- fix "cd:" url (#151121)
- provide location() in public Package api
- allow running distribution upgrade in testmode
- extend HAL interface
- rev 1762
* Wed Feb 15 2006 kkaempf@suse.de
- pass normal and locale packages from selections correctly.
- its "baseconf" for base selections.
- Make 'ZYpp' an obvious singleton.
- provide releasenotesUrl.
- dont continue upgrade without target.
- implement 'fake' hal for testing.
- fix package sizes.
- more solver testcases.
- rev 1754
* Tue Feb 14 2006 kkaempf@suse.de
- extend requires of libzypp-devel
- provide package sizes for UI
- provide more UI helpers
- implement Product and related functions
- fix split provides in distribution upgrade
- provide locale information to system
- ask HAL for available devices
- reduce debug information in solver
- filter architectures in source, not in solver
- rev 1743
* Tue Feb 14 2006 visnov@suse.de
- disable another testsuite for now
- fetch the default locale from environment
- support user-defined formatting of log
- rev 1710
* Mon Feb 13 2006 visnov@suse.de
- providing basic product information from susetags source
- public API for preferred language
- implemented redirect of logging (#149001)
- report start/finish of source data parsing (#150211)
- store/restore source aliases properly (#150256)
- disable a lot of debug logging to speed up solver
- properly rewrite URL for CDn directory layouts (#149870)
- rev 1706
* Sun Feb 12 2006 kkaempf@suse.de
- add save/restore state to facilitate UI 'cancel'
- enable target/store
- add 'forceResolve' call and flag to resolver to switch between
  task-oriented ZMD and interactive YaST behaviour.
- Fix resolver problem solution texts.
- improve solver problem solution offerings.
- fix media access handling to better support multiple
  requestors to single media.
- move the media number checking to the source (media requestor)
  which knows how to verify the correct media.
- Fix CD ordering (#149871), adding testcases.
- Move 'PoolItemList' and 'PoolItemSet' typedefs inside classes.
- Add selections to testcases.
- rev 1673
* Sat Feb 11 2006 kukuk@suse.de
- Fix missing return in Source.cc:124
* Fri Feb 10 2006 kkaempf@suse.de
- cope with empty arch field in selections
- enable dummy "enableStorage" function
- rev 1610-branch
* Fri Feb 10 2006 kkaempf@suse.de
- fix random data return in Source.cc
- rev 1610
* Fri Feb 10 2006 kkaempf@suse.de
- adapt zmd-backend to SourceImpl API change
- rev 1608
* Fri Feb 10 2006 kkaempf@suse.de
- fix the packages parser bug. Now all packages are parsed
  including (english) translations.
  source/susetags is back to svn head.
- rev 1600
* Fri Feb 10 2006 kkaempf@suse.de
- fix off-by-one bug in bitfield handling
- revert source/susetags to rev 1411
- rev 1586
* Thu Feb  9 2006 kkaempf@suse.de
- dont prereq-sort non-packages
- rev 1584
* Thu Feb  9 2006 kkaempf@suse.de
- rev 1582
* Thu Feb  9 2006 kkaempf@suse.de
- update to rev 1543
* Thu Feb  9 2006 ro@suse.de
- require hal-devel in libzypp-devel
- re-merge fixes (RPM_OPT_FLAGS)
* Wed Feb  8 2006 kkaempf@suse.de
- make solver behaviour a bit more interactive
- rev 1537
* Wed Feb  8 2006 schwab@suse.de
- Fix syntax error in configure script.
- Use RPM_OPT_FLAGS.
* Wed Feb  8 2006 kkaempf@suse.de
- update for qt ui integration
- rev 1504
* Tue Feb  7 2006 kkaempf@suse.de
- split off libzypp-zmd-backend
- rev 1466
* Tue Feb  7 2006 kkaempf@suse.de
- another update to svn
* Mon Feb  6 2006 kkaempf@suse.de
- finish rpm callbacks
- finish UI API
- fix state change resolver<->pool
- zmd backend stuff
- speed up tag file parsing
- rev 1405
* Mon Feb  6 2006 schubi@suse.de
- disabling failing tests of s390 and ppc
* Mon Feb  6 2006 schubi@suse.de
- Snapshoot rev 1367
* Mon Feb  6 2006 kkaempf@suse.de
- use hashes for pool
- rev 1343
* Fri Feb  3 2006 schubi@suse.de
- removed Obsoletes:    yast2-packagemanager
* Fri Feb  3 2006 schubi@suse.de
- Snapshoot 3 Feb 2005 (11:30)
* Thu Feb  2 2006 schubi@suse.de
- Snapshoot 2 Feb 2005 (14:00)
* Thu Feb  2 2006 schubi@suse.de
- Snapshoot 2 Feb 2005 ( integrating YaST )
* Wed Jan 25 2006 mls@suse.de
- converted neededforbuild to BuildRequires
* Sat Jan 14 2006 kkaempf@suse.de
- Initial version
