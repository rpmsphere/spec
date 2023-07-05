Name:           cec
Version:        8
Release:        4.1
License:        GPL
BuildRequires:  make gcc
Group:          System/Base
Source:         https://noc.panteion.gr/source/aoetools/cec-8.tgz
Summary:        Coraid Ethernet Console

%description
The Coraid Ethernet Console (cec) is a lightweight protocol for connecting two
endpoints using raw ethernet frames. The communication is not secure.

%prep
%setup -q

%build
%__make %{?jobs:-j%{jobs}} CC="%__cc -Wl,--allow-multiple-definition"

%install
rm -rf "$RPM_BUILD_ROOT"
%__install -D -m0755 cec "$RPM_BUILD_ROOT%{_sbindir}/cec"
%__install -D -m0644 cec.8 "$RPM_BUILD_ROOT%{_mandir}/man8/cec.8"

%clean
rm -rf "$RPM_BUILD_ROOT"

%files
%doc HACKING LICENSE NEWS README
%{_sbindir}/cec
%{_mandir}/man8/cec.8.gz

%changelog
* Tue Oct 25 2011 Wei-Lun Chao <bluebat@member.fsf.org> - 8
- Rebuilt for Fedora

* Sat May 5 2008 George Pantazis <ggpanta@gmail.com>
- initial build
