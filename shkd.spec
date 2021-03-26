%global debug_package %{nil}

Name:		shkd
Version:	0.1
Release:	3.1
Summary:	Simple HotKey Daemon
License:	BSD
URL:		https://github.com/baskerville/%{name}
Source0:	%{name}-master.zip

%description
shkd is a simple hotkey daemon for the Linux console.

%prep
%setup -q -n %{name}-master
sed -i 's|-lm|-lm -Wl,--allow-multiple-definition|' Makefile

%build
%make_build

%install
%make_install PREFIX="%{_prefix}"

%files
%doc README.md
%license LICENSE
%{_bindir}/%{name}
%{_mandir}/man*/%{name}.1*
%{_sysconfdir}/shkdrc
%{_sysconfdir}/udev/rules.d/98-shk-local.rules
%{_unitdir}/shkd@.service

%changelog
* Thu Dec 21 2017 Wei-Lun Chao <bluebat@member.fsf.org> - 0.1
- Rebuild for Fedora
