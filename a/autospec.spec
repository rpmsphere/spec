Name:          autospec
Version:       1.10.0
Release:       2.1
Summary:       Create specfiles and automatically update/check/fix rpm packages
Summary(it):   Crea specfile ed aggiorna/controlla/corregge in modo automatico pacchetti rpm
Group:         Development/Tools
URL:           https://www.openmamba.org/packages.html
Source:        autospec-%{version}.tar.bz2
Requires:      cpio, coreutils, curl, findutils, grep, sed
Requires:      /bin/mktemp
Requires:      /usr/bin/getopt
Requires:      bzip2
Requires:      gzip
Requires:      unzip
Requires:      ftp
Requires:      %{name}-plugins = %{?epoch:%epoch:}%{version}-%{release}
License:       GPL
BuildArch:     noarch

%description
Autospec is a tool for automatically generating specfiles and updating rpm packages.
Install autospec if you are a packager or you just want to build/upgrade rpm packages in an easy and quick way.

%description -l it
Autospec è un tool in grado di generare in modo automatico specfile ed aggiornare pacchetti rpm.
Installa autospec se sei un packager o se vuoi creare/aggiornare pacchetti rpm in modo semplice e rapido.

%package plugins
Summary:       Autospec plugins
Summary(it):   Plugin di autospec
Group:         Development/Tools
Requires:      %{name}-libs = %{?epoch:%epoch:}%{version}-%{release}
Requires:      %{name}-tests = %{?epoch:%epoch:}%{version}-%{release}
Requires(pre): rpm

%description plugins
This package contains the plugins needed for generating specfiles, updating rpm packages, and extracting files from a source rpm package.

%description -l it plugins
Questo pacchetto contiene i plugin necessari per generare specfile, aggiornare pacchetti rpm, estrarre file da pacchetti source rpm (srpm).

%package libs
Summary:       Autospec libraries
Summary(it):   Librerie di autospec
Group:         Development/Tools

%description libs
This package contains the library functions needed by autospec, and their plugins.
They can be used by external tools that manage rpm packages and specfiles.

%description -l it libs
Questo pacchetto contiene le librerie necessarie al funzionamento di autospec e dei suoi plugin.
Possono anche essere stilizzate da tool esterni che lavorano su rpm e specfile.

%package tests
Summary:       Autospec tests
Summary(it):   Test per autospec
Group:         Development/Tools

%description tests
This package contains the tests to check rpm packages for quality and security issues.

%description -l it tests
Questo pacchetto contiene i test per il controllo di qualità e sicurezza dei pacchetti rpm.
Possono anche essere stilizzate da tool esterni che lavorano su rpm e specfile.

%package tools
Summary:       Autospec extra tools
Summary(it):   Programmi extra basati su autospec
Group:         Development/Tools
Requires:      %{name}-libs = %{?epoch:%epoch:}%{version}-%{release}

%description tools
This package contains some extra tools.

%description -l it tools
Questo pacchetto contiene alcuni script extra.

%prep
%setup -q

%build
make prefix=%{_prefix}

%install
[ "$RPM_BUILD_ROOT" != / ] && rm -rf "$RPM_BUILD_ROOT"
make install DESTDIR=$RPM_BUILD_ROOT prefix=%{_prefix}

%files
%{_bindir}/%{name}
%lang(it) %{_mandir}/it/man1/autospec.*
%lang(it) %{?_localedir:%{_localedir}}%{!?_localedir:%_datadir/locale}/it/LC_MESSAGES/autospec_fe.mo
%doc AUTHORS BUGS ChangeLog COPYING NEWS TODO
%doc autospec-it-HOWTO

%files plugins
%{_bindir}/config-getvar
%{_bindir}/pck-extract
%{_bindir}/pck-update
%{_bindir}/spec-create
%config %{_sysconfdir}/%{name}.conf
%{_datadir}/%{name}/templates/*
%lang(it) %{?_localedir:%{_localedir}}%{!?_localedir:%_datadir/locale}/it/LC_MESSAGES/config-getvar.mo
%lang(it) %{?_localedir:%{_localedir}}%{!?_localedir:%_datadir/locale}/it/LC_MESSAGES/pck-extract.mo
%lang(it) %{?_localedir:%{_localedir}}%{!?_localedir:%_datadir/locale}/it/LC_MESSAGES/pck-update.mo
%lang(it) %{?_localedir:%{_localedir}}%{!?_localedir:%_datadir/locale}/it/LC_MESSAGES/spec-create.mo

%files libs
%{_datadir}/%{name}/lib/*
%lang(it) %{?_localedir:%{_localedir}}%{!?_localedir:%_datadir/locale}/it/LC_MESSAGES/lib*.mo

%files tests
%{_datadir}/%{name}/tests
%lang(it) %{?_localedir:%{_localedir}}%{!?_localedir:%_datadir/locale}/it/LC_MESSAGES/test??_*.mo

%files tools
%{_bindir}/extract-specs
%{_bindir}/autoupdate-*

%changelog
* Tue May 22 2012 Wei-Lun Chao <bluebat@member.fsf.org> - 1.10.0
- Rebuilt for Fedora
* Tue May 01 2012 Davide Madrisan <davide.madrisan@gmail.com> 1.10.0-1mamba
- update to 1.10.0
* Wed Apr 18 2012 Davide Madrisan <davide.madrisan@gmail.com> 1.9.4-1mamba
- update to 1.9.4
* Sun Apr 01 2012 Davide Madrisan <davide.madrisan@gmail.com> 1.9.3-1mamba
- update to 1.9.3
* Sun Feb 05 2012 Davide Madrisan <davide.madrisan@gmail.com> 1.9.2-1mamba
- update to 1.9.2
* Wed Jan 25 2012 Davide Madrisan <davide.madrisan@gmail.com> 1.9.1-1mamba
- update to 1.9.1
* Sun Jan 15 2012 Davide Madrisan <davide.madrisan@gmail.com> 1.9.0-1mamba
- update to 1.9.0
* Thu Dec 29 2011 Davide Madrisan <davide.madrisan@gmail.com> 1.8.2-1mamba
- update to 1.8.2
* Tue Dec 20 2011 Davide Madrisan <davide.madrisan@gmail.com> 1.8.1-1mamba
- update to 1.8.1
* Sat Apr 02 2011 Davide Madrisan <davide.madrisan@gmail.com> 1.8.0-1mamba
- update to 1.8.0
* Sun Mar 20 2011 Davide Madrisan <davide.madrisan@gmail.com> 1.7.3-1mamba
- update to 1.7.3
* Thu Feb 10 2011 Silvan Calarco <silvan.calarco@mambasoft.it> 1.7.2-2mamba
- restored requirements for autospec-plugins, autospec-libs and autospec-tests
- removed %%dir entry for non empty directories
* Sat Jan 15 2011 Davide Madrisan <davide.madrisan@gmail.com> 1.7.2-1mamba
- update to 1.7.2
* Wed Dec 29 2010 Davide Madrisan <davide.madrisan@gmail.com> 1.7.1-1mamba
- update to 1.7.1
* Wed Dec 22 2010 Davide Madrisan <davide.madrisan@gmail.com> 1.7.0-1mamba
- update to 1.7.0
* Sun Nov 28 2010 Davide Madrisan <davide.madrisan@gmail.com> 1.6.3-1mamba
- update to 1.6.3
* Tue Nov 02 2010 Davide Madrisan <davide.madrisan@gmail.com> 1.6.2-1mamba
- update to 1.6.2
* Fri Oct 22 2010 Davide Madrisan <davide.madrisan@gmail.com> 1.6.1-1mamba
- update to 1.6.1
* Wed Oct 06 2010 Davide Madrisan <davide.madrisan@gmail.com> 1.6.0-1mamba
- update to 1.6.0
* Sat Aug 21 2010 Silvan Calarco <silvan.calarco@mambasoft.it> 1.5.0-11mamba
- added patch get_default_arch_from_rpm that uses rpm --eval %%{_host_cpu} to find default architecture
* Mon Aug 16 2010 Silvan Calarco <silvan.calarco@mambasoft.it> 1.5.0-10mamba
- added noarch_allow_upload_to_given_arch_only-2 patch to fix noarch support also for operations 6,7 and 11
* Thu Aug 12 2010 Silvan Calarco <silvan.calarco@mambasoft.it> 1.5.0-9mamba
- patch noarch_allow_upload_to_given_arch_only: support configuration of @arch@ in arch_no_arch_upload
* Mon Aug 09 2010 Silvan Calarco <silvan.calarco@mambasoft.it> 1.5.0-8mamba
- patch replace_obsolete_PreReq: replace obsolete PreReq tags with Requires(pre) or Requires(post)
* Sun Aug 08 2010 Silvan Calarco <silvan.calarco@mambasoft.it> 1.5.0-7mamba
- added hidden_spec_old_file patch: create specfile backups as old files (i.e. prefixed by '.')
- patch fix_undefined_SPECFILE_PREPROCESSED: infofile.create bug when specfile_preprocessed already exists
* Wed Aug 04 2010 Silvan Calarco <silvan.calarco@mambasoft.it> 1.5.0-6mamba
- added PreReq for rpm also to autospec-plugins package
* Wed Aug 04 2010 Silvan Calarco <silvan.calarco@mambasoft.it> 1.5.0-5mamba
- added patch dont_backup_srpm_with_nosrpm_option to make it work better with multiarch uploads
* Mon Aug 02 2010 Silvan Calarco <silvan.calarco@mambasoft.it> 1.5.0-4mamba
- added patch: use rpm option --whatprovides to find unidentified requirements
* Mon Aug 02 2010 Silvan Calarco <silvan.calarco@mambasoft.it> 1.5.0-3mamba
- added patch to replace apt with smart in default configured application for rpm download and installation
* Sat Jul 31 2010 Silvan Calarco <silvan.calarco@mambasoft.it> 1.5.0-2mamba
- added patch install_srpms_with_nodeps for compatibility with rpm5
* Mon Jul 19 2010 Davide Madrisan <davide.madrisan@gmail.com> 1.5.0-1mamba
- update to 1.5.0
* Thu Jul 01 2010 Silvan Calarco <silvan.calarco@mambasoft.it> 1.4.17-4mamba
- patch: reduce severity from error to warning if host command fails as happens using qemu-arm environment
* Thu Jul 01 2010 Silvan Calarco <silvan.calarco@mambasoft.it> 1.4.17-3mamba
- added fix_get_RPMS_name patch to fix identification of old packages to backup
* Thu Jun 17 2010 Silvan Calarco <silvan.calarco@mambasoft.it> 1.4.17-2mamba
- added PreReq for rpm for correct user configuration
- added patches: curl_pass_netlink_opts and rpm-whatprovides-optimize
* Fri May 14 2010 Davide Madrisan <davide.madrisan@gmail.com> 1.4.17-1mamba
- update to 1.4.17
* Thu Apr 15 2010 Davide Madrisan <davide.madrisan@gmail.com> 1.4.16-1mamba
- update to 1.4.16
* Wed Mar 24 2010 Davide Madrisan <davide.madrisan@gmail.com> 1.4.15-1mamba
- update to 1.4.15
* Sat Mar 13 2010 Davide Madrisan <davide.madrisan@gmail.com> 1.4.14-1mamba
- update to 1.4.14
* Wed Feb 17 2010 Davide Madrisan <davide.madrisan@gmail.com> 1.4.13-1mamba
- update to 1.4.13
* Wed Feb 17 2010 Davide Madrisan <davide.madrisan@gmail.com> 1.4.12-1mamba
- update to 1.4.12
* Tue Jan 12 2010 Davide Madrisan <davide.madrisan@gmail.com> 1.4.11-1mamba
- update to 1.4.11
* Thu Jan 10 2010 Davide Madrisan <davide.madrisan@gmail.com> 1.4.10-1mamba
- update to 1.4.10
* Fri Oct 23 2009 Davide Madrisan <davide.madrisan@gmail.com> 1.4.9-1mamba
- update to 1.4.9
* Wed Oct 14 2009 Davide Madrisan <davide.madrisan@gmail.com> 1.4.8-1mamba
- update to 1.4.8
* Sun Jul 05 2009 Davide Madrisan <davide.madrisan@gmail.com> 1.4.7-1mamba
- update to 1.4.7
* Sun Apr 19 2009 - Silvan Calarco <silvan.calarco@mambasoft.it> (1.4.6-3mamba)
- applied a fix to the relocate_RPM_dirs patch
* Sat Apr 18 2009 - Silvan Calarco <silvan.calarco@mambasoft.it> (1.4.6-2mamba)
- added relocate_RPM_dirs patch
* Fri Apr 10 2009 Davide Madrisan <davide.madrisan@gmail.com> 1.4.6-1mamba
- update to 1.4.6
* Sun Feb 15 2009 Davide Madrisan <davide.madrisan@gmail.com> 1.4.5-1mamba
- update to 1.4.5
- add missing %%defattr in 'plugins' subpackage
* Tue Dec 23 2008 Davide Madrisan <davide.madrisan@gmail.com> 1.4.4-1mamba
- update to 1.4.4 (Christmas Release)
* Thu Nov 20 2008 Davide Madrisan <davide.madrisan@gmail.com> 1.4.3-1mamba
- update to 1.4.3
* Fri Nov 14 2008 Davide Madrisan <davide.madrisan@gmail.com> 1.4.2-1mamba
- update to 1.4.2
* Wed Oct 29 2008 Davide Madrisan <davide.madrisan@gmail.com> 1.4.1-1mamba
- update to 1.4.1
* Mon Oct 13 2008 Davide Madrisan <davide.madrisan@gmail.com> 1.4.0-1mamba
- update to 1.4.0
- new subpackages plugins libs tools
* Fri Oct 03 2008 Davide Madrisan <davide.madrisan@gmail.com> 1.3.2-1mamba
- update to 1.3.2
* Tue Sep 30 2008 Davide Madrisan <davide.madrisan@gmail.com> 1.3.1-1mamba
- update to 1.3.1
* Mon Sep 01 2008 Davide Madrisan <davide.madrisan@gmail.com> 1.3.0-1mamba
- update to 1.3.0
* Fri Aug 15 2008 Davide Madrisan <davide.madrisan@gmail.com> 1.2.2-1mamba
- update to 1.2.2
* Fri Jun 13 2008 Davide Madrisan <davide.madrisan@gmail.com> 1.2.1-1mamba
- update to 1.2.1
* Sun May 11 2008 Davide Madrisan <davide.madrisan@gmail.com> 1.2.0-1mamba
- update to 1.2.0
- plugins moved to %%{_datadir}/%%{name}/plugins
- install autospec templates %%{_datadir}/%%{name}/templates
* Fri Feb 29 2008 Davide Madrisan <davide.madrisan@gmail.com> 1.1.9-1mamba
- update to 1.1.9
* Wed Jan 30 2008 Davide Madrisan <davide.madrisan@gmail.com> 1.1.8-1mamba
- update to version 1.1.8
* Sat Dec 31 2007 Davide Madrisan <davide.madrisan@gmail.com> 1.1.7-1mamba
- update to version 1.1.7
* Sun Dec 23 2007 Davide Madrisan <davide.madrisan@gmail.com> 1.1.6-1mamba
- update to version 1.1.6
* Fri Dec 14 2007 Davide Madrisan <davide.madrisan@gmail.com> 1.1.5-1mamba
- update to version 1.1.5
* Mon Dec 10 2007 Davide Madrisan <davide.madrisan@gmail.com> 1.1.4-1mamba
- update to version 1.1.4
* Sun Dec 02 2007 Davide Madrisan <davide.madrisan@gmail.com> 1.1.3-1mamba
- update to version 1.1.3
* Thu Nov 29 2007 Davide Madrisan <davide.madrisan@gmail.com> 1.1.2-1mamba
- update to version 1.1.2
* Mon Nov 26 2007 Davide Madrisan <davide.madrisan@gmail.com> 1.1.1-1mamba
- update to version 1.1.1
- add requirement for ftp
* Tue Nov 20 2007 Davide Madrisan <davide.madrisan@gmail.com> 1.1.0-1mamba
- update to version 1.1.0
* Tue Nov 13 2007 Davide Madrisan <davide.madrisan@gmail.com> 1.0.2-1mamba
- update to version 1.0.2
* Fri Oct 26 2007 Davide Madrisan <davide.madrisan@gmail.com> 1.0.1-1mamba
- update to version 1.0.1
- do not use the %%makeinstall macro for compatibility with other distros
* Wed Sep 26 2007 Davide Madrisan <davide.madrisan@gmail.com> 1.0-1mamba
- update to version 1.0
* Sat Sep 08 2007 Silvan Calarco <silvan.calarco@mambasoft.it> 0.9.99-2mamba
- patch: remove protocol prefix (https:// ftp://) before checking server dns reachability
* Thu Sep 06 2007 Davide Madrisan <davide.madrisan@gmail.com> 0.9.99-1mamba
- update to version 0.9.99 by autospec
* Thu Jun 07 2007 Davide Madrisan <davide.madrisan@gmail.com> 0.9.98-1mamba
- update to version 0.9.98 by autospec
* Sat May 05 2007 Davide Madrisan <davide.madrisan@gmail.com> 0.9.97-1mamba
- update to version 0.9.97 by autospec
* Tue Apr 24 2007 Davide Madrisan <davide.madrisan@gmail.com> 0.9.96-1mamba
- update to version 0.9.96 by autospec
* Tue Mar 27 2007 Davide Madrisan <davide.madrisan@gmail.com> 0.9.95-1mamba
- update to version 0.9.95 by autospec
* Thu Mar 01 2007 Davide Madrisan <davide.madrisan@gmail.com> 0.9.94-1qilnx
- update to version 0.9.94 by autospec
* Fri Feb 09 2007 Davide Madrisan <davide.madrisan@qilinux.it> 0.9.93-1qilnx
- update to version 0.9.93 by autospec
* Mon Jan 29 2007 Davide Madrisan <davide.madrisan@qilinux.it> 0.9.92-1qilnx
- update to version 0.9.92 by autospec
* Tue Jan 09 2007 Davide Madrisan <davide.madrisan@qilinux.it> 0.9.91-1qilnx
- update to version 0.9.91 by autospec
* Thu Dec 21 2006 Davide Madrisan <davide.madrisan@qilinux.it> 0.9.90-1qilnx
- update to version 0.9.90 by autospec
* Wed Nov 29 2006 Davide Madrisan <davide.madrisan@qilinux.it> 0.9.14-1qilnx
- update to version 0.9.14 by autospec
- ncompress tool removed from the list of static requirements
- do require /bin/mktemp instead of /usr/bin/mktemp for portability
* Mon Nov 06 2006 Davide Madrisan <davide.madrisan@qilinux.it> 0.9.13-1qilnx
- update to version 0.9.13 by autospec
* Mon Jun 19 2006 Davide Madrisan <davide.madrisan@qilinux.it> 0.9.12-1qilnx
- update to version 0.9.12 by autospec
* Sun Jun 11 2006 Davide Madrisan <davide.madrisan@qilinux.it> 0.9.11-1qilnx
- update to version 0.9.11 by autospec
- new documentation file `autobuild_example.rules'
* Wed May 31 2006 Davide Madrisan <davide.madrisan@qilinux.it> 0.9.10-1qilnx
- update to version 0.9.10 by autospec
* Tue May 16 2006 Davide Madrisan <davide.madrisan@qilinux.it> 0.9.9-1qilnx
- update to version 0.9.9 by autospec
* Mon May 08 2006 Davide Madrisan <davide.madrisan@qilinux.it> 0.9.8-1qilnx
- update to version 0.9.8 by autospec
* Mon Apr 17 2006 Davide Madrisan <davide.madrisan@qilinux.it> 0.9.7-1qilnx
- update to version 0.9.7 by autospec
* Mon Mar 20 2006 Davide Madrisan <davide.madrisan@qilinux.it> 0.9.6-1qilnx
- update to version 0.9.6 by autospec
* Sun Mar 05 2006 Davide Madrisan <davide.madrisan@qilinux.it> 0.9.5-1qilnx
- update to version 0.9.5 by autospec
* Fri Feb 03 2006 Davide Madrisan <davide.madrisan@qilinux.it> 0.9.4-1qilnx
- update to version 0.9.4 by autospec
* Sat Jan 14 2006 Davide Madrisan <davide.madrisan@qilinux.it> 0.9.3-1qilnx
- update to version 0.9.3 by autospec
- requires rpm >= 4.4.4
* Sun Jan 01 2006 Davide Madrisan <davide.madrisan@qilinux.it> 0.9.2-1qilnx
- update to version 0.9.2 by autospec
* Sun Dec 18 2005 Davide Madrisan <davide.madrisan@qilinux.it> 0.9.1-1qilnx
- update to version 0.9.1 by autospec
* Thu Dec 15 2005 Davide Madrisan <davide.madrisan@qilinux.it> 0.9.0-1qilnx
- update to version 0.9.0
* Sat Dec 03 2005 Davide Madrisan <davide.madrisan@qilinux.it> 0.8.9-1qilnx
- update to version 0.8.9
* Sat Nov 26 2005 Davide Madrisan <davide.madrisan@qilinux.it> 0.8.8-qilnx
- update to version 0.8.8
* Thu Nov 24 2005 Davide Madrisan <davide.madrisan@qilinux.it> 0.8.7-qilnx
- update to version 0.8.7
- fixed typo in license tag
* Sun Nov 20 2005 Davide Madrisan <davide.madrisan@qilinux.it> 0.8.6-qilnx
- update to version 0.8.6
* Tue Nov 15 2005 Davide Madrisan <davide.madrisan@qilinux.it> 0.8.5-qilnx
- update to version 0.8.5
* Thu Nov 10 2005 Davide Madrisan <davide.madrisan@qilinux.it> 0.8.4-qilnx
- update to version 0.8.4
- requires host
* Sun Nov 06 2005 Davide Madrisan <davide.madrisan@qilinux.it> 0.8.3-1qilnx
- update to version 0.8.3
- requires cpio
* Sun Oct 30 2005 Davide Madrisan <davide.madrisan@qilinux.it> 0.8.2-1qilnx
- update to version 0.8.2
* Sun Oct 16 2005 Davide Madrisan <davide.madrisan@qilinux.it> 0.8.1-1qilnx
- update to version 0.8.1
* Mon Oct 09 2005 Davide Madrisan <davide.madrisan@qilinux.it> 0.8.0-1qilnx
- update to version 0.8.0
* Sun Oct 02 2005 Davide Madrisan <davide.madrisan@qilinux.it> 0.7.3-1qilnx
- update to version 0.7.3
- added more runtime requirements
* Fri Sep 30 2005 Davide Madrisan <davide.madrisan@qilinux.it> 0.7.2-1qilnx
- update to version 0.7.2
- requires sudo
* Wed Sep 28 2005 Davide Madrisan <davide.madrisan@qilinux.it> 0.7.1-1qilnx
- update to version 0.7.1
* Sat Sep 24 2005 Davide Madrisan <davide.madrisan@qilinux.it> 0.7.0-1qilnx
- update to version 0.7.0
* Wed Aug 31 2005 Davide Madrisan <davide.madrisan@qilinux.it> 0.6.4-1qilnx
- update to version 0.6.4
* Fri Aug 05 2005 Davide Madrisan <davide.madrisan@qilinux.it> 0.6.3-1qilnx
- update to version 0.6.3
* Fri Jul 29 2005 Davide Madrisan <davide.madrisan@qilinux.it> 0.6.2-1qilnx
- update to version 0.6.2
* Sat May 28 2005 Davide Madrisan <davide.madrisan@qilinux.it> 0.6.1-1qilnx
- update to version 0.6.1
* Mon Apr 25 2005 Davide Madrisan <davide.madrisan@qilinux.it> 0.6.0-1qilnx
- update to version 0.6.0
* Sat Apr 09 2005 Davide Madrisan <davide.madrisan@qilinux.it> 0.5.4-1qilnx
- update to version 0.5.4
* Fri Mar 25 2005 Davide Madrisan <davide.madrisan@qilinux.it> 0.5.3-1qilnx
- update to version 0.5.3
* Sun Mar 21 2005 Davide Madrisan <davide.madrisan@qilinux.it> 0.5.2-1qilnx
- update to version 0.5.2
* Sun Mar 13 2005 Davide Madrisan <davide.madrisan@qilinux.it> 0.5.1-1qilnx
- update to version 0.5.1
* Fri Mar 11 2005 Davide Madrisan <davide.madrisan@qilinux.it> 0.5.0-1qilnx
- update to version 0.5.0
* Fri Mar 02 2005 Davide Madrisan <davide.madrisan@qilinux.it> 0.4.15-1qilnx
- update to version 0.4.15
* Tue Feb 15 2005 Davide Madrisan <davide.madrisan@qilinux.it> 0.4.14-1qilnx
- update to version 0.4.14
* Sat Jan 29 2005 Davide Madrisan <davide.madrisan@qilinux.it> 0.4.13-1qilnx
- update to version 0.4.13
* Mon Jan 24 2005 Davide Madrisan <davide.madrisan@qilinux.it> 0.4.12-1qilnx
- update to version 0.4.12
* Sun Jan 16 2005 Davide Madrisan <davide.madrisan@qilinux.it> 0.4.11-1qilnx
- update to version 0.4.11
* Sun Jan 09 2005 Davide Madrisan <davide.madrisan@qilinux.it> 0.4.10-1qilnx
- update to version 0.4.10
* Thu Dec 16 2004 Davide Madrisan <davide.madrisan@qilinux.it> 0.4.9-2qilnx
- added BUGS to %%docs
* Wed Dec 15 2004 Davide Madrisan <davide.madrisan@qilinux.it> 0.4.9-1qilnx
- update to version 0.4.9
* Sun Nov 14 2004 Davide Madrisan <davide.madrisan@qilinux.it> 0.4.8-1qilnx
- update to version 0.4.8
* Sun Oct 24 2004 Davide Madrisan <davide.madrisan@qilinux.it> 0.4.7-1qilnx
- update to version 0.4.7 by autospec
* Tue Oct 19 2004 Davide Madrisan <davide.madrisan@qilinux.it> 0.4.6-1qilnx
- update to version 0.4.6 by autospec
* Thu Oct 14 2004 Davide Madrisan <davide.madrisan@qilinux.it> 0.4.5-1qilnx
- update to version 0.4.5 by autospec
* Wed Oct 06 2004 Davide Madrisan <davide.madrisan@qilinux.it> 0.4.4-1qilnx
- update to version 0.4.4 by autospec
* Tue Oct 05 2004 Davide Madrisan <davide.madrisan@qilinux.it> 0.4.3-1qilnx
- update to version 0.4.3 by autospec
- added the document rpm4QiLinux-it-HOWTO
* Mon Oct 04 2004 Davide Madrisan <davide.madrisan@qilinux.it> 0.4.2-1qilnx
- update to version 0.4.2 by autospec
* Fri Oct 01 2004 Davide Madrisan <davide.madrisan@qilinux.it> 0.4.1-1qilnx
- update to version 0.4.1
* Mon Sep 13 2004 Davide Madrisan <davide.madrisan@qilinux.it> 0.4.0-1qilnx
- update to version 0.4.0
* Tue Sep 01 2004 Davide Madrisan <davide.madrisan@qilinux.it> 0.3.9-1qilnx
- update to version 0.3.9
* Fri Aug 27 2004 Davide Madrisan <davide.madrisan@qilinux.it> 0.3.8-1qilnx
- update to version 0.3.8
* Wed Aug 25 2004 Davide Madrisan <davide.madrisan@qilinux.it> 0.3.7-1qilnx
- update to version 0.3.7
* Wed Aug 20 2004 Davide Madrisan <davide.madrisan@qilinux.it> 0.3.6-1qilnx
- update to version 0.3.6
* Sat Aug 09 2004 Davide Madrisan <davide.madrisan@qilinux.it> 0.3.5-1qilnx
- update to version 0.3.5
* Thu Aug 05 2004 Davide Madrisan <davide.madrisan@qilinux.it> 0.3.4-1qilnx
- first public release
