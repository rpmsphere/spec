%global debug_package %{nil}

Summary:	AfterStep Window Manager (NeXTalike)
Name:		AfterStep
Version:	2.2.9
Release:	1
License:	GPL
Group:		User Interface/Desktops
URL:		http://www.afterstep.org
Vendor:		The AfterStep Team (see TEAM in docdir)
Source0:	ftp://ftp.afterstep.org/stable/%{name}-%{version}.tar.gz
Source1:	Xclients.afterstep.switchdesk
Source2:	afterstep.gdm
Source3: 	AfterStep.kdm
Source4: 	AfterStep.menu
Source5: 	AfterStep.menumethod
Source6: 	afterstep.desktop.xsessions
Source7: 	afterstep.desktop.wm-properties
Source8:	afterstep.fedora.README
Requires:	%{name}-libs 
Obsoletes:	libAfterImage

%description
  AfterStep is a Window Manager for X which started by emulating the
  NEXTSTEP look and feel, but which has been significantly altered
  according to the requests of various users. Many adepts will tell you
  that NEXTSTEP is not only the most visually pleasant interface, but
  also one of the most functional and intuitive out there. AfterStep
  aims to incorporate the advantages of the NEXTSTEP interface, and add
  additional useful features.

  The developers of AfterStep have also worked very hard to ensure
  stability and a small program footprint. Without giving up too many
  features, AfterStep still works nicely in environments where memory is
  at a premium.

%package libs
summary:	libraries required by afterstep 2.0
version:	%{version}
release:	%{release}
License:	GPL
group:		User Interface/Desktops
Provides: 	%{name}-libs

%description libs
  Libraries neeeded by AfterStep 2.0

%package devel
summary:	AfterStep libs include files
version:	%{version}
release:	%{release}
License:	GPL
group:		User Interface/Desktops
Requires: 	%{name}-libs 

%description devel
  AfterStep libs include files

%prep
%setup -q
sed -i 's|png_ptr->jmpbuf|png_jmpbuf (png_ptr)|' libAfterImage/export.c libAfterImage/import.c
sed -i 's|png_ptr->io_ptr|png_get_io_ptr (png_ptr)|' libAfterImage/import.c

%build
for i in libAfterBase libAfterImage autoconf ; do
cp -f /usr/share/automake-*/config.guess $i/
done
export CC="gcc -Wl,--allow-multiple-definition"
export LDFLAGS=-Wl,--allow-multiple-definition
CFLAGS=$RPM_OPT_FLAGS \
./configure \
	--prefix=/usr	                          \
	--mandir=%{_mandir}                       \
	--enable-sharedlibs                       \
	--disable-staticlibs			  \
	--enable-ascp                             \
	--enable-i18n                             \
	--with-helpcommand="aterm -e man"         \
	--with-desktops=1 --with-deskgeometry=2x3 \
	--with-imageloader="qiv --root"
	
make

if [[ -x /usr/bin/sgml2html ]]; then sgml2html doc/afterstep.sgml; fi
#cd src/ASDocGen && ./ASDocGen -l log.html -t html && cd ../..

%install
mkdir -p $RPM_BUILD_ROOT%{_datadir}/gnome/wm-properties $RPM_BUILD_ROOT%{_libdir}

make DESTDIR=$RPM_BUILD_ROOT LDCONFIG=/bin/true install
rm -f $RPM_BUILD_ROOT%{_bindir}/{sessreg,xpmroot}
for f in libASGTK libAfter{Base,Conf,Image,Step}; do
   rm %{buildroot}/usr/lib/$f.so*
   cp -a $f/$f.so* %{buildroot}%{_libdir}
done

mkdir -p %{buildroot}%{_datadir}/xsessions
install -m 0644 %{SOURCE6} %{buildroot}%{_datadir}/xsessions/%{name}.desktop

%clean
rm -rf %{buildroot}

%files
%doc ChangeLog NEW README* TEAM UPGRADE doc/languages doc/licences doc/code TODO doc/*.html
#doc src/ASDocGen/html/*html
%{_bindir}/*
%dir %{_datadir}/afterstep
%{_datadir}/afterstep/*
#{_mandir}/man1/*
%{_datadir}/xsessions/AfterStep.desktop
%{_datadir}/gnome/wm-properties/AfterStep.desktop

%files libs
%doc libAfterImage/README 
%{_libdir}/lib*.so*

%files devel
%dir %{_includedir}/libAfterBase
%dir %{_includedir}/libAfterConf
%dir %{_includedir}/libAfterImage
%dir %{_includedir}/libAfterStep
%dir %{_includedir}/libASGTK
%{_includedir}/libAfterBase/*
%{_includedir}/libAfterConf/*
%{_includedir}/libAfterImage/*
%{_includedir}/libAfterStep/*
%{_includedir}/libASGTK/*
#{_mandir}/man3/*
#doc src/ASDocGen/html/API/*html

%pre
for i in /usr /usr/local /usr/X11R6 ; do
	if [ -d $i/share/afterstep_old ]; then
		rm -r $i/share/afterstep_old;
	fi
	# %config /usr/share/afterstep should take care of this.
	#if [ -d $i/share/afterstep ]; then
	#	cp -pr $i/share/afterstep $i/share/afterstep_old;
	#	exit;
	#fi
done

%post

if [ -x /usr/sbin/fndSession ]; then /usr/sbin/fndSession || true ; fi

%postun

if [ -x /usr/sbin/fndSession ]; then /usr/sbin/fndSession || true ; fi

%changelog
* Fri Oct 04 2019 Wei-Lun Chao <bluebat@member.fsf.org> - 2.2.9
- Rebuild for Fedora

* Thu Dec 11 2008 Feather Mountain <john@ossii.com.tw> - 2.2.8-1.ossii
- new version.
- Rebuild for M6(OSSII)

* Wed Oct 18 2006 J. Krebs <rpm_speedy@yahoo.com> - 20:2.2.3-2
- added Smooth look, support for xinerama, removed -gdb configure flag.
- added Menu patches for various bug-fixes.

* Tue Oct 11 2006 J. Krebs <rpm_speedy@yahoo.com> - 20:2.2.3-1
- new version.

* Wed May 25 2006 J. Krebs <rpm_speedy@yahoo.com> - 20:2.2.2-1
- new version.

* Tue Mar 21 2006 J. Krebs <rpm_speedy@yahoo.com> - 20:2.2.1-3
- changed prefix path to /usr.

* Thu Mar  9 2006 Sean Dague <sean@dague.net> - 20:2.2.1-1
- bring up to 2.2.1 release
- make find session call on Mandrake, so it actually shows up in kdm

* Mon Jan 09 2006 J. Krebs <rpm_speedy@yahoo.com> 20:2.2.0-1
- brought up to 2.1.2 release.
- updated distro defines.

* Mon Aug 08 2005 J. Krebs <rpm_speedy@yahoo.com> 20:2.1.2-2
- updated configuration defines.

* Sat Jul 23 2005 J. Krebs <rpm_speedy@yahoo.com> 20:2.1.2-1
- brought up to 2.1.2 release.

* Tue Jun 14 2005 J. Krebs <rpm_speedy@yahoo.com> 20:2.1.1-6
- removed xloadimage with qiv. FC4 no longer provides xloadimage.
- qiv is an optional package and not a require for install.

* Sun Jun 12 2005 J. Krebs <rpm_speedy@yahoo.com> 20:2.1.1-5
- added epoch info back in and tweaked requires.

* Fri Jun 10 2005 J. Krebs <rpm_speedy@yahoo.com> 20:2.1.1-4
- AfterStep now works correctly under Fedora gdm & switchdesk.

* Fri Jun 10 2005 J. Krebs <rpm_speedy@yahoo.com> 20:2.1.1-3
- replaced "copyright" with "license" .spec file.

* Thu Jun 09 2005 J. Krebs <rpm_speedy@yahoo.com> 20:2.1.1-2
- eliminated epoch and fver from .spec file.

* Mon Jun 06 2005 J. Krebs <rpm_speedy@yahoo.com> 20:2.1.1-1
- brought up to 2.1.1 release.

* Tue May 17 2005 J. Krebs <rpm_speedy@yahoo.com> 20:2.1.0-1
- brought up to 2.1.0 release.

* Wed May 04 2005 J. Krebs <rpm_speedy@yahoo.com> 20:2.00.05-1
- brought up to 2.00.05 release.

* Mon Mar 28 2005 J. Krebs <rpm_speedy@yahoo.com> 20:2.00.04-2
- Activated postcard-to-developer.

* Tue Mar 22 2005 J. Krebs <rpm_speedy@yahoo.com> 20:2.00.04-1
- brought up to 2.00.04 release

* Mon Mar  7 2005 Sean Dague <sean@dague.net> 20:2.00.03-3
- set provides manually on libs, move some docs to main and devel

* Sun Mar  6 2005 Sean Dague <sean@dague.net> 20:2.00.03-2
- add with tagging to fedora vs. mandrake issues

* Thu Mar 03 2005 J.Krebs <rpm_speedy@yahoo.com> 20:2.00.03-1
- brought up to 2.00.03 release
- separated Fedora desktop config files into a separate rpm

* Sat Feb 26 2005 Sean Dague <sean@dague.net> 20:2.00.02-2
- brought up to 2.00.02 release

* Wed Sep 28 2004 Graydon Saunders <graydon@epiphyte.net> 2.00.00
- added %%{prefix}
- added the man pages to the -libs package

* Sun Dec 14 2003 Andre Costa <acosta@ar.microlink.com.br>
- split into three different RPMs
- AfterStep-libs is now required for AfterStep
- use qiv instead of xv for root image
- removed check for buildroot location on %%clean
- removed references to RH startmenu

* Mon Dec 6 1999 David Mihm <webmaster@afterstep.org>
  [AfterStep-1.7.149-1]
- Updated to current version

* Wed Jun 9 1999 David Mihm <webmaster@afterstep.org>
  [AfterStep-1.7.111-1]
- Now this spec file is included in the distribution.
- Upgrade to latest snaphost 1.7.111
- Many thanks to Ryan Weaver for this spec file to include!!

* Tue Jun  8 1999 Ryan Weaver <ryanw@infohwy.com>
  [AfterStep-1.7.108-2]
- Made changes to spec to configure and install more like RedHat
  installations.
- Added %config to the /usr/share/afterstep listing to allow rpm to
  backup this dir if needed.

* Tue Jun  8 1999 Ryan Weaver <ryanw@infohwy.com>
  [AfterStep-1.7.108-1]
- Added patches 16-18 to make version 1.7.108

* Fri May 28 1999 Ryan Weaver <ryanw@infohwy.com>
  [AfterStep-1.7.105-1]
- Upgraded to 1.7.90 and added patches 1-15 to make it version 1.7.105.
- Made RPM relocatable.
- Building dynamic libs instead of static.

* Mon Feb  8 1999 Ryan Weaver <ryanw@infohwy.com>
  [AfterStep-1.6.10-1]
- Upgraded to 1.6.10

* Mon Jan  4 1999 Ryan Weaver <ryanw@infohwy.com>
  [AfterStep-1.6.6-3]
- Added a pre-install script to check to see if a previous versions
  share directory exists... If one does, it will copy it to afterstep_old.

* Thu Dec 31 1998 Ryan Weaver <ryanw@infohwy.com>
  [AfterStep-1.6.6-2]
- Configuring with no special settings and installing into
  default dirs as per David Mihm <davemann@ionet.net>
