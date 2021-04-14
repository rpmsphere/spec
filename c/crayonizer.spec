Name: crayonizer
Summary: A console colorer app
Version: 2.2
Release: 3.1
Group: Applications/Text
License: GPLv3
URL: https://github.com/ColumPaget/Crayonizer
Source0: https://codeload.github.com/ColumPaget/Crayonizer/tar.gz/v%{version}#/Crayonizer-%{version}.tar.gz

%description
Crayonizer is a command-line app that "crayonizes" (i.e. colors in) the output
of other command-line apps. It's written in straight-C with few dependancies.

%prep
%setup -q -n Crayonizer-%{version}

%build
%configure
make %{?_smp_mflags}

%install
#make_install
install -Dm755 crayonizer %{buildroot}%{_bindir}/%{name}
install -d %{buildroot}%{_sysconfdir}/%{name}.d
cp examples/* %{buildroot}%{_sysconfdir}/%{name}.d

%files
%license LICENSE
%doc README.md
%{_bindir}/*
%{_sysconfdir}/%{name}.d

%changelog
* Thu Nov 01 2018 Wei-Lun Chao <bluebat@member.fsf.org> - 2.2
- Rebuilt for Fedora
