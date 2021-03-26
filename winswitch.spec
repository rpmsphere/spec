%define nautilus_lib %{_libdir}/nautilus

Summary: Front end for controlling remote desktop sessions
Vendor: devloop.org.uk
Name: winswitch
Version: 0.12.20
Release: 5.1
License: GPL3
Group: Networking
URL: http://winswitch.org/
Source: winswitch-%{version}.tar.gz
Obsoletes: shifter
BuildRequires: libpng-devel
BuildRequires: python, setuptool, pygtk2-devel, python-setuptools

%description
Start and control remote GUI sessions via xpra, NX, VNC, RDP or plain ssh X11 forwarding.
You can start, suspend, resume and send supported sessions to other clients.

%changelog
* Thu Dec 18 2014 Wei-Lun Chao <bluebat@member.fsf.org> - 0.12.20
- Rebuild for Fedora

* Tue Jun 14 2011 Antoine Martin <antoine@nagafix.co.uk> 0.12.3-1
- mDNS readers are now removed correctly (was causing segfaults on exit)
- exit cleanly on all platforms, freeing all resources and waiting if needed
- VNC full desktop sessions can be started more than once (oops)
- fix segfaults in the X11 session detection code
- fix file descriptor leaks in X11 code and screen capture
- support many more KDE applications using the "--nofork" parameter
- avoid sending really big icon files! (above 128KB)

* Mon May 30 2011 Antoine Martin <antoine@nagafix.co.uk> 0.12.2-6
- Fix for xpra session never terminating when command exits
- Fix for applications requiring access to gnome-keyring daemon

* Fri May 27 2011 Antoine Martin <antoine@nagafix.co.uk> 0.12.2-1
- KDE fix preventing the tray icon from being clicked on
- GStreamer audio and video now correctly stop when the client close it
- Support for Xpra's new 'adaptive JPEG' mode using bandwidth controls
- many new options can now be selected in the session dialogs

* Wed May 18 2011 Antoine Martin <antoine@nagafix.co.uk> 0.12.1-3
- one liner fix for menu not showing on KDE
- more RPM specfile dependency fixes for openSUSE

* Tue May 17 2011 Antoine Martin <antoine@nagafix.co.uk> 0.12.1-2
- RPM specfile dependency fixes for CentOS and openSUSE

* Wed May 4 2011 Antoine Martin <antoine@nagafix.co.uk> 0.12.1-1
- Fix spurious VNC timeouts due to log file buffering
- Avoid error message when SSH sessions terminate
- SSH needs password OR keys

* Mon May 2 2011 Antoine Martin <antoine@nagafix.co.uk> 0.12.0-1
- Adds GStreamer video streaming option for shadowing sessions
- Reliable sound support
- Xpra keyboard mapping fixes
- Detect applications that can only be started once per session and show warning
- Session pre-loading fixes
- Pre-connect to local sessions for ultra-fast startup
- Detect firewalls blocking mDNS

* Sun Apr 3 2011 Antoine Martin <antoine@nagafix.co.uk> 0.11.4-2
- Use /usr/lib for distributions that do not have /usr/libexec

* Tue Mar 29 2011 Antoine Martin <antoine@nagafix.co.uk> 0.11.4-1
- File transfers to remote servers without using SFTP
- Ability to whitelist server commands
- Stale connections are properly dropped, allowing re-connect to work
- Warn when files cannot be opened remotely
- Thunar file manager integration
- Moved most non user-visible commands to "/usr/libexec"
- Added "--help" and manual page to most commands
- Prevent code from logging ssh key passphrase in debug mode!

* Tue Mar 1 2011 Antoine Martin <antoine@nagafix.co.uk> 0.11.3-1
- Ability to integrate transparently into the main start menu
- Server will auto-start again when connecting over SSH
- Minor bugfixes

* Mon Jan 24 2011 Antoine Martin <antoine@nagafix.co.uk> 0.11.2-1
- Minor bug fixes

* Fri Dec 10 2010 Antoine Martin <antoine@nagafix.co.uk> 0.11.1-1
- Small GUI bug fixes
- SELinux detection
- Ability to start a custom command from the menus

* Sun Oct 10 2010 Antoine Martin <antoine@nagafix.co.uk> 0.11.0-1
- Complete re-write of the SSH transport layer using twisted-conch

* Wed Aug 11 2010 Antoine Martin <antoine@nagafix.co.uk> 0.10.0-1
- Complete rewrite of the sound support using gstreamer rtp, much more efficient than pulseaudio

* Sat May 08 2010 Antoine Martin <antoine@nagafix.co.uk> 0.9.19-1
- Fix some SSH tunnelling issues
- xpra preloading
- UI cleanup

* Thu May 06 2010 Antoine Martin <antoine@nagafix.co.uk> 0.9.18-1
- Another one-liner fix...

* Thu May 06 2010 Antoine Martin <antoine@nagafix.co.uk> 0.9.17-1
- Proper re-release, with fixlets for remote SSH servers and updated release files

* Thu May 06 2010 Antoine Martin <antoine@nagafix.co.uk> 0.9.16-1
- Windows and UI fixes

* Sat May 01 2010 Antoine Martin <antoine@nagafix.co.uk> 0.9.15-1
- Emergency release to fix annoying small bug in 0.9.14

* Sat May 01 2010 Antoine Martin <antoine@nagafix.co.uk> 0.9.14-1
- First release to support Windows servers

* Sat Apr 24 2010 Antoine Martin <antoine@nagafix.co.uk> 0.9.13-1
- Minor bug fixes

* Mon Apr 19 2010 Antoine Martin <antoine@nagafix.co.uk> 0.9.12-1
- Emergency fix for utmp errors

* Sat Apr 17 2010 Antoine Martin <antoine@nagafix.co.uk> 0.9.11-1
- Screenshot support

* Fri Apr 16 2010 Antoine Martin <antoine@nagafix.co.uk> 0.9.10-1
- Minor fixes

* Thu Apr 08 2010 Antoine Martin <antoine@nagafix.co.uk> 0.9.9-1
- first public release

* Mon Jan 11 2010 Antoine Martin <antoine@nagafix.co.uk> 0.9.0-1
- first rpm spec file

%prep
%setup -q

%build
%{__python} setup.py build
 
%install
rm -rf $RPM_BUILD_ROOT
%{__python} setup.py install -O1 --prefix /usr --skip-build --root $RPM_BUILD_ROOT
%ifarch x86_64 ppc64
mkdir -p $RPM_BUILD_ROOT/%{nautilus_lib}
mv $RPM_BUILD_ROOT/usr/lib/nautilus/extensions-2.0 $RPM_BUILD_ROOT/%{nautilus_lib}/
rmdir $RPM_BUILD_ROOT/usr/lib/nautilus
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%files
%doc COPYING
%{_bindir}/winswitch_*
%{_bindir}/wcw
/usr/lib*/python*/*packages/winswitch*
%{_libexecdir}/winswitch
/etc/winswitch
/usr/share/winswitch
/usr/share/applications/winswitch.desktop
/usr/share/icons
/usr/share/mime
/usr/share/man
/usr/share/Thunar
/usr/share/Vash
%{nautilus_lib}/extensions-2.0/python/nautilus_winswitch.*
