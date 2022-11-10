Name:           birq
Version:        1.6.1
Release:        1
Summary:        Balance IRQ 
Group:          System Environment/Base
License:        New BSD licence
URL:            https://src.libcode.org/pkun/birq
Source0:        https://src.libcode.org/pkun/birq/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
#Source1:        birq.init
Source2:        birq.sysconfig
Source3:        birq.service
BuildRequires:  autoconf

%description
BIRQ stands for Balance IRQs. This is software to balance interrupts between CPUs on Linux while high load.
Copyright (c) 2013 Serj Kalichev <serj.kalichev@gmail.com>

%prep
%setup -q
chmod 755 configure

%build
aclocal
autoconf
autoheader
automake --add-missing
%configure
CFLAGS="%{optflags}" make %{?_smp_mflags}

%install
install -D -p -m 0755 %{name} %{buildroot}%{_sbindir}/%{name}
mkdir -p %{buildroot}%{_sysconfdir}
install examples/birq.conf $RPM_BUILD_ROOT%{_sysconfdir}/birq.conf
install -D -p -m 0644 %{SOURCE3} %{buildroot}%{_unitdir}/birq.service
install -D -p -m 0644 %{SOURCE2} %{buildroot}%{_sysconfdir}/sysconfig/%{name}

%files
%doc README LICENCE doc/birq.md
%{_sbindir}/%{name}
%{_sysconfdir}/sysconfig/%{name}
%config(noreplace) %attr(644,root,root) %{_sysconfdir}/birq.conf
%{_unitdir}/%{name}.service

%post
%systemd_post birq.service

%preun
%systemd_preun birq.service

%postun
%systemd_postun_with_restart birq.service

%changelog
* Sun Oct 23 2022 Wei-Lun Chao <bluebat@member.fsf.org> - 1.6.1
- Rebuilt for Fedora
* Mon Jun 29 2015 Roman Dmitriev <rnd@rajven.ru> - 1.2.0
- update to 1.2.0
* Wed Jun 24 2015 Roman Dmitriev <rnd@rajven.ru> - 1.1.3
- Initial packaging.
