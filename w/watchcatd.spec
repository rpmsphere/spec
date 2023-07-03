%undefine _debugsource_packages

Name: watchcatd
Summary: Process monitoring daemon
Version: 1.3.1
Release: 1
Group: admin
License: Free Software
URL: https://oss.digirati.com.br/watchcatd/
Source0: %{name}-%{version}.tar.gz
BuildRequires: libevent-devel

%description
A bug or malicious attacks to machine can lock up a process, leading to a
deadlock or an unexpected condition. For example: an Apache httpd with
mod_(php|perl|lua|your_preferred_script_language) running a bad script. When
the monitored process locks up, the watchcat helps killing him. It is the best
thing to do.

%prep
%setup -q
sed -i -e 's|ev_flags|ev_evcallback.evcb_flags|' -e 's|ev_arg|ev_evcallback.evcb_arg|' slave.c

%build
make %{?_smp_mflags} PREFIX=/usr

%install
#make install DESTDIR=%{buildroot} PREFIX=/usr
install -Dm0755 catmaster %{buildroot}%{_bindir}/catmaster
install -Dm0755 catslave %{buildroot}%{_bindir}/catslave
install -Dm0600 watchcatd.prod.conf %{buildroot}/etc/watchcatd.conf
install -Dm0644 watchcatd.8 %{buildroot}%{_mandir}/man8/watchcatd.8
install -Dm0644 watchcatd.conf.5 %{buildroot}%{_mandir}/man5/watchcatd.conf.5

%files
%doc ChangeLog COPYRIGHT TODO
#%{_sysconfdir}/init.d/%{name}
%{_sysconfdir}/%{name}.conf
%{_bindir}/*
#%{_libdir}/%{name}
%{_mandir}/man5/%{name}.conf.5*
%{_mandir}/man8/%{name}.8*

%changelog
* Sun Dec 12 2021 Wei-Lun Chao <bluebat@member.fsf.org> - 1.3.1
- Rebuilt for Fedora
