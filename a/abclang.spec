%undefine _debugsource_packages
%define _name abc

Summary: ABC programming language
Name: abclang
Version: 1.05.03
Release: 6.1
License: freeware
Group: Development/Languages
Source: https://homepages.cwi.nl/~steven/abc/implementations/abc-unix.tar.gz
URL: https://homepages.cwi.nl/~steven/abc/

%description
ABC is an interactive programming language and environment for personal
computing, originally intended as a good replacement for BASIC. It was
designed by first doing a task analysis of the programming task.

ABC is easy to learn (an hour or so for someone who has already programmed),
and yet easy to use. Originally intended as a language for beginners, it has
evolved into a powerful tool for beginners and experts alike.

%prep
%setup -q -n %{_name}-unix

%build
%__make -f Makefile.unix DESTABC=%{_bindir} DESTLIB=%{_datadir}/%{name} DESTMAN=%{_mandir}/man1

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{_bindir} $RPM_BUILD_ROOT%{_datadir}/%{name} $RPM_BUILD_ROOT%{_mandir}/man1
make -f Makefile.unix install DESTROOT=$RPM_BUILD_ROOT DESTABC=%{_bindir} DESTLIB=%{_datadir}/%{name} DESTMAN=%{_mandir}/man1
mv $RPM_BUILD_ROOT%{_bindir}/%{_name} $RPM_BUILD_ROOT%{_bindir}/%{name}
mv $RPM_BUILD_ROOT%{_mandir}/man1/%{_name}.1 $RPM_BUILD_ROOT%{_mandir}/man1/%{name}.1

%files 
%doc BUGS doc/* EDITOR PROBLEMS README TODO
%{_bindir}/%{_name}*
%{_datadir}/%{name}
%{_datadir}/man/man1/%{name}.1.*

%clean
rm -rf $RPM_BUILD_ROOT

%changelog
* Sun Sep 23 2012 Wei-Lun Chao <bluebat@member.fsf.org> - 1.05.03
- Rebuilt for Fedora
