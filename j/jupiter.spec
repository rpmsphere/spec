Summary:	Hardware Control System for Computers
Name:		jupiter
Version:	0.1.11
Release:	5.1
License:	GPL
Group:		X11/Applications
Source0:	%{name}_%{version}.tar.gz
URL:		http://sourceforge.net/projects/jupiter/
Requires:	coreutils, gnome-python2-gnome, xorg-x11-apps, rfkill
BuildArch:	noarch

%description
Simple, easy to use hardware and power management applet.

%prep
%setup -q

%build

%install
install -d $RPM_BUILD_ROOT%{_sysconfdir}/{pm,xdg,pm/power.d,pm/sleep.d,xdg/autostart}
install -d $RPM_BUILD_ROOT%{_datadir}/{applications,pixmaps}
install -d $RPM_BUILD_ROOT/var/jupiter
install -d $RPM_BUILD_ROOT/{usr,usr/bin}
install -d $RPM_BUILD_ROOT/{usr/lib,usr/lib/jupiter,usr/lib/jupiter/scripts,usr/lib/jupiter/kernel}
install -d $RPM_BUILD_ROOT/lib/udev/rules.d

install -m 755 lib/udev/rules.d/80-drm.rules $RPM_BUILD_ROOT/lib/udev/rules.d
install -m 755 pm/power.d/* $RPM_BUILD_ROOT%{_sysconfdir}/pm/power.d/
install -m 755 pm/sleep.d/* $RPM_BUILD_ROOT%{_sysconfdir}/pm/sleep.d/
install xdg/autostart/* $RPM_BUILD_ROOT%{_sysconfdir}/xdg/autostart/
install usr/share/applications/* $RPM_BUILD_ROOT%{_datadir}/applications/
install usr/share/pixmaps/*.png $RPM_BUILD_ROOT/usr/share/pixmaps/
install usr/lib/jupiter/scripts/* $RPM_BUILD_ROOT/usr/lib/jupiter/scripts/
install usr/lib/jupiter/kernel/* $RPM_BUILD_ROOT/usr/lib/jupiter/kernel/
install -m 755 usr/bin/jupiter $RPM_BUILD_ROOT/usr/bin/

sed -i 's|/usr/share/pixmaps/%{name}.png|%{name}|' $RPM_BUILD_ROOT%{_datadir}/applications/%{name}.desktop

sed -i 's|/usr/bin/env python$|/usr/bin/python2|' %{buildroot}%{_bindir}/%{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post
if [ ! "$(grep jupiter /etc/group)" ]; then
  echo "Adding Jupiter group"
  groupadd jupiter
fi
echo -n "Adding users to Jupiter group: "
  for i in $(awk -F: '$6 ~ /\/home/ && $3 >= 500 {print $1}' /etc/passwd);
  do
    echo -n $i" "
    usermod -G jupiter -a $i 2>/dev/null || true
  done
echo -e "\nAdding jupiter to sudoers"
if [ -d "/etc/sudoers.d" ]; then
  echo "%jupiter ALL=NOPASSWD: /usr/lib/jupiter/scripts/bluetooth, /usr/lib/jupiter/scripts/cpu-control, /usr/lib/jupiter/scripts/primary, /usr/lib/jupiter/scripts/rotate, /usr/lib/jupiter/scripts/touchpad, /usr/lib/jupiter/scripts/vga-out, /usr/lib/jupiter/scripts/wifi" > /etc/sudoers.d/999-jupiter
  chmod 0440 /etc/sudoers.d/999-jupiter
  chown root:root /etc/sudoers.d/999-jupiter
fi

echo -e "\nAltering sudo tty permissions"
sed -i "s/^Defaults[ \t]*requiretty/#Defaults    requiretty/g" /etc/sudoers
echo "Setting permissions.."
chown -R root:root /usr/lib/jupiter
chmod -R 755 /usr/lib/jupiter
chmod 755 /usr/bin/jupiter
chmod -R 755 /etc/pm/power.d/*jupiter*
if [ ! -d "/var/jupiter" ]; then
  mkdir /var/jupiter
fi
if [ -d "/var/jupiter" ]; then
  chown -R root:jupiter /var/jupiter
  chmod -R 775 /var/jupiter
fi
if [ -e "/usr/lib/jupiter/scripts/jupiter" ]; then
  /usr/lib/jupiter/scripts/jupiter 2>/dev/null || true
fi


%files
%dir  /usr/lib/jupiter/scripts
%attr(755,root,root) /usr/lib/jupiter/scripts
%dir  /usr/lib/jupiter/kernel
%attr(755,root,root) /usr/lib/jupiter/kernel
%dir /etc/pm/power.d
%dir /etc/pm/sleep.d
%attr(755,root,root) /etc/pm/power.d
%attr(755,root,root) /etc/pm/sleep.d
%{_sysconfdir}/xdg/autostart/*.desktop
%{_datadir}/applications/jupiter.desktop
/usr/share/pixmaps/*
/etc/pm/power.d/*jupiter*
/etc/pm/sleep.d/*jupiter*
/lib/udev/rules.d/80-drm.rules
%attr(755,root,root) /usr/bin/jupiter
%dir /var/jupiter
%attr(775,root,jupiter) /var/jupiter

%changelog
* Wed Jul 16 2014 Wei-Lun Chao <bluebat@member.fsf.org> - 0.1.11
- Rebuilt for Fedora
* Sat Dec 15 2012 Andrew Wyatt <andrew@fuduntu.org> - 0.1.11-1
- Bug fixes
* Thu Dec 13 2012 Andrew Wyatt<andrew@fuduntu.org> - 0.1.10-1
- Apply changes contributed by laevar @ Fuduntu Forum
* Thu Dec 06 2012 Andrew Wyatt<andrew@fuduntu.org> - 0.1.9-1
- Transient hints when notifying (Ubuntu only)
- Disable tooltip (does not provide useful info)
* Thu Oct 18 2012 Andrew Wyatt<andrew@fuduntu.org> - 0.1.8-1
- Additional dmidecode dependency removed
* Sun Sep 30 2012 Andrew Wyatt<andrew@fuduntu.org> - 0.1.7-1
- Update to remove dependency on dmidecode
* Fri Sep 14 2012 Andrew Wyatt<andrew@fuduntu.org> - 0.1.6-2
- Restore Jupiter settings on resume from suspend / hibernate
- Reduce power of WIFI adapter when unplugged
* Mon Aug 06 2012 Andrew Wyatt<andrew@fuduntu.org> - 0.1.4-1
- Do not show temp if unavailable
- Merge patches from laevar
* Thu Mar 22 2012 Andrew Wyatt<andrew@fuduntu.org> - 0.1.3-1
- Fix small errors in touchpad status and Bluetooth status outputs
* Mon Mar 12 2012 Andrew Wyatt <andrew@fuduntu.org> - 0.1.2-1
- Add Jorge to Jupiter Project
- Add Jorge's Python Jupiter replacing jupiter.exe
- Fix notification icon to change on power mode change
- Fix Tooltip 
- Fix Performance menu not changing with power change
- Update Touchpad toggle for new touchpad type
- Update scripts to fix a few minor bugs
* Wed Jan 18 2012 Andrew Wyatt <andrew@fuduntu.org> 0.0.53-2
- Fix image path in scripts
* Wed Jan 11 2012 Andrew Wyatt <andrew@fuduntu.org> 0.0.53
- Fix Performance On Demand label
- Click-Pad / Touchpad fix
- Remove camera from sudoers (Raphael Gradenwitz)
- Fix vga out restore (Raphael Gradenwitz)
* Sat Dec 31 2011 Andrew Wyatt <andrew@fuduntu.org> 0.0.52
- Apply zombie patch (Rodrigo Araújo)
* Mon Aug 15 2011 Andrew Wyatt <andrew@fuduntu.org> 0.0.51
- Add Radeon OSS power management support
- Cleanup pixmaps
- Support "ADP" power supply type
* Sun Apr 03 2011 Andrew Wyatt <andrew@fuduntu.org> 0.0.50
- Move %jupiter to sudoers.d
- Update power saving tweaks for newer kernel rev
- Don't restart ACPID if it isn't running
- Remove redundant battery / power mode function
* Sat Jan 29 2011 Andrew Wyatt <andrew.wyatt@fewt.com> 0.0.49
- Fix bug in SATA link power management policy switch
* Sat Jan 22 2011 Andrew Wyatt <andrew.wyatt@fewt.com> 0.0.48
- Move external commands to a function
- Updated WIFI script to use rfkill properly
* Sat Jan 22 2011 Andrew Wyatt <andrew.wyatt@fewt.com> 0.0.47
- Added link to Jupiter Website on About dialog
* Sat Dec 11 2010 Andrew Wyatt <andrew.wyatt@fewt.com> 0.0.46
- Initial support for device power management management
- SATA Link power management support
- USB Autosuspend support
* Mon Nov 18 2010 Andrew Wyatt <andrew.wyatt@fewt.com> 0.0.45
- Default VGA mode if none set is now clone.
- Fix a power mode setting bug on desktops that forces powersave on start-up
