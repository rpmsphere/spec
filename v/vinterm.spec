Name:               vinterm
Version:            0.5.0
Release:            11.4
Summary:            Vintage Style Terminal Emulator
Source:             https://vinterm.googlecode.com/files/vinterm-%{version}.tar.gz
Source1:            vinterm.desktop
Patch1:             vinterm-add_missing_includes.patch
Patch2:             vinterm-disable_opt.patch
Patch3:             vinterm-verbose_build.patch
Patch4:             vinterm-fix_icon_destdir.patch
URL:                https://code.google.com/p/vinterm/
Group:              System/X11/Utilities
License:            GPL-3.0+
BuildRequires:      libconfig-devel
BuildRequires:      SDL-devel
BuildRequires:      libao-devel
BuildRequires:      ncurses-devel
BuildRequires:      gcc-c++
BuildRequires:      make
BuildRequires:      pkgconfig
BuildRequires:      hicolor-icon-theme

%description
Use a terminal in style, like in the good old days! Vintage Terminal is a
terminal emulator that simulates the looks of a 1980s monitor.

Vintage Terminal has the following features:
* Very basic terminal emulator support;
* Scaling (zoom);
* Has a authentic old look based on a IBM 5151 monitor.

%prep
%setup -q
%patch 1
%patch 2
%patch 3
%patch 4
%__chmod 0644 data/vinterm.desktop
sed -i '6i #include <cstdint>' terminal/pty.h

%build
%__make %{?_smp_mflags} \
    PREFIX="%{_prefix}" \
    MANPREFIX="%{_mandir}" \
    VINTERMPREFIX="%{_datadir}/%{name}" \
    OPTFLAGS="%{optflags}" \
    DEBUG=no \
    CC="%__cxx"

%install
%make_install \
    PREFIX="%{_prefix}" \
    MANPREFIX="%{_mandir}" \
    VINTERMPREFIX="%{_datadir}/%{name}" \
    OPTFLAGS="%{optflags}" \
    DEBUG=no \
    CC="%__cxx"

%files
%doc AUTHORS HACKING LICENSE NEWS README
%{_bindir}/vinterm
%{_datadir}/vinterm
%{_datadir}/applications/vinterm.desktop
%{_datadir}/icons/*/*/apps/vinterm.*
%{_mandir}/man1/vinterm.1*

%changelog
* Mon Oct 14 2013 Wei-Lun Chao <bluebat@member.fsf.org> - 0.5.0
- Rebuilt for Fedora
* Mon Aug 19 2013 pascal.bleser@opensuse.org
- update to 0.5.0:
  * mouse support for applications
  * copy/paste mouse support for terminal (still a little buggy)
  * faster screen update on long text output
  * window title update upon request from applications
  * added application icon to the WM menus
* Thu Aug  1 2013 pascal.bleser@opensuse.org
- update to 0.4.1:
  * added the ability to rollback the terminal
  * added audible beep
  * commands can now be started in the terminal initializtiaon from the
    commandline
  * an alias to vim was changed to make it able to use <C-PgUp> and <C-PgDown>
  * added special charset for curses
* Fri Jul 26 2013 pascal.bleser@opensuse.org
- update to 0.4.0:
  * Unicode/multiple locales environment has been implemented (the font is
    still not Unicode)
  * add window icon
  * cursor improvements
  * when starting vinterm in a tiling window manager, the size of the
    framebuffer is now set correctly
  * various positioning issues that caused problems with editors like ViM and
    nano have been fixed
* Thu Apr 19 2012 pascal.bleser@opensuse.org
- update to 0.3.0:
  * Window resize/maximize implemented
  * Full screen (CTRL+F11)
  * Full screen with 80 columns (CTRL+SHIFT+F11)
  * Manual page written
* Thu Apr 12 2012 pascal.bleser@opensuse.org
- update to 0.2.0:
  * full terminal capabilites implemented
* Tue Apr  3 2012 pascal.bleser@opensuse.org
- update to 0.1.2:
  * changed initialization file to run .bashrc on startup
  * added control keys support (such as HOME, END, PAGE UP...)
  * normal color was made darker, so that bright colors standout more
  * fixed incorrect window title version
  * fixed memory leaks
* Sun Apr  1 2012 pascal.bleser@opensuse.org
- update to 0.1.1:
  * partial VT100 support implemented, enough to run alpine, vim and nethack
    and use commands like clear, more and less
  * character effects implemented: bold, underlined, blink, reversed and dim
  * a file is now run when the terminal is started: ~/.vinterm_profile -- it
    comes preconfigured with some useful settings for a monochrome terminal
* Sun Mar 25 2012 pascal.bleser@opensuse.org
- initial version (0.1.0)
