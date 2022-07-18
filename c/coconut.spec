%define __python /usr/bin/python3

Name:           coconut
Version:        1.6.0
Release:        1
Summary:        A functional programming language that compiles to Python
License:        MIT
Group:          Development/Languages/Python
URL:            https://github.com/evhub/coconut
Source:         https://files.pythonhosted.org/packages/source/c/coconut/coconut-%{version}.tar.gz
BuildRequires:  python3-devel
BuildArch:      noarch

%description
Coconut is a functional programming language that compiles to
Python. Since all valid Python is valid Coconut, using Coconut will
only extend and enhance what is already capable of in Python.

Coconut enhances the repertoire of Python programmers to include
tools for functional programming. Coconut code runs the same on any
Python version.

%prep
%setup -q
find . -type f -exec sed -i 's/\r$//' {} +
find . -name '*.py' -exec sed -i -e '/^#!\//, 1d' {} +

%build
%py3_build

%install
%py3_install

%files
%doc README.rst CONTRIBUTING.md DOCS.md FAQ.md HELP.md
%license LICENSE.txt
%{_bindir}/coconut*
%{python3_sitelib}/coconut*
%{_datadir}/jupyter/kernels/coconut/kernel.json

%changelog
* Sun Jun 19 2022 Wei-Lun Chao <bluebat@member.fsf.org> - 1.6.0
- Rebuilt for Fedora
* Thu Jul  2 2020 gwasser@gmail.com
- Update to 1.4.3
* Sat Oct  5 2019 gwasser@gmail.com
- New features:
  * #465: new addpattern def shorthand syntax (thanks @MichalMarsalek for the issue!)
  * #301, #504, #505: full support for Python 3.6 f-strings on all targets including (thanks @m-burst for the PR!)
  * #323: added support for |**> kwargs pipes (thanks @ArneBachmann for the issue!)
  * #490: new (assert) operator function (thanks @arnauorriols for the issue!)
  * #503: added support for Python 3.8 positional-only arguments (thanks @pavelbraginskiy fo the issue!)
  * #483: fmap now works on numpy arrays (thanks @hoishing for the issue!)
  * #494: added support for pattern-matching in data definitions (thanks @arnauorriols for the issue!)
  * #493: added truncation for long MatchError messages (thanks @arnauorriols for the issue!)
  * #482: added support for Python 3.8 assignment expressions under --target 3.8 (thanks @terrdavis for the issue!)
  * #446, #458: data types are now hashable (thanks @m-burst for the PR!)
  * #502: addpattern, recursive_iterator, and TCO'd functions are now pickleable
  * #488: fewer __coconut__.py files are created when compiling in --package mode
* Tue Dec 11 2018 gwasser@gmail.com
- Update spec for better python macro use and package names
* Fri Sep 28 2018 Todd R <toddrme2178@gmail.com>
- Update to 1.4.0
  * #320: added import hook to automatically compile imported Coconut files (thanks @ArneBachmann!)
  * #347: added where clauses
  * #270: added a memoize decorator (thanks @iamrecursion!)
  * #403: added a TYPE_CHECKING constant
  * #409: added support for M `bind` x -> y syntax
  * #419: data type equality is now typed (thanks everyone in #418!)
  * #331: support negative pattern-matching with match ... not in ...
  * #411: count now supports a step size of 0
  * #394: scan now has an initializer argument
  * #398: creating a new indented block after a colon is no longer necessary for any statement
  * #229: --strict now warns on unused imports
  * #327: interpreter now supports reload built-in (thanks, @ArneBachmann!)
  * #382: interpreter now supports compiling to arbitrary file names
  * #393: unicode operators for multiplication and matrix multiplication have been switched
  * #153: function composition precedence is now such that f..g(x) is the same as f..(g(x)) not (f..g)(x)
  * #395: built-in attributes changed to remove initial underscores
* Sun Jun 10 2018 jengelh@inai.de
- Fix repeated name in summary (rpmlint).
- Trim rhetoric parts from description.
- Use find "+" logic.
* Thu May 24 2018 toddrme2178@gmail.com
- Fix dependencies
* Thu Dec  7 2017 sleep_walker@opensuse.org
- take package from home:geewass:python
- rewrite to cleanup, use singlespec
