%global debug_package %{nil}

Name: awib
Summary: A brainfuck compiler written in brainfuck
Version: 0.4
Release: 10.1
Group: Development/Languages
URL: https://github.com/matslina/awib
Source0: %{name}-%{version}.tar.gz
License: GPLv3
BuildRequires: python

%description
Awib is a brainfuck compiler written in brainfuck. It's portable, optimising,
polyglot and supports multiple target platforms. Awib compiles brainfuck source
code into well performing 386 Linux binaries, C code, Ruby code, Go code and
Tcl code. Awib is itself polyglot in brainfuck, C, bash and Tcl.

%prep
%setup -q

%build
make -i binary

%install
rm -rf %{buildroot}
install -Dm755 %{name} %{buildroot}%{_bindir}/%{name}

%files
%doc README.md COPYING DEVEL
%{_bindir}/%{name}

%changelog
* Thu Jan 22 2015 Wei-Lun Chao <bluebat@member.fsf.org> - 0.4
- Rebuild for Fedora
