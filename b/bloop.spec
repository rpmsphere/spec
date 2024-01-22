Summary: The BlooP and FlooP languages implemented as a Perl interpreter
Name: bloop
Version: 1a
Release: 1
License: see README
Group: Applications
Source0: http://catb.org/retro/%{name}.shar.gz
Patch0: bloop-1.diff
BuildArch: noarch

%description
The BlooP and FlooP languages from Chapter XIII of Goedel, Escher, Bach:
An Eternal Golden Braid by Douglas R. Hofstadter. BlooP mechanizes
primitive-recursive functions, FlooP mechanizes general-recursive ones.
Thoroughly primitive otherwise. Implemented as a Perl interpreter which
generates Perl and promptly interprets it (how Hofstadterian!),
by John Cowan <cowan@locke.ccil.org>.

%prep
%setup -c -T
cp %{SOURCE0} .
gunzip bloop.shar.gz
sh bloop.shar
patch < %{PATCH0}

%build

%install
install -Dm755 %{name} %{buildroot}%{_bindir}/%{name}
install -d %{buildroot}%{_datadir}/%{name}
install -m644 *.?loop %{buildroot}%{_datadir}/%{name}
install -Dm644 %{name}.1 %{buildroot}%{_mandir}/man1/%{name}.1

%files
%doc README
%{_bindir}/%{name}
%{_datadir}/%{name}
%{_mandir}/man1/%{name}.1*

%changelog
* Sun Dec 24 2023 Wei-Lun Chao <bluebat@member.fsf.org> - 1a
- Rebuilt for Fedora
