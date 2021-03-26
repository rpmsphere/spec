%global debug_package %{nil}

Name:           computertemp
Version:        0.9.6.1
Release:        6.1
License:        GPL-2.0
Summary:        Displaying the temperature of your CPU and disks
Url:            http://computertemp.berlios.de
Group:          System/GUI/GNOME
Source0:        %{name}-%{version}.tar.bz2
# PATCH-FIX-OPENSUSE computertemp-use-libexecdir.patch vuntz@novell.com -- Make it install the applet in the right directory
Patch0:         computertemp-use-libexecdir.patch
# PATCH-FIX-UPSTREAM computertemp-better-theming-and-fixes.patch vuntz@opensuse.org -- Better handling of dark themes, and various other fixes that were in the same commits. Taken from svn: based on svn diff -r 9:10 and svn diff -r 13:17 http://svn.infinicode.org/computertemp/trunk/computertemp
Patch1:         computertemp-better-theming-and-fixes.patch
BuildRequires:  GConf2-devel
BuildRequires:  intltool
BuildRequires:  pygtk2-devel

%description
Computer Temperature Monitor is a little applet for the GNOME desktop
that shows the temperature of your computer CPU and disks on screen.

It also allows you to log temperatures to a file. You can set alarms to
notify you when a tempertature is reached. Several monitors can be
added to the panel to monitor different sensors.

%lang_package
%prep
%setup -q
%patch0 -p1
%patch1 -p0

%build
export PYTHON=/usr/bin/python2
%configure --disable-schemas-install
%__make %{?jobs:-j%jobs}

%install
%make_install
%find_lang %{name}

sed -i 's|/usr/bin/env python$|/usr/bin/python2|' %{buildroot}%{_libexecdir}/%{name}

%clean
rm -rf %{buildroot}

%post
GCONF_CONFIG_SOURCE=xml:merged:/etc/gconf/gconf.xml.defaults \
	/usr/bin/gconftool-2 --makefile-install-rule computertemp.schemas

%files -f %{name}.lang
%doc AUTHORS ChangeLog NEWS README TODO
%{_libexecdir}/computertemp
%{_libdir}/bonobo/servers/*.server
%{_datadir}/computertemp/
%{python2_sitelib}/computertemp/
/etc/gconf/schemas/computertemp.schemas

%changelog
* Tue Mar 27 2018 Wei-Lun Chao <bluebat@member.fsf.org> - 0.9.6.1
- Rebuild for Fedora
* Wed Dec 15 2010 vuntz@opensuse.org
- Add computertemp-better-theming-and-fixes.patch that contains
  fixes from svn:
  + Removed event_box, now using just a hbox
  + Better handling of dark themes
  + Use of gtk.Tooltip() API instead of deprecated API
  + Better "theme changed" handling
  + Add padding of 2 pixels to the text
  + Allow custom icons in ~/.local/share/computertemp
- Stop passing --libexecdir=%%{_libexecdir}/gnome-panel to
  configure, it's not needed. We can therefore remove the
  gnome-panel BuildRequires.
- Add gnome-python-desktop BuildRequires (which is already a
  Requires), for directory ownership, to fix build.
* Fri Aug 28 2009 vuntz@novell.com
- Merge the changes that were done in GNOME:Contrib: update
  BuildRequires, Requires, and clean up the spec file.
* Fri Aug 14 2009 vuntz@novell.com
- Various small cleanups in spec file.
- Remove AutoReqProv: it's default now.
- Remove checks for old versions of openSUSE.
* Wed Aug 12 2009 dominique-obs@leuenberger.net
- Define new python macros on openSUSE <= 11.1.
* Sun Aug  9 2009 coolo@novell.com
- use new python macros
* Fri Sep 12 2008 mauro@suse.de
- a minor issue with the directories ownership was fixed in the
  spec
* Mon Sep  8 2008 mauro@suse.de
- initial package for SuSE. computertemp 0.9.6.1 (based on the
  jpr's opensuse version).
