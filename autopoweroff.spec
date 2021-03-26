Name: autopoweroff
Summary: Automatically power off a computer if not used
Version: 3.0.0
Release: 1%{?dist}
Group: System Environment/Daemons
License: GPL
URL: https://github.com/deragon/autopoweroff
Source0: http://downloads.sourceforge.net/%{name}/%{name}-%{version}.tar.gz
BuildArch: noarch
BuildRequires:  desktop-file-utils
#Requires: /usr/bin/python
#Requires: SysVinit
#Requires: iputils
#Requires: python

%description
GUI configurator available from menus System/Administration/Autopoweroff

Autopoweroff is a Python script that is started at boot time, and which
function is to shutdown the computer at a specific time, but only if
some conditions are met.

The computer will shutdown if all the above conditions are met:

  1. Any hosts that the computer is dependent on is not answering ping
     anymore.

  2. There is no more keyboard and mouse activity on the computer.

  3. The user has not disabled Autopoweroff.

One good use of Autopoweroff is for home use, on a firewall/router
server. You can setup Autopoweroff to shutdown the server every evening
at say, 22:00. However, your server might serve other computers in your
home. Autopoweroff will shutdown the server after 22:00 only when no
other computer on the network is responding to ping.  For example, if at
22:43 you are still working on your thin client in the living room, the
server in your baseman will remain up. As soon as you shutdown the
workstation, the server will wait for some time (configurable) and
then go down.

By setting the BIOS properly, the server can come up by itself every
morning.  Autopoweroff has nothing to do with this process.  But with
this setting, your home server does not need to run 24/7; you can save
electricity and noise without the hassle of having to shut down and
start the server manually.

Contact:

  Project website:   https://github.com/deragon/autopoweroff
  Business website:  http://www.deragon.biz
  Email:             hans@deragon.biz

%prep
%setup -q

%build
%configure
make %{?_smp_mflags}

%install
make install DESTDIR=%{buildroot}

postinstall scriptlet (using /bin/sh):
# Upgrading or creating currently installed configuration file.
/usr/sbin/autopoweroff-upgrade


FEDORACOMPATIBLE=0
SUSECOMPATIBLE=0

if [ -f /etc/fedora-release ]; then
  FEDORACOMPATIBLE=1
  echo -e "\nFedora system detected."
elif [ -f /etc/redhat-release ]; then
  FEDORACOMPATIBLE=1
  echo -e "\nRed Hat system detected."
elif [ -f /etc/mandrake-release ]; then
  FEDORACOMPATIBLE=1
  echo -e "\nMandrake system detected."
elif [ -f /etc/SuSE-release ]; then
  SUSECOMPATIBLE=1
  echo -e "\nSuSE system detected."
fi

# Setting up the proper init file for Red Hat/Fedora.
INITDST="/etc/init.d/autopoweroff"

# When reinstalling the same version with `rpm --force`, the symlink will exist.
# We therefore need to delete and the recreate it.
rm -f ${INITDST}

if [ -f /etc/rc.d/init.d/functions ]; then
  ln -s \
    /usr/share/autopoweroff/init.d/autopoweroff.redhat ${INITDST}
elif [ -f /etc/rc.status ]; then
  ln -s \
    /usr/share/autopoweroff/init.d/autopoweroff.rc-status ${INITDST}
elif [ -f /lib/lsb/init-functions ]; then
  ln -s \
    /usr/share/autopoweroff/init.d/autopoweroff.lsb ${INITDST}
else
  echo -e "ERROR:  Could not setup bootstrap scripts.\n"\
          "       autopoweroff will not be started automatically."
fi

chmod +x ${INITDST}

if ((${FEDORACOMPATIBLE} || ${SUSECOMPATIBLE})); then

  # Setting up run level 3 and 5 to startup autopoweroff.
  # See /etc/inittab for explanation of these run levels.
  chkconfig --add autopoweroff
  chkconfig --level 35 autopoweroff on
cat <<EOF

Autopoweroff has been added to the boot process.  It will start
automatically next time this machine is rebooted.

WARNING:  Since Autopoweroff will start next time this machine is
          rebooted, it has to be configured now.

          You can configure Autopoweroff by clicking on
          "Application/System Tools/Autopoweroff" on the desktop, or run
          in a terminal the command "autopoweroff".

          Another alternative is to edit
          /etc/autopoweroff/autopoweroff.conf directly.  This
          %configuration file contains the instructions on how to setup each
          %section.


To start Autopoweroff now instead of waiting for the next reboot, run:

  ${INITDST} start

EOF
fi

if [ -x /usr/bin/consolehelper ]; then
  # Deleting autopoweroff binary if one already exist, just in case.
  rm -f /usr/bin/autopoweroff >/dev/null 2>&1
  ln -s consolehelper /usr/bin/autopoweroff 
fi
preuninstall scriptlet (using /bin/sh):
if [ -f /etc/fedora-release ]; then
  FEDORACOMPATIBLE=1
  echo -e "Fedora system detected."
elif [ -f /etc/redhat-release ]; then
  FEDORACOMPATIBLE=1
  echo -e "Red Hat system detected."
elif [ -f /etc/mandrake-release ]; then
  FEDORACOMPATIBLE=1
  echo -e "Mandrake system detected."
fi

if ((${FEDORACOMPATIBLE})); then
  chkconfig --del autopoweroff
  echo "Removed Autopoweroff from boot process."
fi

/etc/init.d/autopoweroff stop
echo "Autopoweroff stopped."

rm -f /etc/init.d/autopoewroff

# Since we do not include /etc/autopoweroff.conf in the %files section,
# we most manually perform the operation that rpm -e would otherwise
# perform.
mv /etc/autopoweroff/autopoweroff.conf \
   /etc/autopoweroff/autopoweroff.conf.rpmsave
echo "warning: /etc/autopoweroff.conf saved as /etc/autopoweroff.conf.rpmsave"
postuninstall scriptlet (using /bin/sh):

# Deleting symlink to consolehelper if there is one.
rm -rf /usr/bin/autopoweroff >dev/null 2>&1
%files
%{_sysconfdir}/%{name}
%{_sysconfdir}/pam.d/%{name}
%{_sysconfdir}/security/console.apps/%{name}
%{_sbindir}/%{name}-gui
%{_sbindir}/%{name}-upgrade
%{_sbindir}/%{name}d
%{_desktopdir}
%{_datadir}/%{name}
%{_datadir}/doc

%changelog
* Thu Apr 27 2017 root <root@localhost.localdomain>
- Regenerated spec using rpm2spec
* Wed Nov 12 2003 Hans Deragon <hans@deragon.biz>
- See https://github.com/deragon/autopoweroff#change-history for full history
of Autopoweroff.

