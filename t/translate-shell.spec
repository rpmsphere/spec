Name:           translate-shell
Version:        0.9.6.2
Release:        1
License:        Public Domain
Summary:        Command-line interface and interactive shell for Google Translate
Group:          Text tools
URL:            http://www.soimort.org/translate-shell
Source0:	https://github.com/soimort/translate-shell/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  gawk >= 4.0
Requires:       gawk >= 4.0
Recommends:     fribidi
Recommends:     mplayer
Recommends:     rlwrap
Recommends:     groff
Recommends:     curl

%description
Translate Shell is a command-line interface and interactive shell
for Google Translate. It works just the way you want it to be.

Translate Shell is a complete rewrite of Google Translate CLI Legacy,
which is a tiny script written in 100 lines of AWK code.
Translate Shell is backward compatible with Google Translate CLI Legacy
in its command-line usage; furthermore, it provides more functionality
including verbose translation, Text-to-Speech and interactive mode, etc.

%prep
%setup -q

%build
%make_build

%install
install -pd %{buildroot}%{_bindir}
install -pd %{buildroot}%{_mandir}/man1
install -pm0755 build/trans %{buildroot}%{_bindir}
install -pm0644 man/trans.1 %{buildroot}%{_mandir}/man1

%files
%doc LICENSE README.md WAIVER CONTRIBUTING.md
%{_bindir}/*
%{_mandir}/man1/*

%changelog
* Fri Apr 07 2017 Wei-Lun Chao <bluebat@member.fsf.org> - 0.9.6.2
- Update to 0.9.6.2

* Wed May 18 2016 dglent <dglent> 0.9.4-1.mga5
+ Revision: 1016615
- Version 0.9.4
- Fixes mga#18455
- Version 0.9.2
- Fixes mga#17355
- Fix man file path
- Version 0.9.0.9
- Version 0.9.0.8

* Fri Apr 10 2015 dglent <dglent> 0.8.23-1.mga5
+ Revision: 820038
- New version 0.8.23

* Wed Oct 15 2014 umeabot <umeabot> 0.8.21-2.mga5
+ Revision: 742091
- Second Mageia 5 Mass Rebuild

* Mon Sep 29 2014 dglent <dglent> 0.8.21-1.mga5
+ Revision: 731593
- imported package translate-shell
