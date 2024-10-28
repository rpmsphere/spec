Name:                   kenny
Summary:                A kennyspeak translator
Version:                1.7
Release:                3.1
Group:                  Amusements/Toys/Other
License:                artistic
URL:                    https://www.cgarbs.de/kenny.en.html
Source:                 %{name}-%{version}.tar.gz
BuildArch:              noarch

%description
Converts to and from kennyspeak.

%prep
%setup -q

%install
mkdir -p $RPM_BUILD_ROOT%{_bindir}
mkdir -p $RPM_BUILD_ROOT%{_mandir}/man1
install -m755 kenny.pl $RPM_BUILD_ROOT%{_bindir}
install -m444 kenny.pl.1 $RPM_BUILD_ROOT%{_mandir}/man1

%files
%{_bindir}/*
%{_mandir}/*/*
%doc README kenny.html copyright changelog.Debian.gz README.html

%changelog
* Fri Jul 27 2012 Wei-Lun Chao <bluebat@member.fsf.org> - 1.7
- Rebuilt for Fedora
