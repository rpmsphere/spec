%undefine _debugsource_packages

Summary:	A sequencial, functional logic programming language
Name:		elizalang
Version:	0.11
Release:	3.1
License:	GPLv3
Group:		Development/Languages
Source0:	http://www.eliza.ch/dist/Source/Eliza.zip
URL:		http://www.eliza.ch
BuildRequires:	gcc-c++, coco-c

%description
Eliza borrows concepts from Prolog, Lisp, Icon, Haskell, Bash, Oz and C/C++.
From Prolog it borrows backtracking. From Lisp stems the concept of first-
order-functions. This concept had a great influence on the design of the
language. Icon has influenced Eliza with its efficiency and the generators.
Haskell is present through its separation of declaration and definition of
functions and the syntax of the declaration. Also the influence of Oz is
quite important. Eliza should be equally suited for constraint programming.
C++ has found its way into the language with its functors and namespaces.
Eliza uses pipes as Bash does, for example.

%prep
%setup -q -c

%build
make

%install
rm -rf $RPM_BUILD_ROOT
install -Dm755 eliza $RPM_BUILD_ROOT%{_bindir}/%{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%doc gpl-3.0.txt eliza.atg *.eliza
%{_bindir}/%{name}

%changelog
* Sun Dec 16 2012 Wei-Lun Chao <bluebat@member.fsf.org> - 0.11
- Rebuilt for Fedora
