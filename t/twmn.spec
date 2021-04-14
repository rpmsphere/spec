Name:     twmn
Version:  1.2git
Release:  3.1
Summary:  A notification system for tiling window managers
Group:    User Interface/X
License:  LGPLv3
URL:      https://github.com/sboli/twmn
Source0:  %{name}-master.zip
BuildRequires: boost-devel
BuildRequires: qt5-devel
Provides: desktop-notification-daemon

%description
twmnc: command line tool to send notifications to twmnd. You can also use
notify-send for a similar purpose, but twmnc is more powerful.

twmnd: daemon listening to notification requests and showing them one after
another. Configure it at ~/.config/twmn/twmn.conf.

Notifications are shown in a one-line bar called the notification slide.
They can be navigated through and activated with shortcuts.

%prep
%setup -q -n %{name}-master

%build
qmake-qt5
sed -i 's|-Werror|-Wno-deprecated-declarations|' *.pro */*.pro
make %{?_smp_mflags}

%install
sed -i 's|/usr/local|%{buildroot}/usr|' */Makefile
make install DESTDIR=%{buildroot}

%files
%doc TODO LICENSE README.md
%{_bindir}/%{name}*

%changelog
* Thu Jul 19 2018 Wei-Lun Chao <bluebat@member.fsf.org> - 1.2git
- Rebuilt for Fedora
