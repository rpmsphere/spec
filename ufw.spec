Name:           ufw
Version:        0.33 
Release:        9.1
Summary:        Uncomplicated Firewall
License:        GPL-3.0
Group:          Productivity/Networking/Security
URL:            http://launchpad.net/%{name}
Source0:        %{name}-%{version}.tar.bz2
Source1:        ufw-init
Source2:        ufw.service
BuildArch:      noarch
BuildRequires:  iptables
BuildRequires:  python-devel
BuildRequires:  systemd

%description
The Uncomplicated Firewall is a front-end for netfilter, which
aims to make it easier for people unfamiliar with firewall concepts.
Ufw provides a framework for managing netfilter as well as 
manipulating the firewall.

%prep
%setup -q

%build
python setup.py build

%install
rm -rf %{buildroot}
python setup.py install --prefix=/usr --root %{buildroot}
mkdir -p $RPM_BUILD_ROOT/etc/init.d/
install -m 755 $RPM_SOURCE_DIR/ufw-init $RPM_BUILD_ROOT/etc/init.d/ufw
ln -s /etc/init.d/ufw $RPM_BUILD_ROOT/usr/sbin/rcufw
ln -s /usr/share/man/man8/ufw.8.gz $RPM_BUILD_ROOT/usr/share/man/man8/rcufw.8.gz
mkdir -p $RPM_BUILD_ROOT/usr/bin/
ln -s /usr/sbin/ufw $RPM_BUILD_ROOT/usr/bin/ufw
mkdir -p $RPM_BUILD_ROOT/usr/lib/systemd/
mkdir -p $RPM_BUILD_ROOT/usr/lib/systemd/system
install -m 644 $RPM_SOURCE_DIR/ufw.service $RPM_BUILD_ROOT/usr/lib/systemd/system/ufw.service
sed -i 's| /bin/python| python|' %{buildroot}%{_sbindir}/ufw

%files
%defattr(-,root,root)
/lib/ufw/ufw-init
/lib/ufw/ufw-init-functions
/lib/ufw/user.rules
/lib/ufw/user6.rules
/usr/lib/python%python_version/site-packages/ufw-%{version}-py%python_version.egg-info
/usr/sbin/ufw
/usr/sbin/rcufw
/usr/bin/ufw
/usr/share/man/man8/ufw-framework.8.gz
/usr/share/man/man8/ufw.8.gz
/usr/share/man/man8/rcufw.8.gz
%config/etc/init.d/ufw
%config/etc/ufw
%config/etc/ufw/applications.d
%config/etc/default/ufw
/usr/lib/systemd/system/ufw.service
/lib/ufw
/usr/lib/python%python_version/site-packages/ufw
/usr/share/ufw
/usr/share/ufw/iptables
/usr/share/ufw/messages/*.mo

%changelog
* Mon Oct 14 2013 Wei-Lun Chao <bluebat@member.fsf.org> - 0.33
- Rebuild for Fedora
* Fri Nov  9 2012 johann.luce@wanadoo.fr
-fix problem systemd move in /usr
  fix various warning OBS
* Tue Oct 16 2012 johann.luce@wanadoo.fr
-fix systemd tag to start automaticaly ufw
* Mon Sep 17 2012 johann.luce@wanadoo.fr
- Update in 0.33
  fix dependance python-base
  fix lang zh_TW
* Wed Apr  4 2012 johann.luce@wanadoo.fr
- Updated in 0.31.1
  fix various warning OBS
  add script init file for systemd
* Tue Oct 11 2011 johann.luce@wanadoo.fr
  bug on restart in init file-
* Mon Oct 10 2011 johann.luce@wanadoo.fr
  add opensuse init script -
* Thu Oct  6 2011 johann.luce@wanadoo.fr
  add %%lang tag in spec file-
* Wed Oct  5 2011 johann.luce@wanadoo.fr
  OpenSuSE Factory-
* Wed Oct  5 2011 johann.luce@wanadoo.fr
  Delete patch commit.py-
* Wed Oct  5 2011 johann.luce@wanadoo.fr
  Changes in spec file for lang-
* Tue Oct  4 2011 johann.luce@wanadoo.fr
  Changes in spec file for python version -
* Tue Oct  4 2011 johann.luce@wanadoo.fr
  Changes on buildarch -
* Tue Oct  4 2011 johann.luce@wanadoo.fr
  Errors in spec file -
* Tue Oct  4 2011 johann.luce@wanadoo.fr
  first on OpenSUSE 11.4 -
