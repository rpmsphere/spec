Summary:        Wake-on-LAN magic packet sender
Name:           wakeonlan
Version:        0.42
Release:        1
Source:         https://github.com/jpoliv/wakeonlan/archive/refs/tags/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
License:        Artistic
URL:            https://github.com/jpoliv/wakeonlan
Group:          Networking/Remote access
BuildArch:      noarch

%description
Wakeonlan is a Perl script that sends 'magic packets' to
wake-on-LAN enabled ethernet adapters and motherboards, in
order to switch on remote computers.

%prep
%setup -q

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
rm -rf %{buildroot}
install -Dm755 wakeonlan %{buildroot}%{_bindir}/%{name}
install -Dm644 blib/man1/%{name}.1 %{buildroot}%{_mandir}/man1/%{name}.1

%files
%doc examples Changes README.md
%{_bindir}/wakeonlan
%{_mandir}/man1/%{name}.1*

%changelog
* Sun Jun 26 2022 Wei-Lun Chao <bluebat@member.fsf.org> - 0.42
- Rebuilt for Fedora
* Tue Dec 11 2012 Alex Burmashev <alex.burmashev@rosalab.ru> 0.41-3
+ Revision: d67eac9
- merging with rosa2012.1 of project wakeonlan
