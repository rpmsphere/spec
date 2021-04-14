Name:			wordsearch
Summary:		Tool to create wordsearch puzzles
Version:		1.4.1
Release:		6.1
Group:			Amusements/Games/Logic
License:		GPL
URL:			http://decafbad.net/projects/wordsearch
Source:			%{name}-%{version}.tar.gz
BuildRoot:		%{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildArch:		noarch
Requires:		perl

%description
Tool to create wordsearch puzzles.

%prep
%setup -q

%install
%{__rm} -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/%{_bindir}
install -m 755 wordsearch.pl $RPM_BUILD_ROOT/%{_bindir}/
install -m 755 numbergenerator.pl $RPM_BUILD_ROOT/%{_bindir}/

%files
%defattr(-,root,root)
%{_bindir}/wordsearch.pl
%{_bindir}/numbergenerator.pl
%doc README COPYING CHANGELOG

%clean
%{__rm} -rf $RPM_BUILD_ROOT

%changelog
* Sun Aug 05 2012 Wei-Lun Chao <bluebat@member.fsf.org> - 1.4.1
- Rebuilt for Fedora
