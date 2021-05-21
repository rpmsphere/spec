Summary:	A program to use the special keys on internet/multimedia keyboards
Name:		hotkeys
Version:	0.5.7.1
Release:	32.1
License:	GPL
Group:		System/Kernel and hardware
URL:		http://ypwong.org/hotkeys/
Source0:	http://alioth.debian.org/projects/%{name}/%{name}_%{version}.tar.bz2
Source2:	hotkeys-defs.zip
Source1:	%{name}.init
Patch1:		hotkeys-0.5.7.1_mutefix.patch
Patch2:		hotkeys-0.5.7.1-db4.patch
Patch3:		hotkeys-0.5.7.1-gcc43.diff
Patch4:		hotkeys-0.5.7.1-includedir.patch
BuildRequires:  libpng-devel
BuildRequires:  libdb-devel
BuildRequires:	libxml2-devel
BuildRequires:	xosd-devel
BuildRequires:	gtk2-devel
BuildRequires:	gettext-devel
BuildRequires:	libxkbfile-devel
BuildRequires:	libXmu-devel
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
Patch5: %{name}_%{version}.1-shadow.patch
Patch0: %{name}_%{version}.1-gohome.patch

%description
The HotKeys daemon listens for the "special" hotkeys that you won't
normally use on your Internet/Multimedia keyboards. The buttons perform
their intended behaviors, such as volume up and down, mute the speaker,
or launch applications. It has On-screen display (OSD) to show the
volume, program that's being started, etc. It features an XML-based
keycode configuration file format, which makes it possible to define the
hotkeys to launch any programs you want.

%prep
%setup -q
%patch0 -p1 -b .gohome
%patch1 -p0
%patch2 -p1
%patch3 -p0
%patch4 -p0
%patch5 -p1 -b .shadow

%build
autoreconf -fi
%if %{fedora} < 18
%configure --with-xosd --with-gtk
%else
%configure --with-xosd --with-gtk --with-db4-inc=%{_includedir}/libdb4 --with-db4-lib=%{_libdir}/libdb4
%endif
%__make
# CC="gcc -I%{_includedir}/libxml2 -I%{_includedir}/libxml2/libxml"
cat > README.mdk <<EOF
Adding a new keyboard
----------------------
If you have a keyboard not supported by this package, you can create 
your own file, by using xev, and writing the xml config files based 
on the examples provided.

Then, you can send them to the author, Anthony Wong <ypwong@ypwong.org>, 
in order to have them included in the tarball. I will also take 
contribution, send them to <misc@mandriva.org>, or fill a bugreport
on qa.mandriva.com ( i prefer bug report as i may forget mail ).

Keyboard for owner of Samsung X10
----------------------------------
For people owning a Samsung X10, the provided keymap requires 2 commands
to activate all keys. Place a script in /etc/X11/xinit.d/ that contains :

#!/bin/bash
setkeycodes 0x74 122
setkeycodes 0x75 123

and use the samsungX10.def file.
See http://www.samsungpc.com/products/x10_x10plus/x10.htm if your are not sure this is
yours.
EOF

echo "WebBrowser=www-browser">> src/%{name}.conf
echo "Shell=xvt">> src/%{name}.conf

%install
rm -rf $RPM_BUILD_ROOT

%makeinstall
install -d $RPM_BUILD_ROOT/%{_sysconfdir}/X11/xinit/xinitrc.d
install -m 644 src/%{name}.conf $RPM_BUILD_ROOT/%{_sysconfdir}
install -m 755 %{SOURCE1} $RPM_BUILD_ROOT%{_sysconfdir}/X11/xinit/xinitrc.d/%{name}.sh

unzip %{SOURCE2} -d $RPM_BUILD_ROOT/%{_datadir}/%{name}
chmod 644 AUTHORS BUGS COPYING INSTALL TODO def/sample.xml

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-, root, root)
%doc AUTHORS BUGS COPYING INSTALL TODO def/sample.xml README.mdk
%{_bindir}/%{name}
%{_datadir}/%{name}
%{_mandir}/man1/%{name}.1*
%config(noreplace) %{_sysconfdir}/%{name}.conf
%{_sysconfdir}/X11/xinit/xinitrc.d/%{name}.sh

%changelog
* Thu Nov 17 2011 Wei-Lun Chao <bluebat@member.fsf.org> - 0.5.7.1
- Rebuilt for Fedora

* Tue Apr 12 2011 Funda Wang <fwang@mandriva.org> 0.5.7.1-19mdv2011.0
+ Revision: 652846
- build with db 5.1

* Sun Dec 05 2010 Oden Eriksson <oeriksson@mandriva.com> 0.5.7.1-18mdv2011.0
+ Revision: 611100
- rebuild

* Fri Jan 29 2010 Funda Wang <fwang@mandriva.org> 0.5.7.1-17mdv2010.1
+ Revision: 497890
- fix build

  + Buchan Milne <bgmilne@mandriva.org>
    - Rebuild for db-4.8

* Fri Sep 11 2009 Thierry Vignaud <tv@mandriva.org> 0.5.7.1-16mdv2010.0
+ Revision: 437893
- rebuild

* Fri Mar 06 2009 Antoine Ginies <aginies@mandriva.com> 0.5.7.1-15mdv2009.1
+ Revision: 350289
- 2009.1 rebuild

* Thu Jul 31 2008 Oden Eriksson <oeriksson@mandriva.com> 0.5.7.1-14mdv2009.0
+ Revision: 257562
- fix build

  + Thierry Vignaud <tv@mandriva.org>
    - rebuild

* Fri Dec 21 2007 Olivier Blin <oblin@mandriva.com> 0.5.7.1-11mdv2008.1
+ Revision: 136485
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %$RPM_BUILD_ROOT on Pixel's request

  + Michael Scherer <misc@mandriva.org>
    - fix email and url, noted by titi


* Sun Dec 31 2006 Crispin Boylan <crisb@mandriva.org> 0.5.7.1-11mdv2007.0
+ Revision: 102912
- Add missing X11 requires
- Add buildRequires for patch2
- Patch2: db4 support
- Import hotkeys

* Fri Jul 14 2006 Olivier Blin <blino@mandriva.com> 0.5.7.1-10mdv2007.0
- allow to automatically load hotkeys at X11 startup
  (can be configured in /etc/sysconfig/hotkeys)
- mkrel
- new URL

* Thu Jun 30 2005 Michael Scherer <misc@mandriva.org> 0.5.7.1-9mdk
- applied patch from Michael Collard, ( crash when muting if
  something else is on the screen via libxosd )

* Sat Mar 12 2005 Michael Scherer <misc@mandrake.org> 0.5.7.1-8mdk 
- added samsungX10, update the instructions ( thanks to yann malet )
- use generic default

* Thu Jan 13 2005 Michael Scherer <misc@mandrake.org> 0.5.7.1-7mdk
- corrected Dell keyboard, ( Yvon TANGUY ), and extract the good sources.

* Tue Jan 04 2005 Michael Scherer <misc@mandrake.org> 0.5.7.1-6mdk
- added Dell Inspiron 8600, thanks to Yvon TANGUY

* Fri Oct 29 2004 Guillaume Rousse <guillomovitch@mandrake.org> 0.5.7.1-5mdk 
- precision and samsungx30 definition files

* Tue Oct 05 2004 Michael Scherer <misc@mandrake.org> 0.5.7.1-4mdk 
- added Fujistu-Siemens Amilo Pro, thanks to Libor Tomsik

* Sat Jul 24 2004 Michael Scherer <misc@mandrake.org> 0.5.7.1-3mdk 
- add vaio.def, for my laptop ( orignal by Alexander Jorda ) 
- add README.mdk
- fix BuildRequires

* Thu Apr 08 2004 Michael Scherer <misc@mandrake.org> 0.5.7.1-2mdk 
- Birthday rebuild
