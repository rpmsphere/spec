Summary: Command-line Python utility to select the default ALSA sound card
Name: asoundconf
Version: 0.1
Release: 4.1
License: GPL
Group: Sound
URL: https://code.launchpad.net/~motu/asoundconf-ui
# rev 8 of http://bazaar.launchpad.net/~crimsun/asoundconf-ui/asoundconf-trunk
Requires: alsa-utils
Source0: %name-%version.tar
BuildArch: noarch

%description
Command-line Python utility to configure a user's alsa-lib asoundrc.
Useful if you have two cards, and switch between the two.
There is already this functionality in GNOME, but this is
indeed useful if you do not use that desktop environment,
and asoundconf also supports PulseAudio toggling.

%prep
%setup -q

%build

%install
install -Dm755 asoundconf ${RPM_BUILD_ROOT}%_bindir/asoundconf
install -Dm644 asoundconf.1 ${RPM_BUILD_ROOT}%_mandir/man1/asoundconf.1

sed -i 's|/usr/bin/python|/usr/bin/python2|' %{buildroot}%{_bindir}/asoundconf

%files 
%_bindir/asoundconf
%_mandir/man1/asoundconf.1*

%changelog
* Thu Apr 14 2016 Wei-Lun Chao <bluebat@member.fsf.org> - 0.1
- Rebuild for Fedora
* Tue Apr 01 2014 Igor Vlasenko <viy@altlinux.ru> 0.1-alt1
- synced changes from aur.archlinux.org/packages/asoundconf (1.0.1-3)
  (see also http://wiki.marklesh.com/How-to/Asoundconf)
- (closes: #29795)
* Tue Oct 25 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.0.bzr8-alt1.1.1
- Rebuild with Python-2.7
* Tue Dec 01 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.0.bzr8-alt1.1
- Rebuilt with python 2.6
* Wed Jan 28 2009 Igor Vlasenko <viy@altlinux.ru> 0.0.bzr8-alt1
- initial build
