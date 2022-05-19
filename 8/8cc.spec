Name: 8cc
Summary: Simple and clean C11 compiler
Version: 0.742
Release: 1
Group: Development
License: MIT
Source0: %{name}-master.zip
URL: https://github.com/rui314/8cc
Patch0: 8cc_fix_cflags.patch

%description
8cc is a compiler for the C programming language. It's intended to support all
C11 language features while keeping the code as small and simple as possible.

%prep
%setup -q -n %{name}-master
#%patch0 -p 1

%build
make %{?_smp_mflags}

%install
install -Dm755 %{name} %{buildroot}%{_bindir}/%{name}

%files
%doc LICENSE
%{_bindir}/%{name}

%changelog
* Sun Dec 26 2021 Wei-Lun Chao <bluebat@member.fsf.org> - 0.742
- Rebuilt for Fedora
