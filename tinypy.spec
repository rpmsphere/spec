%global debug_package %{nil}

Name:               tinypy
Version:            1.1
Release:            6.1
Summary:            Minimalist Implementation of Python
Source:             http://tinypy.googlecode.com/files/tinypy-%{version}.tar.gz
URL:                http://www.tinypy.org/
Group:              Development/Languages/Python
License:            MIT
BuildRequires:      python-devel
BuildRequires:      gcc make glibc-devel pkgconfig

%description
tinypy includes a whole heap of features:
- parser and bytecode compiler written in tinypy
- fully bootstrapped
- luaesque virtual machine with garbage collection written in C
- it's "stackless" sans any "stackless" features
- cross-platform :) it runs under windows / linux / macosx
- a fairly decent subset of python
  * classes and single inheritance
  * functions with variable or keyword arguments
  * strings, lists, dicts, numbers
  * modules, list comprehensions
  * exceptions with full traceback
  * some builtins

%prep
%setup -q
sed -i 's|python |python2 |' setup.py

%build
python2 setup.py linux math

%install
install -D -m0755 build/tinypy %{buildroot}%{_bindir}/tinypy

%clean
rm -rf %{buildroot}

%files
%doc *.txt examples
%{_bindir}/tinypy

%changelog
* Sun Jan 27 2013 Wei-Lun Chao <bluebat@member.fsf.org> - 1.1
- Rebuild for Fedora
* Sun Oct 23 2011 pascal.bleser@opensuse.org
- initial version (1.1)
