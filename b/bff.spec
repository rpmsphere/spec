%undefine _debugsource_packages

Name:           bff
Version:        1.0.7
Release:        1
License:        BSD-3-Clause
Summary:        Moderately-optimizing brainfuck interpreter
URL:            https://swapped.cc/bff/
Group:          Development/Languages
Source:         https://swapped.cc/bff/files/%{name}-%{version}.tar.gz

%description
Moderately-optimizing brainfuck interpreter.

%prep
%setup -q

%build
make

%install
install -D -m 755 bff %{buildroot}%{_bindir}/%{name}

%files
%{_bindir}/%{name}
%doc README.md

%changelog
* Sun Dec 8 2024 Wei-Lun Chao <bluebat@member.fsf.org> - 1.0.7
- Rebuilt for Fedora
* Sun Sep 18 2011 adam@mizerski.pl
- update to 1.0.4
- use gcc directly instead of make
* Sat Sep 17 2011 jengelh@medozas.de
- Remove redundant tags/sections from specfile
- Use %%_smp_mflags for parallel build
* Fri May 27 2011 cfarrell@novell.com
- license update: BSD-3-Clause
  Spec file should have license with version. Use syntax from
  spdx.org/licenses
* Sun Apr 11 2010 adam@mizerski.pl
- new package
