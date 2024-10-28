Summary: Applet to select the default ALSA sound card
Name: asoundconf-gtk
Version: 1.6
Release: 4.1
License: GPL
Group: Sound
URL: https://code.launchpad.net/asoundconf-ui
Requires: asoundconf
Source0: %name-%version.tar.gz
Patch0: asoundconf-gtk_1.6-0ubuntu1.diff.gz
BuildArch: noarch

%description
Based on asoundconf code, but as a GTK+ front-end.
Useful if you have two cards, and switch between the two.
There is already this functionality in GNOME, but this is
indeed useful if you do not use that desktop environment,
and asoundconf-gtk also supports PulseAudio toggling.

%prep
%setup -q
%patch 0 -p1

%build

%install
install -Dm755 asoundconf-gtk/asoundconf-gtk ${RPM_BUILD_ROOT}%_bindir/asoundconf-gtk
install -Dm644 debian/asoundconf-gtk.8 ${RPM_BUILD_ROOT}%_mandir/man8/asoundconf-gtk.8
install -Dm644 asoundconf-gtk.desktop ${RPM_BUILD_ROOT}%_datadir/applications/asoundconf-gtk.desktop

sed -i 's|/usr/bin/env python|/usr/bin/python2|' %{buildroot}%{_bindir}/asoundconf-gtk

%files 
%_bindir/asoundconf-gtk
%_mandir/man8/asoundconf-gtk.8*
%_datadir/applications/asoundconf-gtk.desktop

%changelog
* Thu Apr 14 2016 Wei-Lun Chao <bluebat@member.fsf.org> - 1.6
- Rebuilt for Fedora
* Tue Oct 25 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.6-alt1.1.1
- Rebuild with Python-2.7
* Mon Dec 07 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.6-alt1.1
- Rebuilt with python 2.6
* Wed Jan 28 2009 Igor Vlasenko <viy@altlinux.ru> 1.6-alt1
- first build
