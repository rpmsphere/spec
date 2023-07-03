%undefine _debugsource_packages

Name: xswarm
Summary: An X windows animated wasp and bee swarm demo
Version: 2.3
Release: 4.1
Group: Amusements/Graphics
License: GPL
URL: https://hpux.connect.org.uk/hppd/hpux/X11/Demos/%{name}-%{version}/
Source0: https://hpux.connect.org.uk/ftp/hpux/X11/Demos/%{name}-%{version}/%{name}-%{version}-src-11.00.tar.gz
BuildRequires: imake
BuildRequires: libX11-devel
BuildRequires: libXext-devel

%description
A group of bees swarm towards a single wasp (both are represented by straight
lines), leading to interesting movement patterns. There are multitude of
command-line options to control the demo, including use of the root window,
mouse control of the wasp, the speed and acceleration constants and the
background colour.

%prep
%setup -q

%build
xmkmf -a
make

%install
install -Dm755 %{name} %{buildroot}%{_bindir}/%{name}
install -Dm644 %{name}.6 %{buildroot}%{_mandir}/man6/%{name}.6

%files
%doc README*
%{_bindir}/*
%{_mandir}/man6/%{name}.6*

%changelog
* Tue Jan 02 2018 Wei-Lun Chao <bluebat@member.fsf.org> - 2.3
- Rebuilt for Fedora
