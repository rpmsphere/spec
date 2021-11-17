Name:		tksimsys
Version:	3.4
Release:	1
Summary:	Simulation for Biocybernetic Systems
License:	GPLv2+
URL:		https://github.com/bluebat/tksimsys
Group:		Education/Science
Source0:	%{name}-%{version}.tar.gz
BuildArch:	noarch
Requires:	tk

%description
Tksimsys was written to offer a convenient way to build and simulate
biocybernetic systems. From the pull-down menu you can choose an element,
give it a value and an order. There are different input functions, conductors,
dividers, connectors, characteristics and output channels. The value of many
variables could be changed interactively. After start it shows the
output curves, which could be stopped on the way or directed to standard output.
You could also load, save, shift and print the models designed.

%prep
%setup -q

%build
%__make

%install
%__make DESTDIR=%{buildroot} install

%files
%doc README LICENSE ChangeLog
%{_bindir}/%{name}
%{_datadir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_mandir}/man1/%{name}.1.*

%changelog
* Thu Dec 30 2008 Wei-Lun Chao <bluebat@member.fsf.org> 3.4-1
- Initial package
