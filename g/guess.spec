Name: guess
Summary: A session environment management for GNOME Desktops
Version: 0.3.3
Release: 3.1
Group: Converted/utils
License: see /usr/share/doc/guess/copyright
URL: http://mein-neues-blog.de/guess-03-gnome-sessions/
Source0: http://repository.mein-neues-blog.de:9000/archive/%{name}-%{version}_all.tar.gz
BuildArch: noarch
BuildRequires: desktop-file-utils

%description
Guess is a software for starting and stopping different sets of programs – sessions –
inside a GNOME (GTK) environment. It is able to load files stored in a session folder
on startup and to place/resize/move the windows after they appeared on the desktop.

One can configure different programs with their positions, sizes and start/stop
commands and put them together in different sessions. For easier configuration a wizard
is implemented wich is a great support in figuring out settings and commands.

%prep
%setup -q -c

%build

%install
mkdir -p %{buildroot}
cp -a * %{buildroot}

sed -i 's|python|python2|' %{buildroot}%{_bindir}/%{name}
sed -i 's|/usr/bin/env python$|/usr/bin/python2|' %{buildroot}%{_datadir}/%{name}/*.py
expand %{buildroot}%{_datadir}/%{name}/%{name}.py > %{buildroot}%{_datadir}/%{name}/%{name}.tmp
mv -f %{buildroot}%{_datadir}/%{name}/%{name}.tmp %{buildroot}%{_datadir}/%{name}/%{name}.py

%files
%{_bindir}/*
%{_datadir}/applications/*
%{_datadir}/%{name}
%{_datadir}/pixmaps/*

%changelog
* Wed May 25 2016 Wei-Lun Chao <bluebat@member.fsf.org> - 0.3.3
- Rebuilt for Fedora
