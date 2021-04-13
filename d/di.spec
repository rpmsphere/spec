%global debug_package %{nil}

Name:           di
Version:        4.49
Release:        1
Summary:        Disk Information Utility
Source:         https://downloads.sourceforge.net/project/diskinfo-di/di-%{version}.tar.gz
URL:            https://gentoo.com/di/
Group:          System/Filesystems
License:        zlib/libpng

%description
'di' is a disk information utility, displaying everything
(and more) that your 'df' command does. It features the
ability to display your disk usage in whatever format you
desire/prefer/are used to. It is designed to be portable
across many platforms.

%prep
%setup -q

%build
make

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}
make prefix=$RPM_BUILD_ROOT%{_prefix} install
mv $RPM_BUILD_ROOT%{_datadir}/locale/{en,en_US}
install -D -m 0644 di.1 $RPM_BUILD_ROOT%{_mandir}/man1/di.1
%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%doc LICENSE* MANIFEST README.txt
%{_bindir}/di
%{_bindir}/mi
%{_mandir}/man1/di.1.*

%changelog
* Sun Apr 4 2021 Wei-Lun Chao <bluebat@member.fsf.org> - 4.49
- Rebuild for Fedora
* Mon Jul  5 2010 pascal.bleser@opensuse.org
- update to 4.25:
  * support for disk quotas has been added
  * the -q command line option will display the usage without the
    user's quota
* Fri May 14 2010 pascal.bleser@opensuse.org
- update to 4.24:
  * a Spanish translation was added
  * the static configuration files were fixed to include missing
    defines
* Tue May 11 2010 pascal.bleser@opensuse.org
- update to 4.23:
  * internationalized titles have been fixed to line up properly
    with their respective columns
  * the default block size display has been changed to use the
    "human readable" (scaled) format
* Thu May  6 2010 pascal.bleser@opensuse.org
- update to 4.22
* Tue Apr 20 2010 pascal.bleser@opensuse.org
- update to 4.21
* Wed Mar 31 2010 pascal.bleser@opensuse.org
- update to 4.20:
  * adds support for VMS
* Tue Feb  2 2010 pascal.bleser@opensuse.org
- update to 4.19:
  * totals have been fixed to add properly when using small block
    sizes (e.g., -d1)
  * totals for mixed pooled and non-pooled filesystems have been
    fixed
  * a fix for automounted directories has been implemented
* Mon Nov 30 2009 pascal.bleser@opensuse.org
- update to 4.18:
  * code cleanup
  * default configuration method has been changed to use a shell script
* Mon Nov 23 2009 pascal.bleser@opensuse.org
- update to 4.17:
  * totals have been changed to be more intuitive and simply add up whatever filesystems are displayed
* Tue Sep 22 2009 pascal.bleser@opensuse.org
- update to 4.16:
  * fixes bugs when filenames are specified on the command line
- changes from 4.14:
  * the disk space labels have been updated to match SI standards, and will correctly display Gigas or Gibis, etc
* Mon May 26 2008 guru@unixtech.be
- new upstream version
* Sun Jan 20 2008 guru@unixtech.be
- new upstream version
* Sat Dec 22 2007 guru@unixtech.be
- moved to openSUSE Build Service
* Fri Jun  1 2007 guru@unixtech.be
- new upstream version
* Tue Feb 27 2007 guru@unixtech.be
- new upstream version
* Fri Nov  3 2006 guru@unixtech.be
- new upstream version
* Fri Oct  6 2006 guru@unixtech.be
- new upstream version
* Sun Sep 24 2006 guru@unixtech.be
- new upstream version
* Sun Sep  3 2006 guru@unixtech.be
- new upstream version
* Thu Mar 30 2006 guru@unixtech.be
- use find_lang macro
- new upstream version
* Mon Nov 21 2005 guru@unixtech.be
- new upstream version
* Tue Jul 26 2005 guru@unixtech.be
- version 4.0
* Fri Mar 12 2004 guru@unixtech.be
- first RPM
