Name:       system-monitoring-center
Version:    0.3.0
Release:    1.beta1
Summary:    Provides information about system performance and usage.
License:    GPLv3
URL:        https://github.com/hakandundar34coding/system-monitoring-center
Source0:        system-monitoring-center.0.3.0-beta1.tar.gz
BuildRequires:  python3-setuptools
BuildArch:      noarch
Requires:       bash >= 5.0
Requires:       dmidecode
Requires:       hwdata
Requires:       glx-utils
Requires:       iproute2
Requires:       libwnck3
Requires:       python3 >= 3.7
Requires:       python3-cairo
Requires:       python3-gobject
Requires:       python3-pyopengl
Requires:       systemd
Requires:       util-linux >= 2.33

%description
Provides information about CPU/RAM/Disk/Network/GPU performance, sensors,
processes, users, storage, startup programs, services, environment
variables and system.

%prep
%setup -qn system-monitoring-center-0.3.0-beta1

%build

%install
python3 setup.py install --user --rpm --%{?buildroot}

%post
sudo chown -R $USER /usr/share/system-monitoring-center/src/Main.py

%files
/usr/bin/system-monitoring-center
/usr/share/applications/tr.org.pardus.system-monitoring-center.desktop
/usr/share/icons/hicolor/scalable/actions/system-monitoring-center*
/usr/share/icons/hicolor/scalable/apps/system-monitoring-center*
/usr/share/locale/*/LC_MESSAGES/system-monitoring-center.mo
/usr/share/man/man1/system-monitoring-center.1.gz
/usr/share/polkit-1/actions/tr.org.pardus.pkexec.system-monitoring-center.policy
/usr/share/system-monitoring-center/*

%changelog
* Sun Dec 12 2021 Wei-Lun Chao <bluebat@member.fsf.org> - 0.6
- Rebuilt for Fedora

