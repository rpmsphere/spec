%define binary %{name}
%define icon %{name}.png
%define desktopfile %{name}.desktop
%define consolefile %{name}.console.apps
%define pamfile %{name}.pam.d

Name: autoplus
Version: 1.4
Release: 7.1
Summary: Dangermouse's installer script
Group: Applications/Productivity
License: GPLv2+
URL: https://dnmouse.org/scripts/%{name}
Source0: %{name}-%{version}.tar.gz
BuildArch: noarch
Requires: fedora-release >= 15
Requires: zenity
Obsoletes: fedoraplus
Conflicts: easylife,fedorautils-latest

%description
Installer script to install multimedia, browser plugins and graphics drivers.

%prep
%setup -q 

%build

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{_datadir}/%{name}
install -Dpm 0755 %{binary} $RPM_BUILD_ROOT%{_datadir}/%{name}/%{binary}
install -Dpm 0644 %{icon} $RPM_BUILD_ROOT%{_datadir}/pixmaps/%{icon}
install -Dpm 0644 %{consolefile} $RPM_BUILD_ROOT/etc/security/console.apps/%{name}
install -Dpm 0644 %{pamfile} $RPM_BUILD_ROOT/etc/pam.d/%{name}
mkdir -p $RPM_BUILD_ROOT%{_bindir}
ln -sf %{_bindir}/consolehelper $RPM_BUILD_ROOT%{_bindir}/%{name}
install -Dpm 0644 %{desktopfile} $RPM_BUILD_ROOT%{_datadir}/applications/%{desktopfile}

%post
# Create desktop icon the logged regular user

#Save previous IFS
PREVIOUS_IFS=$IFS

#Populate arrays with regular users' name and respective homes
COUNT=0
unset USERS
unset HOMES
while IFS=':' read user pass uid gid gecos HOME shell; do

        if [[ "$uid" -gt 499 && "$uid" -lt 65534 ]]; then

                if [[ -e "$HOME"/.config/user-dirs.dirs ]]; then

                        DF=$(cat "$HOME"/.config/user-dirs.dirs | grep -i DESKTOP_DIR | cut -d/ -f2)
                        DESKTOPFOLDER[$COUNT]="$HOME"/"${DF%\"}"

                        # Copy icon-launcher to desktop folder
                        %{__cp} %{_datadir}/applications/%{desktopfile} "${DESKTOPFOLDER[$COUNT]}"
                        %{__chmod} a+rwx "${DESKTOPFOLDER[$COUNT]}/%{desktopfile}"

                        let COUNT++
        
                fi

        fi

done < /etc/passwd
        
#Restore previous IFS
IFS=$PREVIOUS_IFS

%files
%config(noreplace) %{_sysconfdir}/pam.d/%{name}
%config(noreplace) %{_sysconfdir}/security/console.apps/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/%{name}/%{name}
%{_datadir}/pixmaps/%{name}.png
%{_bindir}/%{name}

%changelog
* Wed Jul 18 2012 Wei-Lun Chao <bluebat@member.fsf.org> - 1.4
- Rebuilt for Fedora
* Mon Feb 27 2012 Dave Wilks <dave@dnmouse.org> 1.4-5
- Created launcher for lightscribe software
* Thu Feb 23 2012 Dave Wilks <dave@dnmouse.org> 1.4-4
- Added Verbose mode for livecd-creator to stop people from thinking its frozen
* Fri Feb 3 2012 Dave Wilks <dave@dnmouse.org> 1.4-3
- Added Handbrake for ripping dvd's 
* Thu Feb 2 2012 Dave Wilks <dave@dnmouse.org> 1.4-2
- Added error log for experimental respin backup 
* Sat Jan 28 2012 Dave Wilks <dave@dnmouse.org> 1.4-1
- Another Bugfix for experimental respin backup for non default repos installed
* Sun Jan 22 2012 Dave Wilks <dave@dnmouse.org> 1.4-0
- Another Bugfix for experimental respin backup
* Mon Jan 16 2012 Dave Wilks <dave@dnmouse.org> 1.3-9
- Bugfix for experimental respin backup
* Thu Jan 12 2012 Dave Wilks <dave@dnmouse.org> 1.3-8
- Minor bug fix removed shell refresh
* Wed Jan 11 2012 Dave Wilks <dave@dnmouse.org> 1.3-6/7
- Added gnome-wether-extension
* Tue Jan 10 2012 Dave Wilks <dave@dnmouse.org> 1.3-5*
- Added alacarte with fix so it works
* Mon Jan 9 2012 Dave Wilks <dave@dnmouse.org> 1.3-5
- Remade respin option so more reliable should work 99%% of time now!
* Sun Jan 8 2012 Dave Wilks <dave@dnmouse.org> 1.3-3/4
- Bug fix Livecd tools directory changed
* Sat Jan 7 2012 Dave Wilks <dave@dnmouse.org> 1.3-2
- Added experimental option to create a livedvd backup
- of os
* Mon Dec 12 2011 Dave Wilks <dave@dnmouse.org> 1.3-1
- set livna repo disabled by default as never updates
- updated sun java to ver 6u29
* Sat Dec 10 2011 Dave Wilks <dave@dnmouse.org> 1.3-0
- fix for nautilus dropbox as they fucked up their rpms again
* Wed Nov 30 2011 Dave Wilks <dave@dnmouse.org> 1.2-9
-bug fix for googleearth
* Fri Nov 11 2011 Dave Wilks <dave@dnmouse.org> 1.2-8
-changed to livna as atrpms links no longer work
* Mon Nov 7 2011 Dave Wilks <dave@dnmouse.org> 1.2-6
-removed themes as now in repo's
* Tue Oct 4 2011 Dave Wilks <dave@dnmouse.org> 1.2-5
-Updated to use adobe 64bit flash
* Sat Sep 24 2011 Dave Wilks <dave@dnmouse.org> 1.2-4
-Updated to latest sun java
* Mon Sep 19 2011 Dave Wilks <dave@dnmouse.org> 1.2-3
-Renabled cinlerra 
* Sun Aug 28 2011 Dave Wilks <dave@dnmouse.org> 1.2-2
-Added 5 extra themes not in repos yet
* Sun Aug 28 2011 Dave Wilks <dave@dnmouse.org> 1.2-1
-Added a link to proper help page for bugs etc..
* Thu Aug 18 2011 Dave Wilks <dave@dnmouse.org> 1.2
-Added a warning for those using sugar 
* Wed Aug 17 2011 Dave Wilks <dave@dnmouse.org> 1.1-9
- libdvdcss is now pulled from atrpms as livna is to unreliable
- changed vbox bug due to dumb naming in vbox repo
* Thu Jun 16 2011 Dave Wilks <dave@dnmouse.org> 1.1-8
- removed air as no longer developed for linux and buggy
- updated imagination to install from rpmfusion as now in repos at last
- removed cinelera as no f15 repo now
* Thu Jun 2 2011 Dave Wilks <dave@dnmouse.org> 1.1-7
- fixed launcher java vbox warning restart needed
* Thu Jun 2 2011 Dave Wilks <dave@dnmouse.org> 1.1-5
- enabled new f15 vbox repo
- changed name 
- updated to latest sun java
- bug fix air not installing keyring (i686)
- added fedoraplus as obselete
- added requiremnent above fedora release 14
- removed dist number
* Wed May 25 2011 Dave Wilks <dave@dnmouse.org> 1.1-4
- temp set vbox repo to f14 for f15 as no repo yet
* Wed May 25 2011 Dave Wilks <dave@dnmouse.org> 1.1-3
- bug fix adobeair calling in wrong deps
* Wed Apr 27 2011 Dave Wilks <dave@dnmouse.org> 1.1-2
- changed adobeair install from repo
* Sat Apr 23 2011 Dave Wilks <dave@dnmouse.org> 1.1-1
- disabled dropbox repo once installed rebuilt for f15
- also removed autologin no longer need in f15
* Thu Apr 7 2011 Dave Wilks <dave@dnmouse.org> 1.1-0
- changed download source of lightscribe
* Thu Mar 31 2011 Dave Wilks <dave@dnmouse.org> 1.0-9
- added ffmpeg2theora
* Wed Mar 16 2011 Dave Wilks <dave@dnmouse.org> 1.0-8
- added update rpmfusion repos
* Mon Mar 14 2011 Dave Wilks <dave@dnmouse.org> 1.0-7
- Updated skype deps
* Sun Mar 13 2011 Dave Wilks <dave@dnmouse.org> 1.0-6
- Bug fix wrong repo for googleearth added freeglut for bug in mplayer
* Thu Mar 10 2011 Dave Wilks <dave@dnmouse.org> 1.0-5
- Bug fixed missed -y on rpmfusion repo install
* Mon Mar 07 2011 Dave Wilks <dave@dnmouse.org> 1.0-4
- Updated to latest java 6u24 and latest mplayer codecs added i586 support
* Tue Feb 15 2011 Dave Wilks <dave@dnmouse.org> 1.0-3
- change logo, thanks Robin
* Wed Feb 09 2011 Dave Wilks <dave@dnmouse.org> 1.0-2
- remove realplayer due to its bugs
* Sun Feb 06 2011 Dave Wilks <dave@dnmouse.org> 1.0-1
- added new selinux rule for dropbox
* Tue Feb 5 2008 Dave Wilks <dave@dnmouse.org> 1.0-0
- initial release of rpm from script
