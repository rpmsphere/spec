Summary: Media Center
Name: elisa
Version: 0.5.17
Release: 1
# Elisa is GPLv3 and plugins are MIT.
# See the included COPYING file for the details.
License: GPLv3 and MIT
Group: Applications/Multimedia
URL: http://elisa.fluendo.com/
Source0: http://elisa.fluendo.com/static/download/elisa/elisa-%{version}.tar.gz
# Patch to disable trying to load the Windows only plugins we don't include :
# wmd smbwin32 elisa_updater winremote
Patch0: elisa-0.5.9-nowinplugins.patch
# Mandatory
Requires: python2-setuptools
Requires: python-imaging
Requires: gnome-python2-extras
# elisa/core/utils/misc.py at least requires this
Requires: python2-twisted
# Plugins. The bad are actually mandatory (they contain the GUI for instance)
Requires: elisa-plugins-good = %{version}
Requires: elisa-plugins-bad = %{version}
# For the "official" default font ("MgOpen Cosmetica")
Requires: mgopen-cosmetica-fonts
# For the "build" itself, most of the above aren't required
BuildRequires: python2-devel
BuildRequires: python2-twisted
BuildRequires: python2-setuptools
Buildarch: noarch
# We used to have a "common" package providing the "devel" :
Obsoletes: elisa-common < 0.5.9

%description
Media center solution using the GStreamer multimedia framework.

%package devel
Summary: Development files for the Elisa Media Center
Group: Applications/Multimedia
# Mandatory
Requires: python2-setuptools
Requires: python-imaging
Requires: gnome-python2-extras
# elisa/core/utils/misc.py at least requires this
Requires: python2-twisted
# The whole point of having this devel package is to have some files being
# the same as in the main package, but without the plugins requirements, in
# order to be able to rebuild them. We'd have a circular dependency otherwise.

%description devel
Development files for the Elisa Media Center.

%prep
%setup -q
##%patch0 -p1
echo -e 'Name[zh_TW]=艾麗莎媒體中心\nComment[zh_TW]=可遙控在電視上播放影片與音樂' >> data/%{name}.desktop

%build
python2 setup.py build

%install
%{__rm} -rf %{buildroot}
python2 setup.py install \
    --single-version-externally-managed \
    -O1 --skip-build --root %{buildroot}
# Create empty plugins directory
%{__mkdir_p} %{buildroot}%{python2_sitelib}/elisa/plugins

sed -i 's|/usr/bin/python$|/usr/bin/python2|' %{buildroot}%{_bindir}/*

%clean
%{__rm} -rf %{buildroot}

%files
%doc COPYING FAQ* LICENSE* NEWS RELEASE
%{_bindir}/elisa
# Doesn't work (as of 0.5.2), and not sure what it's used for anyway
%exclude %{_bindir}/elisa-get
%{_datadir}/applications/elisa.desktop
%exclude %{_datadir}/applications/elisa-mobile.desktop
%{_datadir}/dbus-1/services/com.fluendo.elisa.service
%exclude %{_datadir}/icons/elisa.png
%{_datadir}/pixmaps/elisa.png
%{python2_sitelib}/elisa/
%{python2_sitelib}/elisa-*.egg-info/
%{python2_sitelib}/elisa-*-nspkg.pth
%{python2_sitelib}/elisa_generic_setup.py*
%{_mandir}/man1/elisa.1*

%files devel
%doc COPYING FAQ* LICENSE* NEWS RELEASE
# These files are in the main package too, but need to be duplicated here
%{python2_sitelib}/elisa/
%{python2_sitelib}/elisa-*.egg-info/
%{python2_sitelib}/elisa-*-nspkg.pth
%{python2_sitelib}/elisa_generic_setup.py*

%changelog
* Mon Feb 26 2018 Wei-Lun Chao <bluebat@member.fsf.org> - 0.5.17
- Rebuilt for Fedora
* Tue Sep 30 2008 Matthias Saou <http://freshrpms.net/> 0.5.12-1
- Update to 0.5.12.
* Tue Sep 23 2008 Matthias Saou <http://freshrpms.net/> 0.5.11-1
- Update to 0.5.11.
* Tue Sep 16 2008 Matthias Saou <http://freshrpms.net/> 0.5.10-1
- Update to 0.5.10.
* Tue Sep  9 2008 Matthias Saou <http://freshrpms.net/> 0.5.9-1
- Update to 0.5.9.
* Mon Sep  2 2008 Matthias Saou <http://freshrpms.net/> 0.5.8-3
- Update to 0.5.8.
- Replace the "common" package approach with a split out "devel" one which
  contains some duplicated files from the main package.
* Tue Aug 26 2008 Matthias Saou <http://freshrpms.net/> 0.5.7-1
- Update to 0.5.7.
* Tue Aug 19 2008 Matthias Saou <http://freshrpms.net/> 0.5.6-1
- Update to 0.5.6.
- Require the exact same elisa plugins version, as elisa and all plugins are
  always released all at once and should always match.
* Mon Aug 11 2008 Matthias Saou <http://freshrpms.net/> 0.5.5-1
- Update to 0.5.5.
* Fri Aug  8 2008 Matthias Saou <http://freshrpms.net/> 0.5.4-1
- Update to 0.5.4.
* Tue Jul 29 2008 Matthias Saou <http://freshrpms.net/> 0.5.3-1
- Update to 0.5.3.
* Wed Jul 23 2008 Matthias Saou <http://freshrpms.net/> 0.5.2-4
- Update to 0.5.2.
- Split a "common" sub-package required by the main "elisa" package and
  providing a "devel" sub-package.
- Add plugins requirements, made possible thanks to the above hack.
- Update requirements, moving many to the proper plugins sub-packages.
* Tue Jul 15 2008 Matthias Saou <http://freshrpms.net/> 0.5.1-6
- Update to the fixed 0.5.1 tarball.
- Remove Windows specific plugins from the default configuration.
* Mon Jul 14 2008 Matthias Saou <http://freshrpms.net/> 0.5.1-4
- Use the right 0.5 branch, it's the "upicek" one, not "0.5", go figure...
* Sat Jul 12 2008 Matthias Saou <http://freshrpms.net/> 0.5.1-3
- Use a bzr branch as sources, as the 0.5.1 tarball is completely broken.
- Don't exclude the docs.
* Fri Jul 11 2008 Matthias Saou <http://freshrpms.net/> 0.5.1-1
- Update to 0.5.1.
- Include as sources the no longer provided elisa.desktop and elisa.png.
- Remove no longer needed desktop file patch.
* Wed Mar 12 2008 Matthias Saou <http://freshrpms.net/> 0.3.5-1
- Update to 0.3.5.
- Add new included files.
- Include empty plugins directory.
* Tue Mar  4 2008 Matthias Saou <http://freshrpms.net/> 0.3.4-1
- Update to 0.3.4.
- Add new elisa-plugins-* requirements.
* Sun Feb 24 2008 Matthias Saou <http://freshrpms.net/> 0.3.3-2
- Require pigment-python instead of pigment now that it has been split out.
* Thu Jan 17 2008 Matthias Saou <http://freshrpms.net/> 0.3.3-1
- Update to 0.3.3.
- Add python-BeautifulSoup requirement (#416921).
- Do not include i386 only binary libgstflvdemux.so plugin, for YouTube plugin.
* Tue Oct  9 2007 Matthias Saou <http://freshrpms.net/> 0.3.2-1
- Update to 0.3.2.
- Add new external_plugins python directory.
* Tue Sep  4 2007 Matthias Saou <http://freshrpms.net/> 0.3.1-3
- Add requirement of mgopen-fonts (see upstream trac #571).
* Tue Aug 28 2007 Matthias Saou <http://freshrpms.net/> 0.3.1-2
- Update python2-setuptools build requirement to new python-setuptools-devel.
* Sat Aug  4 2007 Matthias Saou <http://freshrpms.net/> 0.3.1-1
- Update to 0.3.1.
- Update License field.
- Update requirement to pigment >= 0.3.1.
- Remove no longer needed desktopentry and nobangpy patches.
- Update desktop patch.
* Wed May 16 2007 Matthias Saou <http://freshrpms.net/> 0.1.6-4
- Patch desktop file to remove useless bits (Version and extra Categories).
* Tue May  8 2007 Matthias Saou <http://freshrpms.net/> 0.1.6-3
- Change Coherence requirement to python-Coherence to match package name change.
* Mon May  7 2007 Matthias Saou <http://freshrpms.net/> 0.1.6-2
- Change coherence requirement to Coherence to match package name change.
* Fri May  4 2007 Matthias Saou <http://freshrpms.net/> 0.1.6-1
- Update to 0.1.6.
* Mon Apr 16 2007 Matthias Saou <http://freshrpms.net/> 0.1.5-1
- Update to 0.1.5.
- Disable gst requirements which aren't part of Fedora (oops!).
- Patch out the hash-bang python from scripts not meant to be executed.
- Rip out the root user test condition to installing the desktop entry.
* Fri Mar 23 2007 Matthias Saou <http://freshrpms.net/> 0.1.4.2-1
- Update to 0.1.4.2.
* Wed Feb 21 2007 Matthias Saou <http://freshrpms.net/> 0.1.4.1-1
- Update to 0.1.4.1.
* Thu Feb  8 2007 Matthias Saou <http://freshrpms.net/> 0.1.3-1
- Initial RPM release.
