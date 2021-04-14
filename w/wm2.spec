%undefine _debugsource_packages

Name:         wm2
License:      X11/MIT
Group:        User Interface/X
URL:          http://www.all-day-breakfast.com/wm2/
Version:      4
Release:      978.1
Summary:      A minimalist window manager
Source:       wm2-4.tar.gz
Patch:        wm2-4.dif
BuildRequires: gcc-c++, libX11-devel, libXext-devel, libXmu-devel

%description
wm2 is a window manager for X.  It provides an unusual style of window
decoration and as little functionality as I feel comfortable with in a
window manager.  wm2 is not configurable, except by editing the source
and recompiling the code, and is really intended for people who don't
particularly want their window manager to be too friendly.

wm2 provides:
-- Decorative frames for your windows.
-- The ability to move, resize, hide and restore windows.
-- No icons.
-- No configurable root menus, buttons or mouse or keyboard bindings.
-- No virtual desktop, toolbars or integrated applications.

%prep
%setup
%patch
sed -i 's|(int)x|atoi(x)|' Client.C

%build
make

%install
rm -rf $RPM_BUILD_ROOT
install -Dm755 wm2 $RPM_BUILD_ROOT%{_bindir}/%{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%doc README
%{_bindir}/wm2

%changelog
* Sun Nov 25 2012 Wei-Lun Chao <bluebat@member.fsf.org> - 4
- Rebuilt for Fedora
* Fri Apr 30 2004 - nadvornik@suse.cz
- fixed dangerous compiler warnings
* Sun Jan 11 2004 - adrian@suse.de
- build as user
* Wed Sep 18 2002 - ro@suse.de
- removed bogus self-provides
* Wed Apr 24 2002 - nadvornik@suse.cz
- used macro %%{_lib}
* Mon Dec 10 2001 - schwab@suse.de
- Link with g++.
* Wed Oct 11 2000 - nadvornik@suse.cz
- added I18N patch
* Mon Aug 14 2000 - nadvornik@suse.cz
- sorted
- added buildroot
* Tue Jun 27 2000 - schwab@suse.de
- Fix compilation problems.
- Add ed to neededforbuild.
* Mon Jun 05 2000 - ro@suse.de
- specfile cleanup
* Mon Sep 20 1999 - ro@suse.de
- added provides windowmanager
* Mon Sep 13 1999 - bs@suse.de
- ran old prepare_spec on spec file to switch to new prepare_spec.
* Mon Jul 07 1997 - maddin@suse.de
- first S.u.S.E. version wm2-4
- adepted paths to S.u.S.E. Linux
- copied README to /usr/doc/packages/wm2
