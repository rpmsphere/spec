Summary:	Tool ala dig from BIND
Name:		drill
Version:	0.9.2
Release:	10
License:	GPL
Group:		Networking/Other
URL:		http://www.nlnetlabs.nl/dnssec/drill.html
Source0:	http://www.nlnetlabs.nl/downloads/drill/%{name}-%{version}.tar.bz2
BuildRequires:	compat-openssl10-devel

%description
Drill is a tool ala dig from BIND. It was designed with DNSSEC in
mind and should be a useful debugging/query tool for DNSSEC. 

%prep
%setup -q -n %{name}
chmod 644 ChangeLog README

%build
%configure
%make_build CFLAGS="%{optflags} -fPIC"

%install
rm -rf %{buildroot}
install -d %{buildroot}%{_bindir}
install -d %{buildroot}%{_mandir}/man1
install -m0755 drill %{buildroot}%{_bindir}/
install -m0755 doc/drill.1 %{buildroot}%{_mandir}/man1/

%clean
rm -rf %{buildroot}

%files
%doc ChangeLog README 
%{_bindir}/drill
%{_mandir}/man1/drill.1*

%changelog
* Tue May 14 2019 Wei-Lun Chao <bluebat@member.fsf.org> - 0.9.2
- Rebuild for Fedora
* Fri Feb 17 2017 Andrey Bondrov <andrey.bondrov@rosalab.ru> 0.9.2-10
- (7d6b94b) MassBuild#1257: Increase release tag
