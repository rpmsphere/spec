%global _name Espruino

Summary: The Espruino JavaScript interpreter
Name: espruino
Version: 1.99git
Release: 3.1
License: MPL 2.0
Group: Development/Language
URL: https://github.com/espruino/Espruino
Source: %{_name}-master.zip
BuildRequires: git python2

%description
Espruino is a JavaScript interpreter for microcontrollers. It is designed for
devices with as little as 128kB Flash and 8kB RAM.
Please support Espruino by ordering one of our official boards or donating.

%prep
%setup -q -n %{_name}-master
sed -i 's|if USE_64BIT|ifdef USE_64BIT|' src/jsnative.c

%build
RELEASE=1 make

%install
install -Dm755 %{name} %{buildroot}%{_bindir}/%{name}

%files
%doc *.md LICENSE ChangeLog
%{_bindir}/%{name}

%changelog
* Fri Aug 31 2018 Wei-Lun Chao <bluebat@member.fsf.org> - 1.99git
- Rebuild for Fedora
