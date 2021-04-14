%undefine _debugsource_packages

Name:          untex
Version:       1.3
Release:       4.1
Summary:       Command to strip LaTeX commands from input
Group:         Applications/Publishing
URL:           ftp://ftp.thp.uni-duisburg.de/pub/source/
Source:        ftp://ftp.thp.uni-duisburg.de/pub/source/%{name}-%{version}.tar.gz
License:       GPL

%description
Like detex untex removes some LaTeX commands from the files listed in the
arguments (or standard input) and prints the output to standard output.
Has some alternative options, and the source code too, of course.

%prep
%setup -q

%build
make -j1

%install
rm -rf $RPM_BUILD_ROOT
install -D -m 755 untex $RPM_BUILD_ROOT%{_bindir}/untex
install -D -m 644 untex.man $RPM_BUILD_ROOT%{_mandir}/man1/untex.1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%{_bindir}/untex
%{_mandir}/man1/untex.*

%changelog
* Wed Jun 29 2011 Wei-Lun Chao <bluebat@member.fsf.org> - 1.3
- Rebuilt for Fedora
* Wed Dec 12 2007 Aleph0 <aleph0@openmamba.org> 1.3-2mamba
- fixed manpage name
* Wed Dec 28 2005 Alessandro Ramazzina <alessandro.ramazzina@qilinux.it> 1.3-1qilnx
- package created by autospec
