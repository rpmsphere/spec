%undefine _debugsource_packages

Summary:        C Read-Eval-Print Loop
Name:           cepl
Version:        5.6.0
Release:        8.1
License:        GPLv3
Group:          Development/C
URL:            https://github.com/alyptik/cepl
Source0:        https://github.com/alyptik/cepl/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  readline-devel
BuildRequires:  elfutils-libelf-devel

%description
An interactive C (ISO/IEC 9899:2011) read–eval–print loop (REPL)
currently supporting multiple compilers, shell-esque readline
key-bindings/tab-completion, and incremental undo.

%prep
%setup -q
sed -i 's|\$(READLINE)/lib/libreadline.a \$(READLINE)/lib/libhistory.a|-lreadline -lhistory|' config.mk

%build
make %{name}

%install
rm -rf $RPM_BUILD_ROOT
%make_install PREFIX=/usr

%files
%doc README.md LICENSE.md
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1*
%{_datadir}/zsh/site-functions/_cepl

%changelog
* Fri Feb 23 2018 Wei-Lun Chao <bluebat@member.fsf.org> - 5.6.0
- Rebuilt for Fedora
