Name:           qemacs
BuildRequires:  libpng-devel
BuildRequires:  libX11-devel
BuildRequires:  libXext-devel
BuildRequires:  libXv-devel
Version:        0.3.3
Release:        6.1
URL:            https://bellard.org/qemacs/
Source0:        https://bellard.org/qemacs/qemacs-%{version}.tar.gz
Patch0:         qemacs-0.3.3.patch
Summary:        Quick Emacs is a very small but powerful editor
License:        LGPL-2.1+
Group:          Productivity/Editors/Other

%description
Full screen editor with an Emacs look and feel with all Emacs common
features: multi-buffer, multi-window, command mode, universal argument,
keyboard macros, config file with C like syntax, minibuffer with
completion and history.

Full UTF8 support, including bidirectional editing respecting the
Unicode bidi algorithm. Arabic and Indic scripts handling (in
progress).

WYSIWYG HTML/XML/CSS2 mode graphical editing. Also supports lynx like
rendering on VT100 terminals.

WYSIWYG DocBook mode based on XML/CSS2 renderer.

C mode: coloring with immediate update. Emacs like auto-indent.

Shell mode: colorized VT100 emulation so that your shell work exactly
as you expect. Compile mode with next/prev error.

Input methods for most languages, including Chinese (input methods come
from the Yudit editor).

Hexadecimal editing mode with insertion and block commands. Unicode
hexa editing of UTF8 files also supported.

X11 support. Support multiple proportional fonts at the same time (as
XEmacs). X Input methods supported. Xft extension supported for anti
aliased font display.

Authors:
--------
    Fabrice Bellard  <fabrice.bellard@free.fr>

%prep
%setup -q
%patch0 -p1

%build
export CFLAGS="$RPM_OPT_FLAGS"
export CXXFLAGS="$RPM_OPT_FLAGS"
./configure \
	--prefix=/usr \
	%{_target_platform}
make STRIP=:

%install
make -e DESTDIR=$RPM_BUILD_ROOT install
chmod 644 $RPM_BUILD_ROOT/%{_mandir}/man1/*

%files
%doc COPYING Changelog README TODO qe-doc.html config.eg tests
%{_bindir}/*
%{_datadir}/%{name}
%{_mandir}/man1/*

%changelog
* Fri Sep 08 2017 Wei-Lun Chao <bluebat@member.fsf.org> - 0.3.3
- Rebuild for Fedora
* Thu Jan  5 2012 pgajdos@suse.com
- build also with libpng15
  * libpng15.patch
* Thu Jun 29 2006 nadvornik@suse.cz
- don't use deprecated libpng functions
* Mon May 29 2006 schwab@suse.de
- Don't strip binaries.
* Wed May 24 2006 schwab@suse.de
- Use RPM_OPT_FLAGS.
- Don't strip binaries.
* Wed Jan 25 2006 mls@suse.de
- converted neededforbuild to BuildRequires
* Tue Nov  8 2005 dmueller@suse.de
- don't build as root
* Thu Sep  8 2005 mfabian@suse.de
- Bugzilla #114849: man pages should not have executable
  permissions.
* Tue Apr 12 2005 mfabian@suse.de
- fix to build with gcc 4.
* Fri May  2 2003 mfabian@suse.de
- new package: qemacs-0.3.1
- add DESTDIR support to Makefile
- add a qemacs man page as a .so link to the qe man page
- avoid crash when ~/.qe/config contains errors, print error to
  stdout instead of to the qemacs screen which doesn't yet exist.
  when reading ~/.qe/config.
- move welcome message after the do_refresh() to make it actually
  visible.
