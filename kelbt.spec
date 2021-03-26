Name:			kelbt
Version:		0.14
Summary:		Backtracking LR Parsing
License:		GPLv2
URL:			http://www.complang.org/kelbt/
Group:			Development/Tools/Debuggers
Release:		7.1
Source:			%{name}-%{version}.tar.gz
BuildRoot:		%{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires:		gcc-c++

%description
Kelbt generates backtracking LALR(1) parsers. Where traditional LALR(1) parser
generators require static resolution of shift/reduce conflicts, Kelbt generates
parsers that handle conflicts by backtracking at runtime. Kelbt is able to
generate a parser for any context-free grammar that is free of hidden left
recursion.

Kelbt is different from other backtracking LR systems in two ways. First, it
introduces a class of actions called undo actions. These actions are invoked as
the backtracker undoes parsing and allow the user to revert any side effects of
forward semantic actions. This makes it possible to backtrack over language
constructs that must modify global state in preparation for handling context
dependencies.

Second, Kelbt enables a user-controlled parsing strategy that approximates that
of generalized recursive-descent parsing with ordered choice. This makes it
easy for the user to resolve language ambiguities by ordering the grammar
productions of a non-terminal according to precedence. It is approximate in the
sense that for most grammars the equivalent of an ordered choice parsing
strategy is achieved. In cases where productions are parsed out of the order
given, there is a simple grammar transformation that remedies the problem. See
the CASCON paper for more details.

As a proof of concept, Kelbt has been used to write a partial C++ parser
(included) that is composed of strictly a scanner, a name lookup stage and a
grammar with standard semantic actions and semantic undo actions.

%prep
%setup -q
%if 0%{fedora} > 16
sed -i 's| compare| this->compare|' aapl/bstcommon.h aapl/avlcommon.h
%endif

%build
%configure
%{__make} %{?jobs:-j%jobs}

%install
%{__rm} -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/%{_bindir}
install -m 755 kelbt/%{name} $RPM_BUILD_ROOT/%{_bindir}/%{name}

%files
%defattr(-,root,root)
%{_bindir}/%{name}
%doc ChangeLog COPYING CREDITS TODO

%clean
%{__rm} -rf $RPM_BUILD_ROOT

%changelog
* Tue Aug 07 2012 Wei-Lun Chao <bluebat@member.fsf.org> - 0.14
- Rebuild for Fedora
* Sun Jan  3 2010 David Bolt <dbolt@davjam.org> 0.14
- First RPM package.
