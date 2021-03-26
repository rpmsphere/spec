Name:		thintron
Version:	2015.01
Release:	1%{?dist}
Summary:	Thin Suite for Client, Kiosk and Host
License:	MIT
Group:		Applications/Internet
Source0:	%{name}-%{version}.tar.gz
BuildArch:	noarch
Requires:	gtkdialog

%description
Thintron is a suite for thin client, thin kiosk and thin host.

%prep
%setup -q

%build
make

%install
make DESTDIR=%{buildroot} install

%files
%doc README.md ChangeLog
%{_bindir}/%{name}
%{_bindir}/%{name}-session
%{_datadir}/%{name}
%{_datadir}/locale/*/LC_MESSAGES/%{name}.mo
%{_datadir}/xsessions/%{name}.desktop

%changelog
* Tue Jan 27 2015 Wei-Lun Chao <bluebat@member.fsf.org> - 2015.01
- Inital package
