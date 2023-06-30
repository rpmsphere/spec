Summary: DVD Copier/Archiver
Name: dvdshrink
URL: https://ozzzy.dyndns.org
Version: 2.6.1
Release: 2.1
Source0: ftp://ozzzy.dyndns.org/pub/%{name}-%{version}-11mdk.tar.gz
Group: Multimedia/Video
License: GPL
Requires: perl-GTK transcode dvdauthor dvdbackup gocr mjpegtools subtitleripper mkisofs dvd+rw-tools
BuildArch: noarch

%description
Dvdshrink is a bash front-end for many packages that will allow 
you to make 'fair use' archival copies of a DVD. It ships with 
a Gtk2 front-end (for the front-end) making things a bit simpler.

%prep
%setup -q -c

%install
mkdir -p %{buildroot}
cp -a usr %{buildroot}
mv %{buildroot}%{_datadir}/applications/%{name} %{buildroot}%{_datadir}/%{name}
mkdir -p %{buildroot}%{_datadir}/pixmaps
mv %{buildroot}%{_datadir}/icons/* %{buildroot}%{_datadir}/pixmaps

%files
%{_bindir}/xdvdshrink.pl
%{_bindir}/dvdshrink
%{_bindir}/dvdsfunctions
%{_bindir}/batchrip.sh
%{_bindir}/stuff
%{_datadir}/pixmaps/%{name}.xpm
%{_datadir}/pixmaps/batchrip.xpm
%{_datadir}/%{name}
%{_defaultdocdir}/%{name}

%changelog
* Tue Apr 19 2016 Wei-Lun Chao <bluebat@member.fsf.org> - 2.6.1
- Rebuilt for Fedora
* Sun Dec 27 2009 Rick Saunders <ozzzy1@gmail.com> 2.6.1-11
- Stephen Isard applied fixes for subtitles
* Fri May 04 2007 Rick Saunders <ozzzy1@gmail.com> 2.6.1-10
- XML used to build DVD on drive now, no need to edit in the
- t option for dvdauthor
* Mon Dec 11 2006 Rick Saunders <ozzzy1@gmail.com> 2.6.1-9
- Fixed inconsequential bug in checkbox setting
* Thu Oct 26 2006 Rick Saunders <ozzzy1@gmail.com> 2.6.1-8
- Fixed bug in passing language to dvdauthor
* Thu Jun 29 2006 Rick Saunders <ozzzy1@gmail.com> 2.6.1-7
- Fixed a bug in 'testselect'
* Wed Mar 01 2006 Rick Saunders <ozzzy1@gmail.com> 2.6.1-5
- Added a trap to 'remultiplexing' that will stop the program
- from erroring out if a spurious 'splitting' error occurs in
- mplex
* Tue Feb 21 2006 Rick Saunders <ozzzy1@gmail.com> 2.6.1-4
- Changed where FIFOs are kept
- Fixed typo that could cause an error
* Fri Aug 26 2005 Rick Saunders <ozzzy1@gmail.com> 2.6.1
- Attempt to fix A/V synch problems with some machines
- Removed 'Kill BASH' button, now a dialog
- GUI fixes
* Tue Aug 09 2005 Rick Saunders <ozzzy1@gmail.com> 2.6.0
- Removed the disabling -X test for subtitle2pgm in both 
- xdvdshrink.pl and dvdshrink dvdshrink will use the -X 
- if it detects a version that requires it 
* Sat Apr 22 2005 Rick Saunders <ozzzy1@gmail.com> 2.6.0
- Massive code rewrite for readability/utility
- Added rudimentary A/V de-synch detection in source
- Added ISO save WITH burn
- New DVD menus/opening trailer
* Tue Apr 05 2005 Rick Saunders <ozzzy1@gmail.com> 2.5.1-3
- Fixed a bug (??) in the 'Milliseconds' function
* Mon Apr 04 2005 Rick Saunders <ozzzy1@gmail.com> 2.5.1
- DVD menuing system added to multi-episode DVDs
* Fri Mar 18 2005 Rick Saunders <ozzzy1@gmail.com> 2.5.0
- Major changes to GUI (mostly look and feel)
- Minimal 'restart' mode added to 'episode' mode
- Some new functionality in GUI
* Mon Mar 07 2005 Rick Saunders <ozzzy1@gmail.com> 2.4.1
- Minor changes to GUIs
- More code optimization in the functions file
* Fri Mar 05 2005 Rick Saunders <ozzzy1@gmail.com> 2.4.0
- New GUI functions and logic
- Some code optimization
- Fixed show-stopping bug in subtitle XML checker
- All scripts now show same version number
* Tue Mar 02 2005 Rick Saunders <ozzzy1@gmail.com> 2.4.beta1-1mdk
- Various niggling fixes for issues pointed out by Hawkwind
- Fixed audio selection bug pointed out by Agios
- Disabled ability to select dts audio tracks
* Fri Feb 27 2005 Rick Saunders <ozzzy1@gmail.com> 2.3.2-3mdk
- Bugfix in 'requantize' function
- Additional functionality in 'xbatchrip.pl'
* Fri Feb 25 2005 Rick Saunders <ozzzy1@gmail.com> 2.3.2-2mdk
- Functionality for 'xbatchrip.pl'
- Bugfixes in 'batchrip.sh'
- Bugfixes in 'dvdsfunctions'
- Added the 'batchrip.sh' functions to 'dvdsfunctions'
- Code cleanup
- Added the functionality of 'buildxml.sh' and 'builddvd.sh' to
- the 'batchrip.sh' script
* Tue Feb 22 2005 Rick Saunders <ozzzy1@gmail.com> 2.3.1-1mdk
- Re-write of the xbatchrip.pl GUI
- Added requantization factor PERL script
- Small modification done to 'dvdshrink' and it's functions
- to make the requantization factor a bit more sane
* Sun Feb 20 2005 Rick Saunders <ozzzy1@gmail.com> 2.2.4-2mdk
- Added GUI script for batchrip.sh
* Sat Feb 19 2005 Rick Saunders <ozzzy1@gmail.com> 2.2.4-1mdk
- Added batchrip.sh and txt file to RPM
- Added buildxml.sh to RPM
- Added functionality for batch ripping
- Fixed bug when custom shrink factor selected
- Fixed help items
* Fri Feb 11 2005 Rick Saunders <ozzzy1@gmail.com> 2.2.3-2mdk
- One minor change to 'dvdshrink' to fix an error in 'checktools'
* Sat Feb 05 2005 Rick Saunders <ozzzy@gmail1.com> 2.2.3-1mdk
- Minor changes to bash scripts to enhance functionality of GUI
- Added several features to GUI
* Thu Jan 27 2005 Rick Saunders <ozzzy@gmail1.com> 2.2.2-1mdk
- initial RPM release
