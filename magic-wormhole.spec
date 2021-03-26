Name: magic-wormhole
Summary: Securely and simply transfer data between computers
Version: 0.10.5
License: MIT
Release: 1.1
Group: Network
URL: https://github.com/warner/magic-wormhole
Source0: https://github.com/warner/magic-wormhole/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildArch: noarch
BuildRequires: python3-devel
#Requires: python3-autobahn
#Requires: python3-click,
#Requires: python3-hkdf,
#Requires: python3-humanize,
#Requires: python3-nacl,
#Requires: python3-six,
#Requires: python3-spake2,
#Requires: python3-tqdm,
#Requires: python3-twisted,
#Requires: python3:any
Provides: python3-magic-wormhole,
Provides: python3-wormhole,
Provides: wormhole

%description
Magic Wormhole provides a command-line tool and Python library named
"wormhole" which makes it possible to very easily transfer short
pieces of text or arbitrary-sized files or directories from one
computer to another.

The two endpoints are identified by using identical "wormhole codes":
in general, the sending machine generates and displays the code,
which must then be typed into the receiving machine.  The codes are
short and human-pronounceable, using a phonetically-distinct
wordlist.  The receiving side offers tab-completion on the codewords,
so usually only a few characters must be typed.  Wormhole codes are
single-use and do not need to be memorized.

%prep
%setup -q

%build
python3 setup.py build

%install
python3 setup.py install --prefix=/usr --root=%{buildroot}
install -Dm644 docs/wormhole.1 %{buildroot}%{_mandir}/man1/wormhole.1
install -Dm644 docs/wormhole-server.8 %{buildroot}%{_mandir}/man8/wormhole-server.8

%files
%doc *.md LICENSE
%{_bindir}/wormhole
%{_bindir}/wormhole-server
%{python3_sitelib}/*
%{_mandir}/man?/*

%changelog
* Sun Mar 04 2018 Wei-Lun Chao <bluebat@member.fsf.org> - 0.10.5
- Rebuild for Fedora
