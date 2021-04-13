Name:        medit
Version:     1.2.92
Release:     0
Summary:     Multiplatform GTK+2 text editor
Group:       Applications/Editors
License:     GPLv2+
URL:         http://mooedit.sourceforge.net/
Source0:     http://sourceforge.net/projects/mooedit/files/medit/%{version}/%{name}-%{version}-devel.tar.bz2
BuildRequires:   libpng-devel
BuildRequires:   gcc-c++ intltool
BuildRequires:   gtk2-devel libxml2-devel pcre-devel pygtk2-devel libSM-devel

%description
Medit is a multiplatform GTK+2 text editor.
Features:
* Configurable syntax highlighting
* Configurable keyboard accelerators
* Multiplatform - works both on unix and windows

%prep
%setup -q -n %{name}-%{version}-devel

%build
export PYTHON=/usr/bin/python2
export LIBS=-lgmodule-2.0
%configure
%__make

%install
%__make DESTDIR=$RPM_BUILD_ROOT install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%{_bindir}/*
%{_datadir}/applications/%{name}.desktop
%{_datadir}/%{name}-1
%{_datadir}/locale/*/LC_MESSAGES/*
%exclude %{_datadir}/icons/hicolor/icon-theme.cache
%{_datadir}/icons/hicolor/48x48/apps/medit.png
%{_mandir}/man1/*
%{_datadir}/doc/%{name}-1

%changelog
* Sun Apr 04 2021 Wei-Lun Chao <bluebat@member.fsf.org> - 1.2.92
- Rebuild for Fedora
* Sat Aug 30 2008 Funda Wang <fundawang@mandriva.org> 0.9.4-1mdv2009.0
+ Revision: 277537
- New version 0.9.4
* Tue Jul 29 2008 Thierry Vignaud <tvignaud@mandriva.com> 0.9.2-3mdv2009.0
+ Revision: 252270
- rebuild
  + Pixel <pixel@mandriva.com>
    - rpm filetriggers deprecates update_menus/update_scrollkeeper/update_mime_database/update_icon_cache/update_desktop_database/post_install_gconf_schemas
* Mon Jan 21 2008 Funda Wang <fundawang@mandriva.org> 0.9.2-1mdv2008.1
+ Revision: 155675
- New version 0.9.2
- rediff patch0
  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot
  + Thierry Vignaud <tvignaud@mandriva.com>
    - kill re-definition of %%buildroot on Pixel's request
* Sat Dec 01 2007 Funda Wang <fundawang@mandriva.org> 0.9.0-1mdv2008.1
+ Revision: 114221
- New version 0.9.0
* Sat Nov 17 2007 Jérôme Soyer <saispo@mandriva.org> 0.8.11-1mdv2008.1
+ Revision: 109208
- New release 0.8.11
* Tue Aug 07 2007 Funda Wang <fundawang@mandriva.org> 0.8.10-1mdv2008.0
+ Revision: 59667
- New version 0.8.10
* Wed Aug 01 2007 Funda Wang <fundawang@mandriva.org> 0.8.9-1mdv2008.0
+ Revision: 57568
- New version 0.8.9
* Thu Jul 12 2007 Funda Wang <fundawang@mandriva.org> 0.8.8-1mdv2008.0
+ Revision: 51500
- Fix file list
- New version
* Thu Jun 14 2007 Funda Wang <fundawang@mandriva.org> 0.8.6-1mdv2008.0
+ Revision: 39539
- SILent renew tarball
- New version
- New version
  add dirty patch that skips update-icon-cache and mime database when building
  + Jérôme Soyer <saispo@mandriva.org>
    - Import medit
* Tue May 09 2006 UTUMI Hirosi <utuhiro78@dummy.org> 0.6.98-1mdk
- new release
* Mon May 08 2006 UTUMI Hirosi <utuhiro78@dummy.org> 0.6.97-1mdk
- first spec for Mandriva
