%undefine _debugsource_packages

Name: pipexec
Summary: Create a directed graph of processes and pipes
Version: 2.5.5
Release: 3.1
License: GPLv2
Group: utils
URL: https://github.com/flonatel/pipexec
Source0: https://github.com/flonatel/pipexec/releases/download/%{version}/%{name}-%{version}.tar.xz

%description
pipexec creates an arbitrary network (directed graph) of processes and
pipes in between - even cycles are possible.
It overcomes the short comings of shells that are typically only able
to create non cyclic trees.

pipexec also monitors all its child processes and is able to restart
the whole network of processes and pipes if one crashes.
Therefore pipexec can be used in SYSV-init or systemd configuration to
run a network of processes.

The package also contains two tools 'ptee' and 'peet' which are the piped
version of the 'tee' and 'eet' (reverse tee) commands.

%prep
%setup -q

%build
./configure --prefix=/usr
sed -i 's|-Wall|-Wall -fPIE|' Makefile
make

%install
make install DESTDIR=%{buildroot}

%files
%doc LICENSE README.md
%{_bindir}/*

%changelog
* Fri Oct 13 2017 Wei-Lun Chao <bluebat@member.fsf.org> - 2.5.5
- Rebuilt for Fedora
