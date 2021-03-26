Name:           seyon
BuildRequires:  bison freetype-devel libX11-devel
License:        GPL v2 or later
Group:          Hardware/Modem
AutoReqProv:    on
Version:        2.20c
Release:        1023
Summary:        Telecommunications under the X Window System
Source:         %{name}-%{version}.tar.bz2
Source1:        %{name}-kermit-1.0.tar.bz2
Source2:        %{name}_skel.tar.bz2
Patch:          %{name}-%{version}.dif
Patch1:         %{name}-%{version}-strings.patch
Patch2:         %{name}-%{version}-gcc-error.patch

%description
Telecommunications under the X Window System.



Authors:
--------
    Muhammad M. Saggaf <alsaggaf@mit.edu>

%define kermit seyon-kermit-1.0
%define _xorg7libs %_lib
%define _xorg7libs32 lib
%define _xorg7libshare share
%define _xorg7prefix /usr
%define _xorg7mandir %_mandir

%prep
%setup -a 1 -a 2
%patch -p1
%patch1
%patch2

%build
xmkmf
make CCOPTIONS="$RPM_OPT_FLAGS"
cd %{kermit}
make config

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/etc/skel
install -d $RPM_BUILD_ROOT%{_xorg7prefix}/bin
make "DESTDIR=$RPM_BUILD_ROOT" install install.man
install %{kermit}/seyon-kermit $RPM_BUILD_ROOT%{_xorg7prefix}/bin
ln -sf xterm $RPM_BUILD_ROOT%{_xorg7prefix}/bin/seyon-emu
#
mv 1-BUGREPORT BUGREPORT
mv 1-CHANGES CHANGES
mv 1-FAQ FAQ
mv 1-HISTORY HISTORY
mv 1-README README
mv 1-TODO TODO
mv %{kermit}/README README-kermit
# remove unpackaged files
rm -rf $RPM_BUILD_ROOT/etc/skel/.seyon

%clean
rm -rf $RPM_BUILD_ROOT

%post
%run_permissions
%verifyscript
%verify_permissions -e %{_xorg7prefix}/bin/seyon

%files
%defattr(-,root,root,-)
%doc BUGREPORT CHANGES FAQ HISTORY README TODO README-kermit
%doc skel
%verify(not mode) %attr(0755, root, uucp) %{_xorg7prefix}/bin/seyon
%{_xorg7prefix}/bin/seyon-emu
%{_xorg7prefix}/bin/seyon-kermit
%config %attr(644, root, root) %{_prefix}/%{_xorg7libshare}/X11/app-defaults/Seyon
%config %attr(644, root, root) %{_prefix}/%{_xorg7libshare}/X11/app-defaults/Seyon-color
%doc %attr(644, root, root) %{_prefix}/%{_xorg7libs32}/X11/seyon.help
%doc %attr(644, root, root) %{_xorg7mandir}/man1/seyon.1x.gz
%changelog
* Thu Mar 29 2007 - coolo@suse.de
- BuildRequire bison
* Wed Jul 26 2006 - pnemec@suse.cz
- fix specfile to build with X.org 7.x
* Wed Jan 25 2006 - mls@suse.de
- converted neededforbuild to BuildRequires
* Thu Dec 15 2005 - pnemec@suse.cz
- fixed gcc error [#136963]
* Fri Nov 04 2005 - pnemec@suse.cz
- fix permisions
* Wed Nov 02 2005 - dmueller@suse.de
- don't build as root
* Fri Jun 17 2005 - meissner@suse.de
- use RPM_OPT_FLAGS correctly.
* Mon Nov 03 2003 - ltinkl@suse.cz
- package according to permissions.secure and call run_permissions
* Mon Jun 02 2003 - ro@suse.de
- remove unpackaged files from buildroot
* Tue Jan 14 2003 - nadvornik@suse.cz
- fixed multi-line string literals
* Fri Aug 17 2001 - adostal@suse.cz
- fix neededforbuild (freetype2)
- convert gz to bz2 and fix spec (%%{name}, %%{_tmppath})
* Tue Aug 14 2001 - cstein@suse.de
- moved default config files from aaa_skel (/etc/skel/.seyon) into
  the DOC-directory of this package.
* Thu Mar 01 2001 - ro@suse.de
- don't redeclare usleep
* Fri May 26 2000 - bubnikv@suse.cz
- sorted
* Fri Mar 24 2000 - bubnikv@suse.cz
- added buildroot
* Thu Oct 21 1999 - freitag@suse.de
- update to version 2.20c, seyon-kermit stays V. 1.0
* Mon Sep 13 1999 - bs@suse.de
- ran old prepare_spec on spec file to switch to new prepare_spec.
* Thu Dec 10 1998 - bs@suse.de
- mkdir /etc/skel before make install.
* Thu Feb 06 1997 - rj@suse.de
- Version 2.14c
	- lock-directory now /var/lock
	- seyon-kermit now included
	- seyon-kermit has lock-default in /var/lock
