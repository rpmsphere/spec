Summary:	Nyancat rendered in your terminal
Name:		nyancat
Version:	1.5.2
Release:	1
Group:		Toys
License:	NCSA
URL:		https://github.com/klange/nyancat
Source0:	https://github.com/klange/nyancat/archive/%{name}-%{version}.tar.gz
BuildRequires:  python2-devel

%description
Nyancat rendered in your terminal.

%files
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1*
%{_unitdir}/%{name}@.service
%{_unitdir}/%{name}.socket

%prep
%setup -q

%build
%make_build \
	LFLAGS="%{ldflags}" \
	CPPFLAGS="%{optflags}" \
	CC=%{__cc}

%install
mkdir -p %{buildroot}/%{_bindir}
mkdir -p %{buildroot}/%{_mandir}/man1
mkdir -p %{buildroot}/%{_unitdir}
install -m 0755 src/%{name} %{buildroot}/%{_bindir}/%{name}
install -m 0644 nyancat.1 %{buildroot}/%{_mandir}/man1
install -m 0644 systemd/*.{service,socket} %{buildroot}/%{_unitdir}

%changelog
* Mon Dec 10 2018 Wei-Lun Chao <bluebat@member.fsf.org> - 1.5.2
- Rebuilt for Fedora
* Fri Feb 17 2017 Andrey Bondrov <andrey.bondrov@rosalab.ru> 1.5.1-3
- (c2a5c5e) MassBuild#1257: Increase release tag
