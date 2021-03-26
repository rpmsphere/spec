Name: portspoof
Summary: Art of Annoyance, Camouflage and Active (Offensive) Defense
Version: 1.0
Release: 5.1
Group: Applications/System
License: GPL
URL: http://portspoof.org/
Source0: %{name}-master.zip
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

%description
The Portspoof program primary goal is to enhance OS security through a set of
techniques that will slow down and keep your attackers out from staying low
profile during their reconnaissance against your system(s). By default the
attacker's reconnaissance phase should be time consuming and easily detectable
by your intrusion detection systems...

Portspoof can be also used as an 'Exploitation Framework Frontend', that turns
your system into responsive and aggressive machine. In practice this means that
your server will be able to exploit your attackers' tools and exploits in an
automated manner. This approach is purely based on Active (Offensive) Defense
concepts.

%prep
%setup -q -n %{name}-master

%build
%configure
make %{?_smp_mflags}

%install
%make_install

%files
%doc README README.md NEWS COPYING COPYRIGHT.GPL FAQ DOCS ChangeLog AUTHORS
%{_bindir}/*
%{_sysconfdir}/*

%changelog
* Mon Oct 21 2013 Wei-Lun Chao <bluebat@member.fsf.org> - 1.0
- Rebuild for Fedora
