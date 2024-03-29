Name:       spectacle-tools
Summary:    RPM Spec file generator and management tool
Version:    0.33
Release:    1
Group:      Development/Tools
License:    GPLv2+
BuildArch:  noarch
URL:        https://github.com/sailfishos/spectacle
Source0:    https://github.com/sailfishos/spectacle/archive/refs/tags/%{version}.tar.gz#/spectacle-%{version}.tar.gz
Source1:    autospectacle.pl
Source100:  spectacle.yaml
Requires:   PyYAML
Requires:   python3-urlgrabber
Requires:   python3-cheetah
Requires:   perl
BuildRequires:  python3-devel
BuildRequires:  python3-cheetah

%description
Spectacle is the toolset for packaging maintenance of MeeGo, including the tool
to generate spec files from metadata file in YAML format, and tools to convert
spec files or spec-builder's ini files to YAML format.

For spectacle managed packages, all generic packaging information will be stored
in the YAML file, and it also allows maintaining customizations in the spec file
directly with special enclosure tags.

Three separated tools will be installed:
* specify: the tool to generate or to update spec file, based on YAML
* ini2spectacle: the tool to convert spec-builder .ini to YAML and new spec file
* spec2spectacle: the tool to convert original spec to YAML and new spec file

%prep
%setup -q -n spectacle-%{version}

%build
make tmpls
CFLAGS="$RPM_OPT_FLAGS" python3 setup.py build

%install
rm -rf $RPM_BUILD_ROOT
python3 setup.py install --root=$RPM_BUILD_ROOT --prefix=%{_prefix}
make install-data DESTDIR=${RPM_BUILD_ROOT}
install -m 0755 %{SOURCE1} ${RPM_BUILD_ROOT}%{_bindir}

sed -i 's|/usr/bin/python -tt|/usr/bin/python3 -tt|' %{buildroot}%{_bindir}/*

%files
%doc README.md AUTHORS COPYING TODO
%doc examples/
%dir %{_datadir}/spectacle
%{_datadir}/spectacle/*
%{_bindir}/*
%{python3_sitelib}/*

%changelog
* Sun Oct 30 2022 Wei-Lun Chao <bluebat@member.fsf.org> - 0.33
- Rebuilt for Fedora
* Mon Jul  2 2012 Marko Saukko <sage@merproject.org> - 0.25
- Release 0.25
- Fixes MER#192: Spectacle version check should be removed
- Fixes MER#388: Remove packaging-tools warning from 'specify' call
- Fixes MER#402: Option to specify which package gets %%find_lang file list
- Fixes BMC#15189: If the file is not available remove the created 0 size file.
* Tue Jun  5 2012 Marko Saukko <sage@merproject.org> - 0.24.1
- Update to version 0.24.1
* Mon May 21 2012 Marko Saukko <sage@merproject.org> - 0.24
- Update to version 0.24
* Mon Oct 10 2011 Jian-feng Ding <jian-feng.ding@intel.com> - 0.23
- Release 0.23, with the following changes:
  - Support auto %%post* scripts for systemd services
  - New tool deb2spectacle to convert deb packages to rpm
  - Arch specifying support for "Files"
  - Enhance cmake support
  - And the following bugs were fixed:
  - BMC#15643: *.desktop in subpkg cannot trigger auto-handling
  - BMC#15013: squeeze out all empty values from list key
  - BMC#18173: Added error checks for placeholders validity in spec file
  - BMC#23539: more precise req for Icon %%post handling
* Fri Feb 25 2011 Jian-feng Ding <jian-feng.ding@intel.com> - 0.22
- Release 0.22, with the following changes:
  - Enhanced arch namespace support, more precise expand values for arm
    ix86 => "%%{ix86}"
    arm => "%%{arm}"
    armv5 => "armv5el armv5tel armv5tejl"
    armv7 => "armv7el armv7tel armv7l armv7hl armv7nhl"
  - "autogen" as the "Configure" will run "./configure automatically
  - More friendly warning message for YAML syntax errors (BMC#11262, BMC#11766)
  - Data file GROUPS and pkgconfig-provides.csv were updated to latest
  - No keyword "NoIconCache" to avoid inserting 'gtk-update-icon-cache' lines
  - Let keyword "Description" to be mandatory and more strict checking
  - And the following bugs were fixed:
  - BMC#10495: handling of tarfile and its filename
  - BMC#11166: Added missing initialize extra flags for AutoSubPackages
  - BMC#11619: skip %%exclude files in when it parse extras from filelists
  - BMC#12975: need not gtk-update-icon-cache for Qt based pkg
  - BMC#12235: crash with subpkg without Name
  - BMC#12720: crash with empty %%files section in .spec
  - BMC#11661: more generic services files matching
* Wed Nov 24 2010 Jian-feng Ding <jian-feng.ding@intel.com> - 0.21
- Release 0.21, with the following changes:
  - More precise version comparison according MeeGo packaging guideline
  - Full support of AutoReq/AutoProv/AutoReqProv spec directives in specify
    and spec2spectacle
  - Monitor and warning for GPLv3 like licenses
  - New YAML template for the convenience of new packages
  - Option to append new sub-package to exist YAML file automatically
  - Distinguish different source of logger output
  - Cleanup for "print" statement, for better py3k compatibility
  - Change "RunFdupes" to a list key
* Sat Sep 18 2010 Jian-feng Ding <jian-feng.ding@intel.com> - 0.20
- Release 0.20, with the following changes:
  - Support new %%qmake rpm building macros for builder "qmake"
  - Add "QMakeOptions" for extra options for "qmake" builder
  - Architecture tags supported
  - Changed the applying rule of "UpdateDesktopDB": insert scripts
    in spite of whether *.desktop found
  - Help to generate packaging Makefile from template if not exists
  - Query to cleanup old tarballs after auto-downloading
  - README and test cases were updated according changes
* Mon Aug 23 2010 Jian-feng Ding <jian-feng.ding@intel.com> - 0.19
- Release 0.19, with the following changes:
  - Fixed bugs in non-ASCII chars handling
  - Fixed bugs in output path options
  - Support new builder: 'cmake'
  - More warnings for invalid YAML values:
  - Lower version running spectacle detected
  - User to use 'setup.py install' to install, warning and abort
  - Invalid configure settings for some special builders
  - Warning for "new" spec file
  - Warning for "Epoch" keyword
  - Duplicate "rm -rf %%{buildroot}" similar lines
  - Several bugs in subpkg available keys warning fixed
  - New header lines in generated spec to avoid misleading
  - Rewrote color text output code to drop third-party GPLV3 module
  - Accept alternative types for the following cases:
  - PkgBR, can be specified as BuildRequires
  - URL, can be typed as Url
  - but with warning message
  - Decent quit when empty YAML file found
  - "setup.py develop" supported
  - Update of document
* Wed Jul  7 2010 Jian-feng Ding <jian-feng.ding@intel.com> 0.18
- Release 0.18, with the following changes:
  specify:
  - Support new builder: 'qmake'
  - Added all sub-package specific keywords, including:
  - License
  - Version, Release, Epoch
  - NoAutoreq, NoAutoprov
  - BuildArch
  - URL
  - Added the following new keywords:
  - BuildConflicts
  - Prefix
  - More precise duplicate checking for customized spec part:
  - duplicate '/sbin/ldconfig' in %%post/postun
  - duplicate scripts for special files handling:
    Info, Desktop, Icon, Schema, etc
  - duplicate "%%defattr" line in %%files
  - Checking for valid configure/builder values
  - Checking for valid keywords for sub-packages
  - Warning for PkgBR/PkgConfigBR in sub-packages
  - Added Icon/Scheme auto-handling for sub-packages
  spec2spectacle:
  - Fixed bugs in parsing of Perl packages' spec
  - More old spec directives support: Prereq, BuildConflicts
* Tue May 18 2010 Jian-feng Ding <jian-feng.ding@intel.com> 0.17
- Release 0.17, with the following changes:
  specify:
  - Add compatible support for older 'OtherDistros'
  - More precise handling for *.desktop in packages
  - Better match rules for desktop files and info files
  - Newkey 'UpdateDesktopDB' to do the 'update-desktop-database'
    operation in a explicit way
  - More precise handling for python module installation path
  spec2spectacle:
  - Fixings for macro definitions' parsing
* Sat May  8 2010 Anas Nashif <anas.nashif@intel.com> - 0.16
- Fixed rpmlint errors
- Do not install tests
* Fri Apr 30 2010 Jian-feng Ding <jian-feng.ding@intel.com> 0.16
- Fixed modules installation path in Debian/Ubuntu system
* Thu Apr 22 2010 Jian-feng Ding <jian-feng.ding@intel.com> 0.16
- Update to 0.16, with the following changes:
  specify:
  - New key 'NoDesktop' to skip desktop files in package
  - New key 'RpmLintIgnore' to ignore rpmlintrc
  - README updated with new MeeGo information
* Thu Apr 22 2010 Jian-feng Ding <jian-feng.ding@intel.com> 0.15
- Add lost requires for 'python-cheetah', fixed BMC#779
* Wed Mar 31 2010 Jian-feng Ding <jian-feng.ding@intel.com> 0.15
- Update to 0.15, with the following changes:
  specify:
  - Architecture namespace support
  - supported archs: ix86, arm
  - supported keywords: Requires, PkgBR, PkgConfigBR, Patches, ConfigOptions
  - New keyword 'NoFiles' to support empty main package
  - Customized %%pre/preun/post/postun scripts for sub-packages
  - Precise duplicate checking for auto-generated Requires
  - More proper automatic processing for Icons files
  - More proper automatic processing for Desktop files
  - More proper automatic processing for share libraries
  - Decent handling for exceptions of YAML errors and key interrupts
  spec2spectacle:
  - More tolerance for problems in input spec
  - Parsing for customized %%pre/preun/post/postun scripts of sub packages
  - More helping warning messages
  doc and testsuites:
  - new cases for new features
  - README, as the reference, updated according all changes
* Wed Mar 17 2010 Jian-feng Ding <jian-feng.ding@intel.com> 0.14
- Update to 0.14, with the following changes:
  specify:
  - Proposals for pkgconfig requires to replace buildrequires
  - Checking for MeeGo approved Groups
  - series.conf support for 'Patches', with more friendly comments
  - Support for new builder: 'qmake', 'perl'
  - Accurate checking for mandatory/invalid/empty keys, and checking
    for the types of all keys
  - More customized scripts in spec for  %%pre/preun/post/postun
    sections
  - Testsuites: the spectacle specific testing framework and about
    45 cases to cover the most features' checking
  - Automatic locale data including, if found 'intltool' in PkgBR,
    `find_lang` rpm macro will be inserted to spec to search locale
    data, but 'NoAutoLocale' keyword can suppress it.
  - New keywords:
  - 'ExclusiveArch' of the corresponding spec one
  - 'Files' to enable putting file list in YAML for small packages
  - 'AutoDepend' to enable/disable automatic requires for sub-pkg
  - 'AsWholeName' to make sub-pkg use its name without the main
    package name as prefix. ("-n" options in spec)
  - Dropped 'PostScripts' key, use customized "%%post" in spec instead
  - Renamed 'NeedCheckSection' to 'Check', with compatibily support
    for all renamed/dropped keys.
  spec2spectacle:
  - Support parsing of %%pre/preun/post/postun scripts
  - Support parsing of %%check section in spec
  - Support parsing of "-n" and "-p" options of spec headers
  - More accurate parsing of pkgconfig build requires
* Tue Feb 23 2010 Jian-feng Ding <jian-feng.ding@intel.com> 0.13
- Update to 0.13, with the following changes:
  - Added python-urlgrabber to 'Requires'
  - Added new document to package: TODO and examples/*
    Changes of features:
  - Support fdupes
  - Add new key 'NoSetup' and 'SetupOptions' and new customized section
    ">> setup" for %%setup customization.
  - Include YAML file as Source100.
  - Enhaneced message printing: colorized and different levels:
  - info/warning/error/ask
  - ini2spec: Skip missed *.desc files and leave 'Description' empty with
    warning printing.
  - Type checkings for all list-typed tags
  - Add date string to generated spec.
  - Try to find out the source prefix path from tarballs if 'SourcePrefix'
    not specified.
  - Using urlgrabber to download src files for several advantages.
  - Give info about possible usage of pkgconfig to replace BuildRequires,
    based on a predefined database(pkgconfig-provides.csv).
  - Checking for proved MeeGo Groups.
  - More careful checking for duplicates values for auto-generated ones:
  - sub-pkg's 'Requires' of base package
  - '--disable-static' of ConfigOptions
  - 'defattr(-,root,root,-)' in %%files
  - Static library detect and automatic handling
  - Add perl package support.
  - Tools' cmdln options changes: need not to specify file path now, tools
    will search in CWD with expected ext names.
  - Add support for UseAsNeeded/NoAutoReq/NoAutoProv boolean keys
  - Use the value 'configure' as the default value of 'Configure' tag.
  - Cleanup obsoletes files to backup sub-dirs: all spec-builder files and
    origin spec file, in converter tools.
  - Other bug fixings and minor changes...
* Tue Feb  9 2010 Jian-feng Ding <jian-feng.ding@intel.com> 0.11
- update to 0.11, with the following changes:
    Changes of features:
  - download newer source package automatically
  - new optional YAML key 'SourcePrefix' to specify the prefix path for tarballs
  - new optional YAML key 'FilesInput' to specify extra %%files input file in spec
  - new optional YAML key 'SupoprtOtherDistros' to support other distros explicit
  - complete the support for Requires(pre/post/preun/postun)/Conflicts/Provides/Obseletes
    for both main package and sub packages
  - support Epoch spec directive
  - support %%check spec section
  - more convenient cmdln options for all tools
* Fri Jan 22 2010 Jian-feng Ding <jian-feng.ding@intel.com> 0.10
- update to 0.10, many features and fixes were added
* Mon Jan 18 2010 Jian-feng Ding <jian-feng.ding@intel.com> 0.9
- Update to 0.9, new tool spec2spectacle added
* Fri Jan 15 2010 Jian-feng Ding <jian-feng.ding@intel.com> 0.8
- Add python-cheetah to BuildReq
* Sat Jan  2 2010 nashif <anas.nashif@intel.com> - 0.8
- Update to 0.8
* Wed Dec 30 2009 Jian-feng Ding <jian-feng.ding@intel.com> 0.7
- Update to 0.7
* Tue Dec 29 2009 Jian-feng Ding <jian-feng.ding@intel.com> 0.6
- Update to 0.6
* Sun Dec 13 2009 Anas Nashif <anas.nashif@intel.com> - 0.4
- Support creating releases from SCM
* Sun Dec 13 2009 Anas Nashif <anas.nashif@intel.com> - 0.2
- Update to 0.2
* Sun Dec 13 2009 Anas Nashif <anas.nashif@intel.com> - 0.1
- Initial release for moblin
