Name: gcountdown
Summary: An alarm clock in system tray
Version: 1.0
Release: 8.1
Group: User Interface/Desktops
License: MIT
URL: https://bitbucket.org/fboender/gcountdown/
Source0: https://bitbucket.org/fboender/gcountdown/downloads/%{name}-%{version}.tar.gz
Source1: %{name}.glade
Source2: apert.wav
BuildArch: noarch
Requires: python-pyglet
Requires: pygtk2-libglade
Requires: notify-python

%description
gCountDown is a very simple alarm countdown timer. It sits in your system tray
where you can click it to set an alarm. Once the time runs out, you will be
alerted.

%prep
%setup -q

%build

%install
mkdir -p %{buildroot}%{_bindir} %{buildroot}%{_datadir}/%{name}
install -m755 %{name} %{buildroot}%{_datadir}/%{name}
install -m644 *.png %{SOURCE1} %{SOURCE2} %{buildroot}%{_datadir}/%{name}
ln -s ../share/%{name}/%{name} %{buildroot}%{_bindir}/%{name}

sed -i 's|/usr/bin/env python$|/usr/bin/python2|' %{buildroot}%{_datadir}/%{name}/%{name}

%files
%doc *.txt
%{_bindir}/%{name}
%{_datadir}/%{name}

%changelog
* Mon Oct 21 2013 Wei-Lun Chao <bluebat@member.fsf.org> - 1.0
- Rebuilt for Fedora
