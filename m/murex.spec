%undefine _debugsource_packages

Summary: Bash-like shell and scripting environment
Name: murex
Version: 2.6.0520
Release: 1
License: GPL-2
Group: Development/Language
URL: https://github.com/lmorg/murex
Source0: https://codeload.github.com/lmorg/murex/tar.gz/refs/tags/v%{version}#/%{name}-%{version}.tar.gz

%description
murex is a shell, like bash / zsh / fish / etc. It follows a similar syntax to
POSIX shells like Bash however supports more advanced features than you'd
typically expect from a $SHELL. It aims to be similar enough to traditional
shells that you can retain most of your muscle memory, while not being afraid
to make breaking changes where "bash-isms" lead to unreadable, hard to maintain,
or unsafe code. murex is designed for DevOps productivity so it isn't suited for
high performance workloads beyond what you'd typically run in Bash (eg pipelines
forked as concurrent processes).

%prep
%setup -q

%build
go build .

%install
install -Dm755 %{name} %{buildroot}%{_bindir}/%{name}

%clean
rm -rf ${RPM_BUILD_ROOT}

%files
%doc LICENSE *.md
%{_bindir}/%{name}

%changelog
* Sun Apr 24 2022 Wei-Lun Chao <bluebat@member.fsf.org> - 2.6.0520
- Rebuilt for Fedora
