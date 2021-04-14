Name:			kenny
Summary:		A kennyspeak translator
Version:		1.7
Release:		3.1
Group:			Amusements/Toys/Other
License:		artistic
URL:			http://www.cgarbs.de/kenny.en.html
Source:			%{name}-%{version}.tar.gz
BuildRoot:		%{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildArch:		noarch

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
%defattr(-,root,root,0755)
%{_bindir}/*
%{_mandir}/*/*
%doc README kenny.html copyright changelog.Debian.gz README.html

%clean
%{__rm} -rf $RPM_BUILD_ROOT

%changelog
* Fri Jul 27 2012 Wei-Lun Chao <bluebat@member.fsf.org> - 1.7
- Rebuilt for Fedora
