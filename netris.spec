Name: netris
Version: 0.52
Release: 11.1
Summary: A free network version of Tetris
License: GPLv2
Group: Games/Other
URL: ftp://ftp.netris.org/pub/netris/
Source0: ftp://ftp.netris.org/pub/netris/%name-%version.tar.gz
Source2: %name.6
Patch0: %name-0.52-alt-warnings-Wall_fix.patch
Patch1: %name-0.52-alt-configure-tests_fix.patch
Patch2: netris-openbsd-src-snprintf.patch
BuildRequires: ncurses-devel

%description
A free version of Tetris. This game uses ncurses library and can work
in console or pseudo-terminal. You can play against computer or on the
network against your friends.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2

%build
#./Configure -O2 --cextra "%optflags -Werror"
./Configure
make

%install
install -pD -m 755 %name %buildroot%_bindir/%name
install -pD -m 755 sr %buildroot%_bindir/sample-robot
install -pD -m 644 %SOURCE2 %buildroot%_mandir/man6/%name.6

%files
%doc README FAQ robot_desc
%_bindir/%name
%_bindir/sample-robot
%_mandir/man6/%name.6.*

%changelog
* Wed Jun 03 2015 Wei-Lun Chao <bluebat@member.fsf.org> - 0.52
- Rebuild for Fedora
* Fri Apr 19 2013 Dmitry V. Levin (QA) <qa_ldv@altlinux.org> 0.52-alt5.2.qa1
- NMU: rebuilt for updated dependencies.
* Sat Apr 23 2011 Igor Vlasenko <viy@altlinux.ru> 0.52-alt5.2
- NMU: desktop file cleanup (thanks to php-coder@)
* Wed Apr 06 2011 Igor Vlasenko <viy@altlinux.ru> 0.52-alt5.1
- NMU: converted debian menu to freedesktop
* Fri Dec 05 2008 Slava Semushin <php-coder@altlinux.ru> 0.52-alt5
- Removed obsolete %%update_menus/%%clean_menus calls (noted by repocop)
* Sun May 18 2008 Slava Semushin <php-coder@altlinux.ru> 0.52-alt4
- Added manual page (from OpenBSD/FreeBSD)
- Install sample-robot program (like OpenBSD/FreeBSD does)
- Added patch to use snprintf() instead of sprintf() (from OpenBSD)
- Spec cleanup
* Sat Sep 09 2006 Slava Semushin <php-coder@altlinux.ru> 0.52-alt3
- Fixed build with gcc4 and -Werror
- Separate warnings-fix patch to configure-tests_fix and
  warnings-Wall_fix patches
- Enable _unpackaged_files_terminate_build
- Give compiler flags via Configure options
- Formatted %%description
- Changed my name in Packager tag
* Wed Jan 18 2006 php-coder <php-coder@altlinux.ru> 0.52-alt2
- Removed useless Summary and %%description in koi8-r and utf8 charsets
- Use %%def_enable instead of %%add_optflags for enable -Werror flag
- Dont use --silent and --no-print-directory options for make
* Mon Jan 02 2006 php-coder <php-coder@altlinux.ru> 0.52-alt1
- Initial build for ALT Linux Sisyphus
- Using -Werror flag for compiler by default
