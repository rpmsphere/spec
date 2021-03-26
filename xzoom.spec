%global debug_package %{nil}

Name: xzoom
Version: 0.3
Release: 8.1
License: distributable
Group: System/X11
Summary: X zoomer
Source: ftp://metalab.unc.edu/pub/Linux/libs/X/%name-%version.tgz
Patch0: %name-%version.debian.diff
Patch1: %name-%version.shm.diff
URL: ftp://metalab.unc.edu/pub/Linux/libs/X/
BuildRequires: imake libXext-devel

%description
Xzoom displays in its window a magnified area of the X11 display.
The user can interactively change the zoomed area, the window size,
magnification (optionally different magnification for X and Y axes)
or rotate or mirror the image.

Authors:
--------
    Itai Nahshon <nahshon@best.com>

%prep
%setup -q
%patch0 -p 1
%patch1

%build
xmkmf
make

%install
install -Dm 755 xzoom $RPM_BUILD_ROOT%_bindir/xzoom
install -Dm 644 xzoom.man $RPM_BUILD_ROOT%_mandir/man1/xzoom.1

%files
%_bindir/*
%_mandir/man1/*
%doc README xzoom.lsm

%changelog
* Wed Nov 13 2013 Wei-Lun Chao <bluebat@member.fsf.org> - 0.3
- Rebuild for Fedora
* Tue Apr 12 2011 Fr. Br. George <george@altlinux.ru> 0.3-alt3
- BuildRequires recalculated
* Tue Dec 09 2008 Fr. Br. George <george@altlinux.ru> 0.3-alt2
- libXext-devel added
* Mon Aug 27 2007 Fr. Br. George <george@altlinux.ru> 0.3-alt1
- Initial build for ALT
* Mon Nov 11 2002 - ro@suse.de
- changed neededforbuild <xf86 xdevel> to <x-devel-packages>
* Mon Dec 03 2001 - egmont@suselinux.hu
- Initial release
