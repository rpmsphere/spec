%global debug_package %{nil}

Summary: A window manager library and "screen for X11"
Name: parti
Version: 0.0.7.36
Release: 11.1
License: GPL
Requires: pygtk2, xorg-x11-server-utils, xorg-x11-server-Xvfb, python-pillow, dbus-python, python-uuid
Group: User Interface/Desktops
URL: http://code.google.com/p/partiwm
Source: %{name}-all-%{version}.tar.gz
BuildRequires: python, setuptool, Cython

### Patches ###
# if building a generic rpm (without .so) which works as client only
Patch0: disable-posix-server.patch

%description
Parti is a tabbing/tiling (one might say "partitioning") window manager.
Its goal is to bring this superior window management interface to modern,
mainstream desktop environments.

%changelog
* Thu Feb 16 2012 Wei-Lun Chao <bluebat@member.fsf.org> - 0.0.7.36
- Rebuild for Fedora
* Thu Feb 08 2012 Antoine Martin <antoine@nagafix.co.uk> 0.0.7.36-1
- fix clipboard bug which was causing Java applications to crash
- ensure we always properly disconnect previous client when new connection is accepted
- avoid warnings with Java applications, focus errors, etc
* Wed Feb 01 2012 Antoine Martin <antoine@nagafix.co.uk> 0.0.7.35-1
- ssh password input fix
- ability to take screenshots ("xpra screenshot")
- report server version ("xpra version")
- slave windows (drop down menus, etc) now move with their parent window
- show more session statistics: damage regions per second
- posix clients no longer interfere with the GTK/X11 main loop
- ignore missing properties when they are changed, and report correct source of the problem
- code style cleanups and improvements
* Thu Jan 19 2012 Antoine Martin <antoine@nagafix.co.uk> 0.0.7.34-1
- security: restrict access to run-xpra script (chmod)
- security: cursor data sent to the client was too big (exposing server memory)
- fix thread leak - properly this time, SIGUSR1 now dumps all threads
- off-by-one keyboard mapping error could cause modifiers to be lost
- pure python/cython method for finding modifier mappings (faster and more reliable)
- retry socket read/write after temporary error EINTR
- avoid warnings when asked to refresh windows which are now hidden
- auto-refresh was using an incorrect window size
- logging formatting fixes (only shown with logging on)
- hide picture encoding menu when mmap in use (since it is then ignored)
* Fri Jan 13 2012 Antoine Martin <antoine@nagafix.co.uk> 0.0.7.33-1
- readonly command line option
- correctly stop all network related threads on disconnection
- faster pixel data transfers for large areas
- fix auto-refresh jpeg quality
- fix potential exhaustion of mmap area
- fix potential race in packet compression setup code
- keyboard: better modifiers detection, synchronization of capslock and numlock
- keyboard: support all modifiers correctly with and without keyboard-sync option
* Thu Dec 28 2011 Antoine Martin <antoine@nagafix.co.uk> 0.0.7.32-1
- bug fix: disconnection could leave the server (and X11 server) in a broken state due to threaded UI calls
- bug fix: don't remove window focus when just any connection is lost, only when the real client goes away
- bug fix: initial windows should get focus (partial fix)
- support key repeat latency workaround without needing raw keycodes (OS X and MS Windows)
- command line switch to enable client side key repeat: "--no-keyboard-sync" (for high latency/jitter links)
- session info dialog: shows realtime connection and server details
- menu entry in system tray to raise all managed windows
- key mappings: try harder to unpress all keys before setting the new keymap
- key mappings: try to reset modifier keys as well as regular keys
- key mappings: apply keymap using Cython code rather than execing xmodmap
- key mappings: fire change callbacks only once when all the work is done
- use dbus for tray notifications if available, prefered to pynotify
- show full version information in about dialog
* Wed Nov 28 2011 Antoine Martin <antoine@nagafix.co.uk> 0.0.7.31-1
- threaded server for much lower latency
- fast memory mapped transfers for local connections
- adaptive damage batching, fixes window refresh
- xpra "detach" command
- fixed system tray for Ubuntu clients
- fixed maximized windows on Ubuntu clients
* Tue Nov 01 2011 Antoine Martin <antoine@nagafix.co.uk> 0.0.7.30-1
- fix for update batching causing screen corruption
- fix AttributeError jpegquality: make PIL (aka python-imaging) truly optional
- fix for jitter compensation code being a little bit too trigger-happy
* Wed Oct 26 2011 Antoine Martin <antoine@nagafix.co.uk> 0.0.7.29-2
- fix partial packets on boundary causing connection to drop (properly this time)
* Tue Oct 25 2011 Antoine Martin <antoine@nagafix.co.uk> 0.0.7.29-1
- fix partial packets on boundary causing connection to drop
- improve disconnection diagnostic messages
- scale cursor down to the client's default size
- better handling of right click on system tray icon
- posix: detect when there is no DISPLAY and error out
- support ubuntu's appindicator (yet another system tray implementation)
- remove harmless warnings about missing properties on startup
* Tue Oct 18 2011 Antoine Martin <antoine@nagafix.co.uk> 0.0.7.28-2
- fix password mode - oops
* Tue Oct 18 2011 Antoine Martin <antoine@nagafix.co.uk> 0.0.7.28-1
- much more efficient and backwards compatible network code, prevents a CPU bottleneck on the client
- forwarding of system notifications, system bell and custom cursors
- system tray menu to make it easier to change settings and disconnect
- automatically resize Xdummy to match the client's screen size whenever it changes
- PNG image compression support
- JPEG and PNG compression are now optional, only available if the Python Imaging Library is installed
- scale window icons before sending if they are too big
- fixed keyboard mapping for OSX and MS Windows clients
- compensate for line jitter causing keys to repeat
- fixed cython warnings, unused variables, etc
* Fri Sep 22 2011 Antoine Martin <antoine@nagafix.co.uk> 0.0.7.27-1
- compatibility fix for python 2.4 (remove "with" statement)
- slow down updates from windows that refresh continuously
* Wed Sep 20 2011 Antoine Martin <antoine@nagafix.co.uk> 0.0.7.26-1
- minor changes to support the Android client (work in progress)
- allow keyboard shortcuts to be specified, default is meta+shift+F4 to quit (disconnects client)
- clear modifiers when applying new keymaps to prevent timeouts
- reduce context switching in the network read loop code
- try harder to close connections cleanly
- removed some unused code, fixed some old test code
* Wed Aug 31 2011 Antoine Martin <antoine@nagafix.co.uk> 0.0.7.25-1
- Use xmodmap to grab the exact keymap, this should ensure all keys are mapped correctly
- Reset modifiers whenever we gain or lose focus, or when the keymap changes
* Mon Aug 15 2011 Antoine Martin <antoine@nagafix.co.uk> 0.0.7.24-1
- Use raw keycodes whenever possible, should fix keymapping issues for all Unix-like clients
- Keyboard fixes for AltGr and special keys for non Unix-like clients
* Fri Jul 27 2011 Antoine Martin <antoine@nagafix.co.uk> 0.0.7.23-2
- More keymap fixes..
* Wed Jul 20 2011 Antoine Martin <antoine@nagafix.co.uk> 0.0.7.23-1
- Try to use setxkbmap before xkbcomp to setup the matching keyboard layout
- Handle keyval level (shifted keys) explicitly, should fix missing key mappings
- More generic option for setting window titles
- Exit if the server dies
* Thu Jun 02 2011 Antoine Martin <antoine@nagafix.co.uk> 0.0.7.22-1
- minor fixes: jpeg, man page, etc
* Fri May 20 2011 Antoine Martin <antoine@nagafix.co.uk> 0.0.7.21-1
- ability to bind to an existing display with --use-display
- --xvfb now specifies the full command used. The default is unchanged
- --auto-refresh-delay does automatic refresh of idle displays in a lossless fashion
* Wed May 04 2011 Antoine Martin <antoine@nagafix.co.uk> 0.0.7.20-1
- more reliable fix for keyboard mapping issues
* Mon Apr 25 2011 Antoine Martin <antoine@nagafix.co.uk> 0.0.7.19-1
- xrandr support when running against Xdummy, screen resizes on demand
- fixes for keyboard mapping issues: multiple keycodes for the same key
* Mon Apr 4 2011 Antoine Martin <antoine@nagafix.co.uk> 0.0.7.18-2
- Fix for older distros (like CentOS) with old versions of pycairo
* Sat Mar 28 2011 Antoine Martin <antoine@nagafix.co.uk> 0.0.7.18-1
- Fix jpeg compression on MS Windows
- Add ability to disable clipboard code
- Updated man page
* Wed Jan 19 2011 Antoine Martin <antoine@nagafix.co.uk> 0.0.7.17-1
- Honour the pulseaudio flag on client
* Thu Aug 25 2010 Antoine Martin <antoine@nagafix.co.uk> 0.0.7.16-1
- Merged upstream changes.
* Thu Jul 01 2010 Antoine Martin <antoine@nagafix.co.uk> 0.0.7.15-1
- Add option to disable Pulseaudio forwarding as this can be a real network hog.
- Use logging rather than print statements.
* Mon May 04 2010 Antoine Martin <antoine@nagafix.co.uk> 0.0.7.13-1
- Ignore minor version differences in the future (must bump to 0.0.8 to cause incompatibility error)
* Tue Apr 13 2010 Antoine Martin <antoine@nagafix.co.uk> 0.0.7.12-1
- bump screen resolution
* Sun Jan 11 2010 Antoine Martin <antoine@nagafix.co.uk> 0.0.7.11-1
- first rpm spec file

%prep
%setup -q -n %{name}-all-%{version}
%patch0 -p0

%build
rm -rf build install
python2 make_constants_pxi.py wimpiggy/lowlevel/constants.txt wimpiggy/lowlevel/constants.pxi
CFLAGS=-O0 python2 setup.py build

%install
rm -rf $RPM_BUILD_ROOT
python2 setup.py install -O1  --prefix /usr --skip-build --root $RPM_BUILD_ROOT
# remove .so (not suitable for a generic RPM)
#rm -f "${RPM_BUILD_ROOT}/usr/lib/python2.6/site-packages/wimpiggy/bindings.so"
#rm -f "${RPM_BUILD_ROOT}/usr/lib/python2.6/site-packages/xpra/wait_for_x_server.so"

sed -i 's|/usr/bin/python$|/usr/bin/python2|' %{buildroot}%{_bindir}/*

%clean
rm -rf $RPM_BUILD_ROOT

%files
%{_bindir}/parti
%{_bindir}/parti-repl
%exclude %{_bindir}/xpra
%exclude %{python2_sitelib}/xpra
%{python2_sitelib}/parti
%{python2_sitelib}/wimpiggy
%{python2_sitelib}/parti_all-*.egg-info
%exclude /usr/share/xpra
/usr/share/parti
/usr/share/wimpiggy
%exclude /usr/share/man/man1/xpra.*
/usr/share/man/man1/parti.*
