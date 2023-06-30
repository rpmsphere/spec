%undefine _debugsource_packages

Name: morse
Summary: Classic morse trainer program
Version: 2.5
Release: 8.4
License: BSD
Group: Communications
URL: https://catb.org/~esr/morse/
Source0: %name-%version.tar.gz
Patch: morse2.5-nosound.patch
BuildRequires: libX11-devel alsa-lib-devel pulseaudio-libs-devel xmlto
#BuildRequires: xsltproc docbook-dtds docbook-style-xsl

%description
Morse Classic is a Morse-code training program for aspiring radio hams. It
can generate random tests or simulated QSOs resembling those used in
the ARRL test (a QSO generator is included). There are a plethora of
options to vary the training method. In one of the simpler modes,
this program will take text from standard input and render it as
Morse-code beeps.

%prep
%setup -q
#sed -i '/\$(X11LIBS)/s/\(\$(X11LIBS) \)\(.*\)/\2 \1/g' morse.d/Makefile
%patch -p1

%build
rm -f morse.1
make DEVICE=ALSA QSO morse.1
rm -f morse.d/morse
make -C morse.d DEVICE=ALSA morse

%install
mkdir -p %buildroot%_bindir %buildroot%_mandir/man1
install -m 755 morse.d/%name[^.]* %buildroot%_bindir/
install -m 755 QSO %buildroot%_bindir/
install -m 644 %name.1 %buildroot%_mandir/man1

%files
%doc README HISTORY
%_mandir/man1/%name.1*
%_bindir/%{name}*
%_bindir/QSO

%changelog
* Mon Oct 14 2013 Wei-Lun Chao <bluebat@member.fsf.org> - 2.5
- Rebuilt for Fedora
* Sun Dec 16 2012 Fr. Br. George <george@altlinux.ru> 2.5-alt1
- Autobuild version bump to 2.5
* Tue Jun 28 2011 Fr. Br. George <george@altlinux.ru> 2.4-alt1
- Autobuild version bump to 2.4
- Various backends provided
* Thu Dec 06 2007 Fr. Br. George <george@altlinux.ru> 2.1-alt1
- Initial build for ALT
- Getopt bug fixed (X instead of X:)
- Nosound patch applied (for text conversion)
* Tue Jan 25 2005 Eric S. Raymond <esr@snark.thyrsus.com> - 2.1-1
- Patched to use termios(3) rather than ioctls() and sigaction rather
  than sigset(3).  This should allow it to run under Mac OS X.
* Mon Jan 24 2005 Eric S. Raymond <esr@snark.thyrsus.com> - 2.0-1
- Initial build.  See HISTORY file in the distribution for prior history
