#undefine _debugsource_packages

Summary: A human readable quasi-concatenative programming language
Name: cognate
Version: 0.20220504
Release: 1
License: BSD-2-Clause
Group: Development/Languages
Source0: https://github.com/cognate-lang/cognate/archive/refs/tags/nightly.tar.gz#/%{name}-nightly.tar.gz
URL: https://github.com/cognate-lang/cognate
BuildRequires: vim-common

%description
Cognate is a small dynamic quasi-concatenative language for functional programming.
Cognate aims to express complex programs in a simple and readable way through its
unique syntax, which emphasises embedding comments into statements. This makes
programs very readable and helps a programmer better express their intentions.

%prep
%setup -q -n %{name}-nightly

%build
make

%install
install -Dm755 cognac %{buildroot}%{_bindir}/cognac

%files 
%doc LICENSE *.md
%{_bindir}/cognac

%clean
rm -rf $RPM_BUILD_ROOT

%changelog
* Sun Oct 02 2022 Wei-Lun Chao <bluebat@member.fsf.org> - 0.20220504
- Rebuilt for Fedora
