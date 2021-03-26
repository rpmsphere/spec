#
# spec file for package moblin-panel-web (Version 0.1.3)
#
# Copyright (c) 2010 SUSE LINUX Products GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#

# norootforbuild

Name: moblin-panel-web
Summary: Moblin Internet Panel for use with the Chrome Browser
Group: Applications/Internet
Version: 0.1.6
License: GPLv2
URL: http://www.moblin.org/
Release: 27.2
Source0: %{name}-%{version}.tar.bz2
Source1: moblin-panel-web.ff
Source2: png-files.tar.gz
Patch1:  moblin-panel-web-0.1.6-fix-64bit.patch
Patch2:  moblin-panel-web-correct-install-path.patch
Patch3:  moblin-panel-web-fix-64bit-casting.patch
Patch4:	 fix-sync-preferences.patch
Patch5:	chromium7-profile-provider.patch
Patch6:	chromium-browser_exec.patch

BuildRequires: python
BuildRequires: gnome-common
BuildRequires: intltool

BuildRequires: pkgconfig(glib-2.0)
BuildRequires: pkgconfig(gtk+-2.0)
Buildrequires: libmx-devel
BuildRequires: mutter-moblin-devel
BuildRequires: pkgconfig(xt)
BuildRequires: pkgconfig(sqlite3)
BuildRequires: zip
BuildRequires: chromium-devel
BuildRequires: gcc-c++

Provides: panel(web)

Requires: rsync
Requires(post): %{_sbindir}/update-alternatives
Requires(postun): %{_sbindir}/update-alternatives

Requires: chromium
Obsoletes: moblin-web-browser-panel < 1.9.3_20091015-11.1
Obsoletes: moblin-panel-internet

%description
Moblin internet panel for use with the Chrome Browser

%prep
%setup -q 
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1

tar zxvf %{SOURCE2}

%build
./autogen.sh 
%configure

make %{?_smp_mflags}

%install
%makeinstall

install -d %{buildroot}/usr/share/mutter-moblin/panels
install -m 755 %{SOURCE1} %{buildroot}/%{_libexecdir}/moblin-panel-web.ff
sed -i 's.@libexecdir@.%{_libexecdir}.g' %{buildroot}/%{_libexecdir}/moblin-panel-web.ff

%find_lang moblin-panel-web

mv %{buildroot}/%{_libexecdir}/moblin-panel-web %{buildroot}/%{_libexecdir}/moblin-panel-web.bin
mv %{buildroot}/usr/share/dbus-1/services/org.moblin.UX.Shell.Panels.internet.service %{buildroot}/usr/share/dbus-1/services/org.moblin.UX.Shell.Panels.internet.service.ff

%clean
rm -rf %{buildroot}

%post
/sbin/ldconfig
update-alternatives --verbose --install %{_libexecdir}/moblin-panel-web moblin-panel-web %{_libexecdir}/moblin-panel-web.ff 1000 \
 --slave /usr/share/dbus-1/services/org.moblin.UX.Shell.Panels.internet.service org.moblin.UX.Shell.Panels.internet.service /usr/share/dbus-1/services/org.moblin.UX.Shell.Panels.internet.service.ff

%posttrans 
update-alternatives --verbose --install %{_libexecdir}/moblin-panel-web moblin-panel-web %{_libexecdir}/moblin-panel-web.ff 1000 \
 --slave /usr/share/dbus-1/services/org.moblin.UX.Shell.Panels.internet.service org.moblin.UX.Shell.Panels.internet.service /usr/share/dbus-1/services/org.moblin.UX.Shell.Panels.internet.service.ff

%postun
/sbin/ldconfig
if [ $1 = 0 ]; then
   %{_sbindir}/update-alternatives --remove moblin-panel-web %{_libexecdir}/moblin-panel-web.ff
fi

%files -f moblin-panel-web.lang
%defattr(-,root,root,-)
%{_datadir}/mutter-moblin/panels/*.desktop
%{_libexecdir}/moblin-panel-web.ff
%{_libexecdir}/moblin-panel-web.bin
%{_datadir}/dbus-1/services/org.moblin.UX.Shell.Panels.internet.service.ff
%{_datadir}/moblin-panel-web/netpanel/*.png
%{_datadir}/moblin-panel-web/netpanel/*.css
%{_datadir}/moblin-panel-web/search-icons/*.ico
#%exclude %{_libdir}/debug/

%changelog
* Wed Jul 13 2016 Wei-Lun Chao <bluebat@member.fsf.org> -
- Rebuild for Fedora
* Tue Oct 26 2010 Wei-Lun Chao <bluebat@member.fsf.org>
- Rebuild for OSSII
* Thu Oct  7 2010 awafaa@opensuse.org
- Add chromium-browser_exec.patch to fix correct browser name
- Remove chromium-lib-svn55059.patch as not needed
* Tue Oct  5 2010 awafaa@opensuse.org
- Replace LD_LIBRARY_PATH=/usr/lib/chromium-browser with
  LD_LIBRARY_PATH=/usr/lib/chromium in moblin-panel-web.ff
* Tue Oct  5 2010 glin@novell.com
- Amend moblin-panel-web.ff to change the path according to the
  distro setting
* Thu Sep 30 2010 awafaa@opensuse.org
- Add chromium7-profile-provider.patch to fix build errors against
  chromium 7.0
* Mon Sep 20 2010 awafaa@opensuse.org
- Disable chromium-lib-svn55059.patch
* Fri Sep 17 2010 awafaa@opensuse.org
- Update tarball to sync with upstream
- Add upstream patches fix-sync-preferences.patch &
  chromium-lib-svn55059.patch
* Mon Sep  6 2010 glin@novell.com
- Add moblin-panel-web-fix-64bit-casting.patch to fix a 64bit casting
  error
* Fri Sep  3 2010 glin@novell.com
- Add moblin-panel-web-correct-install-path.patch
  * correct the installation path of the desktop file
  * add a missing file to Makefile.am
- Amend moblin-panel-web.ff to change the path according to the
  distro setting
* Thu Aug  5 2010 andrea@opensuse.org
- added moblin-panel-web-0.1.6-fix-64bit.patch to begin to fix
  64bit compilation
* Mon Jul 12 2010 jlee@novell.com
- Changed to use %%{_libexecdir} in spec file.
* Wed Jul  7 2010 awafaa@opensuse.org
- Remove links to static build of chromium
* Tue Jun 29 2010 awafaa@opensuse.org
- Add moblin-panel-web-chromium-configure.patch to look for
  chromium and not chromium-browser
* Wed Jun 23 2010 awafaa@opensuse.org
- Replace unkown %%autogen macro in spec
* Mon Jun 14 2010 awafaa@opensuse.org
- Use the statically built Chromium from Contrib
* Thu Jun 10 2010 awafaa@opensuse.org
- Update to version 0.1.5, using Chrome as default browser
* Wed Jan 27 2010 glin@novell.com
- Add moblin-panel-web-update-ru-translations.patch to update
  Russian translations.
* Wed Nov 11 2009 glin@novell.com
- initial import
