#global _binary_filedigest_algorithm 1
#global _source_filedigest_algorithm 1
#global __brp_mangle_shebangs  true

Summary: Another file integrity checker
Summary(fr): afick, logiciel de controle d'intégrite
Name: afick
Version: 3.7.0
Release: 1
Group: Applications/System
License: GPL
Source: %{name}-%{version}.tgz
URL: https://afick.sourceforge.net
BuildArch: noarch

%description
afick is a portable file integrity checker
(it only needs standard perl to work).
it will be run daily by cron to detect new/deleted/modified files
It works by first (init) making an snapshot of strategic directories 
attributes, and then compare the disk status with this snapshot.
A Graphical interface is available in afick-gui package.

%description -l fr
afick est un logiciel de controle d'intégrité portable
(il est codé en language perl).
Il permet, par un cron quotidien, de détecter les fichiers nouveaux/supprimé/modifiés.
Il travaille en fabriquant une image (init) des repertoires ou fichiers essentiels dans
une base de donnée. Le cron compare l'état du disque avec cette 'image'.
Une interface graphique est disponible dans le package afick-gui.

%prep
%setup -q
#%patch
perl Makefile.pl Makefile_sys.in

%install
mkdir -p $RPM_BUILD_ROOT
make DESTDIR=$RPM_BUILD_ROOT installspec
#make DESTDIR=$RPM_BUILD_ROOT install-doc
make DESTDIR=$RPM_BUILD_ROOT install-gui
# for ghost
cd $RPM_BUILD_ROOT && touch var/lib/afick/afick.dir var/lib/afick/afick.pag var/lib/afick/afick.ctr var/lib/afick/history

%clean
[ "$RPM_BUILD_ROOT" != "/" ] && rm -rf "$RPM_BUILD_ROOT 2> /dev/null"

%pre
#force save old config on upgrade
if [ "$1" = 2 ]
then
	#update
	if [ -f /usr/bin/afick_preinstall.pl ]
	then
		afick_preinstall.pl -c /etc/afick.conf
	else
		cp -f /etc/afick.conf /etc/afick.conf.sav
	fi
	#echo "save old config as /etc/afick.conf.rpmsave"
fi
# check perl version
perlversion=$( perl -e 'if ( $] < 5.008 ){ print 1} else { print 0};' )
if [ $perlversion -eq 1 ]
then
	#check for perl-Digest-MD5
	# in old release, needs an external package
	# but is included in new perl releases
	perl -e 'eval { require Digest::MD5 }; exit 1 if $@'
	if [ $? -eq 1 ]
	then
		echo "afick requires perl-Digest-MD5 package"
		exit
	else
		echo "found perl-Digest-MD5 : ok"
	fi
fi

%post
afick_postinstall.pl -c /etc/afick.conf

%files
%doc AUTHORS
%doc Changelog
%doc COPYING
%doc COPYRIGHT
%doc INSTALL
%doc linux.conf
%doc NEWS
%doc README
%doc QUICKSTART
%doc TODO
%doc afick.lsm
%config %attr(0600 root root)  /etc/afick.conf
%config %attr(0755 root root) /etc/cron.daily/afick_cron
%config /etc/logrotate.d/afick
%attr(0755 root root) /usr/bin/afick.pl
%attr(0755 root root) /usr/bin/afick
%attr(0755 root root) /usr/bin/afick_archive.pl
%attr(0755 root root) /usr/bin/afick_archive
%attr(0755 root root) /usr/bin/afick_format.pl
%attr(0755 root root) /usr/bin/afick_learn.pl
%attr(0755 root root) /usr/bin/afickonfig.pl
%attr(0755 root root) /usr/bin/afickonfig
%attr(0755 root root) /usr/bin/afick-common.pl
%attr(0755 root root) /usr/bin/afick_postinstall.pl
%attr(0755 root root) /usr/bin/afick_preinstall.pl
%dir %attr(0755 root root) /usr/lib/afick
%dir %attr(0755 root root) /usr/lib/afick/lib
%dir %attr(0755 root root) /usr/lib/afick/lib/Afick
%attr(0644 root root) /usr/lib/afick/lib/Afick/Constant.pm
%attr(0644 root root) /usr/lib/afick/lib/Afick/Msg.pm
%attr(0644 root root) /usr/lib/afick/lib/Afick/Lock.pm
%attr(0644 root root) /usr/lib/afick/lib/Afick/Log.pm
%attr(0644 root root) /usr/lib/afick/lib/Afick/Tst.pm
%attr(0644 root root) /usr/lib/afick/lib/Afick/Gen.pm
%attr(0644 root root) /usr/lib/afick/lib/Afick/Directives.pm
%attr(0644 root root) /usr/lib/afick/lib/Afick/Macros.pm
%attr(0644 root root) /usr/lib/afick/lib/Afick/Aliases.pm
%attr(0644 root root) /usr/lib/afick/lib/Afick/Cfg.pm
%attr(0644 root root) /usr/lib/afick/lib/Afick/Backend.pm
%attr(0644 root root) /usr/lib/afick/lib/Afick/Control.pm
%attr(0644 root root) /usr/lib/afick/lib/Afick/Learn.pm
%attr(0644 root root) /usr/lib/afick/lib/Afick/Report.pm
%attr(0644 root root) /usr/lib/afick/lib/Afick/WinAcl.pm
%attr(0644 root root) /usr/lib/afick/lib/Afick/Object.pm
%attr(0644 root root) /usr/lib/afick/lib/Afick/Plugins.pm
%doc /usr/share/man/man1/afick.1*
%doc /usr/share/man/man1/afick_archive.1*
%doc /usr/share/man/man1/afick_format.1*
%doc /usr/share/man/man1/afick_learn.1*
%doc /usr/share/man/man1/afickonfig.1*
%doc /usr/share/man/man5/afick.conf.5*
%dir %attr(0700 root root) /var/lib/afick
%ghost /var/lib/afick/afick.pag
%ghost /var/lib/afick/afick.dir
%ghost /var/lib/afick/afick.ctr
%ghost /var/lib/afick/history
%dir %attr(0700 root root) /var/lib/afick/archive
%dir %attr(0700 root root) /var/log/afick/

%package doc
Summary: html doc for afick
Group: Applications/System
BuildArch: noarch
Requires:  afick >= 3.4.2

%description doc
afick-doc contains all html doc (a copy of the online web site).
It is an optionnal package

%description -l fr doc
Le package afick-foc contient la documentation au format html : 
une copie du site web en ligne.
C'est un package optionnel.

%pre doc
#make DESTDIR=$RPM_BUILD_ROOT install-doc

%files doc 
%doc html

%package gui
Summary: A graphical interface for afick
Group: Applications/System
BuildArch: noarch
Requires:  perl-Tk
Requires:  afick >= 2.0

%description gui
afick-gui is perl/tk tool for afick software
It can be used to launch afick with differents options
and to have a graphical view of results
It comes with menu for integration in kde/gnome ...

%description -l fr gui
afick-gui est une interface graphique pour afick, écrite en perl-tk.
elle permet de lancer afick avec ses différentes options,
et d'avoir une visualisation graphique des résultats

%post gui
if [ -x /usr/bin/update-menus ]; then /usr/bin/update-menus || true ; fi

%postun gui
if [ "$1" = "0" -a -x /usr/bin/update-menus ]; then /usr/bin/update-menus || true ; fi

%files gui 
%doc AUTHORS
%doc Changelog
%doc COPYING
%doc COPYRIGHT
%doc INSTALL
%doc linux.conf
%doc NEWS
%doc README
%doc QUICKSTART
%doc TODO
%doc afick.lsm
%attr(0755 root root) /usr/bin/afick-tk.pl
%attr(0755 root root) /usr/bin/afick_learn_tk.pl
/usr/bin/afick-tk
/usr/bin/afick-gui
/usr/share/menu/afick-gui
%dir /usr/share/applnk/
%dir /usr/share/applnk/System/
/usr/share/applnk/System/afick.desktop
%dir /usr/share/gnome/
%dir /usr/share/gnome/apps/
%dir /usr/share/gnome/apps/System/
/usr/share/gnome/apps/System/afick.desktop
%dir /usr/share/applications/
/usr/share/applications/afick.desktop
/usr/share/icons/afick.xpm
/usr/share/icons/afick.png
%dir /usr/share/pixmaps
/usr/share/pixmaps/afick.xpm
/usr/share/pixmaps/afick.png
%doc /usr/share/man/man1/afick-tk.1*
%doc /usr/share/man/man1/afick_learn_tk.1*

%changelog
* Thu Apr 1 2021 Wei-Lun Chao <bluebat@member.fsf.org> - 3.7.0
- Rebuilt for Fedora

* Fri Nov 06 2020 Eric Gerbier <gerbier@users.sourceforge.net> 3.7.0
- (Afick::Backend) now store data as an object instead joined tab
- remove glob warning : use Use File::Glob::bsd_glob instead glob
- keep env shebang on rpm + deb

* Fri Nov 30 2018 Eric Gerbier <gerbier@users.sourceforge.net> 3.6.1
- fix window's acl sid in lower case
- suppress wanted_create
- move global variables to Afick::Report
- move print_dangling,print_new,print_change,print_delete to to Afick::Report
- move file_info sub into Object.pm
- (Backend) : add empty sub, check update mode in del sub
- add export/import database options
- ( Afick::Plugins ) merge print/print_csv/export_raw in print_common
- search option can also apply on --csv and --export
- linux.conf : do not scan /usr/lib/.build-id/
- (windows) fix acl display in human way
- (Afick::Object) move is_changed/display_changed in Object.pm
- add duplicates option (as Plugins)
- use env in shebang to fix cron problem on debian/ubuntu

* Fri Dec 08 2017 Eric Gerbier <gerbier@users.sourceforge.net> 3.6.0
- add Afick::WinAcl lib
- add Afick::Object lib
- add Afick::Plugins lib
- format of print/csv/search is changed
- tests on syslog work with systemd/journalctl
- new directive utc_time
- all windows acl are now in lower case
- (windows) afick-gui work on windows 8 8.1 and 10
- (windows) fix installer

* Fri Aug 05 2016 Eric Gerbier <gerbier@users.sourceforge.net> 3.5.3
- bugfix, allow arobase in filenames
- add afick_learn_tk tool and Afick::Learn lib
- use afick's constants for config grammar
- Afick::Backend remove global Hashfile, move open_database/close_database
- add Afick::Report lib

* Fri Aug 05 2016 Eric Gerbier <gerbier@users.sourceforge.net> 3.5.2
- back to old print/close syntax for compatibility with old perl
- (windows) fix perl warnings on activeperl 5.20 about S_ISLNK
- fix perl warnings about regex syntax
- (Lock.pm) add basename method
- add Afick's modules in auto-control
- add Afick::Backend Afick::Control
- fix bad dates in specfile (changelog section)
- improve doc about exclude_* directives (syntax, multi-lines)
- fix a bug with exclure_re on pattern with space character
- add report_context directive, to show all changed attributes
- default backend now to storable
- improve linux.conf
- (afick_learn) bugfix on gid
- (afick_learn) bugfix on empty rule
- (afick-tk) manage report_summary, report_context directives
- (afick-tk) split main sub in small functions
- (afick-tk) remove menu_option (duplicate from configuration/directives)
- (afick-tk) config_directives : add keep button to match old menu_option behavior
- (afick-tk) improve directives doc : add new directives, match config_directives names and order
- (afick-tk) add learn feature (in configuration menu)
- (afick-tk) clean code : remove unused variables

* Fri Dec 04 2015 Eric Gerbier <gerbier@users.sourceforge.net> 3.5.1
- new Afick::Log class to analyse afick's logs
- new afick_learn.pl tool (using Afick::Log)
- new afick_format.pl tool (using Afick::Log)
- change window's installer from old setup2go to modern inno setup
- (windows) only use cmd files (no more bat)
- tgz install will now be under /opt/afick, no more merged into system
- some recode using modern perl syntaxe
- change perl shebang for more generic, using env
- (afick-tk) fix bug on write config file (bad old write_config)
- (afick-tk) fix bug on write new config file

* Wed May 13 2015 Eric Gerbier <gerbier@users.sourceforge.net> 3.5.0
- use Afick::Cfg
- new directive report_summary
- (afick_format) bugfix, skip WARNING lines to detect first real line 
- (afick_format) add run,config metadata on xml output

* Fri Jan 09 2015 Eric Gerbier <gerbier@users.sourceforge.net> 3.4.3
- (afick) fix sparse error Odd number of elements in anonymous hash
- (afick) rename all same variables with same name ra_toscan
- (afick) add internal doc
- (afick) clean code, remove dead code (test_dbm_available, make_regex)
- (afick) rename update sub into update_database
- (afick) remove Nbmod global variable
- (control) control sub also use is_changed
- (linux, windows) remove inode, mtime from default rules (dummy change detection)
- (afick-tk) after save config, reload only if same name

* Fri Dec 12 2014 Eric Gerbier <gerbier@users.sourceforge.net> 3.4.2
- (packages) remove /etc/cron.daily from rpm package (avoid rpm warnings)
- (packages) move html doc in new afick-doc package (rpm, deb)
- (afick) backport from 3.5 , stop parcours sub as soon as possible ( exceptions and already seen files)
- (afick) backport from 3.5 : detect temporary files
- (afick) backport from 3.5 : use new top_parcours sub 
- (afick) recode exclude tests , a control file may be an exception
- (afick) rename create sub into create_database
- (afick) code cleaning, recode the scanning tree engine (parcours)
- (control) add history and archive (directives) in control files
- (control) also apply file normalisation on control files
- (control) avoid duplicated scan of control files
- (control) auto_control_check gets files to check from Control hash
- (windows) remove log directories from scan
- (linux) update linux.conf to remove dummy changes
- (Gen) fix some others problem from windows tests in to_abspath
- (afick-tk) fix bug on saved config file name on unix (bad name)
- (afick-tk) test if abort on file selection for configfile save (avoid error message)

* Sun Nov 23 2014 Eric Gerbier <gerbier@users.sourceforge.net> 3.4.1
- (Msg) add showstack method to help debug
- (Aliases) fix warning if empty masq in _decode_alias_unit
- (Tst) avoid code redondancy in _is_fileval
- (Gen) fix bug in to_abspath for windows env
- (Directives) add is_initialized method to detect overload
- (windows) fix bug on afick control : sort windows acl
- standardize directory separator (reg_name) after environment replacement in read_configuration sub
- in read_configuration, in debug mode, display also expanded rule line
- (windows) remove acl if too long to avoid SDBM error
- (windows) remove winsxs from scan in windows.conf
- (windows) add directory for 32 bits applications on 64 bit windows
- (afick-tk) remove afick's command line options
- (afick-tk) force use same path for all afick commands (wrapper)
- (afick-tk) in verbose mode, show full command line (wrapper)
- (afick-tk) allow start without file config : load default config
- (afick-tk) new sub build_cmdline to share common code for wrapper options between afick and afickonfig calls

* Fri Aug 23 2013 Eric Gerbier <gerbier@users.sourceforge.net> 3.4
- integrate changes from 3.3.1 to 3.3.4 in a stable release

* Sat May 4 2013 Eric Gerbier <gerbier@users.sourceforge.net> 3.3.4
- fix bugs in afickonfig.pl
- improve afickonfig : work on all config types
- use pod doc for all perl scripts
- use Afick::Aliases
- add regression tests
- (afick_planning) add test for mail errors

* Mon Apr 22 2013 Eric Gerbier <gerbier@users.sourceforge.net> 3.3.3
- fix inconsitence between command line parameters and config directives : 
	full_newdel -> report_full_newdel
	missing_file => warn_missing_file
	dead_symlinks => warn_dead_symlinks
- suppress global Directives variables in afick.pl
- (afick-common) get_configuration also use Afick::Macros and Afick::Directives

* Mon Apr 15 2013 Eric Gerbier <gerbier@users.sourceforge.net> 3.3.2
- use Afick::Macros 
- fix pod doc (html)
- new macro : archive_retention

* Fri Apr 12 2013 Eric Gerbier <gerbier@users.sourceforge.net> 3.3.1
- use Afick::Directives for check_directives
- bugfix overload last rule if allow_overload
- (windows) force install of Tk module

* Fri Dec 21 2012 Eric Gerbier <gerbier@users.sourceforge.net> 3.3
- add arg to close_database
- use Afick::Gen
- fix report_url option
- fix check_update call

* Fri Nov 09 2012 Eric Gerbier <gerbier@users.sourceforge.net> 3.2
- windows : move database files to database directory
- use Afick::Tst
- fix bug on progress option
- fix bug on print_config
- fix warning on unlock
- fix warning on config file (path)
- fix : only display dangling links if dead_symlinks is set
- fix quiet option
- fix report_syslog option
- fix aficonfig delete config var
- afickonfig : add list option 
- add stat_date plugin
- can print_config without any writable perm
- merge from trunk 2.22

* Fri Jul 20 2012 Eric Gerbier <gerbier@users.sourceforge.net> 3.1
- merge with trunk 2.21 (nagios)
- first stable release

* Fri Jul 13 2012 Eric Gerbier <gerbier@users.sourceforge.net> 2.21
- add nagios nsca option in afick_cron

* Fri May 04 2012 Eric Gerbier <gerbier@users.sourceforge.net> 3.0.3
- use Afick::Lock

* Tue Mar 13 2012 Eric Gerbier <gerbier@users.sourceforge.net> 3.0.2
- use Afick::Msg

* Wed Feb 08 2012 Eric Gerbier <gerbier@users.sourceforge.net> 3.0.1
- use Afick::Constant

* Sun Feb 05 2012 Eric Gerbier <gerbier@users.sourceforge.net> 2.20
- add sha-256, sha-512 checksum (to be used instead sha-1)
- (bugfix) print display sha in same format as sha1sum/... command

* Thu Nov 10 2011 Eric Gerbier <gerbier@users.sourceforge.net> 2.19
- (afick.spec) add compatibility with old rpm digest format
- add csv option (export database in csv format)
- add MAILAUTH macro for mail auth (windows)
- add relative_path directive
- can use chroot directories using AFICK_CHROOT
- begin to merge get_configuration and read_configuration

* Wed Oct 05 2011 Eric Gerbier <gerbier@users.sourceforge.net> 2.18
- rename calc_control into auto_control_check
- add auto_control_prepare sub
- rename get_names into get_script_list
- add get_database_list
- rename add_database_control into auto_control_prepdb
- check also database in auto-control_check
- try to compute checksum without NOATIME
- add is_special_dir sub
- environment variables in config file are expanded on fly at begin of run
- config pod doc match config sample sections names
- (windows) fix a bug : alias are case-sensitive
- (windows) fix afick_set_planning bug, use absolute path to afick_planning
- (windows) fix a bug in stat_secu : getpwent does not work on windows
- (windows) fix a bug in afick_planning.pl about commented macros
- (windows) add a delete button in afick_set_planning.pl
- (windows) fix junction directories warning (can not open directory in parcours)

* Tue Jun 07 2011 Eric Gerbier <gerbier@users.sourceforge.net> 2.17
- arguments for --list option should now be separetd by a comma instead space (bug reported by Margaret Garland)
- arguments for --list can also be given in on several args
- common version with afick-tk

* Fri Dec 10 2010 Eric Gerbier <gerbier@users.sourceforge.net> 2.16-1
- fix bug in print_digest (bug report from Andy Bach )
- fix bug base_checksum in degraded mode
- rename set_planning.pl into afick_set_planning.pl

* Wed Apr 21 2010 Eric Gerbier <gerbier@users.sourceforge.net> 2.15-1
- add 64 bits lib directories in afick.conf and afickonfig.pl
- (afickonfig.pl) addlib also add libs from ldd command on perl binary
- afick_cron now use sh syntax instead bash syntax (patch from Mike Muise)
- avoid loosing time in print_digest in null (patch from Mike Muise)
- fix hostname call for non GNU unix in afick_cron (patch from Mike Muise)
- fix english typo (suggest from Francis Favorini)
- fix error with activeperl 5.10.1.1007 on S_ISBLK (bug  request from Francis Favorini)
- check_config warns about environment variables in config file
- clean_config try to replace environment variables in config file
- allow to work as admin on vista/seven (uac)

* Fri Jul 24 2009 Eric Gerbier <gerbier@users.sourceforge.net> 2.14-1
- only one dangling info report
- output compatibility with md5sum/sha1sum commands
- fix a bug on negative rule 
- add quiet option, not recommanded (feature request from Kevin Crowston)
- (gui) add command line options database,history,archive to allow analyse on another computer

* Fri Jan 16 2009 Eric Gerbier <gerbier@users.sourceforge.net> 2.13-1
- (unix) remove udev files from scan
- begin to remove global variables (Id, Field)
- reference date is now $BASETIME 
-  move to_abspath to afick-common
- recode messaging to use same low-level subs (report)
- add LF in report sub
- new crlf sub
- detect date in the future (Running)
- new directive/option : only suffix
- new analysis option stat_ext
- print dangling file as info if warn_dead_symlinks is disabled
- test for existing database and die if not

* Thu Oct 16 2008 Eric Gerbier <gerbier@users.sourceforge.net> 2.12-1
- (windows) afick_planning now send report instead summary and use LINES macro
- (unix) fix a warning with perl 5.10 on Constant subroutine main::S_IWGRP redefined
- fix perlcritic warnings
- (unix) new MOUNT macro to use a remote database when using batch task on unix (afick_cron)
- add a security to avoid exlude auto-control files
- better Makefile.pl diagnostics (I hope)

* Thu Apr 10 2008 Eric Gerbier <gerbier@users.sourceforge.net> 2.11-1
- afick_planning can also send a mail on windows (add MAILHOST macro)
- only one doc source : the included pod doc

* Thu May 17 2007 Eric Gerbier <gerbier@users.sourceforge.net> 2.10.1
- post_install can replace environment variables in afick's config
- windows config file now use environment variables (Manuel Martin suggest)
- rename set_planning.bat to afick_postinstall.bat
- display warning for too long acl on windows (SDBM error) 
- add report_syslog directive and option
- dynamic choice of database backend
- change directives compare algorythme (diff_tab sub)
- remove usage sub (all doc in pod)
- add report_url option
- adapt afick_cron to old shell syntax (ash ...) to fix bug with anacron  ( Slass100 report)
- prepare code for daemon mode (with gamin use)
- checksum do not change atime any more if possible
- improved afick change detection (warnings not only on checksum)

* Tue Sep 26 2006 Eric Gerbier <gerbier@users.sourceforge.net> 2.9.1
- fix bug on temporary files (init parameters to 0) ? (afick)
- fix bug for exclude* (multi-line works again, was broken in 2.7-1) (afick-common), thanks Manuel Martin
- use more constants (afick)
- skip checksum on empty files (afick)
- recode addfile in checksum sub to avoid exit (croak) on errors (afick)
- change warning to debug for checksum access on windows (afick)
- updated windows config file (add exclude by Manuel Martin)
- (afickonfig) add man option (first use of Pod::Usage)
- (afickonfig) add opt_ prefix for opt variables
- (afickonfig) for addpath option on windows, add  %%systemroot%% and %%ProgramFiles%%
- (afick-gui) : add archive menu
- (afick) fix a bug on exceptions with globing and ignore_case

* Mon Sep 04 2006 Eric Gerbier <gerbier@users.sourceforge.net> 2.9.0
- add database files in rpm database (ghost)
- new warning_def and debug_def default subroutines (afick-common) to avoid duplicate code
- new option --check_update to check for a new version (afick)
- use perlcritic to clean perl code (follow Conway rules)
- rename planning.bat to set_planning.bat and planning.pl to set_planning.pl (windows)
- fix tar.gz install for hpux users (thanks Menguy Jacques)
- fix a bug on print_config option (afick)
- add afick_archive.pl tool
- info, debug, warning now have an internal new line terminator
- tar.gz, debian and rpm install now use common scripts for pre-install and post-install (clean config configuration)
- improved configuration upgrade with "local config section"
- clean_config do not remove comments any more (afick/afickonfig bugfix)
- running an update action on a missing database switch to init action (usefull for batch job)
- change allow_overload default directive value to yes
- addpath and addlib option now work on microsoft os (afickonfig bugfix)

* Fri Jul 07 2006 Eric Gerbier <gerbier@users.sourceforge.net> 2.8.3
- new my_die sub to be consistent (as warning, info ...)
- add a locking mecanism on database (my_lock, my_unlock, close_database sub)
- add new debugging tool ( debug_begin, debug_end, get_caller )
- add signal trapping for a clean exit
- fix bug if macro VERBOSE = 1( no mail sent if no changes) on afick_cron
- nice macro value is used by afick.pl
- change auto_control check for rfc needs
- fix a bug with follow_symlinks doc which does not match behavior
- new windows packager Setup2Go 
- (windows package) save config file before install
- (windows package) remove task from service planning on uninstall
- (windows package) remove hard-coded path to afick directory

* Wed Aug 17 2005 Eric Gerbier <gerbier@users.sourceforge.net> 2.8.2
- default config file can be set in AFICK_CONFIG environment var
- afick-gui can be started by not-root users
- rename afick.cron into afick_cron (cron filename limitation on debian : no dots )

* Mon Jun 06 2005 Eric Gerbier <gerbier@users.sourceforge.net> 2.8.1
- fix date on control file to match history/archive date
- more general addrule sub
- improve auto-control on directives changes
- fix bad directives display, with a new uniq sub (get_list_dir)

* Mon Jun 06 2005 Eric Gerbier <gerbier@users.sourceforge.net> 2.8.0
- restrict permissions on database files
- now add all afick's programs to database
- allow md5 and sha1 checksum
- stat_secu : add uid and gid orphans
- doc translation to french
- Makefile.pl can change shebang (perl path) on perl scripts (suggest from paulhargreaves)
- upgrade from tar.gz now save old config file

* Sun May 01 2005 Eric Gerbier <gerbier@users.sourceforge.net> 2.7.1
- fix problem with mkdir (add -p) on src.rpm (thanks Sinner)
- add real elapsed time in timing option for afick.pl (thanks Roland Friedwagner)
- remove symbolic links from running testing (thanks Roland Friedwagner)
- fix problem with tar.gz install (afickonfig return code)
- fix bug on get_configuration sub for multi-line exclude
- add follow_symlinks directive to have control checksum behavior on symbolic links (Roland Friedwagner)
- add directive allow_overload
- add macro REPORT
- fix bug with root dir on windows (thanks Jean-Marc Mongrelet)
- fix bug for exceptions and quoted files
- (afick-tk)now use get_configuration (from afick_common)
- (afick-tk) add directives configuration menu

* Mon Feb 07 2005 Eric Gerbier <gerbier@users.sourceforge.net> 2.7.0
- add print_directive, print_macro, print_alias, print_rule options
- add addpath and addlib options to afickonfig command
- get macro constant from Fcntl instead POSIX (define socket and links)
- add search option to get a filtered output from database
- add stat_secu and stat_size options
- add tab2hash, get_filemode, get_filesize, is_type, split_record sub
- add open_database, statistics sub
- move rech_parent sub to afick-common
- run afickonfig.pl --addpath --addlib in rpm and tgz install
- change default max_checksum_size to ~ 10 Mo
- fix test_os.sh script perms bug
- better section split in config file
- use same format for all printed dates (last run ...)
- add uninstall target in Makefile for tar.gz installers
- allow new fileinfo fields (add norm_info and is_changed sub)
- (afick-tk) redesign progress window (split files and pourcents)
- (afick-tk) add 2 times window (elapsed, remaining time)
- (afick-tk) in progress mode, reduce the number of update calls
- (afick-tk) add stat_secu, stat_size and search in analysis menu
- (afick-tk) add "addpath/addlib" (afickonfig call) in configuration menu
- (afick-tk) new wrapper sub to allow afickonfig call
- (afick-tk) now use is_microsoft sub (afick-common)

* Thu Jan 13 2005 Eric Gerbier <gerbier@users.sourceforge.net> 2.6.2
- fix a bug on afickonfig with directives
- avoid scan if list mode contains exceptions (rech_parent)
- open database in read-only mode if compare (bug report from Brian Warshawsky)
- do not write control file in compare mode

* Thu Jan 6 2005 Eric Gerbier <gerbier@users.sourceforge.net> 2.6.1
- now create history file, archive dir if not exists
- on window, launch icon is now in afick menu
- add a warning if nothing to scan
- debug and clean list options treatement

* Wed Dec 15 2004 Eric Gerbier  <gerbier@users.sourceforge.net> 2.6.0 
- restrict config file perm (security)
- add max_checksum_size directive for partial checksum on big files (idea from Emmanuel Florac)
- add exclude_re directive for regular expressions filter
- on history, delete change entry color to black (afick-gui)
- change color for deleted from blue to brown (afick-gui)
- move style declare to where it is used (afick-gui)
- change clean history algo (work on one file only) (afick-gui)

* Wed Nov 10 2004 Eric Gerbier <gerbier@users.sourceforge.net> 2.5.0
- fix bug on print_config option
- add alias, macros, rules options on afickonfig
- check config validity at end of afickonfig
- add info on check_config
- now use common lib afick_common.pl
- add option clean_config (afick.pl)
- rewrite alias parsing ( now in good order)
- fix bug in E alias use

* Fri Oct 15 2004 Eric Gerbier <gerbier@users.sourceforge.net> 2.4.0
- change tar.gz for aix
- add short option -A for --archive
- clean rpm files with rpmlint
- now check macro syntaxe (afick.pl)
- fix bug in planning.pl (remove rem)
- add afick_planning.pl to send MessageBox to user on windows from service planning
- test if archive dir exists (afick.pl)
- now can choice day/time for service planning (planning.pl)
- change all dates from gmt to local time
- print_config option now print macros/alias/rules too
- add current version in report header
- add exclude_prefix directive
- rewrite exclude algo to be faster

* Wed Jul 21 2004 Eric Gerbier <gerbier@users.sourceforge.net> 2.3.1
- remove perl-Digest-MD5 dependency to work on recent distrib with perl 5.8
  a perl test is now done in pre-install stage

* Tue Jun 29 2004 Eric Gerbier <gerbier@users.sourceforge.net> 2.3.0 (gui)
- fix bad pourcent display on init (to 0)
- replace configuration buttons by menus

* Tue Jun 29 2004 Eric Gerbier <gerbier@users.sourceforge.net> 2.3.0
- add afickonfig.pl tool to manage afick's config file
- add --database/-D option
- add comments on running options in output
- add check_config option
- rename scan.cmd into afick_scan.cmd
- change print_config output to the same format as config file
- test if exists before adding to service planning on windows
- remove old 'h' attribute (replaced by md5, or sha1)

* Mon May 10 2004 Eric Gerbier <gerbier@users.sourceforge.net> 2.2.0 (gui)
- replace buttons by menus
- add bind keys for quicker actions
- replace double quotes by simple if possible

* Mon May 10 2004 Eric Gerbier <gerbier@users.sourceforge.net> 2.2.0
- replace double quotes by simple if possible
- add the NICE macro to control afick cron job priority
- add the BATCH macro to control afick cron job run
- fix missing file name in print mode
- bug on dangling links, defined as top file in config file ( bad $rep)

* Mon Apr 5 2004 Eric Gerbier <gerbier@users.sourceforge.net> 2.1.0 (gui)
- reference to array in sub
- add history menu for history and archive access
- add colors in text 
- common colors
- now have a common load sub for all entries (pipe or saved files)
- a common sub (display_message) for all helps

* Mon Apr 5 2004 Eric Gerbier <gerbier@users.sourceforge.net> 2.1.0
- reference to array in sub
- new directive debug
- add an eval on FileSecurity to avoid perl crash or warning
- remove -T flag to have same version on all os
- a new Makefile.pl for tgz install (check dependencies)
- fix a bug with --print and archive mode
- add a planning.bat on windows to insert a task in planning

* Wed Mar 3 2004 Eric Gerbier <gerbier@users.sourceforge.net> 2.0.0
- add ignore_case directive/option
- add history directive/option
- add archive directive
- bug in soustractive alias
- remove/clean global var
- split in 2 packages command-line and gui
- add a makefile for tgz package
- add macro VERBOSE to suppress useless mail if no changes

* Wed Jan 28 2004 Eric Gerbier <gerbier@users.sourceforge.net> 1.8.0
- for new files, display inode date
- for deleted files, display parent change date
- output format change to allow automatic parsing (comments)
- add all perl dependencies in package
- resolv all name to absolute path
- afick-tk, more homogenous gui
- afick-tk, add tree view
- afick-tk, add balloon for context help

* Sat Jan 17 2004 Eric Gerbier <gerbier@users.sourceforge.net> 1.7.0
- add a line to explain fields on print action
- add html doc 
- add acl instead uid field on windows (Win32::Filesecurity)
- now use POSIX macros for portability
- afick-tk, add a little 'wizard'
- afick-tk, now display file number and percent
- clean code with more global var and hash
- add sha1 checksum

* Thu Jan 01 2004 Eric Gerbier <gerbier@users.sourceforge.net> 1.6.0
- fix a bug on report_url
- detect changes during scan
- fix a bug on deleted directories if not report_full
- add a new -t/timing flag to print cpu statistics
- add a new -r/--running_files to warn about modified files during program run

* Wed Dec 10 2003 Eric Gerbier <gerbier@users.sourceforge.net> 1.5.0
- add exclude_suffix directive
- add progress option for afick-tk
- new sub warning
- add new warnings on bad config lines
- fix a bug on alias resolution
- afick-tk, add progress bar and file stat
- afick-tk, add warning section, and update window
- afick-tk, rewrite widget structure
- afick-tk, new warning sub
- afick-tk, change saved output to .log
- afick-tk, rewrite help

* Thu Nov 27 2003 Eric Gerbier <gerbier@users.sourceforge.net> 1.4.1
- afick.cron, now test -x (leo west)
- rewrite afick help in a better way
- a better control between afick and afick.pl calls

* Thu Nov 13 2003 Eric Gerbier <gerbier@users.sourceforge.net> 1.4.0
- add an auto-control to check afick changes
- afick-tk, version in title
- perl checking for sub arguments
- change getopt for compatibility with old perl version
- allways get a hostname in cron job
- the exit status now depends upon changes

* Tue Oct 14 2003 Eric Gerbier <gerbier@users.sourceforge.net> 1.3.0
- add file type
- sort results
- add menu entries
- add report_full_newdel directive
- add ignore_missing_file directive
- add WARNING word for all warning
- add long options (gnu, posix)
- default config file change according operating system
- afick-tk, change cursor to clock during search
- afick-tk, radio-buttons to configure options
- afick-tk, fix bug in save config on windows

* Thu Oct 02 2003 Eric Gerbier <gerbier@users.sourceforge.net> 1.2.0
- add report and debug subroutines to have more general use
- add report_url directive (stdout, stderr, null)
- now have summary and detailed output
- test for directories for equal scan
- automatic database init on first install
- fix a bug on -l flag
- remove checksum on sockets
- afick-tk , edit and save config file
- afick-tk , report stderr too
- afick-tk , clear output after each operation
- afick-tk , outpout expand to fill window

* Mon Sep 22 2003 Eric Gerbier <gerbier@users.sourceforge.net> 1.1.0
- debian appliance
- new warn_dead_symlinks directive
- bugfix in md5 checksum
- distinguish dir and dir/ for =
- add quit buttons in afick-tk
- add about window in afick-tk
- add manpage for afick-tk
- add log file for cron jobs
- add logrotate for log file
- improved cron job (mailto and lines macros)

* Sat Sep 20 2003 Eric Gerbier <gerbier@users.sourceforge.net> 1.0.0
- default config file is /etc/afick.conf
- default database in /var/lib/afick
- default run by cron on a daily base
- database name now in config file (-b option is obsolete now)
- new "equals" file directive in config file ( directories to scan, withour recurse)
- new beta tk interface : afick-tk
- add ctime (c) and block count (b) parameters
- md5 parameter for use instead "h" (obsolete)

* Mon Aug 18 2003 Eric Gerbier <gerbier@users.sourceforge.net>
- release 0.9.3 : add aliases
- new config man page

* Tue Aug 12 2003 Eric Gerbier <gerbier@users.sourceforge.net>
- release 0.9.2 : add attributes

* Tue Sep 10 2002 Eric Gerbier <gerbier@users.sourceforge.net>
- Initial spec file created by autospec ver. 0.6 with rpm 2.5 compatibility
