Name:           wdm
Version:        1.28
Release:        16.1
Summary:        WINGs Display Manager
Group:          User Interface/X
# many MIT source files from xdm, and GPLv2+ from Wings
License:        GPLv2+
URL:            https://voins.program.ru/wdm/
Source0:        https://voins.program.ru/wdm/wdm-%{version}.tar.bz2
# stolen from xdm
Source1:        %{name}.pam
# adapted from debian to use freedesktop
Source2:        wdm-update_wdm_wmlist
# record and reuse previous session before launching generic Xsession
Source3:        wdm-Xsession
# debian patch modified to remove the configure patching
#Patch0:         https://ftp.debian.org/debian/pool/main/w/wdm/wdm_1.28-2.1.diff.gz
Patch0:         wdm_1.28-2.1.diff
# use fedora background/icon and match gdm default config
Patch1:         wdm-1.28-fedora.patch
# fix failsafe path and insecure use of /tmp
Patch2:         wdm-1.28-failsafe_tmp.patch
# fix reconfiguration script
Patch3:         wdm-1.28-reconf.patch
#Patch4:         wdm-1.28-ck.patch
BuildRequires:  giflib-devel
BuildRequires:  WINGs-devel gettext libselinux-devel pam-devel
BuildRequires:  libXt-devel libXmu-devel libXdmcp-devel
BuildRequires:  xrdb xterm systemd
BuildRequires:  ghostscript-core
Requires:       xrdb xterm systemd
Requires:       %{_sysconfdir}/pam.d
# we don't want to have new files, we reuse the kdm/xdm files
Requires:       xdm xorg-x11-xinit
# we use 'include' in the pam file, so
Requires:       pam >= 0.80
# reuse the images
Requires:       desktop-backgrounds-basic

%description
wdm combines the functions of a graphical display manager identifying 
and authenticating a user on a system with some of the functions of a 
session manager in selecting and starting a window manager. Optionally, 
wdm can shutdown (reboot or halt) the system.

wdm is a modification of XFree86's xdm package for graphically handling 
authentication and system login. Most of xdm has been preserved 
(XFree86 4.2.1.1) with the Login interface based on a WINGs. Tom 
Rothamel's "external greet" interface (see AUTHORS) was used to 
communicate wdm with wdmLogin. 

In the distribution, wdm may be called through a wrapper, wdm-dynwm, 
which determines the available window managers using the freedesktop 
information and modifies the wdm-config configuration file accordingly, 
before launching wdm.

%prep
%setup -q
%patch 0 -p1
%patch 1 -p1 -b .fedora
%patch 2 -p1 -b .failsafe_tmp
%patch 3 -p1 -b .reconf
#%patch 4 -p1 -b .ck
sed -i -e 's|get-wings-flags --|pkg-config WINGs --|' -e 's|get-wings-flags|pkg-config|' configure*

%build
export DEF_SERVER='%{_bindir}/X -nolisten tcp'
#export CFLAGS="$RPM_OPT_FLAGS `pkg-config --cflags ck-connector` -DUSE_CONSOLEKIT"
#export LDFLAGS="`pkg-config --libs ck-connector`"

%configure \
   --with-pamdir=%{_sysconfdir}/pam.d \
   --with-logdir=%{_localstatedir}/log \
   --with-runlockdir=%{_localstatedir}/run \
   --with-wdmdir=%{_sysconfdir}/wdm \
   --with-nlsdir=%{_datadir}/locale \
   --with-fakehome=%{_localstatedir}/run/wdm \
   --with-gfxdir=%{_datadir}/pixmaps/wdm \
   --with-Logo=../../backgrounds/tiles/default_blue.jpg \
   --with-defuserpath='/bin:%{_bindir}' \
   --with-defsystempath='/sbin:%{_sbindir}:/bin:%{_bindir}' \
   --enable-selinux \
   --enable-aafont 

make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT INSTALL='install -p'

install -p -m755 %{SOURCE2} $RPM_BUILD_ROOT%{_bindir}/update_wdm_wmlist

# do a wdm wrapper which updates the window manager list before
# launching wdm
cat > $RPM_BUILD_ROOT%{_bindir}/wdm-dynwm << EOF
#!/bin/sh
update_wdm_wmlist
wdm "\$@"
EOF

chmod 0755 $RPM_BUILD_ROOT%{_bindir}/wdm-dynwm

# move the reconfiguration script to _bindir
mv $RPM_BUILD_ROOT%{_sysconfdir}/wdm/wdmReconfig $RPM_BUILD_ROOT%{_bindir}

chmod 0644 $RPM_BUILD_ROOT%{_sysconfdir}/wdm/wdm-config

install -p -m644 %{SOURCE1} $RPM_BUILD_ROOT%{_sysconfdir}/pam.d/wdm

# remove old X session script, and old XFree86 session script
rm $RPM_BUILD_ROOT%{_sysconfdir}/wdm/Xsession.orig
rm $RPM_BUILD_ROOT%{_sysconfdir}/wdm/Xsession.XFree86

# use xdm/kdm files 
# first rename wdm files
for file in Xaccess Xsession Xsetup_0 GiveConsole TakeConsole; do
mv $RPM_BUILD_ROOT%{_sysconfdir}/wdm/$file $RPM_BUILD_ROOT%{_sysconfdir}/wdm/$file.wdm
done

# then use symlinks or wrapper
# calls /etc/X11xinit/Xsession
install -p -m755 %{SOURCE3} $RPM_BUILD_ROOT%{_sysconfdir}/wdm/Xsession
ln -s ../X11/xdm/Xaccess $RPM_BUILD_ROOT%{_sysconfdir}/wdm/Xaccess
ln -s ../X11/xdm/Xsetup_0 $RPM_BUILD_ROOT%{_sysconfdir}/wdm/Xsetup_0
ln -s ../X11/xdm/GiveConsole $RPM_BUILD_ROOT%{_sysconfdir}/wdm/GiveConsole
ln -s ../X11/xdm/TakeConsole $RPM_BUILD_ROOT%{_sysconfdir}/wdm/TakeConsole
ln -s ../X11/xdm/Xsession $RPM_BUILD_ROOT%{_sysconfdir}/wdm/Xsession.xorg

%find_lang %{name}

%files -f %{name}.lang
%doc AUTHORS COPYING ChangeLog* NEWS README* TODO NASA_image_guideline.html 
%config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/pam.d/wdm
%dir %{_sysconfdir}/wdm/
%config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/wdm/wdm-config
%config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/wdm/wdm-config.in
%config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/wdm/Xresources
%config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/wdm/Xservers
%config %{_sysconfdir}/wdm/GiveConsole.wdm
%config %{_sysconfdir}/wdm/TakeConsole.wdm
%config %{_sysconfdir}/wdm/Xaccess.wdm
%config %{_sysconfdir}/wdm/Xclients
%config %{_sysconfdir}/wdm/Xclients.in
%config %{_sysconfdir}/wdm/Xservers.fs
%config %{_sysconfdir}/wdm/Xservers.ws
%config %{_sysconfdir}/wdm/Xsession
%config %{_sysconfdir}/wdm/Xsession.wdm
%config %{_sysconfdir}/wdm/Xsetup_0.wdm
# links
%config %{_sysconfdir}/wdm/GiveConsole
%config %{_sysconfdir}/wdm/TakeConsole
%config %{_sysconfdir}/wdm/Xaccess
%config %{_sysconfdir}/wdm/Xsession.xorg
%config %{_sysconfdir}/wdm/Xsetup_0
%{_bindir}/wdm*
%{_bindir}/update_wdm_wmlist
%{_mandir}/man1/wdm*.1*
%{_datadir}/pixmaps/wdm/
%dir %{_localstatedir}/run/wdm

%changelog
* Sun Sep 09 2012 Wei-Lun Chao <bluebat@member.fsf.org> - 1.28
- Rebuilt for Fedora
* Mon Jul 27 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.28-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild
* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.28-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild
* Mon Mar  3 2008 Patrice Dumas <pertusus@free.fr> 1.28-10
- all the images are now in desktop-backgrounds-basic
* Tue Feb 19 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 1.28-9
- Autorebuild for GCC 4.3
* Wed Aug  1 2007 Patrice Dumas <pertusus@free.fr> 1.28-8
- require system-logos instead of fedora-logos (#250366)
- build requires WINGs-devel instead of WindowMaker-devel
* Thu Nov 30 2006 Patrice Dumas <pertusus@free.fr> 1.28-7
- keep timestamps for shipped files
- enable aa fonts
* Wed Nov 29 2006 Patrice Dumas <pertusus@free.fr> 1.28-6
- fix reconfiguration script
- requires pam recent enough
- don't set noreplace for scripts and example config files
* Wed Nov 29 2006 Patrice Dumas <pertusus@free.fr> 1.28-5
- fix insecure use of /tmp in original wdm script
- remove obsolete session scripts
* Sun Nov 12 2006 Patrice Dumas <pertusus@free.fr> 1.28-4
- add BR libXt-devel and libXmu-devel
* Fri Oct 20 2006 Patrice Dumas <pertusus@free.fr> 1.28-3
- correct wdm-dynwm
* Fri Oct 20 2006 Patrice Dumas <pertusus@free.fr> 1.28-2
- use images from desktop-backgrounds-basic fedora-logos
- record session style before calling the generic Xsession, and add
  previous session and custom session handling.
- ship the original config files
- fix a bug in the default config files
* Thu Oct 19 2006 Patrice Dumas <pertusus@free.fr> 1.28-1
- initial packaging
