Name: secpwgen
Version: 1.3
Release: 3.1
License: 1
Group: Productivity/Security
BuildRequires: openssl-devel
URL: https://www.core-dump.com.hr/?q=node/28
Source: https://www.core-dump.com.hr/software/secpwgen-1.3.tar.gz
Patch: secpwgen-1.3_build_config.patch
Summary: Secure Password Generator

%description
A utility for generating secure passphrases. Implements several methods for
passphrase generation, including the Diceware method with 8192 word dictionary
compiled in the executable.

Authors:
--------
    Zeljko Vrba <zvrba@globalnet.hr>

%prep
%setup -q
%patch

%build
%{__make} -f Makefile.proto OPTFLAGS="%{optflags} -DDISABLE_MLOCKALL"

%install
%{__rm} -rf $RPM_BUILD_ROOT
%{__install} -D -m 0755 secpwgen   $RPM_BUILD_ROOT%{_bindir}/secpwgen
%{__install} -D -m 0644 secpwgen.1 $RPM_BUILD_ROOT%{_mandir}/man1/secpwgen.1

%clean
%{__rm} -rf $RPM_BUILD_ROOT

%files
%{_bindir}/secpwgen
%{_mandir}/man1/secpwgen.1*
%doc ChangeLog README

%changelog
* Tue Aug 21 2012 Wei-Lun Chao <bluebat@member.fsf.org> - 1.3
- Rebuilt for Fedora
