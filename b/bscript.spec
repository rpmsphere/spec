Summary: Portable, fast, lightweight BASIC interpreter
Name: bscript
Version: 0.3
Release: 3.1
License: GPL
Group: Development/Language
URL: http://bscript.sourceforge.net/
Source: http://sourceforge.net/projects/bscript/files/bscript/%{name}-%{version}/%{name}-%{version}.tar.gz

%description
BScript is a (yet another) BASIC interpreter. It is free software and
open-sourced, licensed under the terms of the GNU General Public License
version 2 or later. You can use BScript to teach BASIC to your students,
write understandable shell scripts (good bye, spaghetti code!), automate
simple tasks, or even write a game!

%prep
%setup -q
sed -i '444i break;' src/context.c

%build
%configure
make

%install
%make_install

%files
%defattr(-,root,root)
%doc README COPYING AUTHORS ChangeLog
%{_bindir}/%{name}

%changelog
* Thu Dec 27 2012 Wei-Lun Chao <bluebat@member.fsf.org> - 0.3
- Rebuilt for Fedora
