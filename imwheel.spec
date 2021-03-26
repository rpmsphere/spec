%define cvs	20070707

Summary:	A utility to make wheel mice work under X
Name:		imwheel
Version:	1.0.0
Release:	1
License:	GPL
Group:		System/Kernel and hardware
BuildRequires:	libX11-devel
BuildRequires:	byacc
%if %cvs
Source:		%{name}-%{cvs}.tar.bz2
%else
Source:		http://prdownloads.sourceforge.net/%{name}/%{name}-%{version}.tar.bz2
%endif
Source2:	imwheelrc.generic
Source3:	imwheelrc.MX700

# Taken from Debian; Debian-specific parts removed and util.c section
# re-diffed by AdamW 2007/07
Patch0:		imwheel_1.0.0pre12-7-modified.diff
Patch1:		imwheel-1.0.0pre12-fix-debian-start-imwheel.patch
Patch10:	imwheel-1.0.0pre12-start-when-installed--and--use-option-k.patch
Patch11:	imwheel-1.0.0pre12-enable-extra-buttons-by-default.patch
Patch12:	imwheel-1.0.0pre12-add-cmdline-option-to-specify-rcfile.patch
URL:		http://imwheel.sourceforge.net/

%description 
Imwheel is a tool which can enable the use of extended buttons on
mice with more than the regular three buttons.

It can be used both with X.org and with closed-source
commercial X-servers (for example those made by MetroLink
or Xi Graphics).

%prep

%if %cvs
%setup -q -n %{name}
%else
%setup -q
%endif
%patch0 -p1
%patch1 -p1
%patch10 -p1
%patch11 -p1
%patch12 -p1

%build
%if %cvs
./autogen.sh
%endif
%configure

%__make 

%install
rm -rf %{buildroot}

install -c -D -m 0755 imwheel %{buildroot}%{_bindir}/imwheel
install -c -D -m 0644 imwheel.1 %{buildroot}%{_mandir}/man1/imwheel.1x

# the default configuration
install -D -m 644 debian/startup.conf %{buildroot}%{_sysconfdir}/X11/imwheel/startup.conf
install -D -m 755 debian/60imwheel_start-imwheel %{buildroot}%{_sysconfdir}/X11/xinit.d/imwheel
for i in imwheelrc %{SOURCE2} %{SOURCE3}; do 
      install -D -m 644 $i %{buildroot}%{_sysconfdir}/X11/imwheel/`basename $i`
done
ln -s imwheelrc.MX700 %{buildroot}%{_sysconfdir}/X11/imwheel/imwheelrc.MX500
ln -s imwheelrc.MX700 %{buildroot}%{_sysconfdir}/X11/imwheel/imwheelrc.MX1000

%triggerpostun -- imwheel <= 0.9.9
if [ -f /etc/X11/imwheelrc.rpmsave ]; then
   mv -f /etc/X11/imwheel/imwheelrc /etc/X11/imwheel/imwheelrc.rpmnew
   mv -f /etc/X11/imwheelrc.rpmsave /etc/X11/imwheel/imwheelrc
fi

%clean
rm -fr %buildroot

%files
%dir %{_sysconfdir}/X11/imwheel
%config(noreplace) %{_sysconfdir}/X11/imwheel/startup.conf
%config(noreplace) %{_sysconfdir}/X11/imwheel/imwheelrc
%{_sysconfdir}/X11/imwheel/imwheelrc.*
%{_sysconfdir}/X11/xinit.d/imwheel
%{_bindir}/imwheel
%{_mandir}/man1/*
%doc BUGS ChangeLog COPYING README EMACS

%changelog
* Tue Mar 20 2018 Wei-Lun Chao <bluebat@member.fsf.org> - 1.0.0
- Rebuild for Fedora
* Mon Dec 17 2007 Thierry Vignaud <tvignaud@mandriva.com> 1.0.0-0.20070707.1mdv2008.1
+ Revision: 127050
- kill re-definition of %%buildroot on Pixel's request
* Sat Jul 07 2007 Adam Williamson <awilliamson@mandriva.com> 1.0.0-0.20070707.1mdv2008.0
+ Revision: 49557
- rebuild for 2008
- rediff the util.c portion of the debian patch against current CVS
- remove all bits of the debian patch that are not of interest to us
- improve description
- use current CVS as it has useful changes and a new release is nowhere in sight
* Tue Sep 05 2006 Pixel <pixel@mandriva.com>
+ 2006-09-05 11:12:58 (59957)
- add MX500 and MX1000 (symlinks to MX700)
* Fri Sep 01 2006 Pixel <pixel@mandriva.com>
+ 2006-09-01 16:48:09 (59375)
- new version
- launch with option "-k" to ensure previously running imwheel is killed
- handle migration from /etc/X11/imwheelrc to /etc/X11/imwheel/imwheelrc
- add optional argument --rc <rcfile> (used by mousedrake)
- drop imwheel-solo (obsolete?)
- imwheelrc.generic with binding Thumb1 and Thumb2 to Alt_L|Left and Alt_L|Right,
- imwheelrc.MX700 with binding for Logitech extra buttons
- script xinit.d/imwheel is no more a config file modifiable by user
- add debian patch (esp. to handle extra buttons, ie #10, #11...)
- use debian startup script, but fix it
- enable many buttons without using explicitly -b '4 5 6 7 8 9 10 11...'
- drop patch0 (debian patch handles it, well at least partially)
- drop gcc3.3 gcc3.4 patch2 patch3 (now unneeded)
- drop gpm-glibc2.2 patch1 and x86_64 patch4 (imwheel special gpm is no more)
- drop "improvement" patch5 (debian patch is more extensive)
* Thu Aug 31 2006 Pixel <pixel@mandriva.com>
+ 2006-08-31 14:10:37 (58981)
- Import imwheel
* Fri Feb 10 2006 Thierry Vignaud <tvignaud@mandriva.com> 0.9.9-9mdk
- fix build on x86_64
* Wed Feb 01 2006 Lenny Cartier <lenny@mandriva.com> 0.9.9-8mdk
- from Jean Jacques Brucker <jjbrucker@free.fr> : 
	- improvement to make imwheel available to assign buttons greater than 9.
	- reporting the improvement in the man pages.
* Fri Nov 12 2004 Stefan van der Eijk <stefan@mandrake.org> 0.9.9-7mdk
- BuildRequires: byacc
* Tue Oct 05 2004 Gwenole Beauchesne <gbeauchesne@mandrakesoft.com> 0.9.9-6mdk
- gcc-3.4 and 64-bit fixes
