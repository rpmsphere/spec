Summary:	Better than cat
Name:		dog
Version:	1.7
Release:	17.1
Group:		Text tools
License:	GPLv2
URL:		http://jl.photodex.com/dog/
Source0:	%{name}-%{version}.tar.bz2

%description
Dog is intended as a replacement for the obscure utility "cat". 
In addition to emulating all of the behavior of cat, 
dog also has some functionality that would normally require a 
freaky perl hacker to spew out line noise for perl to interpret. 
This includes extracting ranges of lines of text and string text.

%prep
%setup -q

%build
make CFLAGS="%{optflags}"

%install
install -d %{buildroot}%{_bindir}
install -d %{buildroot}%{_mandir}/man1
install %{name} %{buildroot}%{_bindir}/%{name}-cat
install -m644 %{name}.1 %{buildroot}%{_mandir}/man1/%{name}-cat.1

%files
%doc README AUTHORS COPYING
%{_bindir}/%{name}-cat
%{_mandir}/*/%{name}-cat.1*

%changelog
* Mon Feb 16 2015 Wei-Lun Chao <bluebat@member.fsf.org> - 1.7
- Rebuild for Fedora
* Fri Jul 11 2014 Bernhard Rosenkraenzer <bero@bero.eu> 1.7-17
+ Revision: 9f26ea1
- MassBuild#451: Increase release tag
