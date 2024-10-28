Name:                   wordsearch
Summary:                Tool to create wordsearch puzzles
Version:                2.1
Release:                1
Group:                  Amusements/Games/Logic
License:                BSD-2
URL:                    https://github.com/jensenpat/wordsearch
Source:                 %{name}-%{version}.tar.gz
BuildArch:              noarch

%description
A classic word search game that you can play in your terminal.

%prep
%setup -q

%install
%{__rm} -rf $RPM_BUILD_ROOT
install -Dm755 %{name} $RPM_BUILD_ROOT/%{_bindir}/%{name}
install -Dm644 man/%{name}.6 $RPM_BUILD_ROOT/%{_mandir}/man6/%{name}.6
install -d $RPM_BUILD_ROOT/%{_datadir}/%{name}
install -m644 puzzles/* $RPM_BUILD_ROOT/%{_datadir}/%{name}

%files
%{_bindir}/%{name}
%{_datadir}/%{name}
%{_mandir}/man6/%{name}.6*
%doc README.md LICENSE

%changelog
* Sun Mar 20 2022 Wei-Lun Chao <bluebat@member.fsf.org> - 2.1
- Rebuilt for Fedora
