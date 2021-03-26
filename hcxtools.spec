%global debug_package %{nil}

Name: hcxtools
Summary: Small set of tools convert packets from captures
Version: 5.3.0
Release: 1
Group: Network
License: MIT
URL: https://github.com/ZerBea/hcxtools
Source0: https://github.com/ZerBea/hcxtools/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires: curl-devel
BuildRequires: openssl-devel

%description
This package contains a small set of tools convert packets from captures (h =
hash, c = capture, convert and calculate candidates, x = different hashtypes)
for the use with latest hashcat or John the Ripper. The tools are 100%%
compatible to hashcat and John the Ripper and recommended by hashcat.

Support for hashcat hash-modes: 2500, 2501, 4800, 5500, 12000, 16100,
16800, 16801

Support for John the Ripper hash-modes: WPAPSK-PMK, PBKDF2-HMAC-SHA1, chap,
netntlm, tacacs-plus

%prep
%setup -q

%build
make %{?_smp_mflags} PREFIX=/usr

%install
make install PREFIX=/usr DESTDIR=%{buildroot}
install -d %{buildroot}%{_mandir}/man1/
install -m644 manpages/* %{buildroot}%{_mandir}/man1/

%files
%doc changelog README.md license.txt
%{_bindir}/*
%{_mandir}/man1/*

%changelog
* Thu Dec 12 2019 Wei-Lun Chao <bluebat@member.fsf.org> - 5.3.0
- Rebuild for Fedora

